import pytest
from unittest.mock import patch, MagicMock
import os

from weaviate_vibe_eval.utils.docker_executor import DockerExecutor


@pytest.fixture
def docker_executor():
    """Fixture providing a DockerExecutor instance."""
    return DockerExecutor(image="python:3.9-slim", timeout=10)


def test_is_docker_available(docker_executor):
    """Test detection of Docker availability."""
    with patch("subprocess.run") as mock_run:
        # Mock Docker available
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_run.return_value = mock_process

        assert docker_executor.is_docker_available() is True

        # Mock Docker not available
        mock_process.returncode = 1
        assert docker_executor.is_docker_available() is False

        # Mock Docker command not found
        mock_run.side_effect = FileNotFoundError()
        assert docker_executor.is_docker_available() is False


@pytest.mark.skipif(
    not DockerExecutor().is_docker_available(), reason="Docker not available"
)
def test_execute_simple_code(docker_executor):
    """Test executing a simple Python code snippet."""
    # Simple code that prints to stdout and stderr
    code = """
import sys
print("Hello from Docker!")
print("Error message", file=sys.stderr)
sys.exit(0)
"""

    stdout, stderr, exit_code = docker_executor.execute_code(code)

    assert "Hello from Docker!" in stdout
    assert "Error message" in stderr
    assert exit_code == 0
