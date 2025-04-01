import os
from weaviate_vibe_eval.models.anthropic_model import AnthropicModel
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor
from weaviate_vibe_eval.utils.code_execution import (
    generate_and_execute,
    execute_code_string,
)


def main():
    # Initialize the Anthropic model
    model = AnthropicModel(
        api_key=os.environ.get("ANTHROPIC_API_KEY"), model_name="claude-3-opus-20240229"
    )

    # Initialize Docker executor
    docker_executor = DockerExecutor()

    # Example 1: Generate and execute code
    print("=== Example 1: Generate and Execute ===")
    prompt = """
    Write a Python function that:
    1. Takes a list of integers
    2. Returns the sum of all even numbers in the list
    3. Include a test case with the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    generated_text, execution_result = generate_and_execute(
        model=model, prompt=prompt, docker_executor=docker_executor
    )

    print("Generated Text:")
    print(generated_text)
    print("\nExecution Result:")
    if execution_result:
        stdout, stderr, exit_code = execution_result
        print(f"Exit Code: {exit_code}")
        print(f"Standard Output: {stdout}")
        print(f"Standard Error: {stderr}")
    else:
        print("No code was executed")

    # Example 2: Execute existing code
    print("\n=== Example 2: Execute Existing Code ===")
    code = """
def calculate_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Test the function
print(f"The 10th Fibonacci number is: {calculate_fibonacci(10)}")
"""

    stdout, stderr, exit_code = execute_code_string(
        code=code, docker_executor=docker_executor
    )

    print(f"Exit Code: {exit_code}")
    print(f"Standard Output: {stdout}")
    print(f"Standard Error: {stderr}")


if __name__ == "__main__":
    main()
