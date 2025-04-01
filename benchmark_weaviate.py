#!/usr/bin/env python
import os
import argparse
import json
import time
import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import dotenv

from weaviate_vibe_eval.models.anthropic_model import AnthropicModel
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor
from weaviate_vibe_eval.utils.code_execution import generate_and_execute

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



example_code = """
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
)

assert client.is_ready()

client.close()
"""


def load_benchmark_tasks(tasks_dir: str = "benchmarks") -> Dict[str, Dict[str, Any]]:
    """Load benchmark tasks from the tasks directory."""

    # TODO: Extend this to load tasks from a directory
    return {
        "zero_shot_connect_to_weaviate": {
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
        "in_context_connect_to_weaviate": {
            "prompt": f"""
        Write Python code using the latest Weaviate client syntax,
        to connect to Weaviate Cloud using the environment variables
        WCD_TEST_URL and WCD_TEST_KEY.
        (WCD_TEST_URL is the URL of the Weaviate Cloud instance,
        and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

        Then check that the server is ready to accept requests.
        Don't do anything else.

        These environment variables are already set in the execution environment.

        Here is an example of how to connect to Weaviate:
        {example_code}
        """,
            "description": "Basic Weaviate connection and operations",
        },
    }


def run_benchmark(
    providers: List[str],
    models: List[str],
    tasks: List[str] = None,
    output_dir: str = "results",
    verbose: bool = False,
):
    """Run benchmarks for specified models and tasks."""
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Load tasks
    all_tasks = load_benchmark_tasks()

    # Filter tasks if specified
    benchmark_tasks = {k: v for k, v in all_tasks.items() if not tasks or k in tasks}
    if not benchmark_tasks:
        print("No matching tasks found.")
        return

    # Setup Docker executor with network access
    docker_executor = DockerExecutor(
        network="bridge", timeout=120  # Longer timeout for complex operations
    )

    # Load Weaviate credentials from environment
    wcd_url = os.environ.get("WCD_TEST_URL")
    wcd_key = os.environ.get("WCD_TEST_KEY")

    if not wcd_url or not wcd_key:
        print(
            "Warning: WCD_TEST_URL or WCD_TEST_KEY not set in environment. Weaviate operations may fail."
        )

    # Prepare environment variables for Docker
    env_vars = {"WCD_TEST_URL": wcd_url, "WCD_TEST_KEY": wcd_key}

    # Prepare results
    results = {}

    # Run benchmarks
    for provider in providers:
        for model_name in models:
            model_id = f"{provider}/{model_name}"
            print(f"\n=== Running benchmarks for {model_id} ===")

            try:
                # Create model
                model = create_model(provider, model_name)

                model_results = {}

                # Run each task
                for task_id, task_data in benchmark_tasks.items():
                    print(f"\nTask: {task_id} - {task_data.get('description', '')}")

                    prompt = task_data["prompt"]
                    start_time = time.time()

                    # Generate and execute code
                    generated_text, execution_result = generate_and_execute(
                        model=model,
                        prompt=prompt,
                        docker_executor=docker_executor,
                        model_params=None,
                        inputs=None,
                        packages=["weaviate-client", "python-dotenv", "requests"],
                        env_vars=env_vars,
                    )

                    end_time = time.time()
                    duration = end_time - start_time

                    # Process results
                    if execution_result:
                        stdout, stderr, exit_code = execution_result
                        success = exit_code == 0

                        # Add timestamp
                        timestamp = datetime.datetime.now().isoformat()

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

                        model_results[task_id] = task_result

                        # Print summary
                        status = "✅ PASSED" if success else "❌ FAILED"
                        print(f"{status} in {duration:.2f}s (exit code: {exit_code})")

                        if verbose:
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
                        print("❌ FAILED: No code was executed")

                        # Add timestamp
                        timestamp = datetime.datetime.now().isoformat()

                        model_results[task_id] = {
                            "success": False,
                            "timestamp": timestamp,
                            "duration": duration,
                            "prompt": prompt,
                            "generated_text": generated_text,
                            "error": "No code was executed",
                        }

                results[model_id] = model_results

                # Save results to file
                result_file = os.path.join(
                    output_dir, f"{provider}_{model_name.replace('-', '_')}.json"
                )
                with open(result_file, "w") as f:
                    json.dump(model_results, f, indent=2)

                print(f"\nResults saved to {result_file}")

            except Exception as e:
                print(f"Error running benchmarks for {model_id}: {str(e)}")
                continue

    # Clean up resources
    if hasattr(docker_executor, "cleanup"):
        docker_executor.cleanup()

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Benchmark LLMs on Weaviate code generation"
    )
    parser.add_argument(
        "--providers",
        type=str,
        default="anthropic",
        help="Comma-separated list of providers (default: anthropic)",
    )
    parser.add_argument(
        "--models",
        type=str,
        default="claude-3-7-sonnet-20250219",
        help="Comma-separated list of models",
    )
    parser.add_argument(
        "--tasks",
        type=str,
        default=None,
        help="Comma-separated list of task IDs (default: all tasks)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="results",
        help="Directory to save results (default: results)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed output including generated code",
    )

    args = parser.parse_args()

    providers = [p.strip() for p in args.providers.split(",")]
    models = [m.strip() for m in args.models.split(",")]
    tasks = [t.strip() for t in args.tasks.split(",")] if args.tasks else None

    run_benchmark(
        providers=providers,
        models=models,
        tasks=tasks,
        output_dir=args.output_dir,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()
