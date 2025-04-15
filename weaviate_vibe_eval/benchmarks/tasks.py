"""
Defines tasks for benchmarking LLM code generation capabilities for Weaviate.
Each task is defined as a Task object with its variants, examples, and canonical implementations.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from weaviate_vibe_eval.benchmarks.extensive_example_set import EXTENSIVE_EXAMPLE_SET


def preload_wine_reviews():
    import weaviate
    from weaviate.classes.init import Auth
    import weaviate_datasets as wd
    import os

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ.get("WCD_TEST_URL"),
        auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY")),
        headers={"X-OpenAI-API-Key": os.environ.get("OPENAI_API_KEY")},
    )

    if not client.collections.exists("WineReview"):
        print("Loading WineReviews dataset...")
        d = wd.datasets.WineReviews()
        d.upload_dataset(client, overwrite=True)
    else:
        print("WineReviews dataset already loaded")

    client.close()
    return True


def create_demo_products_collection():
    import weaviate
    from weaviate.classes.init import Auth
    from weaviate.classes.config import Configure, Property, DataType
    import os

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ.get("WCD_TEST_URL"),
        auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY")),
    )

    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    client.collections.create(
        "DemoProducts",
        vectorizer_config=Configure.Vectorizer.none(),
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    client.close()
    return True


class TaskVariant(Enum):
    """Defines different variants of a task."""
    ZERO_SHOT = auto()
    SIMPLE_EXAMPLE = auto()
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
    preparatory_steps: List[str] = field(default_factory=list)  # List of preparatory step function names to run

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
        For example, 'connect' expands to ['zero_shot_connect', 'simple_example_connect']

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
        TaskVariant.SIMPLE_EXAMPLE: """
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
        TaskVariant.SIMPLE_EXAMPLE: """
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
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Created collection: {products_collection.name}")

# Close connection
client.close()
""",
        TaskVariant.EXTENSIVE_EXAMPLES: EXTENSIVE_EXAMPLE_SET
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
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

# Close connection
client.close()
"""
)

# Define the query task
simple_query_task = Task(
    id="basic_semantic_search",
    description="Query a collection to find objects that match a natural language query",
    prompt="""
Write Python code using the latest Weaviate client syntax,
to query the 'WineReview' collection and find wines that
best match the query "dessert wine",
with a limit of maximum 2 results.

The WineReview collection uses the text2vec-openai vectorizer.
The API key is stored in the environment variable OPENAI_API_KEY.

Connect to Weaviate Cloud using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the Weaviate Cloud instance,
and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

Print the title, country, price, and points of each matching wine.
""",
    preparatory_steps=["preload_wine_reviews"],  # This task requires the WineReviews dataset to be loaded
    examples={
        TaskVariant.SIMPLE_EXAMPLE: """
import weaviate
from weaviate.classes.init import Auth
import os

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>),
    headers={
        "X-OpenAI-API-Key": <OPENAI_API_KEY>
    },
)

collection = client.collections.get("<COLLECTION_NAME>")

response = collection.query.near_text(
    query="<YOUR_QUERY>",
    limit=<max_k_results>
)

for obj in response.objects:
    print(obj.properties)  # Print all properties of the object

client.close()
""",
        TaskVariant.EXTENSIVE_EXAMPLES: EXTENSIVE_EXAMPLE_SET
    },
    canonical_implementation="""
import weaviate
from weaviate.classes.init import Auth
import os


client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY")),
    headers={"X-OpenAI-API-Key": os.environ.get("OPENAI_API_KEY")},
)

wine_reviews = client.collections.get("WineReview")

response = wine_reviews.query.near_text(query="dessert wine", limit=2)

for obj in response.objects:
    print("---")
    print(obj.properties["title"])
    print(obj.properties["country"])
    print(obj.properties["price"])
    print(obj.properties["points"])

client.close()
"""
)


complex_hybrid_query_task = Task(
    id="complex_hybrid_query",
    description="Query a collection to find objects that match a natural language query",
    prompt="""
Write Python code using the latest Weaviate client syntax,
to query the 'WineReview' collection and find wines that
best match the query "pair with steak",
with a limit of maximum 5 results,
and a hybrid search with alpha=0.5.

Each result must be have a price less than 50 and a points greater than 90.
Each result must contain at least one of the substrings "spice", "fruit", "berry", "cherry", or "honey" in the review_body.

The WineReview collection uses the text2vec-openai vectorizer.
The API key is stored in the environment variable OPENAI_API_KEY.

Connect to Weaviate Cloud using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the Weaviate Cloud instance,
and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

Print the title, country, price, and points of each matching wine.
""",
    preparatory_steps=["preload_wine_reviews"],  # This task requires the WineReviews dataset to be loaded
    examples={
        TaskVariant.SIMPLE_EXAMPLE: """
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>),
    headers={
        "X-OpenAI-API-Key": <OPENAI_API_KEY>
    },
)

collection = client.collections.get("<COLLECTION_NAME>")

response = collection.query.hybrid(
    query="<YOUR_QUERY>",
    limit=<max_k_results>,
    alpha=<alpha>,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    ),
    return_metadata=MetadataQuery(score=True)
)

for obj in response.objects:
    print(obj.properties)  # Print all properties of the object
    print(f"Score: {obj.metadata.score}")

client.close()
""",
        TaskVariant.EXTENSIVE_EXAMPLES: EXTENSIVE_EXAMPLE_SET
    },
    canonical_implementation="""
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY")),
    headers={"X-OpenAI-API-Key": os.environ.get("OPENAI_API_KEY")},
)

wine_reviews = client.collections.get("WineReview")

response = wine_reviews.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    ),
    return_metadata=MetadataQuery(score=True)
)

for obj in response.objects:
    print("---")
    print(obj.properties["title"])
    print(obj.properties["country"])
    print(obj.properties["price"])
    print(obj.properties["points"])
    print(obj.metadata.score)

client.close()
"""
)

batch_import_task = Task(
    id="batch_import",
    description="Batch import data into a collection",
    prompt="""
Write Python code using the latest Weaviate client syntax,
to add objects to a collection named "DemoProducts" with the following properties:
- name (text property)
- description (text property)

Then, batch import 50 arbitrary objects into the collection.
The object can be as simple as:
{
    "name": "Product {i}",
    "description": "Description {i}"
}

Connect to Weaviate Cloud using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the Weaviate Cloud instance,
and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.)

Then, print the number of objects in the collection.
""",
    preparatory_steps=["create_demo_products_collection"],
    examples={
        TaskVariant.SIMPLE_EXAMPLE: """
import weaviate

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>),
)

collection = client.collections.get("<COLLECTION_NAME>")

data_rows = [
    {"title": f"Object {i+1}"} for i in range(5)
]

with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

print(len(collection))

client.close()
""",
        TaskVariant.EXTENSIVE_EXAMPLES: EXTENSIVE_EXAMPLE_SET
    },
    canonical_implementation="""
import weaviate

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY")),
)

products = client.collections.get("DemoProducts")

data_rows = [
    {
        "name": f"Product {i+1}",
        "description": f"Description {i+1}"
    } for i in range(50)
]

with products.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

print(len(collection))

client.close()
"""
)

made_up_syntax_task = Task(
    id="made_up_syntax",
    description="Test made up syntax, to test instruction following",
    prompt="""
Write Python code using the v8 Weaviate client (`import wv8`) syntax,
to query objects from a Weaviate ObjectStore named "Shop", with ObjectSubSets "Books" and "Games".

Connect to an online WeaviateLite instance, using the environment variables
WCD_TEST_URL and WCD_TEST_KEY.
(WCD_TEST_URL is the URL of the WeaviateLite instance,
and WCD_TEST_KEY is the API key for the WeaviateLite instance.)

Then, ask the WeaviateLite instance to fetch objects from
the given ObjectSubSets, based on the user query
"space exploration related products for my nephew", using
WeaviateLite's query decomposition feature, and a maximum of 10 results.

Then, print the retrieved collection with `print(response)`.
""",
    examples={
        TaskVariant.SIMPLE_EXAMPLE: """
import wv8

lite_client = wv8.connect.WeaviateLite(
    cluster_url="https://your-weaviate-cloud-instance.url",
    auth_credentials="your-api-key"
)

object_store = lite_client.stores.connect(store_id="shop")

response = object_store.retrieve(
    user_query="<USER_QUERY>",
    store_query_strategy="<QUERY_STRATEGY>",  # Could be "decomposition", "agentic", "semantic", "hybrid",
    # object_subsets=["<OBJECT_SUBSET_1>", "<OBJECT_SUBSET_2>"]  # Could include wildcards "*" or "?"
    # max_results=<MAX_RESULTS>
    # max_threshold=<MAX_THRESHOLD>
    # use_graph_search=<USE_GRAPH_SEARCH>
)

print(response)
"""
    },
    canonical_implementation="""
import wv8
import os

lite_client = wv8.connect.WeaviateLite(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=os.environ.get("WCD_TEST_KEY")
)

object_store = lite_client.stores.connect(store_id="Shop")

response = object_store.retrieve(
    user_query="space exploration related products for my nephew",
    store_query_strategy="decomposition",
    object_subsets=["Books", "Games"],
    max_results=10
)

print(response)
"""
)

# Register all tasks
task_registry.register_task(connect_task)
task_registry.register_task(create_collection_task)
task_registry.register_task(simple_query_task)
task_registry.register_task(complex_hybrid_query_task)
task_registry.register_task(batch_import_task)
task_registry.register_task(made_up_syntax_task)

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
    def simple_example_tasks(cls):
        """Return all in-context tasks."""
        return [v for v in cls.all() if v.startswith("simple_example_")]

    @classmethod
    def extensive_examples_tasks(cls):
        """Return all tasks with extensive examples."""
        return [v for v in cls.all() if v.startswith("extensive_examples_")]
