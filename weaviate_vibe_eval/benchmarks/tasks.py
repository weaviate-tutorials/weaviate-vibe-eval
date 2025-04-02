"""
Defines tasks for benchmarking LLM code generation capabilities for Weaviate.
Each task is defined as a Task object with its variants, examples, and canonical implementations.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any


class TaskVariant(Enum):
    """Defines different variants of a task."""
    ZERO_SHOT = auto()
    IN_CONTEXT = auto()
    EXTENSIVE_EXAMPLES = auto()


@dataclass
class Task:
    """
    Represents a benchmark task with its prompt, examples, and canonical implementation.
    """
    id: str
    description: str
    prompt: str
    examples: Dict[TaskVariant, Optional[str]] = field(default_factory=dict)
    canonical_implementation: str = ""  # Single canonical implementation for all variants

    def get_prompt_for_variant(self, variant: TaskVariant) -> str:
        """
        Get the full prompt for a specific variant of the task.
        This includes the base prompt and any examples for in-context variants.
        """
        if variant == TaskVariant.ZERO_SHOT:
            return self.prompt

        example = self.examples.get(variant)
        if not example:
            return self.prompt

        return f"{self.prompt}\n\nHere is some example code:\n\n{example}"

    def get_task_id_for_variant(self, variant: TaskVariant) -> str:
        """Get the full task ID for a specific variant."""
        variant_prefix = variant.name.lower()
        return f"{variant_prefix}_{self.id}"

    def get_variant_description(self, variant: TaskVariant) -> str:
        """Get the description for a specific variant."""
        variant_name = variant.name.capitalize().replace('_', ' ')
        return f"{variant_name}: {self.description}"


class TaskRegistry:
    """
    Registry that holds all task definitions and provides access to them.
    """
    def __init__(self):
        self._tasks: Dict[str, Task] = {}
        self._task_variants: Dict[str, Dict[str, Any]] = {}

    def register_task(self, task: Task) -> None:
        """
        Register a task with the registry.
        Also creates entries for all variants of the task.
        """
        self._tasks[task.id] = task

        # Create entries for each variant
        for variant in TaskVariant:
            if variant in task.examples or variant == TaskVariant.ZERO_SHOT:
                variant_id = task.get_task_id_for_variant(variant)
                self._task_variants[variant_id] = {
                    "prompt": task.get_prompt_for_variant(variant),
                    "description": task.get_variant_description(variant),
                    "task": task,
                    "variant": variant
                }

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by its ID."""
        return self._tasks.get(task_id)

    def get_task_variant(self, variant_id: str) -> Optional[Dict[str, Any]]:
        """Get a task variant by its full ID."""
        return self._task_variants.get(variant_id)

    def get_all_task_variants(self) -> Dict[str, Dict[str, Any]]:
        """Get all task variants."""
        return self._task_variants

    def get_all_tasks(self) -> Dict[str, Task]:
        """Get all base tasks."""
        return self._tasks

    def get_variant_ids_for_task(self, task_id: str) -> List[str]:
        """Get all variant IDs for a specific task."""
        task = self.get_task(task_id)
        if not task:
            return []

        return [
            task.get_task_id_for_variant(variant)
            for variant in TaskVariant
            if variant in task.examples or variant == TaskVariant.ZERO_SHOT
        ]

    def expand_task_names(self, task_names: Optional[List[str]]) -> Optional[List[str]]:
        """
        Expand base task names to include all variants.
        For example, 'connect' expands to ['zero_shot_connect', 'in_context_connect']

        If task_names is None, returns None (indicating all tasks should run).
        """
        if task_names is None:
            return None

        expanded_tasks = []

        for task_name in task_names:
            # Check if it's already a fully qualified task variant ID
            if task_name in self._task_variants:
                expanded_tasks.append(task_name)
            # Check if it's a base task name
            elif task_name in self._tasks:
                # Add all variants of this task
                expanded_tasks.extend(self.get_variant_ids_for_task(task_name))
            else:
                print(f"Warning: Unknown task '{task_name}'. Skipping.")

        return expanded_tasks


# Define the task registry instance
task_registry = TaskRegistry()

# Define the connect task
connect_task = Task(
    id="connect",
    description="Basic Weaviate connection",
    prompt="""
Write Python code using the latest Weaviate client syntax,
to connect to Weaviate Cloud using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the Weaviate Cloud instance,
and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

Then check that the server is ready to accept requests.
Don't do anything else.
""",
    examples={
        TaskVariant.IN_CONTEXT: """
import weaviate
from weaviate.classes.init import Auth

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
)

assert client.is_ready()

client.close()
"""
    },
    canonical_implementation="""
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
"""
)

# Define the create collection task
create_collection_task = Task(
    id="create_collection",
    description="Create a Weaviate collection with properties",
    prompt="""
Write Python code using the latest Weaviate client syntax,
to create a collection named "DemoProducts" with the following properties:
- name (text property)
- description (text property)
- price (number property)
- in_stock (boolean property)

Connect to Weaviate Cloud using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the Weaviate Cloud instance,
and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

If the collection already exists, delete it first.
""",
    examples={
        TaskVariant.IN_CONTEXT: """
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
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
""",
        TaskVariant.EXTENSIVE_EXAMPLES: """
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
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

# Another example - create a collection with a vectorizer
from weaviate.classes.config import Configure, Property, DataType

client.collections.create(
    "Article",
    vectorizer_config=Configure.Vectorizer.text2vec_openai(),
    properties=[  # properties configuration is optional
        Property(name="title", data_type=DataType.TEXT),
        Property(name="body", data_type=DataType.TEXT),
    ]
)

# Another example - create a collection with specific property configurations
from weaviate.classes.config import Configure, Property, DataType, Tokenization

client.collections.create(
    "Article",
    vectorizer_config=Configure.Vectorizer.text2vec_huggingface(),
    properties=[
        Property(
            name="title",
            data_type=DataType.TEXT,
            vectorize_property_name=True,  # Use "title" as part of the value to vectorize
            tokenization=Tokenization.LOWERCASE  # Use "lowecase" tokenization
        ),
        Property(
            name="body",
            data_type=DataType.TEXT,
            skip_vectorization=True,  # Don't vectorize this property
            tokenization=Tokenization.WHITESPACE  # Use "whitespace" tokenization
        ),
    ]
)

# Close connection
client.close()
"""
    },
    canonical_implementation="""
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Create the collection
collection_name = "DemoProducts"

# Delete the collection if it already exists
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

# Close connection
client.close()
"""
)

# Register all tasks
task_registry.register_task(connect_task)
task_registry.register_task(create_collection_task)

# For backward compatibility
BENCHMARK_TASKS = task_registry.get_all_task_variants()

# Enum-like class for task types (makes referring to tasks more explicit)
class TaskType:
    """
    Enum-like class for task types.
    Provides constants for all registered task variants.
    """
    # Dynamic generation of task constants
    for task_id in BENCHMARK_TASKS.keys():
        locals()[task_id.upper()] = task_id

    @classmethod
    def all(cls):
        """Return all task types as a list."""
        return [
            v
            for k, v in cls.__dict__.items()
            if not k.startswith("_") and not callable(getattr(cls, k))
        ]

    @classmethod
    def zero_shot_tasks(cls):
        """Return all zero-shot tasks."""
        return [v for v in cls.all() if v.startswith("zero_shot_")]

    @classmethod
    def in_context_tasks(cls):
        """Return all in-context tasks."""
        return [v for v in cls.all() if v.startswith("in_context_")]

    @classmethod
    def extensive_examples_tasks(cls):
        """Return all tasks with extensive examples."""
        return [v for v in cls.all() if v.startswith("extensive_examples_")]
