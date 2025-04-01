import re
from typing import Dict, Any, Optional, Tuple, Union, List

from weaviate_vibe_eval.models.base_model import BaseModel
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor


def extract_python_code(text: str) -> str:
    """
    Extract Python code blocks from text.

    Args:
        text: Text containing code blocks

    Returns:
        Extracted Python code block or original text if no blocks found
    """
    # Look for Python code blocks with ```python and ``` markers
    # Use a more robust pattern that properly handles the formatting
    python_blocks = re.findall(r"```python\n(.*?)\n```", text, re.DOTALL)

    # If no Python blocks found, look for generic code blocks
    if not python_blocks:
        python_blocks = re.findall(r"```\n(.*?)\n```", text, re.DOTALL)

    # If not even a single block found, return the text as is
    if not python_blocks:
        return text

    # Return the first block found
    return python_blocks[0]


def generate_and_execute(
    model: BaseModel,
    prompt: str,
    docker_executor: DockerExecutor,
    model_params: Optional[Dict[str, Any]] = None,
    inputs: Optional[Dict[str, Any]] = None,
) -> Tuple[str, Optional[Tuple[str, str, int]]]:
    """
    Generate code using any model and execute it in a Docker container.

    Args:
        model: Any model implementing the BaseModel interface
        prompt: Input prompt for code generation
        docker_executor: Docker executor for safe code execution
        model_params: Optional parameters for the model's generate method
        inputs: Optional inputs to provide to the executed code

    Returns:
        Tuple of (generated_text, execution_result)
        where execution_result is (stdout, stderr, exit_code) if code was executed
    """
    # Use default params if none provided
    params = model_params or {}

    # Generate text using the model
    generated_text = model.generate(prompt, **params)

    # Extract code blocks from generated text
    code_block = extract_python_code(generated_text)

    if not code_block:
        return generated_text, None

    # Execute the code block
    execution_result = docker_executor.execute_code(code_block, inputs)
    return generated_text, execution_result


def execute_code_string(
    code: str,
    docker_executor: DockerExecutor,
    inputs: Optional[Dict[str, Any]] = None,
    packages: Optional[List[str]] = None,
    env_vars: Optional[Dict[str, str]] = None,
) -> Tuple[str, str, int]:
    """
    Execute a provided code string in a Docker container.

    Args:
        code: Python code string to execute
        docker_executor: Docker executor for safe code execution
        inputs: Optional inputs to provide to the executed code
        packages: Optional list of pip packages to install before execution
        env_vars: Optional environment variables to set before execution
    Returns:
        Tuple of (stdout, stderr, exit_code)
    """
    return docker_executor.execute_code(code, inputs, packages, env_vars)
