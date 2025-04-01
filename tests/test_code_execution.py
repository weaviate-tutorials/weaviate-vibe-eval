import pytest
from unittest.mock import patch, MagicMock
import dotenv

dotenv.load_dotenv()

from weaviate_vibe_eval.utils.code_execution import (
    extract_python_code,
    generate_and_execute
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

    # Fix: Safely access the call arguments
    if mock_docker_executor.execute_code.call_args is not None:
        # Check if positional arguments exist
        if len(mock_docker_executor.execute_code.call_args[0]) > 0:
            code_arg = mock_docker_executor.execute_code.call_args[0][0]
        # If not, try to get it from keyword arguments
        elif 'code' in mock_docker_executor.execute_code.call_args[1]:
            code_arg = mock_docker_executor.execute_code.call_args[1]['code']
        else:
            pytest.fail("execute_code was called but 'code' argument not found")

        assert "Hello from generated code!" in code_arg
    else:
        pytest.fail("execute_code was called but call_args is None")

    # Check the return values
    assert "Hello from generated code!" in generated_text
    assert result == ("stdout output", "stderr output", 0)


def test_weaviate_network_integration():
    """Test executing Weaviate code with real Docker and network connectivity."""
    # Create an actual Docker executor with network permissions
    docker_executor = DockerExecutor(
        network="bridge",  # Use bridge network for internet access
    )

    # Weaviate code that tests network connectivity
    weaviate_code = """
import weaviate
from weaviate.classes.init import Auth
import dotenv
import os
import requests

dotenv.load_dotenv()

# Test basic network connectivity first
response = requests.get('https://httpbin.org/ip')
print(f"Network connectivity test: {response.status_code}")

# Then test Weaviate connection
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")

if not wcd_url or not wcd_key:
    print("WCD_TEST_URL or WCD_TEST_KEY not set in environment")
    exit(1)

print(f"Attempting to connect to Weaviate at {wcd_url}")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key)
)

is_ready = client.is_ready()
print(f"Weaviate connection ready: {is_ready}")

client.close()
    """

    try:
        import dotenv
        import os
        dotenv.load_dotenv()

        wcd_url = os.getenv("WCD_TEST_URL")
        wcd_key = os.getenv("WCD_TEST_KEY")

        # Execute the code with the real Docker executor
        stdout, stderr, exit_code = docker_executor.execute_code(
            code=weaviate_code,
            packages=["weaviate-client", "python-dotenv", "requests"],
            env_vars={"WCD_TEST_URL": wcd_url, "WCD_TEST_KEY": wcd_key}
        )

        # Print results for debugging
        print(f"Stdout: {stdout}")
        print(f"Stderr: {stderr}")
        print(f"Exit code: {exit_code}")

        # Validate the results
        assert exit_code == 0
        assert "Network connectivity test: 200" in stdout
        assert "Weaviate connection ready: True" in stdout

    except Exception as e:
        pytest.fail(f"Test failed with exception: {str(e)}")
