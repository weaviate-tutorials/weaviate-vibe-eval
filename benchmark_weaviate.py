#!/usr/bin/env python
import os
import json
import time
import datetime
import argparse
from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import dotenv

from weaviate_vibe_eval.models.model import AnthropicModel, CohereModel, ModelNames
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor
from weaviate_vibe_eval.utils.code_execution import generate_and_execute

# Load environment variables
dotenv.load_dotenv()


def create_model(model_enum: ModelNames, api_key: Optional[str] = None):
    """Create a model instance based on model enum."""
    provider = model_enum.provider
    model_name = model_enum.model_name

    if provider.lower() == "anthropic":
        return AnthropicModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"),
        )
    elif provider.lower() == "cohere":
        return CohereModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("COHERE_API_KEY"),
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")


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

# Define benchmark tasks
BENCHMARK_TASKS = {
    "zero_shot_connect": {
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
        "description": "Zero-shot: Basic Weaviate connection",
    },
    "in_context_connect": {
        "prompt": """
            Write Python code using the latest Weaviate client syntax,
            to connect to Weaviate Cloud using the environment variables
            WCD_TEST_URL and WCD_TEST_KEY.
            (WCD_TEST_URL is the URL of the Weaviate Cloud instance,
            and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

            Then check that the server is ready to accept requests.
            Don't do anything else.

            These environment variables are already set in the execution environment.

            Here is an example of how to connect to Weaviate:
            """
        + EXAMPLE_CODE,
        "description": "In-context: Basic Weaviate connection",
    },
    # Add more tasks as needed
}


class BenchmarkRunner:
    """Core functionality for running benchmarks."""

    def __init__(
        self,
        output_dir: str = "results",
        providers: List[str] = ["anthropic", "cohere"],
        models: List[str] = None,
        tasks: List[str] = None,
        verbose: bool = False,
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

    def run_benchmarks(self):
        """Run all benchmarks and collect results."""
        print(
            f"Running benchmarks with {len(self.providers)} providers and {len(self.models)} models..."
        )

        # Determine which tasks to run
        tasks_to_run = self.task_ids or list(BENCHMARK_TASKS.keys())

        # Setup benchmarks
        self.setup()

        try:
            # Filter models by provider
            models_to_run = [
                model for model in self.models
                if model.provider in self.providers
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


def main():
    """Main entry point for the benchmark script."""
    parser = argparse.ArgumentParser(
        description="Run Weaviate code generation benchmarks"
    )
    parser.add_argument(
        "--output-dir", default="results", help="Directory to store results"
    )
    parser.add_argument(
        "--providers", default="anthropic,cohere", help="Comma-separated list of providers"
    )
    parser.add_argument(
        "--models",
        help="Comma-separated list of model enum names (e.g., CLAUDE_3_7_SONNET_20250219,COHERE_COMMAND_A_03_2025)"
    )
    parser.add_argument("--tasks", help="Comma-separated list of tasks to run")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--list-models", action="store_true", help="List available models and exit")

    args = parser.parse_args()

    # If requested, list available models and exit
    if args.list_models:
        print("Available models:")
        for model in ModelNames:
            print(f"  {model.name}: {model.provider}/{model.model_name}")
        return

    # Parse comma-separated lists
    providers = args.providers.split(",")
    models = args.models.split(",") if args.models else None
    tasks = args.tasks.split(",") if args.tasks else None

    # Run benchmarks
    runner = BenchmarkRunner(
        output_dir=args.output_dir,
        providers=providers,
        models=models,
        tasks=tasks,
        verbose=args.verbose,
    )

    runner.run_benchmarks()


if __name__ == "__main__":
    main()
