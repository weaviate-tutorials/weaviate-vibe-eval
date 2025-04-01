"""Repository of canonical implementations for Weaviate tasks."""

CANONICAL_IMPLEMENTATIONS = {
    "zero_shot_connect": """
import os
import weaviate
from weaviate.classes.init import Auth

# Get credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Verify connection
assert client.is_ready()

# Close connection
client.close()
""",

    "in_context_connect": """
import os
import weaviate
from weaviate.classes.init import Auth

# Get credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Verify connection
assert client.is_ready()

# Close connection
client.close()
""",

    # Add more canonical implementations for other tasks as needed
}
