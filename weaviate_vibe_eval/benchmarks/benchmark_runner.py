from typing import Dict, List, Any, Optional
import os
import json
import time
import datetime
import re

from weaviate_vibe_eval.models.model import ModelNames
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor
from weaviate_vibe_eval.utils.code_execution import generate_and_execute, extract_python_code
from weaviate_vibe_eval.models import create_model
from weaviate_vibe_eval.benchmarks.tasks import BENCHMARK_TASKS
from weaviate_vibe_eval.models.judge_model import JudgeModel
from weaviate_vibe_eval.benchmarks.canonical_implementations import CANONICAL_IMPLEMENTATIONS

class BenchmarkRunner:
    """Core functionality for running benchmarks."""

    def __init__(
        self,
        output_dir: str = "results",
        providers: List[str] = ["anthropic", "cohere", "openai", "gemini"],
        models: List[str] = None,
        tasks: List[str] = None,
        verbose: bool = False,
        use_judge: bool = False,
        judge_model: Optional[ModelNames] = None,
    ):
        self.output_dir = output_dir
        self.providers = providers

        # Convert model string names to enum values
        if models is None:
            # Default to all models across all providers
            self.models = list(ModelNames)
        else:
            # Convert string model identifiers to enums
            self.models = []
            for model_str in models:
                # Try to match by enum name first (e.g., "COHERE_COMMAND_A_03_2025")
                try:
                    model_enum = ModelNames[model_str]
                    self.models.append(model_enum)
                    continue
                except KeyError:
                    pass

                # Try to match by model name (e.g., "command-a-03-2025")
                found = False
                for enum_val in ModelNames:
                    if enum_val.model_name == model_str:
                        self.models.append(enum_val)
                        found = True
                        break

                if not found:
                    print(f"Warning: Unknown model '{model_str}'. Skipping.")

        self.task_ids = tasks  # None means all tasks
        self.verbose = verbose
        self.docker_executor = None
        self.env_vars = {}
        self.results = {}
        self.use_judge = use_judge
        self.judge_model = judge_model or ModelNames.CLAUDE_3_7_SONNET_20250219
        self.judge = None if not use_judge else JudgeModel(model_name=self.judge_model)

    def run_benchmarks(self):
        """Run all benchmarks and collect results."""
        print(f"Running benchmarks with {len(self.providers)} providers and {len(self.models)} models...")

        # Determine which tasks to run
        tasks_to_run = self.task_ids or list(BENCHMARK_TASKS.keys())

        # Setup benchmarks
        self.setup()

        try:
            # Filter models by provider
            models_to_run = [
                model for model in self.models if model.provider in self.providers
            ]

            if not models_to_run:
                print(f"Warning: No models match the specified providers: {self.providers}")
                return {}

            # Run benchmarks for each model and task
            for model in models_to_run:
                provider = model.provider
                model_name = model.model_name

                print(f"\n=== Running benchmarks for {provider}/{model_name} ===")

                for task_id in tasks_to_run:
                    if task_id in BENCHMARK_TASKS:
                        print(f"\nTask: {task_id} - {BENCHMARK_TASKS[task_id]['description']}")
                        self.run_task_with_model(task_id, BENCHMARK_TASKS[task_id], model)
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
            if self.use_judge and task_id in CANONICAL_IMPLEMENTATIONS:
                canonical_code = CANONICAL_IMPLEMENTATIONS[task_id]
                task_description = task_data.get("description", "")

                execution_info = None
                if execution_result:
                    execution_info = {
                        "stdout": stdout,
                        "stderr": stderr,
                        "exit_code": exit_code
                    }

                generated_code = extract_python_code(generated_text)

                print(f"  🧠 Running LLM judge evaluation...")
                evaluation = self.judge.evaluate_code(
                    generated_code=generated_code,
                    canonical_code=canonical_code,
                    task_description=task_description,
                    execution_result=execution_info
                )

                # Add evaluation results to task result
                task_result["judge_evaluation"] = evaluation

                # Print brief evaluation summary
                overall_score = evaluation.get("overall_score", 0)
                print(f"  📊 Judge score: {overall_score}/5")

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

    def print_summary(self):
        """Print a summary of benchmark results."""
        print("\n=== BENCHMARK SUMMARY ===")

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

        if total_tasks > 0:
            print(
                f"\nOverall success rate: {total_success}/{total_tasks} ({total_success/total_tasks:.1%})"
            )

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

        # Add judge evaluation summary if available
        if self.use_judge:
            print("\n--- Judge Evaluation Summary ---")
            for model_id, model_results in self.results.items():
                print(f"\n{model_id}:")
                for task_id, task_result in model_results.items():
                    if "judge_evaluation" in task_result:
                        eval_result = task_result["judge_evaluation"]
                        overall = eval_result.get("overall_score", "N/A")
                        print(f"  {task_id}: {overall}/5")

                        # Print individual criteria scores
                        if "scores" in eval_result:
                            for criterion, score in eval_result["scores"].items():
                                print(f"    - {criterion}: {score}/5")

def run_default_benchmarks(use_judge=False, judge_model=None):
    """Run benchmarks with default settings."""
    print("Running Weaviate benchmarks with default settings...")

    judge_info = ""
    if use_judge:
        judge_info = f" with LLM judge evaluation"

    print(f"Running Weaviate benchmarks{judge_info}...")

    # Create and run benchmark with default settings
    runner = BenchmarkRunner(
        output_dir="results",
        use_judge=use_judge,
        judge_model=judge_model
    )

    return runner.run_benchmarks()
