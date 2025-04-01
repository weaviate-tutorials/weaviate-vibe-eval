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
        use_prebuilt: bool = True,
        timeout: int = 30,
        memory_limit: str = "512m",
        network: str = "none",
        additional_volumes: Optional[Dict[str, str]] = None,
        port_mappings: Optional[Dict[int, int]] = None,
    ):
        """
        Initialize the Docker executor.

        Args:
            image: Docker image to use for execution
            use_prebuilt: Whether to use a prebuilt image with common packages
            timeout: Maximum execution time in seconds
            memory_limit: Maximum memory allocation for container
            network: Network mode (default 'none' for isolation)
            additional_volumes: Optional volumes to mount {host_path: container_path}
            port_mappings: Optional port mappings {container_port: host_port}
        """
        self.image = image
        self.use_prebuilt = use_prebuilt
        self.timeout = timeout
        self.memory_limit = memory_limit
        self.network = network
        self.additional_volumes = additional_volumes or {}
        self.port_mappings = port_mappings or {}

    def execute_code(
        self, code: str, inputs: Optional[Dict[str, Any]] = None,
        packages: Optional[List[str]] = None,
        env_vars: Optional[Dict[str, str]] = None
    ) -> Tuple[str, str, int]:
        """
        Execute the provided code within a Docker container.

        Args:
            code: Python code to execute
            inputs: Optional dictionary of input variables
            packages: Optional list of pip packages to install before execution
                     (only used if use_prebuilt=False)
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

            # Create setup script for installing packages if needed
            setup_command = ""
            if packages and not self.use_prebuilt:
                setup_script = os.path.join(temp_dir, "setup.sh")
                with open(setup_script, "w") as f:
                    f.write("#!/bin/bash\n")
                    f.write("pip install --no-cache-dir " + " ".join(packages) + "\n")
                os.chmod(setup_script, 0o755)  # Make script executable
                setup_command = "/code/setup.sh && "

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

            # Add port mappings if specified
            port_args = ""
            for container_port, host_port in self.port_mappings.items():
                port_args += f" -p {host_port}:{container_port}"

            # Add environment variables if specified
            env_args = ""
            if env_vars:
                for key, value in env_vars.items():
                    env_args += f" -e {key}={value}"

            # Simplified command when using prebuilt image and no custom packages
            if self.use_prebuilt and not packages:
                cmd = (
                    f"docker run --rm "
                    f"--name weaviate-exec-{execution_id} "
                    f"{volumes} "
                    f"{port_args} "
                    f"{env_args} "
                    f"--memory={self.memory_limit} "
                    f"--network={self.network} "
                    f"--workdir /code "
                    f"{self.image} "
                    f"python /code/code.py {input_args}"
                )
            else:
                # Regular command with timeout and package installation
                cmd = (
                    f"docker run --rm "
                    f"--name weaviate-exec-{execution_id} "
                    f"{volumes} "
                    f"{port_args} "
                    f"{env_args} "
                    f"--memory={self.memory_limit} "
                    f"--network={self.network} "
                    f"--workdir /code "
                    f"{self.image} "
                    f"bash -c '{setup_command}timeout {self.timeout} python /code/code.py {input_args}'"
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

    def cleanup(self):
        """
        Clean up resources used by the Docker executor.
        """
        # Find and remove any stalled containers from previous executions
        try:
            # List containers with our execution prefix
            result = subprocess.run(
                f"docker ps -a --filter name=weaviate-exec- --format '{{{{.Names}}}}'",
                shell=True, capture_output=True, text=True
            )

            if result.stdout.strip():
                # Found stalled containers, remove them
                print(f"Cleaning up stalled benchmark containers: {result.stdout.strip()}")
                for container in result.stdout.strip().split('\n'):
                    if container:
                        subprocess.run(f"docker rm -f {container}", shell=True)
        except Exception as e:
            print(f"Error during cleanup: {str(e)}")
            pass  # Best effort cleanup
