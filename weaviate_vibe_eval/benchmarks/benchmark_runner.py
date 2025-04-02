from typing import Dict, List, Any, Optional
import os
import json
import time
import datetime
import re

from weaviate_vibe_eval.models.model import ModelNames
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor
from weaviate_vibe_eval.utils.code_execution import (
    generate_and_execute,
    extract_python_code,
)
from weaviate_vibe_eval.models import create_model
from weaviate_vibe_eval.benchmarks.tasks import BENCHMARK_TASKS, task_registry, TaskVariant
from weaviate_vibe_eval.models.judge_model import JudgeModel

# Import canonical implementations for backward compatibility
# This will be removed in future versions
try:
    from weaviate_vibe_eval.benchmarks.canonical_implementations import (
        CANONICAL_IMPLEMENTATIONS,
    )
except ImportError:
    CANONICAL_IMPLEMENTATIONS = {}


class BenchmarkRunner:
    """Core functionality for running benchmarks."""

    def __init__(
        self,
        output_dir: str = "results",
        models: Optional[List[ModelNames]] = None,
        tasks: Optional[List[str]] = None,
        verbose: bool = False,
        use_judge: bool = False,
        judge_model: Optional[ModelNames] = None,
    ):
        self.output_dir = output_dir

        # Handle model selection logic - either use specified models or all models
        self.models = models if models is not None else list(ModelNames)

        # Get list of unique providers from selected models (for reporting purposes)
        self.providers = list(set(model.provider for model in self.models))

        # Expand task names to include all variants
        self.task_ids = task_registry.expand_task_names(tasks)

        self.verbose = verbose
        self.docker_executor = None
        self.env_vars = {}
        self.results = {}
        self.use_judge = use_judge
        self.judge_model = judge_model or ModelNames.CLAUDE_3_7_SONNET_20250219
        self.judge = None if not use_judge else JudgeModel(model_name=self.judge_model)

    def run_benchmarks(self):
        """Run all benchmarks and collect results."""
        provider_count = len(self.providers)
        provider_str = f"{provider_count} provider{'s' if provider_count != 1 else ''}"
        print(f"Running benchmarks with {len(self.models)} models from {provider_str}...")

        # Determine which tasks to run
        tasks_to_run = self.task_ids or list(BENCHMARK_TASKS.keys())

        # Group tasks by base name for better reporting
        task_groups = {}
        for task_id in tasks_to_run:
            # Extract base task name (e.g., "connect" from "zero_shot_connect")
            parts = task_id.split('_')
            if len(parts) >= 2:
                base_name = parts[-1]  # Last part is the base name
                if base_name not in task_groups:
                    task_groups[base_name] = []
                task_groups[base_name].append(task_id)

        # Print task information
        for base_name, variants in task_groups.items():
            variant_names = [v.replace(f"_{base_name}", "") for v in variants]
            print(f"Task '{base_name}': Running {len(variants)} variants ({', '.join(variant_names)})")

        # Setup benchmarks
        self.setup()

        try:
            if not self.models:
                print("Warning: No models selected to run")
                return {}

            # Run benchmarks for each model and task
            for model in self.models:
                provider = model.provider
                model_name = model.model_name

                print(f"\n=== Running benchmarks for {provider}/{model_name} ===")

                for task_id in tasks_to_run:
                    if task_id in BENCHMARK_TASKS:
                        print(
                            f"\nTask: {task_id} - {BENCHMARK_TASKS[task_id]['description']}"
                        )
                        self.run_task_with_model(
                            task_id, BENCHMARK_TASKS[task_id], model
                        )
                    else:
                        print(f"Unknown task: {task_id}")

            # Save results to disk
            self.save_results()

            # Print summary
            self.print_summary()

            return self.results
        finally:
            # Always clean up resources
            self.cleanup()

    def setup(self):
        """Setup resources for benchmark runs."""
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)

        # Setup Docker executor with network access
        self.docker_executor = DockerExecutor(network="bridge", timeout=120)

        # Load Weaviate credentials from environment
        wcd_url = os.environ.get("WCD_TEST_URL")
        wcd_key = os.environ.get("WCD_TEST_KEY")

        if not wcd_url or not wcd_key:
            print(
                "Warning: WCD_TEST_URL or WCD_TEST_KEY not set in environment. Weaviate operations may fail."
            )

        # Prepare environment variables for Docker
        self.env_vars = {"WCD_TEST_URL": wcd_url, "WCD_TEST_KEY": wcd_key}

    def cleanup(self):
        """Clean up resources."""
        if self.docker_executor:
            self.docker_executor.cleanup()

    def run_task_with_model(
        self, task_id: str, task_data: Dict[str, Any], model_enum: ModelNames
    ) -> Dict[str, Any]:
        """Run a single task with a specific model."""
        provider = model_enum.provider
        model_name = model_enum.model_name

        model_id = f"{provider}/{model_name}"
        print(f"\nRunning with model: {model_id}")

        if model_id not in self.results:
            self.results[model_id] = {}

        prompt = task_data["prompt"]

        try:
            # Create model
            model = create_model(model_enum)
            start_time = time.time()

            # Generate and execute code
            generated_text, execution_result = generate_and_execute(
                model=model,
                prompt=prompt,
                docker_executor=self.docker_executor,
                env_vars=self.env_vars,
            )

            end_time = time.time()
            duration = end_time - start_time
            timestamp = datetime.datetime.now().isoformat()

            # Process results
            if execution_result:
                stdout, stderr, exit_code = execution_result
                success = exit_code == 0

                # Save detailed results
                task_result = {
                    "success": success,
                    "timestamp": timestamp,
                    "duration": duration,
                    "prompt": prompt,
                    "generated_text": generated_text,
                    "stdout": stdout,
                    "stderr": stderr,
                    "exit_code": exit_code,
                }

                # Only print brief status during execution
                status = "✅ PASSED" if success else "❌ FAILED"
                print(f"  {status} in {duration:.2f}s (exit code: {exit_code})")

                # Only show detailed output if verbose is enabled
                if self.verbose:
                    print("\nGenerated Code:")
                    print("-------------------")
                    print(generated_text)
                    print("\nOutput:")
                    print("-------------------")
                    print(stdout)
                    if stderr:
                        print("\nErrors:")
                        print("-------------------")
                        print(stderr)
            else:
                print("  ❌ FAILED: No code was executed")

                task_result = {
                    "success": False,
                    "timestamp": timestamp,
                    "duration": duration,
                    "prompt": prompt,
                    "generated_text": generated_text,
                    "error": "No code was executed",
                }

            # Add judge evaluation if enabled
            if self.use_judge:
                # Get the canonical implementation
                canonical_code = None

                # First, try to get from task object (new way)
                task_variant_data = task_registry.get_task_variant(task_id)
                if task_variant_data:
                    task_obj = task_variant_data.get("task")
                    if task_obj and task_obj.canonical_implementation:
                        canonical_code = task_obj.canonical_implementation

                # Fallback to old way for backward compatibility
                if not canonical_code and task_id in CANONICAL_IMPLEMENTATIONS:
                    canonical_code = CANONICAL_IMPLEMENTATIONS[task_id]

                if canonical_code:
                    task_description = task_data.get("description", "")
                    generated_code = extract_python_code(generated_text)

                    print(f"  🧠 Running LLM code comparison...")
                    evaluation = self.judge.compare_code_implementations(
                        generated_code=generated_code,
                        canonical_code=canonical_code,
                        task_description=task_description,
                    )

                    # Add comparison results to task result
                    task_result["code_comparison"] = evaluation

                    # Print brief comparison summary
                    similarity_score = evaluation.get("similarity_score", 0)
                    print(f"  📊 Code similarity score: {similarity_score}/5")

                    if "key_differences" in evaluation and self.verbose:
                        print("  Key differences:")
                        for diff in evaluation["key_differences"]:
                            print(f"    - {diff}")
                else:
                    print("  ⚠️ No canonical implementation found for comparison")

            # Store results
            self.results[model_id][task_id] = task_result
            return task_result
        except Exception as e:
            print(f"  ❌ ERROR: {str(e)}")
            return {
                "success": False,
                "timestamp": datetime.datetime.now().isoformat(),
                "prompt": prompt,
                "error": str(e),
            }

    def save_results(self):
        """Save results to disk."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/benchmark_results_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(self.results, f, indent=2)

        print(f"\nResults saved to {filename}")

        # Also save results in markdown format for better readability
        markdown_filename = f"{self.output_dir}/benchmark_results_{timestamp}.md"
        self.save_markdown_report(markdown_filename)
        print(f"Markdown report saved to {markdown_filename}")

    def save_markdown_report(self, filename: str):
        """Save results to disk in markdown format for better human readability."""
        with open(filename, "w") as f:
            # Write markdown header
            f.write("# Weaviate Benchmark Results\n\n")
            f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Write summary information
            f.write("## Summary\n\n")
            total_success = 0
            total_tasks = 0
            for model_id, model_results in self.results.items():
                success_count = sum(1 for r in model_results.values() if r.get("success", False))
                f.write(f"- **{model_id}**: {success_count}/{len(model_results)} tasks successful\n")
                total_success += success_count
                total_tasks += len(model_results)

            # Write detailed results organized by model
            f.write("## Detailed Results\n\n")
            for model_id, model_results in self.results.items():
                f.write(f"### {model_id}\n\n")

                for task_id, task_result in model_results.items():
                    f.write(f"#### {task_id}\n\n")

                    # Task description if available
                    if task_id in BENCHMARK_TASKS:
                        f.write(f"*{BENCHMARK_TASKS[task_id]['description']}*\n\n")

                    # Success status and runtime
                    success = task_result.get("success", False)
                    duration = task_result.get("duration", 0)
                    status = "✅ SUCCESS" if success else "❌ FAILURE"
                    f.write(f"**Status**: {status} (runtime: {duration:.2f}s)\n\n")

                    # Generated code
                    f.write("**Generated Code**:\n")
                    generated_code = extract_python_code(task_result.get("generated_text", ""))
                    f.write(f"```python\n{generated_code}\n```\n\n")

                    # Judge comparison if available
                    if "code_comparison" in task_result:
                        comp_result = task_result["code_comparison"]
                        similarity = comp_result.get("similarity_score", "N/A")
                        f.write(f"**Similarity Score**: {similarity}/5\n\n")

                        if "differences_summary" in comp_result:
                            f.write(f"**Differences Summary**: {comp_result['differences_summary']}\n\n")

                        if "key_differences" in comp_result:
                            f.write("**Key Differences**:\n")
                            for diff in comp_result["key_differences"]:
                                f.write(f"- {diff}\n")
                            f.write("\n")

                    # Execution output
                    if "stdout" in task_result and task_result["stdout"]:
                        f.write("**Output**:\n")
                        f.write(f"```\n{task_result['stdout']}\n```\n\n")

                    if "stderr" in task_result and task_result["stderr"]:
                        f.write("**Errors**:\n")
                        f.write(f"```\n{task_result['stderr']}\n```\n\n")

                    f.write("---\n\n")

    def print_summary(self):
        """Print a summary of benchmark results."""
        print("\n=== BENCHMARK SUMMARY ===")

        # Add code comparison summary if available
        if self.use_judge:
            print("\n--- Code Comparison Summary ---")
            for model_id, model_results in self.results.items():
                print(f"\n{model_id}:")
                for task_id, task_result in model_results.items():
                    if "code_comparison" in task_result:
                        comp_result = task_result["code_comparison"]
                        similarity = comp_result.get("similarity_score", "N/A")
                        print(f"  {task_id}: Similarity score {similarity}/5")

                        # Only print high-level differences summary
                        if "differences_summary" in comp_result:
                            print(f"    Summary: {comp_result['differences_summary']}")

        # Add detailed task-by-task breakdown
        print("\n--- Results by Task ---")

        # Get list of all tasks that were executed
        all_task_ids = set()
        for model_results in self.results.values():
            all_task_ids.update(model_results.keys())

        # Print results for each task
        for task_id in sorted(all_task_ids):
            print(f"\nTask: {task_id}")
            if task_id in BENCHMARK_TASKS:
                print(f"Description: {BENCHMARK_TASKS[task_id]['description']}")

            for model_id in self.results.keys():
                if task_id in self.results[model_id]:
                    result = self.results[model_id][task_id]
                    success = result.get("success", False)
                    duration = result.get("duration", 0)
                    exit_code = result.get("exit_code", "N/A")

                    status = "✅ PASSED" if success else "❌ FAILED"
                    print(
                        f"  {model_id}: {status} in {duration:.2f}s (exit code: {exit_code})"
                    )

        # Summary by model
        total_success = 0
        total_tasks = 0

        for model_id, model_results in self.results.items():
            success_count = sum(
                1 for r in model_results.values() if r.get("success", False)
            )
            print(f"{model_id}: {success_count}/{len(model_results)} tasks successful")
            total_success += success_count
            total_tasks += len(model_results)
