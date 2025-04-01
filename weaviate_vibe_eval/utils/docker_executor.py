import subprocess
import tempfile
import os
import uuid
from typing import Dict, Any, Optional, Tuple, List


class DockerExecutor:
    """
    Executes generated code safely within a Docker container.
    """

    def __init__(
        self,
        image: str = "weaviate-vibe-benchmark:latest",
        timeout: int = 30,
        network: str = "bridge",
    ):
        """
        Initialize the Docker executor.

        Args:
            image: Docker image to use for execution
            timeout: Maximum execution time in seconds
            network: Network mode ('bridge' for internet access, 'none' for isolation)
        """
        self.image = image
        self.timeout = timeout
        self.network = network

    def execute_code(
        self,
        code: str,
        inputs: Optional[Dict[str, Any]] = None,
        packages: Optional[List[str]] = None,
        env_vars: Optional[Dict[str, str]] = None
    ) -> Tuple[str, str, int]:
        """
        Execute the provided code within a Docker container.

        Args:
            code: Python code to execute
            inputs: Optional dictionary of input variables
            packages: Optional list of pip packages to install before execution
            env_vars: Optional environment variables to set before execution
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
                input_args = "-i /code/inputs.json"

            # Create unified command for package installation if needed
            command = f"python /code/code.py {input_args}"
            if packages:
                packages_str = " ".join(packages)
                command = f"pip install --no-cache-dir {packages_str} && {command}"

            # Add timeout
            command = f"timeout {self.timeout} {command}"

            # Build the Docker command
            docker_cmd = [
                "docker", "run", "--rm",
                f"--name=weaviate-exec-{execution_id}",
                f"-v={temp_dir}:/code",
                f"--network={self.network}",
                "--workdir=/code"
            ]

            # Add environment variables if specified
            if env_vars:
                for key, value in env_vars.items():
                    docker_cmd.append(f"-e={key}={value}")

            # Add image and command
            docker_cmd.extend([self.image, "bash", "-c", command])

            # Execute the command
            process = subprocess.run(docker_cmd, capture_output=True, text=True)
            return (process.stdout, process.stderr, process.returncode)

    def is_docker_available(self) -> bool:
        """
        Check if Docker is installed and available.
        """
        try:
            result = subprocess.run(
                ["docker", "--version"], capture_output=True, text=True, check=False
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def cleanup(self):
        """
        Clean up resources used by the Docker executor.
        """
        # Find and remove any stalled containers from previous executions
        try:
            result = subprocess.run(
                ["docker", "ps", "-a", "--filter", "name=weaviate-exec-", "--format", "{{.Names}}"],
                capture_output=True, text=True
            )

            containers = result.stdout.strip().split('\n')
            for container in containers:
                if container:  # Skip empty lines
                    subprocess.run(["docker", "rm", "-f", container], check=False)
        except Exception as e:
            print(f"Error during cleanup: {str(e)}")
