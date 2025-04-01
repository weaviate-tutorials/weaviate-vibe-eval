#!/usr/bin/env python
import os
import json
import time
import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import dotenv

from weaviate_vibe_eval.models.anthropic_model import AnthropicModel
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor
from weaviate_vibe_eval.utils.code_execution import generate_and_execute
from weaviate_vibe_eval.models.model_names import ModelNames

# Load environment variables
dotenv.load_dotenv()


# Define model factory for easy extension
def create_model(provider: str, model_name: str, api_key: Optional[str] = None):
    """Create a model instance based on provider and model name."""
    if provider.lower() == "anthropic":
        return AnthropicModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"),
        )
    # Add more providers as needed:
    # elif provider.lower() == "openai":
    #     return OpenAIModel(...)
    # elif provider.lower() == "google":
    #     return GoogleModel(...)
    else:
        raise ValueError(f"Unsupported provider: {provider}")


class BenchmarkConfig:
    """Configuration settings for benchmark runs."""

    def __init__(
        self,
        providers: List[str] = ["anthropic"],
        models: List[str] = None,
        tasks: List[str] = None,
        output_dir: str = "results",
        verbose: bool = False
    ):
        self.providers = providers
        # Default to both models if none specified
        self.models = models or [
            ModelNames.CLAUDE_3_7_SONNET.value,
            ModelNames.CLAUDE_3_5_HAIKU.value
        ]
        self.tasks = tasks  # None means all tasks
        self.output_dir = output_dir
        self.verbose = verbose


class BenchmarkTasks:
    """Benchmark tasks and example prompts."""

    # Example code for connecting to Weaviate
    EXAMPLE_CODE = """
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
)

assert client.is_ready()

client.close()
"""

    @classmethod
    def load_tasks(cls, tasks_dir: str = "benchmarks") -> Dict[str, Dict[str, Any]]:
        """Load benchmark tasks from the tasks directory."""

        # Base prompts that can be used for both zero-shot and in-context examples
        base_prompts = {
            "connect_to_weaviate": {
                "prompt": """
            Write Python code using the latest Weaviate client syntax,
            to connect to Weaviate Cloud using the environment variables
            WCD_TEST_URL and WCD_TEST_KEY.
            (WCD_TEST_URL is the URL of the Weaviate Cloud instance,
            and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

            Then check that the server is ready to accept requests.
            Don't do anything else.

            These environment variables are already set in the execution environment.
            """,
                "description": "Basic Weaviate connection and operations",
            },
            # Add more base prompts here
        }

        # Generate all tasks from base prompts
        tasks = {}

        # Add zero-shot variants
        for key, task in base_prompts.items():
            zero_shot_key = f"zero_shot_{key}"
            tasks[zero_shot_key] = {
                "prompt": task["prompt"],
                "description": f"Zero-shot: {task['description']}",
                "base_prompt": key
            }

        # Add in-context variants with examples
        for key, task in base_prompts.items():
            in_context_key = f"in_context_{key}"

            # Choose the appropriate example based on task type
            context_example = ""
            if key == "connect_to_weaviate":
                context_example = f"\n\nHere is an example of how to connect to Weaviate:\n{cls.EXAMPLE_CODE}\n"
            # Add more task-specific examples as needed

            tasks[in_context_key] = {
                "prompt": task["prompt"] + context_example,
                "description": f"In-context: {task['description']}",
                "base_prompt": key
            }

        # TODO: When ready to load from files, implement here
        # if Path(tasks_dir).exists():
        #     # Load tasks from files

        return tasks


class BenchmarkRunner:
    """Core functionality for running benchmarks."""

    def __init__(self, config: BenchmarkConfig):
        self.config = config
        self.docker_executor = None
        self.env_vars = {}
        self.results = {}

    def setup(self):
        """Setup resources for benchmark runs."""
        # Create output directory
        os.makedirs(self.config.output_dir, exist_ok=True)

        # Setup Docker executor with network access
        self.docker_executor = DockerExecutor(
            network="bridge",  # Longer timeout for complex operations
            timeout=120
        )

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
        if hasattr(self.docker_executor, "cleanup"):
            self.docker_executor.cleanup()

    def run_task_with_model(self, task_id: str, task_data: Dict[str, Any],
                            provider: str, model_name: str) -> Dict[str, Any]:
        """Run a single task with a specific model."""
        model_id = f"{provider}/{model_name}"
        print(f"\nRunning with model: {model_id}")

        if model_id not in self.results:
            self.results[model_id] = {}

        prompt = task_data["prompt"]

        try:
            # Create model
            model = create_model(provider, model_name)
            start_time = time.time()

            # Generate and execute code
            generated_text, execution_result = generate_and_execute(
                model=model,
                prompt=prompt,
                docker_executor=self.docker_executor,
                model_params=None,
                inputs=None,
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
                if self.config.verbose:
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

            # Store results
            self.results[model_id][task_id] = task_result
            return task_result

        except Exception as e:
            print(f"  ❌ FAILED: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.datetime.now().isoformat()
            }

    def save_results(self):
        """Save benchmark results to files."""
        for model_id, model_results in self.results.items():
            provider, model_name = model_id.split('/')
            result_file = os.path.join(
                self.config.output_dir,
                f"{provider}_{model_name.replace('-', '_')}.json"
            )
            with open(result_file, "w") as f:
                json.dump(model_results, f, indent=2)
            print(f"\nResults for {model_id} saved to {result_file}")

    def run(self) -> Dict[str, Dict[str, Any]]:
        """Run all benchmarks according to configuration."""
        try:
            # Set up resources
            self.setup()

            # Load tasks
            all_tasks = BenchmarkTasks.load_tasks()

            # Filter tasks if specified
            benchmark_tasks = {k: v for k, v in all_tasks.items()
                              if not self.config.tasks or k in self.config.tasks}

            if not benchmark_tasks:
                print("No matching tasks found.")
                return {}

            # Track summary information
            summary = {}

            # Run benchmarks by task first, then by model
            for task_id, task_data in benchmark_tasks.items():
                print(f"\n=== Running task: {task_id} - {task_data.get('description', '')} ===")

                for provider in self.config.providers:
                    for model_name in self.config.models:
                        model_id = f"{provider}/{model_name}"

                        if model_id not in summary:
                            summary[model_id] = {"passed": 0, "failed": 0, "total": 0}

                        result = self.run_task_with_model(task_id, task_data, provider, model_name)

                        # Update summary statistics
                        summary[model_id]["total"] += 1
                        if result.get("success", False):
                            summary[model_id]["passed"] += 1
                        else:
                            summary[model_id]["failed"] += 1

            # Save results
            self.save_results()

            # Print summary
            self._print_summary(summary, benchmark_tasks)

            return self.results

        finally:
            # Clean up resources
            self.cleanup()

    def _print_summary(self, summary: Dict[str, Dict[str, int]], tasks: Dict[str, Dict[str, Any]]):
        """Print a summary of benchmark results."""
        print("\n" + "="*60)
        print("BENCHMARK SUMMARY")
        print("="*60)

        # Print summary by model
        for model_id, stats in summary.items():
            pass_rate = (stats["passed"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            print(f"\n{model_id}:")
            print(f"  Passed: {stats['passed']}/{stats['total']} ({pass_rate:.1f}%)")

        # Print summary by task
        print("\n" + "-"*60)
        print("Results by Task:")
        print("-"*60)

        for task_id in tasks.keys():
            print(f"\n{task_id}:")
            for model_id in summary.keys():
                if task_id in self.results.get(model_id, {}):
                    result = self.results[model_id][task_id]
                    success = result.get("success", False)
                    duration = result.get("duration", 0)
                    exit_code = result.get("exit_code", "N/A")

                    status = "✅ PASSED" if success else "❌ FAILED"
                    print(f"  {model_id}: {status} in {duration:.2f}s (exit code: {exit_code})")

        print("\n" + "="*60)


def run_benchmark(
    providers: List[str] = ["anthropic"],
    models: List[str] = None,
    tasks: List[str] = None,
    output_dir: str = "results",
    verbose: bool = False,
) -> Dict[str, Dict[str, Any]]:
    """
    Run benchmarks for specified models and tasks.

    This is a simplified interface to the benchmark runner.
    """
    config = BenchmarkConfig(
        providers=providers,
        models=models,
        tasks=tasks,
        output_dir=output_dir,
        verbose=verbose
    )

    runner = BenchmarkRunner(config)
    return runner.run()


# Example of direct usage without CLI args
if __name__ == "__main__":
    # Run benchmarks with default settings (both Claude models)
    results = run_benchmark(verbose=True)

    # # Alternatively, customize your benchmark run:
    # results = run_benchmark(
    #     providers=["anthropic"],
    #     # Use specific models:
    #     models=[ModelNames.CLAUDE_3_7_SONNET.value],
    #     # Run specific tasks:
    #     tasks=["zero_shot_connect_to_weaviate"],
    #     verbose=True
    # )
