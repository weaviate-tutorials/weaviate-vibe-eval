# This file contains extensive examples of how to use the Weaviate API.
# To be used as one big context for the LLM to reference.

EXTENSIVE_EXAMPLE_SET = """
# ================================
# Connect to Weaviate
# ================================
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=<CLUSTER_URL>,
    auth_credentials=Auth.api_key(<API_KEY>)
)

# ================================
# Create a collection
# ================================
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

# Another example - create a collection with a vectorizer
from weaviate.classes.config import Configure, Property, DataType

# ================================
# Create a collection with a vectorizer
# ================================
client.collections.create(
    "Article",
    vectorizer_config=Configure.Vectorizer.text2vec_openai(),
    properties=[  # properties configuration is optional
        Property(name="title", data_type=DataType.TEXT),
        Property(name="body", data_type=DataType.TEXT),
        Property(name="published", data_type=DataType.BOOL),
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

# ================================
# Batch import
# ================================
data_rows = [
    {"title": f"Object {i+1}"} for i in range(5)
]

collection = client.collections.get("MyCollection")

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

# Print the number of objects in the collection
print(len(collection))

# ================================
# Object retrieval (in order of UUID) with metadata
# ================================
from weaviate.classes.query import MetadataQuery

jeopardy = client.collections.get("JeopardyQuestion")
response = jeopardy.query.fetch_objects(
    limit=1,
    return_metadata=MetadataQuery(creation_time=True)
)

for o in response.objects:
    print(o.properties)  # View the returned properties
    print(o.metadata.creation_time)  # View the returned creation time

# ================================
# Simple semantic search with distance
# ================================
from weaviate.classes.query import MetadataQuery

jeopardy = client.collections.get("JeopardyQuestion")
response = jeopardy.query.near_text(
    query="animals in movies",
    limit=2,
    return_metadata=MetadataQuery(distance=True)
)

for o in response.objects:
    print(o.properties)
    print(o.metadata.distance)

# ================================
# Keyword search with scores
# ================================
from weaviate.classes.query import MetadataQuery

jeopardy = client.collections.get("JeopardyQuestion")
response = jeopardy.query.bm25(
    query="food",
    return_metadata=MetadataQuery(score=True),
    limit=3
)

for o in response.objects:
    print(o.properties)
    print(o.metadata.score)

# ================================
# Hybrid search with scores & explanation of each component
# ================================
from weaviate.classes.query import MetadataQuery

jeopardy = client.collections.get("JeopardyQuestion")
response = jeopardy.query.hybrid(
    query="food",
    alpha=0.5,
    return_metadata=MetadataQuery(score=True, explain_score=True),
    limit=3,
)

for o in response.objects:
    print(o.properties)
    print(o.metadata.score, o.metadata.explain_score)

# ================================
# Filter with one condition
# ================================
from weaviate.classes.query import Filter

jeopardy = client.collections.get("JeopardyQuestion")
response = jeopardy.query.fetch_objects(
    filters=Filter.by_property("round").equal("Double Jeopardy!"),
    limit=3
)

for o in response.objects:
    print(o.properties)

# ================================
# Filter with multiple conditions
# ================================
from weaviate.classes.query import Filter

jeopardy = client.collections.get("JeopardyQuestion")
response = jeopardy.query.fetch_objects(
    # Use & as AND
    #     | as OR
    filters=(
        Filter.by_property("round").equal("Double Jeopardy!") &
        Filter.by_property("points").less_than(600)
    ),
    limit=3
)

for o in response.objects:
    print(o.properties)

# ================================
# ContainsAny filter
# ================================
from weaviate.classes.query import Filter

jeopardy = client.collections.get("JeopardyQuestion")

token_list = ["australia", "india"]
response = jeopardy.query.fetch_objects(
    # Find objects where the `answer` property contains any of the strings in `token_list`
    filters=Filter.by_property("answer").contains_any(token_list),
    limit=3
)

for o in response.objects:
    print(o.properties)

# Close connection
client.close()
"""
