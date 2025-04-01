CONNECT_TASK = """
Write Python code using the latest Weaviate client syntax,
to connect to Weaviate Cloud using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the Weaviate Cloud instance,
and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

Then check that the server is ready to accept requests.
Don't do anything else.
"""


# Example code for connecting to Weaviate
CONNECT_EXAMPLE = """
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
)

assert client.is_ready()

client.close()
"""

# Define more task prompts and examples
CREATE_COLLECTION_TASK = """
Write Python code using the latest Weaviate client syntax,
to create a collection named "DemoProducts" with the following properties:
- name (text property)
- description (text property)
- price (number property)
- in_stock (boolean property)

Use environment variables WCD_TEST_URL and WCD_TEST_KEY to connect.
Make sure to check that the server is ready before creating the collection.

If the collection already exists, delete it first.
"""

CREATE_COLLECTION_EXAMPLE = """
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY"))
)

# Create the collection
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)

print(f"Created collection: {products_collection.name}")

# Close connection
client.close()
"""

# Task templates - reusable content for different task types
TASK_TEMPLATES = {
    "connect": {
        "prompt": CONNECT_TASK,
        "description": "Basic Weaviate connection",
        "example": CONNECT_EXAMPLE,
    },
    "create_collection": {
        "prompt": CREATE_COLLECTION_TASK,
        "description": "Create a Weaviate collection with properties",
        "example": CREATE_COLLECTION_EXAMPLE,
    },
    # Add more task templates here
}

# Helper function to create in-context version of a task
def create_in_context_task(task_key):
    """Create an in-context version of a task using its example code."""
    template = TASK_TEMPLATES.get(task_key)
    if not template:
        raise ValueError(f"Task template '{task_key}' not found")

    return {
        "prompt": template["prompt"] + "\n\nHere is an example:\n\n" + template["example"],
        "description": f"In-context: {template['description']}",
    }

# Helper function to create zero-shot version of a task
def create_zero_shot_task(task_key):
    """Create a zero-shot version of a task (no examples)."""
    template = TASK_TEMPLATES.get(task_key)
    if not template:
        raise ValueError(f"Task template '{task_key}' not found")

    return {
        "prompt": template["prompt"],
        "description": f"Zero-shot: {template['description']}",
    }

# Define a task factory to create different variations of tasks
class TaskFactory:
    @staticmethod
    def create_task(task_type, variant):
        """Create a task with the specified type and variant.

        Args:
            task_type: The type of task (e.g., "connect", "create_collection")
            variant: The variant of the task (e.g., "zero_shot", "in_context")

        Returns:
            A task dictionary with prompt and description
        """
        if variant == "zero_shot":
            return create_zero_shot_task(task_type)
        elif variant == "in_context":
            return create_in_context_task(task_type)
        else:
            raise ValueError(f"Unknown task variant: {variant}")

    @staticmethod
    def create_all_variants(task_type):
        """Create all variants of a task type."""
        return {
            f"zero_shot_{task_type}": create_zero_shot_task(task_type),
            f"in_context_{task_type}": create_in_context_task(task_type),
        }

# Build benchmark tasks using the task factory
BENCHMARK_TASKS = {}
# Add all variants of all task types
for task_type in TASK_TEMPLATES.keys():
    BENCHMARK_TASKS.update(TaskFactory.create_all_variants(task_type))

# Enum-like class for task types (makes referring to tasks more explicit)
class TaskType:
    # Dynamic generation of task constants
    for task_id in BENCHMARK_TASKS.keys():
        locals()[task_id.upper()] = task_id

    @classmethod
    def all(cls):
        """Return all task types as a list."""
        return [v for k, v in cls.__dict__.items()
                if not k.startswith('_') and not callable(getattr(cls, k))]

    @classmethod
    def zero_shot_tasks(cls):
        """Return all zero-shot tasks."""
        return [v for v in cls.all() if v.startswith("zero_shot_")]

    @classmethod
    def in_context_tasks(cls):
        """Return all in-context tasks."""
        return [v for v in cls.all() if v.startswith("in_context_")]
