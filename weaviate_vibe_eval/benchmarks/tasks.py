# Example code for connecting to Weaviate
EXAMPLE_CODE = """
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
)

assert client.is_ready()

client.close()
"""

# Define benchmark tasks
BENCHMARK_TASKS = {
    "zero_shot_connect": {
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
        "description": "Zero-shot: Basic Weaviate connection",
    },
    "in_context_connect": {
        "prompt": """
            Write Python code using the latest Weaviate client syntax,
            to connect to Weaviate Cloud using the environment variables
            WCD_TEST_URL and WCD_TEST_KEY.
            (WCD_TEST_URL is the URL of the Weaviate Cloud instance,
            and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

            Then check that the server is ready to accept requests.
            Don't do anything else.

            These environment variables are already set in the execution environment.

            Here is an example of how to connect to Weaviate:
            """
        + EXAMPLE_CODE,
        "description": "In-context: Basic Weaviate connection",
    },
    # Add more tasks as needed
}
