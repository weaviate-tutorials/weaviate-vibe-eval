import subprocess
import tempfile
import os
import uuid
from typing import Dict, Any, Optional, Tuple


class DockerExecutor:
    """
    Executes generated code safely within a Docker container.
    """

    def __init__(
        self,
        image: str = "python:3.9-slim",
        timeout: int = 30,
        memory_limit: str = "512m",
        network: str = "none",
        additional_volumes: Optional[Dict[str, str]] = None,
    ):
        """
        Initialize the Docker executor.

        Args:
            image: Docker image to use for execution
            timeout: Maximum execution time in seconds
            memory_limit: Maximum memory allocation for container
            network: Network mode (default 'none' for isolation)
            additional_volumes: Optional volumes to mount {host_path: container_path}
        """
        self.image = image
        self.timeout = timeout
        self.memory_limit = memory_limit
        self.network = network
        self.additional_volumes = additional_volumes or {}

    def execute_code(
        self, code: str, inputs: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, str, int]:
        """
        Execute the provided code within a Docker container.

        Args:
            code: Python code to execute
            inputs: Optional dictionary of input variables

        Returns:
            Tuple of (stdout, stderr, exit_code)
        """
        # Create a unique ID for this execution
        execution_id = str(uuid.uuid4())[:8]

        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Write code to a temporary file
            code_file = os.path.join(temp_dir, "code.py")
            with open(code_file, "w") as f:
                f.write(code)

            # Write inputs to a JSON file if provided
            input_args = ""
            if inputs:
                import json

                input_file = os.path.join(temp_dir, "inputs.json")
                with open(input_file, "w") as f:
                    json.dump(inputs, f)
                input_args = f"-i /code/inputs.json"

            # Build the Docker command
            volumes = f"-v {temp_dir}:/code"
            for host_path, container_path in self.additional_volumes.items():
                volumes += f" -v {host_path}:{container_path}"

            cmd = (
                f"docker run --rm "
                f"--name weaviate-exec-{execution_id} "
                f"{volumes} "
                f"--memory={self.memory_limit} "
                f"--network={self.network} "
                f"--read-only "
                f"--cap-drop=ALL "
                f"--security-opt=no-new-privileges "
                f"--workdir /code "
                f"--user nobody "
                f"{self.image} "
                f"timeout {self.timeout} python /code/code.py {input_args}"
            )

            # Execute the command
            process = subprocess.run(cmd, shell=True, capture_output=True, text=True)

            return (process.stdout, process.stderr, process.returncode)

    def is_docker_available(self) -> bool:
        """
        Check if Docker is installed and available.

        Returns:
            True if Docker is available, False otherwise
        """
        try:
            result = subprocess.run(
                ["docker", "--version"], capture_output=True, text=True, check=False
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False
