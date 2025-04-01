import re
from typing import Dict, Any, Optional, Tuple, List

from weaviate_vibe_eval.models.base_model import BaseModel
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor


def extract_python_code(text: str) -> str:
    """
    Extract Python code blocks from text.
    """
    # First look for Python-specific code blocks
    python_blocks = re.findall(r"```python\n(.*?)\n```", text, re.DOTALL)

    # If no Python blocks found, look for generic code blocks
    if not python_blocks:
        python_blocks = re.findall(r"```\n(.*?)\n```", text, re.DOTALL)

    # If still no blocks found, look for other code blocks with any language tag
    if not python_blocks:
        python_blocks = re.findall(r"```.*?\n(.*?)\n```", text, re.DOTALL)

    # Return the first block found or the original text
    return python_blocks[0] if python_blocks else text


def generate_and_execute(
    model: BaseModel,
    prompt: str,
    docker_executor: DockerExecutor,
    model_params: Optional[Dict[str, Any]] = None,
    inputs: Optional[Dict[str, Any]] = None,
    packages: Optional[List[str]] = None,
    env_vars: Optional[Dict[str, str]] = None,
) -> Tuple[str, Optional[Tuple[str, str, int]]]:
    """
    Generate code using a model and execute it in a Docker container.
    """
    # Generate text using the model
    generated_text = model.generate(prompt, **(model_params or {}))

    # Extract code blocks from generated text
    code_block = extract_python_code(generated_text)

    if not code_block:
        return generated_text, None

    # Execute the code block
    execution_result = docker_executor.execute_code(
        code=code_block,
        inputs=inputs,
        packages=packages,
        env_vars=env_vars
    )
    return generated_text, execution_result
