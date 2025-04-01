import pytest
from unittest.mock import patch, MagicMock

from weaviate_vibe_eval.utils.code_execution import (
    extract_python_code,
    generate_and_execute,
    execute_code_string,
)
from weaviate_vibe_eval.utils.docker_executor import DockerExecutor


def test_extract_python_code():
    """Test extracting Python code blocks from text."""
    # Test with Python code block
    text_with_python = """
Here's some code:
```python
def hello():
    print("Hello world")
```
"""
    extracted = extract_python_code(text_with_python)
    assert "def hello():" in extracted
    assert 'print("Hello world")' in extracted

    # Test with generic code block
    text_with_generic = """
Here's some code:
```python
def hello():
    print("Hello world")
```
"""
    extracted = extract_python_code(text_with_generic)
    assert "def hello():" in extracted

    # Test with no code block
    text_without_block = "Just some plain text with no code blocks"
    extracted = extract_python_code(text_without_block)
    assert extracted == text_without_block


@pytest.fixture
def mock_model():
    """Fixture providing a mock model."""
    model = MagicMock()
    model.generate.return_value = """
Here's a simple Python script:
```python
print("Hello from generated code!")
```
"""
    return model


@pytest.fixture
def mock_docker_executor():
    """Fixture providing a mock DockerExecutor."""
    executor = MagicMock(spec=DockerExecutor)
    executor.execute_code.return_value = ("stdout output", "stderr output", 0)
    return executor


def test_generate_and_execute(mock_model, mock_docker_executor):
    """Test generating and executing code."""
    # Test with default parameters
    generated_text, result = generate_and_execute(
        model=mock_model,
        prompt="Write a hello world program",
        docker_executor=mock_docker_executor,
    )

    # Check if model.generate was called
    mock_model.generate.assert_called_once()

    # Check if docker_executor.execute_code was called with the extracted code
    mock_docker_executor.execute_code.assert_called_once()
    code_arg = mock_docker_executor.execute_code.call_args[0][0]
    assert "Hello from generated code!" in code_arg

    # Check the return values
    assert "Hello from generated code!" in generated_text
    assert result == ("stdout output", "stderr output", 0)


def test_execute_code_string(mock_docker_executor):
    """Test executing a code string directly."""
    code = 'print("Direct execution")'

    stdout, stderr, exit_code = execute_code_string(
        code=code, docker_executor=mock_docker_executor
    )

    # Check if docker_executor.execute_code was called with the right code
    mock_docker_executor.execute_code.assert_called_once_with(code, None)

    # Check the return values
    assert stdout == "stdout output"
    assert stderr == "stderr output"
    assert exit_code == 0
