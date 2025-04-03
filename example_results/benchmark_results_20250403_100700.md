# Weaviate Benchmark Results

Generated on: 2025-04-03 10:07:00

## Summary

- **anthropic/claude-3-7-sonnet-20250219**: 10/14 tasks successful
- **anthropic/claude-3-5-sonnet-20241022**: 9/14 tasks successful
- **anthropic/claude-3-5-haiku-20241022**: 8/14 tasks successful
- **cohere/command-a-03-2025**: 2/14 tasks successful
- **cohere/command-r-plus-08-2024**: 1/14 tasks successful
- **gemini/gemini-2.5-pro-exp-03-25**: 11/14 tasks successful
- **gemini/gemini-2.0-flash-lite**: 6/14 tasks successful
- **openai/gpt-4o-2024-11-20**: 1/14 tasks successful
- **openai/gpt-4o-mini-2024-07-18**: 3/14 tasks successful
## Detailed Results

### anthropic/claude-3-7-sonnet-20250219

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 6.11s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.embedded import EmbeddedOptions

# Get environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url or not wcd_api_key:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set")

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=wcd_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=wcd_api_key),
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready!")
else:
    print("Weaviate server is not ready!")

# Close the connection
client.close()
```

**Output**:
```
Weaviate server is ready!

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.44s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.25s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables")

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
)

# Collection name
collection_name = "DemoProducts"

# Check if collection exists and delete it if it does
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' exists. Deleting it...")
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")

# Create the collection with properties
collection = client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)

print(f"Collection '{collection_name}' created successfully with the specified properties.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 35, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN),
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.97s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY"))
)

# Create the collection
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the collection with the specified properties
products_collection = client.collections.create(
    name=collection_name,
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
```

**Output**:
```
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.72s)

**Generated Code**:
```python
# ================================
# Connect to Weaviate
# ================================
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get environment variables for Weaviate Cloud connection
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# ================================
# Create a collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing '{collection_name}' collection")

# Create the DemoProducts collection with the specified properties
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Created '{collection_name}' collection with the following properties:")
print("- name (text property)")
print("- description (text property)")
print("- price (number property)")
print("- in_stock (boolean property)")

# Close connection
client.close()
```

**Output**:
```
Deleted existing 'DemoProducts' collection
Created 'DemoProducts' collection with the following properties:
- name (text property)
- description (text property)
- price (number property)
- in_stock (boolean property)

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.21s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import QueryNearText

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
    headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Query for wines matching "dessert wine"
response = (
    client.collections.get("WineReview")
    .query.near_text(
        query="dessert wine",
        limit=2
    )
    .with_additional(["distance"])
    .objects
)

# Print the results
print("Wines matching 'dessert wine':")
print("-" * 50)
for wine in response:
    properties = wine.properties
    print(f"Title: {properties.get('title', 'N/A')}")
    print(f"Country: {properties.get('country', 'N/A')}")
    print(f"Price: ${properties.get('price', 'N/A')}")
    print(f"Points: {properties.get('points', 'N/A')}")
    print(f"Distance: {wine.metadata.distance:.4f}")
    print("-" * 50)

# Close the client
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes.query import QueryNearText
ImportError: cannot import name 'QueryNearText' from 'weaviate.classes.query' (/usr/local/lib/python3.9/site-packages/weaviate/classes/query.py)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.24s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key),
    headers={
        "X-OpenAI-API-Key": openai_api_key
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Query for wines matching "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the results
for obj in response.objects:
    print(f"Title: {obj.properties.get('title', 'N/A')}")
    print(f"Country: {obj.properties.get('country', 'N/A')}")
    print(f"Price: ${obj.properties.get('price', 'N/A')}")
    print(f"Points: {obj.properties.get('points', 'N/A')}")
    print("-" * 50)

# Close the client
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88
--------------------------------------------------

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 11.08s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_api_key),
    headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Query for wines matching "dessert wine"
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_metadata=MetadataQuery(distance=True)
)

# Print the results
print("Wines matching 'dessert wine':")
print("-" * 50)
for wine in response.objects:
    print(f"Title: {wine.properties.get('title', 'N/A')}")
    print(f"Country: {wine.properties.get('country', 'N/A')}")
    print(f"Price: ${wine.properties.get('price', 'N/A')}")
    print(f"Points: {wine.properties.get('points', 'N/A')}")
    print(f"Similarity: {1 - wine.metadata.distance:.4f}")
    print("-" * 50)

# Close the connection
client.close()
```

**Output**:
```
Wines matching 'dessert wine':
--------------------------------------------------
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88
Similarity: 0.5351
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88
Similarity: 0.5188
--------------------------------------------------

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.40s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import QueryReference
from weaviate.classes.filters import Filter

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
    headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Create a filter for price < 50 and points > 90
price_points_filter = Filter.by_property("price").less_than(50).and_filter(
    Filter.by_property("points").greater_than(90)
)

# Create a filter for review_body containing at least one of the specified substrings
review_body_filter = (
    Filter.by_property("review_body").contains_any_text(["spice", "fruit", "berry", "cherry", "honey"])
)

# Combine the filters
combined_filter = price_points_filter.and_filter(review_body_filter)

# Query the WineReview collection
response = (
    client.collections.get("WineReview")
    .query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points", "review_body"]
    )
)

# Print the results
print("Wines that pair well with steak:")
print("-" * 50)
for wine in response.objects:
    props = wine.properties
    print(f"Title: {props['title']}")
    print(f"Country: {props['country']}")
    print(f"Price: ${props['price']}")
    print(f"Points: {props['points']}")
    print("-" * 50)

# Close the client
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.classes.filters import Filter
ModuleNotFoundError: No module named 'weaviate.classes.filters'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.90s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key),
    headers={
        "X-OpenAI-API-Key": openai_api_key
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform hybrid search
response = collection.query.hybrid(
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

# Print results
print(f"Found {len(response.objects)} matching wines:\n")

for obj in response.objects:
    print(f"Title: {obj.properties.get('title')}")
    print(f"Country: {obj.properties.get('country')}")
    print(f"Price: ${obj.properties.get('price')}")
    print(f"Points: {obj.properties.get('points')}")
    print(f"Score: {obj.metadata.score:.4f}")
    print("-" * 50)

# Close the client
client.close()
```

**Output**:
```
Found 5 matching wines:

Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
Score: 0.5000
--------------------------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Score: 0.4632
--------------------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.2212
--------------------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.0658
--------------------------------------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
Score: 0.0149
--------------------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.67s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery, Filter

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Configure OpenAI API key for text2vec-openai vectorizer
client.connect_to_embedded_systems.connect_to_openai(
    api_key=os.environ["OPENAI_API_KEY"]
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Define the filter for price < 50 and points > 90
# Also filter for reviews containing at least one of the specified substrings
price_points_filter = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90)
)

# Define the substring filter using contains_any
substring_filter = Filter.by_property("review_body").contains_any([
    "spice", "fruit", "berry", "cherry", "honey"
])

# Combine the filters
combined_filter = price_points_filter & substring_filter

# Perform hybrid search with the combined filter
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,  # Equal weight between vector and keyword search
    filters=combined_filter,
    limit=5,
    return_metadata=MetadataQuery(score=True)
)

# Print the results
print(f"Found {len(response.objects)} matching wines:\n")

for wine in response.objects:
    print(f"Title: {wine.properties.get('title')}")
    print(f"Country: {wine.properties.get('country')}")
    print(f"Price: ${wine.properties.get('price')}")
    print(f"Points: {wine.properties.get('points')}")
    print(f"Score: {wine.metadata.score}")
    print("-" * 50)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client.connect_to_embedded_systems.connect_to_openai(
AttributeError: 'WeaviateClient' object has no attribute 'connect_to_embedded_systems'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 10.56s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType, Configure
from weaviate.collections import Collection

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
)

# Check if collection exists, if not create it
if not client.collections.exists("DemoProducts"):
    # Create collection with properties
    collection = client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
    )
    print("Collection 'DemoProducts' created.")
else:
    # Get existing collection
    collection = client.collections.get("DemoProducts")
    print("Collection 'DemoProducts' already exists.")

# Prepare batch of objects
objects_to_add = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    }
    for i in range(1, 51)
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for obj in objects_to_add:
        batch.add_object(
            properties=obj
        )

# Get and print the number of objects in the collection
count = collection.aggregate.over_all().total_count
print(f"Number of objects in the collection: {count}")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists.
Number of objects in the collection: 50

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 9.88s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth

# Connect to Weaviate Cloud using environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key),
)

# Check if collection exists, if not create it
if "DemoProducts" not in client.collections.list_all():
    collection = client.collections.create(
        name="DemoProducts",
        properties=[
            {"name": "name", "dataType": ["text"]},
            {"name": "description", "dataType": ["text"]}
        ]
    )
else:
    collection = client.collections.get("DemoProducts")

# Prepare data for batch import
data_rows = [
    {
        "name": f"Product {i+1}",
        "description": f"Description for product {i+1}. This is a sample product."
    } for i in range(50)
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed objects
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Number of objects in the DemoProducts collection: {len(collection)}")

# Close the client
client.close()
```

**Output**:
```
Number of objects in the DemoProducts collection: 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 12.04s)

**Generated Code**:
```python
# ================================
# Connect to Weaviate
# ================================
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ.get("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.environ.get("WCD_TEST_KEY"))
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
    ]
)

# ================================
# Batch import 50 arbitrary objects
# ================================
data_rows = [
    {
        "name": f"Product {i+1}",
        "description": f"Description for product {i+1}"
    } for i in range(50)
]

with products_collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

failed_objects = products_collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Number of objects in the collection: {len(products_collection)}")

# Close connection
client.close()
```

**Output**:
```
Number of objects in the collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

### anthropic/claude-3-5-sonnet-20241022

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 3.19s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.embedded import EmbeddedOptions

# Get credentials from environment variables
url = os.getenv('WCD_TEST_URL')
api_key = os.getenv('WCD_TEST_KEY')

# Create client
client = weaviate.Client(
    url=url,
    auth_client_secret=weaviate.AuthApiKey(api_key)
)

# Check if server is ready
if client.is_ready():
    print("Weaviate server is ready")
else:
    print("Weaviate server is not ready")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:10: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.79s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Get environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check if the server is ready
assert client.is_ready()

# Close the connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.50s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes import Properties, Collection

# Get credentials from environment variables
WEAVIATE_URL = os.getenv('WCD_TEST_URL')
WEAVIATE_API_KEY = os.getenv('WCD_TEST_KEY')

# Initialize the client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Delete the collection if it already exists
try:
    client.collections.delete("DemoProducts")
    print("Existing DemoProducts collection deleted")
except:
    print("No existing DemoProducts collection to delete")

# Create the collection with the specified properties
products = client.collections.create(
    name="DemoProducts",
    properties=[
        Properties.text(name="name", description="The name of the product"),
        Properties.text(name="description", description="The description of the product"),
        Properties.number(name="price", description="The price of the product"),
        Properties.boolean(name="in_stock", description="Whether the product is in stock")
    ]
)

print("DemoProducts collection created successfully")

# Verify the collection exists
collections = client.collections.list()
for collection in collections:
    if collection.name == "DemoProducts":
        print("Collection properties:")
        for prop in collection.properties:
            print(f"- {prop.name}: {prop.data_type}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes import Properties, Collection
ImportError: cannot import name 'Properties' from 'weaviate.classes' (/usr/local/lib/python3.9/site-packages/weaviate/classes/__init__.py)

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.63s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Create the collection
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the collection with properties
products_collection = client.collections.create(
    name=collection_name,
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
```

**Output**:
```
Deleted existing collection: DemoProducts
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 11.44s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with specified properties
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

# Verify the collection was created
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' created successfully!")
else:
    print(f"Failed to create collection '{collection_name}'")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' created successfully!

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.71s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes import Generate

# Get credentials from environment variables
weaviate_url = os.getenv('WCD_TEST_URL')
weaviate_api_key = os.getenv('WCD_TEST_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Create Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the query
response = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({
        "concepts": ["dessert wine"]
    })
    .with_limit(2)
    .do()
)

# Print results
if response and "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
    wines = response["data"]["Get"]["WineReview"]
    for wine in wines:
        print("\nWine Details:")
        print(f"Title: {wine.get('title', 'N/A')}")
        print(f"Country: {wine.get('country', 'N/A')}")
        print(f"Price: ${wine.get('price', 'N/A')}")
        print(f"Points: {wine.get('points', 'N/A')}")
else:
    print("No results found")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes import Generate
ImportError: cannot import name 'Generate' from 'weaviate.classes' (/usr/local/lib/python3.9/site-packages/weaviate/classes/__init__.py)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.20s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Get environment variables
cluster_url = os.getenv('WCD_TEST_URL')
api_key = os.getenv('WCD_TEST_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
    headers={
        "X-OpenAI-API-Key": openai_api_key
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Query for dessert wines
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print results
for obj in response.objects:
    print(f"Title: {obj.properties.get('title', 'N/A')}")
    print(f"Country: {obj.properties.get('country', 'N/A')}")
    print(f"Price: ${obj.properties.get('price', 'N/A')}")
    print(f"Points: {obj.properties.get('points', 'N/A')}")
    print("-" * 50)

# Close the client connection
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88
--------------------------------------------------

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 13.26s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery

# Connect to Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")  # OpenAI API key for text2vec-openai
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Perform semantic search for dessert wines
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_metadata=MetadataQuery(distance=True)
)

# Print results
for wine in response.objects:
    print(f"Title: {wine.properties.get('title', 'N/A')}")
    print(f"Country: {wine.properties.get('country', 'N/A')}")
    print(f"Price: ${wine.properties.get('price', 'N/A')}")
    print(f"Points: {wine.properties.get('points', 'N/A')}")
    print(f"Similarity: {1 - wine.metadata.distance:.4f}")  # Convert distance to similarity
    print("-" * 50)

# Close the client connection
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88
Similarity: 0.5351
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88
Similarity: 0.5188
--------------------------------------------------

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.54s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes import Filter

# Get credentials from environment variables
WEAVIATE_URL = os.getenv('WCD_TEST_URL')
WEAVIATE_API_KEY = os.getenv('WCD_TEST_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Create Weaviate client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
)

# Define the query
query = (
    client.query
    .get("WineReview", [
        "title",
        "country",
        "price",
        "points",
        "review_body"
    ])
    .with_hybrid(
        query="pair with steak",
        alpha=0.5
    )
    .with_where(Filter.and_([
        Filter.less_than("price", 50),
        Filter.greater_than("points", 90),
        Filter.or_([
            Filter.like("review_body", f"*{term}*") 
            for term in ["spice", "fruit", "berry", "cherry", "honey"]
        ])
    ]))
    .with_limit(5)
)

# Execute the query
result = query.do()

# Print results
if 'data' in result and 'Get' in result['data'] and 'WineReview' in result['data']['Get']:
    wines = result['data']['Get']['WineReview']
    if wines:
        print("\nMatching Wines:")
        print("-" * 50)
        for wine in wines:
            print(f"Title: {wine['title']}")
            print(f"Country: {wine['country']}")
            print(f"Price: ${wine['price']}")
            print(f"Points: {wine['points']}")
            print("-" * 50)
    else:
        print("No matching wines found.")
else:
    print("Error: Unable to retrieve results")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes import Filter
ImportError: cannot import name 'Filter' from 'weaviate.classes' (/usr/local/lib/python3.9/site-packages/weaviate/classes/__init__.py)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.05s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Get environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
    headers={
        "X-OpenAI-API-Key": openai_api_key
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Define the search terms for review_body
search_terms = ["spice", "fruit", "berry", "cherry", "honey"]

# Perform hybrid search
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(search_terms)
    ),
    return_metadata=MetadataQuery(score=True)
)

# Print results
print("\nMatching Wines:")
print("--------------")
for obj in response.objects:
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: ${obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
    print(f"Relevance Score: {obj.metadata.score:.4f}")
    print("--------------")

# Close the client
client.close()
```

**Output**:
```

Matching Wines:
--------------
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
Relevance Score: 0.5000
--------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Relevance Score: 0.4630
--------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Relevance Score: 0.2213
--------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Relevance Score: 0.0656
--------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
Relevance Score: 0.0147
--------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 13.86s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Define the flavor terms to search for in review_body
flavor_terms = ["spice", "fruit", "berry", "cherry", "honey"]

# Create the hybrid search query with filters
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,  # Equal weight between vector and keyword search
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(flavor_terms)
    ),
    return_metadata=MetadataQuery(score=True),
    limit=5
)

# Print the results
print("\nBest wine matches for pairing with steak:")
print("==========================================")
for wine in response.objects:
    print(f"\nTitle: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: ${wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print(f"Match Score: {wine.metadata.score}")

# Close the client connection
client.close()
```

**Output**:
```

Best wine matches for pairing with steak:
==========================================

Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
Match Score: 0.5

Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Match Score: 0.4629642069339752

Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Match Score: 0.2213282436132431

Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Match Score: 0.065570168197155

Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
Match Score: 0.01466419454663992

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.41s)

**Generated Code**:
```python
import weaviate
import os
from typing import List
import time

# Get environment variables
WEAVIATE_URL = os.getenv('WCD_TEST_URL')
WEAVIATE_API_KEY = os.getenv('WCD_TEST_KEY')

# Configure client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Define the collection
collection_name = "DemoProducts"

# Create collection if it doesn't exist
try:
    client.collections.delete(collection_name)
except:
    pass

client.collections.create(
    name=collection_name,
    properties=[
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
    ]
)

# Prepare objects for batch import
def generate_objects(num_objects: int) -> List[dict]:
    return [
        {
            "name": f"Product {i}",
            "description": f"Description for product {i}"
        }
        for i in range(num_objects)
    ]

# Batch import objects
collection = client.collections.get(collection_name)
objects = generate_objects(50)

# Configure batch
client.batch.configure(
    batch_size=10,  # Number of objects per batch
    dynamic=True,   # Dynamically adjust batch size
    timeout_retries=3
)

# Start batch import
with client.batch as batch:
    for obj in objects:
        batch.add_object(
            collection_name=collection_name,
            properties=obj
        )

# Wait a moment for eventual consistency
time.sleep(2)

# Get and print the number of objects in the collection
object_count = collection.aggregate.over_all(total_count=True).total_count
print(f"Number of objects in the collection: {object_count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:11: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 11.03s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth

# Get credentials from environment variables
CLUSTER_URL = os.getenv("WCD_TEST_URL")
API_KEY = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=CLUSTER_URL,
    auth_credentials=Auth.api_key(API_KEY),
)

# Create collection if it doesn't exist
try:
    collection = client.collections.get("DemoProducts")
except:
    collection = client.collections.create(
        name="DemoProducts",
        properties=[
            {
                "name": "name",
                "dataType": ["text"],
            },
            {
                "name": "description",
                "dataType": ["text"],
            },
        ]
    )

# Prepare data
data_objects = [
    {
        "name": f"Product {i}",
        "description": f"This is a description for product {i}"
    } for i in range(50)
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for data_object in data_objects:
        batch.add_object(
            properties=data_object,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed imports
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print total number of objects in collection
print(f"Total number of objects in collection: {len(collection)}")

# Close the client
client.close()
```

**Output**:
```
Total number of objects in collection: 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 14.19s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with specified properties
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# Get the collection reference
collection = client.collections.get(collection_name)

# Prepare data for batch import
data_objects = [
    {
        "name": f"Product {i}",
        "description": f"Description for product {i}"
    }
    for i in range(1, 51)  # Creates 50 objects
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for data_object in data_objects:
        batch.add_object(
            properties=data_object,
        )
        if batch.number_errors > 0:
            print("Batch import stopped due to errors.")
            break

# Check for failed objects
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Number of objects in the collection: {len(collection)}")

# Close the client connection
client.close()
```

**Output**:
```
Number of objects in the collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

### anthropic/claude-3-5-haiku-20241022

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.04s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.connect import ConnectionParams

# Create connection parameters from environment variables
connection_params = ConnectionParams.from_params(
    url=os.getenv("WCD_TEST_URL"),
    api_key=os.getenv("WCD_TEST_KEY")
)

# Create Weaviate client
client = weaviate.connect_to_custom(
    connection_params=connection_params
)

# Check server readiness
try:
    client.is_ready()
    print("Weaviate server is ready")
except Exception as e:
    print(f"Error checking server readiness: {e}")
finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 6, in <module>
    connection_params = ConnectionParams.from_params(
TypeError: from_params() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.06s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 11.63s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType

def create_products_collection():
    # Get Weaviate Cloud credentials from environment variables
    wcd_url = os.getenv('WCD_TEST_URL')
    wcd_key = os.getenv('WCD_TEST_KEY')

    # Create Weaviate client
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=wcd_key
    )

    try:
        # Check if collection exists and delete if it does
        if client.collections.exists("DemoProducts"):
            print("Deleting existing DemoProducts collection...")
            client.collections.delete("DemoProducts")

        # Create the collection with specified properties
        client.collections.create(
            name="DemoProducts",
            properties=[
                Property(
                    name="name",
                    data_type=DataType.TEXT
                ),
                Property(
                    name="description", 
                    data_type=DataType.TEXT
                ),
                Property(
                    name="price", 
                    data_type=DataType.NUMBER
                ),
                Property(
                    name="in_stock", 
                    data_type=DataType.BOOLEAN
                )
            ]
        )

        print("DemoProducts collection created successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the client connection
        client.close()

# Run the function
if __name__ == "__main__":
    create_products_collection()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 56, in <module>
    create_products_collection()
  File "/code/code.py", line 11, in create_products_collection
    client = weaviate.connect_to_wcs(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/helpers.py", line 145, in connect_to_wcs
    return connect_to_weaviate_cloud(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/helpers.py", line 80, in connect_to_weaviate_cloud
    return __connect(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/helpers.py", line 411, in __connect
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/helpers.py", line 407, in __connect
    client.connect()
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/client_base.py", line 153, in connect
    await self._connection.connect(self._skip_init_checks)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 162, in connect
    await self._open_connections_rest(self._auth, skip_init_checks)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 296, in _open_connections_rest
    self._client = await _auth.get_auth_session()
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/authentication_async.py", line 93, in get_auth_session
    assert isinstance(self._credentials, AuthClientPassword)
AssertionError

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 8.21s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
)

# Create the collection
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with specified properties
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
```

**Output**:
```
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 10.60s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with specified properties
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

# Close the connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.67s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes as wvc

# Set up Weaviate client connection
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv('WCD_TEST_KEY')),
    headers={
        "X-OpenAI-Api-Key": os.getenv('OPENAI_API_KEY')
    }
)

try:
    # Perform hybrid search on WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    results = wine_collection.query.hybrid(
        query="dessert wine",
        limit=2
    )

    # Print details of matching wines
    for wine in results.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: {wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print("---")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Title: Schmitz 24 Brix 2012 Sauvignon Blanc (Sierra Foothills)
Country: US
Price: 22.0
Points: 85
---
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
---

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 9.08s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY')),
    headers={
        "X-OpenAI-API-Key": os.getenv('OPENAI_API_KEY')
    }
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform near_text search for "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print details of matching wines
for obj in response.objects:
    print(f"Title: {obj.properties.get('title', 'N/A')}")
    print(f"Country: {obj.properties.get('country', 'N/A')}")
    print(f"Price: {obj.properties.get('price', 'N/A')}")
    print(f"Points: {obj.properties.get('points', 'N/A')}")
    print("---")

# Close the client connection
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
---
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
---

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.19s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")

    # Perform a semantic search for dessert wines
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_metadata=MetadataQuery(distance=True)
    )

    # Print details of matching wines
    for wine in response.objects:
        print("Title:", wine.properties.get('title', 'N/A'))
        print("Country:", wine.properties.get('country', 'N/A'))
        print("Price:", wine.properties.get('price', 'N/A'))
        print("Points:", wine.properties.get('points', 'N/A'))
        print("Distance:", wine.metadata.distance)
        print("---")

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 478, in __call
    res = await _Retry(4).with_exponential_backoff(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 31, in with_exponential_backoff
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 28, in with_exponential_backoff
    return await f(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/grpc/aio/_call.py", line 327, in __await__
    raise _create_rpc_error(
grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY", grpc_status:2, created_time:"2025-04-03T08:41:20.258062593+00:00"}"
>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 17, in <module>
    response = wine_collection.query.near_text(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/queries/near_text/query.py", line 97, in near_text
    res = await self._query.near_text(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 490, in __call
    raise WeaviateQueryError(str(e), "GRPC search")  # pyright: ignore
weaviate.exceptions.WeaviateQueryError: Query call with protocol GRPC search failed with message <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY", grpc_status:2, created_time:"2025-04-03T08:41:20.258062593+00:00"}"
>.

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.77s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import HybridSearchOptions

# Load environment variables
WEAVIATE_URL = os.getenv('WCD_TEST_URL')
WEAVIATE_KEY = os.getenv('WCD_TEST_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_KEY),
    headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
)

try:
    # Query the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    results = wine_collection.query.hybrid(
        query="pair with steak",
        hybrid_search_options=HybridSearchOptions(
            alpha=0.5  # Balance between vector and keyword search
        ),
        filters=wine_collection.query.filter.where(
            # Price less than 50
            path=["price"],
            operator="LessThan",
            value=50
        ).and_filter(
            # Points greater than 90
            path=["points"],
            operator="GreaterThan", 
            value=90
        ).and_filter(
            # Review body contains specific substrings
            path=["review_body"],
            operator="ContainsAny",
            value=["spice", "fruit", "berry", "cherry", "honey"]
        ),
        limit=5
    )

    # Print matching wines
    for wine in results.objects:
        print(f"Title: {wine.properties['title']}")
        print(f"Country: {wine.properties['country']}")
        print(f"Price: ${wine.properties['price']}")
        print(f"Points: {wine.properties['points']}")
        print("---")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes.query import HybridSearchOptions
ImportError: cannot import name 'HybridSearchOptions' from 'weaviate.classes.query' (/usr/local/lib/python3.9/site-packages/weaviate/classes/query.py)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.46s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY')),
    headers={
        "X-OpenAI-API-Key": os.getenv('OPENAI_API_KEY')
    }
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform hybrid search with specified conditions
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    )
)

# Print matching wines
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: ${wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print("---")

# Close the client connection
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
---
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
---

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 13.30s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
)

# Get the WineReview collection
wine_collection = client.collections.get('WineReview')

# Define the search query and filters
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,  # Balance between semantic and keyword search
    limit=5,
    return_metadata=MetadataQuery(score=True),
    filters=(
        # Price less than 50
        Filter.by_property("price").less_than(50) &
        # Points greater than 90
        Filter.by_property("points").greater_than(90) &
        # Review body contains one of the specified substrings
        Filter.by_property("review_body").contains_any([
            "spice", "fruit", "berry", "cherry", "honey"
        ])
    )
)

# Print the results
print("Matching Wines:")
for wine in response.objects:
    print(f"Title: {wine.properties.get('title', 'N/A')}")
    print(f"Country: {wine.properties.get('country', 'N/A')}")
    print(f"Price: ${wine.properties.get('price', 'N/A')}")
    print(f"Points: {wine.properties.get('points', 'N/A')}")
    print("---")

# Close the connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 478, in __call
    res = await _Retry(4).with_exponential_backoff(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 31, in with_exponential_backoff
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 28, in with_exponential_backoff
    return await f(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/grpc/aio/_call.py", line 327, in __await__
    raise _create_rpc_error(
grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY", grpc_status:2, created_time:"2025-04-03T08:41:55.645650345+00:00"}"
>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 16, in <module>
    response = wine_collection.query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/queries/hybrid/query.py", line 107, in hybrid
    res = await self._query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 490, in __call
    raise WeaviateQueryError(str(e), "GRPC search")  # pyright: ignore
weaviate.exceptions.WeaviateQueryError: Query call with protocol GRPC search failed with message <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY", grpc_status:2, created_time:"2025-04-03T08:41:55.645650345+00:00"}"
>.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 9.80s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes as wvc

# Read Weaviate Cloud credentials from environment variables
WEAVIATE_URL = os.getenv('WCD_TEST_URL')
WEAVIATE_API_KEY = os.getenv('WCD_TEST_KEY')

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY)
)

try:
    # Create the collection with specified properties
    client.collections.create(
        name="DemoProducts",
        properties=[
            wvc.Property(name="name", data_type=wvc.DataType.TEXT),
            wvc.Property(name="description", data_type=wvc.DataType.TEXT)
        ]
    )

    # Get the collection
    products = client.collections.get("DemoProducts")

    # Prepare batch of objects
    batch_objects = [
        {
            "name": f"Product {i}",
            "description": f"Description {i}"
        } for i in range(50)
    ]

    # Batch import objects
    products.data.insert_many(batch_objects)

    # Print the number of objects in the collection
    object_count = products.aggregate.count()
    print(f"Number of objects in DemoProducts collection: {object_count}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
An error occurred: module 'weaviate.classes' has no attribute 'Property'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.88s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=AuthApiKey(os.getenv('WCD_TEST_KEY')),
)

# Create the collection if it doesn't exist
try:
    # Remove existing collection if needed
    client.collections.delete("DemoProducts")
except:
    pass

# Create the collection with specified properties
client.collections.create(
    name="DemoProducts",
    properties=[
        weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
        weaviate.Property(name="description", data_type=weaviate.DataType.TEXT)
    ]
)

# Get the collection
collection = client.collections.get("DemoProducts")

# Batch import 50 objects
with collection.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i+1}",
                "description": f"Description for Product {i+1}"
            }
        )

# Check for any batch import errors
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Number of objects in the collection: {len(collection)}")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 22, in <module>
    weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Property
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 13.80s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# ================================
# Connect to Weaviate Cloud
# ================================
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
)

# ================================
# Create Collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT)
    ]
)

# ================================
# Batch Import Objects
# ================================
# Get the collection
collection = client.collections.get(collection_name)

# Batch import 50 objects
with collection.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i+1}",
                "description": f"Description for Product {i+1}"
            }
        )

# ================================
# Print Number of Objects
# ================================
# Get the collection again to ensure we have the latest state
collection = client.collections.get(collection_name)
print(f"Number of objects in {collection_name}: {len(collection)}")

# Close the connection
client.close()
```

**Output**:
```
Number of objects in DemoProducts: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

### cohere/command-a-03-2025

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.63s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import get_valid_uuid

# Retrieve environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")

# Initialize the Weaviate client with the Cloud instance
client = Client(
    url=False,  # Do not open the connection automatically
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Open the connection and check if the server is ready
client.is_ready()

# Optionally, print the result to confirm readiness
print("Weaviate server is ready:", client.is_ready())
```

**Errors**:
```
  File "/code/code.py", line 10
    client = Client(
        ^
SyntaxError: keyword argument repeated: url

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 3.55s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve environment variables
CLUSTER_URL = os.getenv("WCD_TEST_URL")
API_KEY = os.getenv("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=CLUSTER_URL,
    auth_credentials=Auth.api_key(API_KEY)
)

# Check if the server is ready
assert client.is_ready()

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.44s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.classes.config import Property, DataType
from weaviate.exceptions import WeaviateNotFoundError

# Retrieve environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")

# Initialize Weaviate client
client = Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Define the collection name
COLLECTION_NAME = "DemoProducts"

# Check if the collection exists and delete it if it does
try:
    client.collections.get(COLLECTION_NAME)
    print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it first.")
    client.collections.delete(COLLECTION_NAME)
except WeaviateNotFoundError:
    print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to create it.")

# Create the collection with the specified properties
client.collections.create(
    name=COLLECTION_NAME,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ],
)

print(f"Collection '{COLLECTION_NAME}' created successfully.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 5, in <module>
    from weaviate.exceptions import WeaviateNotFoundError
ImportError: cannot import name 'WeaviateNotFoundError' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.03s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Retrieve environment variables for Weaviate Cloud connection
CLUSTER_URL = os.getenv("WCD_TEST_URL")
API_KEY = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not CLUSTER_URL or not API_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=CLUSTER_URL,
    auth_credentials=Auth.api_key(API_KEY)
)

# Define the collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the collection with the specified properties
products_collection = client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)

print(f"Created collection: {products_collection.name}")

# Close the connection
client.close()
```

**Output**:
```
Deleted existing collection: DemoProducts

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 35, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN),
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.87s)

**Generated Code**:
```python
import os
from weaviate import WeaviateClient
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth

# ================================
# Connect to Weaviate Cloud
# ================================
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

client: WeaviateClient = WeaviateClient(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
)

# ================================
# Create or delete the collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with specified properties
client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)

print(f"Collection '{collection_name}' created successfully.")

# Close the connection (optional, as the client handles it automatically)
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    client: WeaviateClient = WeaviateClient(
TypeError: __init__() got an unexpected keyword argument 'cluster_url'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 4.73s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client

# Set up Weaviate client
client = Client(
    url=os.getenv("WCD_TEST_URL"),
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WCD_TEST_KEY")),
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Define the query
query = "dessert wine"

# Perform the hybrid search
response = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query)
    .with_limit(2)
    .do()
)

# Extract and print the results
for result in response['data']['Get']['WineReview']:
    print(f"Title: {result['title']}")
    print(f"Country: {result['country']}")
    print(f"Price: {result['price']}")
    print(f"Points: {result['points']}")
    print("-" * 40)
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:6: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 6, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 6.33s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Query for wines matching "dessert wine" with a limit of 2 results
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the title, country, price, and points of each matching wine
for obj in response.objects:
    properties = obj.properties
    print(f"Title: {properties.get('title', 'N/A')}")
    print(f"Country: {properties.get('country', 'N/A')}")
    print(f"Price: {properties.get('price', 'N/A')}")
    print(f"Points: {properties.get('points', 'N/A')}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
----------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
----------------------------------------

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.23s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.classes.query import MetadataQuery
from weaviate.classes.config import Configure

# ================================
# Connect to Weaviate Cloud
# ================================
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY  # Pass OpenAI API key in headers
    }
)

# ================================
# Query the WineReview collection
# ================================
wine_review_collection = client.collections.get("WineReview")

response = wine_review_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_metadata=MetadataQuery(distance=True)
)

# ================================
# Print results
# ================================
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: {wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print(f"Distance: {wine.metadata.distance}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
NameError: name 'weaviate' is not defined

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.11s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import WeaviateClient
from weaviate.classes.query import HybridFusion

# Connect to Weaviate Cloud
client: WeaviateClient = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.AuthApiKey(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Define the query
response = client.collections.get("WineReview").query.hybrid(
    query="pair with steak",
    fusion_type=HybridFusion.RANKED,
    alpha=0.5,
    limit=5,
    filters={
        "operator": "And",
        "operands": [
            {
                "path": ["price"],
                "operator": "LessThan",
                "valueNumber": 50
            },
            {
                "path": ["points"],
                "operator": "GreaterThan",
                "valueNumber": 90
            },
            {
                "operator": "Or",
                "operands": [
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueString": "*spice*"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueString": "*fruit*"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueString": "*berry*"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueString": "*cherry*"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueString": "*honey*"
                    }
                ]
            }
        ]
    },
    return_metadata=weaviate.ReturnMetadata(score=True),
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for result in response.objects:
    print(f"Title: {result.properties['title']}")
    print(f"Country: {result.properties['country']}")
    print(f"Price: {result.properties['price']}")
    print(f"Points: {result.properties['points']}")
    print(f"Score: {result.metadata.score}\n")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
Traceback (most recent call last):
  File "/code/code.py", line 66, in <module>
    return_metadata=weaviate.ReturnMetadata(score=True),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute ReturnMetadata
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.94s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform hybrid search with filters
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=Filter.by_properties(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    ),
    return_metadata=True  # Include metadata like score in the response
)

# Print the desired properties for each matching wine
for obj in response.objects:
    wine_properties = obj.properties
    print(f"Title: {wine_properties['title']}")
    print(f"Country: {wine_properties['country']}")
    print(f"Price: {wine_properties['price']}")
    print(f"Points: {wine_properties['points']}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 28, in <module>
    filters=Filter.by_properties(
AttributeError: type object 'Filter' has no attribute 'by_properties'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.62s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, MetadataQuery
from weaviate.classes.config import Configure

# ================================
# Connect to Weaviate Cloud
# ================================
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.classes.init.Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# ================================
# Query the WineReview collection
# ================================
wine_review_collection = client.collections.get("WineReview")

# Define the filter conditions
filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
)

# Perform the hybrid search
response = wine_review_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    filters=filters,
    limit=5,
    return_metadata=MetadataQuery(score=True)
)

# Print the results
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: {wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print(f"Score: {wine.metadata.score}")
    print("-" * 40)

# Close the connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 478, in __call
    res = await _Retry(4).with_exponential_backoff(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 31, in with_exponential_backoff
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 28, in with_exponential_backoff
    return await f(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/grpc/aio/_call.py", line 327, in __await__
    raise _create_rpc_error(
grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2025-04-03T08:43:46.762231466+00:00", grpc_status:2, grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"}"
>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 27, in <module>
    response = wine_review_collection.query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/queries/hybrid/query.py", line 107, in hybrid
    res = await self._query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 490, in __call
    raise WeaviateQueryError(str(e), "GRPC search")  # pyright: ignore
weaviate.exceptions.WeaviateQueryError: Query call with protocol GRPC search failed with message <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2025-04-03T08:43:46.762231466+00:00", grpc_status:2, grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"}"
>.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 5.34s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.classes.config import Property, DataType
from weaviate.collections.classes.batch import BatchObject

# Connect to Weaviate Cloud using environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")

client = Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Define the collection schema
collection_name = "DemoProducts"
client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ],
)

# Prepare batch objects
batch_objects = []
for i in range(50):
    obj = BatchObject(
        properties={
            "name": f"Product {i}",
            "description": f"Description {i}",
        }
    )
    batch_objects.append(obj)

# Batch import objects
with client.batch.dynamic() as batch:
    batch.add_objects(objects=batch_objects, collection=collection_name)

# Print the number of objects in the collection
object_count = client.collections.get(collection_name).count()
print(f"Number of objects in the collection '{collection_name}': {object_count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:11: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 5.85s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Auth

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
)

# Define the collection schema
collection_name = "DemoProducts"
schema = {
    "classes": [
        {
            "class": collection_name,
            "properties": [
                {
                    "name": "name",
                    "dataType": ["text"],
                },
                {
                    "name": "description",
                    "dataType": ["text"],
                },
            ],
        }
    ]
}

# Create the collection if it doesn't exist
if not client.schema.exists(collection_name):
    client.schema.create(schema)

# Get the collection
collection = client.collections.get(collection_name)

# Prepare 50 arbitrary objects for batch import
data_objects = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}",
    }
    for i in range(50)
]

# Batch import the objects
with collection.batch.dynamic() as batch:
    for obj in data_objects:
        batch.add_object(properties=obj)
        if batch.number_of_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed imports
failed_objects = batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
object_count = collection.aggregate.over_all().total_count()
print(f"Number of objects in the collection: {object_count}")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate import Auth
ImportError: cannot import name 'Auth' from 'weaviate' (/usr/local/lib/python3.9/site-packages/weaviate/__init__.py)

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.68s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# ================================
# Connect to Weaviate Cloud
# ================================
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# ================================
# Create a collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with specified properties
products_collection = client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# ================================
# Batch import 50 arbitrary objects
# ================================
data_objects = [
    {"name": f"Product {i}", "description": f"Description {i}"} for i in range(1, 51)
]

with products_collection.batch.dynamic() as batch:
    for obj in data_objects:
        batch.add_object(properties=obj)
        if batch.number_errors > 0:
            print(f"Batch import encountered {batch.number_errors} errors.")
            break

# Check for failed imports
failed_objects = products_collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# ================================
# Print the number of objects in the collection
# ================================
count = products_collection.aggregate.count()
print(f"Number of objects in the collection: {count}")

# Close the connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 58, in <module>
    count = products_collection.aggregate.count()
AttributeError: '_AggregateCollection' object has no attribute 'count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

### cohere/command-r-plus-08-2024

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.89s)

**Generated Code**:
```python
import os
from weaviate import Client

# Get environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Initialize the Weaviate client
client = Client(
    url=weaviate_url,
    additional_headers={"X-OpenAI-Api-Key": api_key},
)

# Check server status
server_status = client.is_ready().is_ready

print(f"Weaviate server is ready: {server_status}")
```

**Errors**:
```
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.74s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.auth import AuthCredentials

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY are not set.")

auth_client_credentials = AuthCredentials.client_secret(
    client_secret=WCD_TEST_KEY
)

client = Client(
    url=WCD_TEST_URL,
    auth_client_secret=auth_client_credentials
)

# Check if the server is ready
assert client.is_ready(), "Weaviate server is not ready."
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 12, in <module>
    auth_client_credentials = AuthCredentials.client_secret(
  File "/usr/local/lib/python3.9/typing.py", line 710, in __getattr__
    return getattr(self.__origin__, attr)
AttributeError: '_SpecialForm' object has no attribute 'client_secret'

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 11.35s)

**Generated Code**:
```python
import os
from weaviate import Client

# Connect to Weaviate Cloud using environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")
client = Client(wcd_url, auth_client_secret=wcd_key)

# Check if the collection already exists and delete if necessary
if client.data_object.exists("DemoProducts"):
    client.schema.delete_class("DemoProducts")

# Create the "DemoProducts" collection with the specified properties
schema = {
    "class": "DemoProducts",
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
        {
            "name": "price",
            "dataType": ["number"],
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"],
        },
    ],
}

client.schema.create(schema)

print("Collection 'DemoProducts' created successfully!")
```

**Errors**:
```
/code/code.py:7: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(wcd_url, auth_client_secret=wcd_key)
Traceback (most recent call last):
  File "/code/code.py", line 7, in <module>
    client = Client(wcd_url, auth_client_secret=wcd_key)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 13.70s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
wcd_test_url = os.environ.get("WCD_TEST_URL")
wcd_test_key = os.environ.get("WCD_TEST_KEY")

client = Client(
    url=wcd_test_url,
    auth_client_secret=wcd_test_key,
)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.data_object.exists(collection_name):
    client.schema.delete_class(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the collection with properties
collection = client.schema.create_class(
    class_name=collection_name,
    properties={
        "name": {
            "dataType": ["text"],
            "description": "Name of the product"
        },
        "description": {
            "dataType": ["text"],
            "description": "Description of the product"
        },
        "price": {
            "dataType": ["number"],
            "description": "Price of the product"
        },
        "in_stock": {
            "dataType": ["boolean"],
            "description": "Availability of the product"
        }
    },
    vectorizer="text2vec-contextionary",
    moduleConfig={
        "text2vec-contextionary": {
            "vectorizePropertyName": ["name", "description"]
        }
    }
)

print(f"Created collection: {collection.class_name}")

# Close connection
client.close()
```

**Errors**:
```
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.02s)

**Generated Code**:
```python
import os
from weaviate.client import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the specified properties
collection = client.collections.create(
    collection_name,
    properties=[
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
        {
            "name": "price",
            "dataType": ["number"],
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"],
        },
    ],
)

# Print the collection details
print(f"Collection '{collection_name}' created with UUID: {collection.uuid}")
```

**Errors**:
```
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 274.31s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)

# Set the API key for the text2vec-openai vectorizer
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Define the query
query = {
    "vector": {
        "vector": {
            "text2vec-openai": {
                "query": "dessert wine",
                "api_key": OPENAI_API_KEY,
            }
        }
    },
    "class": "WineReview",
    "properties": ["title", "country", "price", "points"],
    "limit": 2,
}

# Generate a unique ID for the query
query_id = generate_uuid5(query, "WeaviateQuery")

# Execute the query
results = client.query.get(query, additional={"id": query_id})

# Print the results
for result in results:
    print(f"Title: {result['title']}")
    print(f"Country: {result['country']}")
    print(f"Price: {result['price']}")
    print(f"Points: {result['points']}")
    print("-" * 20)
```

**Errors**:
```
/code/code.py:8: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 11.91s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
    headers={"X-OpenAI-API-Key": openai_api_key},
)

# Get the 'WineReview' collection
wine_collection = client.collections.get("WineReview")

# Query for wines that match "dessert wine"
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
)

# Process and print the results
for wine in response.objects:
    properties = wine.properties
    print(f"Title: {properties.get('title')}")
    print(f"Country: {properties.get('country')}")
    print(f"Price: {properties.get('price')}")
    print(f"Points: {properties.get('points')}")
    print("=" * 20)

# Close the client connection
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
====================
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
====================

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.16s)

**Generated Code**:
```python
import os
from weaviate.util import generate_uuid5
from weaviate.client import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
client = Client(
    url=os.environ["WCD_TEST_URL"],
    auth_client_secret=os.environ["WCD_TEST_KEY"],
)

# Get the 'WineReview' collection
wine_collection = client.collections.get("WineReview")

# Perform a semantic search with the query "dessert wine"
results = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
)

# Print the title, country, price, and points of each matching wine
for result in results:
    print("Title:", result.properties.get("title"))
    print("Country:", result.properties.get("country"))
    print("Price:", result.properties.get("price"))
    print("Points:", result.properties.get("points"))
    print()
```

**Errors**:
```
/code/code.py:7: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 7, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 15.85s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)


def find_wines_for_steak():
    # Define the query and filters
    query = "pair with steak"
    filters = [
        {
            "path": ["price"],
            "operator": "LessThan",
            "valueNumber": 50,
        },
        {
            "path": ["points"],
            "operator": "GreaterThan",
            "valueNumber": 90,
        },
        {
            "path": ["review_body"],
            "operator": "Like",
            "valueText": ["spice", "fruit", "berry", "cherry", "honey"],
        },
    ]

    # Construct the hybrid search query
    hybrid_search = {
        "vector": {
            "query": query,
            "alpha": 0.5,
            "vectorizer": "text2vec-openai",
            "properties": ["review_body"],
        },
        "filters": filters,
        "limit": 5,
    }

    # Generate a unique ID for the query
    query_uuid = generate_uuid5(query, "Query")

    # Execute the hybrid search query
    results = client.query.hybrid.get(hybrid_search, class_name="WineReview", uuid=query_uuid)

    # Process and print the results
    for result in results["data"]["Get"]["WineReview"]:
        title = result["title"]
        country = result["country"]
        price = result["price"]
        points = result["points"]
        print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")


# Run the function to find and print the matching wines
find_wines_for_steak()
```

**Errors**:
```
/code/code.py:8: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 14.55s)

**Generated Code**:
```python
import os
from weaviate.util import generate_uuid5

from weaviate import Client
from weaviate.filters import WhereFilter, ContainsAny, WhereOperator
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = Client(
    url=WCD_TEST_URL,
    auth_client_secret=WCD_TEST_KEY,
    additional_headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    }
)

# Define the collection name
collection_name = "WineReview"

# Generate a unique ID for the query
query_id = generate_uuid5(collection_name, "query")

# Define the query and filters
query = "pair with steak"
filters = (
    WhereFilter(
        path=["price"],
        operator=WhereOperator.LESS_THAN,
        value=50
    ) &
    WhereFilter(
        path=["points"],
        operator=WhereOperator.GREATER_THAN,
        value=90
    ) &
    WhereFilter(
        path=["review_body"],
        operator=ContainsAny,
        value=["spice", "fruit", "berry", "cherry", "honey"]
    )
)

# Perform the hybrid search
response = client.query.hybrid(
    query=query,
    class_name=collection_name,
    limit=5,
    alpha=0.5,
    where=filters,
    additional={"id": query_id}
)

# Process and print the results
for result in response["data"]["Get"][collection_name]:
    properties = result["properties"]
    print(f"Title: {properties['title']}")
    print(f"Country: {properties['country']}")
    print(f"Price: {properties['price']}")
    print(f"Points: {properties['points']}")
    print("---")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 5, in <module>
    from weaviate.filters import WhereFilter, ContainsAny, WhereOperator
ModuleNotFoundError: No module named 'weaviate.filters'

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 51.90s)

**Generated Code**:
```python
```python
import os
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5
from we
```

**Errors**:
```
  File "/code/code.py", line 1
    ```python
    ^
SyntaxError: invalid syntax

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 15.63s)

**Generated Code**:
```python
import os
from weaviate import Client

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)

# Create a schema for the "DemoProducts" collection
schema = {
    "class": "DemoProducts",
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
    ],
}

# Create the collection if it doesn't exist
client.schema.create_class(schema)

# Function to add objects to the collection
def add_objects_to_collection(objects):
    with client.batch as batch:
        for obj in objects:
            batch.add_data_object(obj, "DemoProducts")

# Generate 50 arbitrary objects
objects_to_add = [{"name": f"Product {i}", "description": f"Description {i}"} for i in range(50)]

# Add objects to the "DemoProducts" collection
add_objects_to_collection(objects_to_add)

# Get the number of objects in the collection
collection_name = "DemoProducts"
collection = client.data_object.get(
    f"{WCD_TEST_URL}/v1/objects/{collection_name}",
    params={"limit": 50},
)
num_objects = len(collection["objects"])

print(f"Number of objects in '{collection_name}' collection: {num_objects}")
```

**Errors**:
```
/code/code.py:7: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
Traceback (most recent call last):
  File "/code/code.py", line 7, in <module>
    client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 13.61s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
wcd_test_url = os.environ.get("WCD_TEST_URL")
wcd_test_key = os.environ.get("WCD_TEST_KEY")

client = Client(
    url=wcd_test_url,
    auth_client_secret=wcd_test_key,
)

# Get or create the collection
collection = client.collections.get("DemoProducts")
if collection is None:
    collection = client.collections.create(
        "DemoProducts",
        class_config={
            "vectorizer": "text2vec-openai",
            "properties": [
                {"name": "name", "dataType": ["text"]},
                {"name": "description", "dataType": ["text"]},
            ],
        },
    )

# Generate 50 objects with arbitrary data
objects_to_import = []
for i in range(50):
    object_data = {
        "name": f"Product {i}",
        "description": f"Description {i}",
        "id": generate_uuid5(),
    }
    objects_to_import.append(object_data)

# Batch import the objects
with collection.batch.dynamic() as batch:
    for obj in objects_to_import:
        batch.add_object(properties=obj)

# Check for any failed imports
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Failed to import {len(failed_objects)} objects.")
    print("First failed object:", failed_objects[0])

# Get and print the number of objects in the collection
collection_objects = collection.get()
num_objects = len(collection_objects)
print(f"Number of objects in 'DemoProducts' collection: {num_objects}")

# Close the client connection
client.close()
```

**Errors**:
```
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.74s)

**Generated Code**:
```python
import os
from weaviate.util import generate_uuid5
from weaviate.util import generate_uuid5_from_string
from weaviate.client import Client

# Connect to Weaviate Cloud using environment variables
client = Client(os.environ["WCD_TEST_URL"], auth_client_secret=os.environ["WCD_TEST_KEY"])

# Create the collection if it doesn't exist
collection_name = "DemoProducts"
if not client.schema.contains(collection_name):
    client.schema.create_class(collection_name, ["name", "description"])

# Batch import 50 objects into the collection
with client.batch as batch:
    for i in range(50):
        object_id = generate_uuid5(collection_name, str(i))
        batch.add_data_object(collection_name, object_id, {
            "name": f"Product {i}",
            "description": f"Description {i}"
        })

# Print the number of objects in the collection
collection = client.data_object.get(collection_name, include=50)
print(f"Number of objects in '{collection_name}' collection: {len(collection['objects'])}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.util import generate_uuid5_from_string
ImportError: cannot import name 'generate_uuid5_from_string' from 'weaviate.util' (/usr/local/lib/python3.9/site-packages/weaviate/util.py)

```

---

### gemini/gemini-2.5-pro-exp-03-25

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 30.20s)

**Generated Code**:
```python
import weaviate
import os
import sys
from weaviate.auth import AuthApiKey

# 1. Get credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# 2. Check if environment variables are set
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

print(f"Attempting to connect to Weaviate Cloud at {wcd_url}...")

try:
    # 3. Connect to Weaviate Cloud using connect_to_wcs helper
    # The 'with' statement ensures the connection is closed automatically
    with weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_client_secret=AuthApiKey(api_key=wcd_api_key),
        # Optional: Add headers if needed, e.g., for module integrations
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY"),
        #     "X-Cohere-Api-Key": os.getenv("COHERE_APIKEY"),
        # }
    ) as client:

        print("Connection successful.")

        # 4. Check if the Weaviate server is ready
        if client.is_ready():
            print("Weaviate server is ready to accept requests.")
        else:
            print("Error: Weaviate server is not ready.")
            sys.exit(1) # Exit with an error code if not ready

except Exception as e:
    print(f"An error occurred during connection or readiness check: {e}")
    sys.exit(1)

# If the script reaches here, connection and readiness check were successful.
# Don't do anything else as requested.
# print("Script finished.")
```

**Output**:
```
Attempting to connect to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
An error occurred during connection or readiness check: connect_to_wcs() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 35.40s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
import sys # Used for exit on error

print("Starting Weaviate connection script...")

# --- Configuration ---
# Get Weaviate Cloud connection details from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")

# --- Validation ---
# Check if environment variables are set
if not wcd_url:
    print("\nError: WCD_TEST_URL environment variable not set.")
    print("Please set the WCD_TEST_URL environment variable with your Weaviate Cloud instance URL.")
    sys.exit(1) # Exit script with error status
if not wcd_key:
    print("\nError: WCD_TEST_KEY environment variable not set.")
    print("Please set the WCD_TEST_KEY environment variable with your Weaviate Cloud API key.")
    sys.exit(1) # Exit script with error status

print(f"\nAttempting to connect to Weaviate Cloud instance at: {wcd_url}")

# --- Connection and Readiness Check ---
client = None  # Initialize client to None for robust error handling in finally block
try:
    # Connect to the Weaviate Cloud instance using environment variables
    # Uses the latest Weaviate client v4 syntax
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,                 # Use the URL from WCD_TEST_URL
        auth_credentials=Auth.api_key(wcd_key) # Use the API key from WCD_TEST_KEY
        # Optional: Add headers if necessary for API keys for third-party modules (e.g., OpenAI, Cohere)
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY"),
        #     "X-Cohere-Api-Key": os.getenv("COHERE_API_KEY")
        # }
    )

    print("Successfully established connection object.")

    # Check that the server is ready to accept requests
    # client.is_ready() returns True if the server is ready, False otherwise.
    # The assert will raise an AssertionError with the provided message if client.is_ready() is False.
    print("Checking if the Weaviate server is ready...")
    assert client.is_ready(), "Weaviate server is not ready!"

    print("Success! Weaviate server is ready to accept requests.")

    # --- Task Complete ---
    # Don't do anything else, as requested.

except Exception as e:
    # Catch potential errors during connection or readiness check
    print(f"\nAn error occurred: {e}")
    # Exit script if connection or readiness fails
    sys.exit(1)

finally:
    # --- Cleanup ---
    # Always ensure the connection is closed if the client object was successfully created.
    # This code will run even if an error occurred after the client was created but before the script finished.
    if client:
        print("Closing Weaviate connection.")
        client.close()
        print("Connection closed.")
    else:
        print("Client object was not created, no connection to close.")

print("\nScript finished.")
```

**Output**:
```
Starting Weaviate connection script...

Attempting to connect to Weaviate Cloud instance at: https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud
Successfully established connection object.
Checking if the Weaviate server is ready...
Success! Weaviate server is ready to accept requests.
Closing Weaviate connection.
Connection closed.

Script finished.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 31.93s)

**Generated Code**:
```python
import weaviate
import os
import sys
from weaviate.auth import AuthApiKey
from weaviate.classes.config import Property, DataType, Configure

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"

# --- Get Weaviate Cloud Credentials from Environment Variables ---
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_api_key = os.environ.get("WCD_TEST_KEY")

# --- Validate Environment Variables ---
if not wcd_url:
    print("ERROR: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("ERROR: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

# --- Connect to Weaviate Cloud (WCS) Instance ---
try:
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(api_key=wcd_api_key),
        # Optional: Add headers if needed, e.g., for module-specific keys
        # headers={
        #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY")
        # }
    )
    client.is_ready() # Check if connection is successful
    print("Successfully connected to Weaviate Cloud.")

except Exception as e:
    print(f"Error connecting to Weaviate: {e}")
    sys.exit(1)

# --- Main Logic ---
try:
    # 1. Check if the collection already exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to create.")

    # 2. Define the collection properties using the latest syntax
    properties_to_create = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER), # Use NUMBER for floats/integers
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    # 3. Create the collection
    print(f"Creating collection '{COLLECTION_NAME}'...")
    demo_products = client.collections.create(
        name=COLLECTION_NAME,
        properties=properties_to_create,
        # Optional: Specify vectorizer configuration if needed
        # vectorizer_config=Configure.Vectorizer.text2vec_openai(),
        # vectorizer_config=Configure.Vectorizer.text2vec_contextionary(), # common default
        vectorizer_config=Configure.Vectorizer.none(), # Explicitly no vectorizer if not needed now
        # Optional: Specify generative configuration if needed
        # generative_config=Configure.Generative.openai()
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully.")
    # You can optionally print the created collection config
    # print(client.collections.get(COLLECTION_NAME).config.get())


except Exception as e:
    print(f"An error occurred during collection management: {e}")

finally:
    # 4. Close the connection
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Weaviate connection closed.")

# --- How to Run ---
# 1. Install the Weaviate client: pip install weaviate-client
# 2. Set environment variables (replace placeholders with your actual credentials):
#    export WCD_TEST_URL="YOUR_WEAVIATE_CLOUD_URL"
#    export WCD_TEST_KEY="YOUR_WEAVIATE_API_KEY"
# 3. Run the script: python your_script_name.py
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Weaviate connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 27.36s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"

# --- Get Connection Details from Environment Variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# --- Validate Environment Variables ---
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

print(f"Connecting to Weaviate Cloud at: {wcd_url}")

# Initialize client variable
client = None

try:
    # --- Connect to Weaviate Cloud ---
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Optional: Add headers if needed, e.g., for module-specific keys
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
        # }
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- Check if Collection Exists and Delete if it Does ---
    print(f"Checking if collection '{COLLECTION_NAME}' exists...")
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' found. Deleting it.")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to create.")

    # --- Define Collection Properties ---
    properties_to_create = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        # Use DataType.NUMBER for floating-point or integer prices
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    # --- Create the Collection ---
    print(f"Creating collection '{COLLECTION_NAME}'...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=properties_to_create,
        # Optional: Configure vectorizer, generative modules etc.
        # vectorizer_config=Configure.Vectorizer.text2vec_openai(),
        # generative_config=Configure.Generative.openai()
    )

    print(f"\nSuccessfully created collection: '{products_collection.name}'")
    print("Collection details:")
    config = client.collections.get(COLLECTION_NAME).config.get()
    print(config)


except Exception as e:
    print(f"\nAn error occurred: {e}")
    sys.exit(1)

finally:
    # --- Close the Connection ---
    if client:
        client.close()
        print("\nConnection closed.")
```

**Output**:
```
Connecting to Weaviate Cloud at: https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate Cloud.
Checking if collection 'DemoProducts' exists...
Collection 'DemoProducts' found. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...

Successfully created collection: 'DemoProducts'
Collection details:
_CollectionConfig(name='DemoProducts', description=None, generative_config=None, inverted_index_config=_InvertedIndexConfig(bm25=_BM25Config(b=0.75, k1=1.2), cleanup_interval_seconds=60, index_null_state=False, index_property_length=False, index_timestamps=False, stopwords=_StopwordsConfig(preset=<StopwordsPreset.EN: 'en'>, additions=None, removals=None)), multi_tenancy_config=_MultiTenancyConfig(enabled=False, auto_tenant_creation=False, auto_tenant_activation=False), properties=[_Property(name='name', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='description', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='price', description=None, data_type=<DataType.NUMBER: 'number'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='in_stock', description=None, data_type=<DataType.BOOL: 'boolean'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None)], references=[], replication_config=_ReplicationConfig(factor=1, async_enabled=False, deletion_strategy=<ReplicationDeletionStrategy.NO_AUTOMATED_RESOLUTION: 'NoAutomatedResolution'>), reranker_config=None, sharding_config=_ShardingConfig(virtual_per_physical=128, desired_count=1, actual_count=1, desired_virtual_count=128, actual_virtual_count=128, key='_id', strategy='hash', function='murmur3'), vector_index_config=_VectorIndexConfigHNSW(multi_vector=None, quantizer=None, cleanup_interval_seconds=300, distance_metric=<VectorDistances.COSINE: 'cosine'>, dynamic_ef_min=100, dynamic_ef_max=500, dynamic_ef_factor=8, ef=-1, ef_construction=128, filter_strategy=<VectorFilterStrategy.SWEEPING: 'sweeping'>, flat_search_cutoff=40000, max_connections=32, skip=False, vector_cache_max_objects=1000000000000), vector_index_type=<VectorIndexType.HNSW: 'hnsw'>, vectorizer_config=None, vectorizer=<Vectorizers.NONE: 'none'>, vector_config=None)

Connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 30.29s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType
import sys

# ================================
# Configuration
# ================================
COLLECTION_NAME = "DemoProducts"

# ================================
# Get Connection Details from Environment Variables
# ================================
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    print("Found WCD_TEST_URL and WCD_TEST_KEY environment variables.")
except KeyError:
    print("Error: Required environment variables WCD_TEST_URL or WCD_TEST_KEY not found.")
    print("Please set these variables before running the script.")
    sys.exit(1) # Exit the script if variables are not set

# ================================
# Connect to Weaviate Cloud
# ================================
print(f"Connecting to Weaviate Cloud at {wcd_url}...")
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Optional: Add headers if needed, e.g., for OpenAI keys
        # headers={
        #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY", "")
        # }
    )
    print("Successfully connected to Weaviate Cloud.")
except Exception as e:
    print(f"Error connecting to Weaviate Cloud: {e}")
    sys.exit(1)

# ================================
# Manage Collection (Delete if exists, then Create)
# ================================
try:
    # 1. Check if the collection exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to create.")

    # 2. Define the properties for the collection
    properties_definition = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER), # Use NUMBER for float/decimal values
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    # 3. Create the collection
    print(f"Creating collection '{COLLECTION_NAME}'...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=properties_definition,
        # No vectorizer specified, will use default ('none' unless configured otherwise)
        # vectorizer_config=Configure.Vectorizer.text2vec_openai() # Example if vectorizer needed
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully with the following configuration:")
    # Optional: Print the collection configuration to verify
    config = products_collection.config.get()
    print(config)

except Exception as e:
    print(f"An error occurred during collection management: {e}")
    sys.exit(1)

# ================================
# Close Connection
# ================================
finally:
    # Ensure the client connection is closed even if errors occur above
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Weaviate connection closed.")

```

**Output**:
```
Found WCD_TEST_URL and WCD_TEST_KEY environment variables.
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully with the following configuration:
_CollectionConfig(name='DemoProducts', description=None, generative_config=None, inverted_index_config=_InvertedIndexConfig(bm25=_BM25Config(b=0.75, k1=1.2), cleanup_interval_seconds=60, index_null_state=False, index_property_length=False, index_timestamps=False, stopwords=_StopwordsConfig(preset=<StopwordsPreset.EN: 'en'>, additions=None, removals=None)), multi_tenancy_config=_MultiTenancyConfig(enabled=False, auto_tenant_creation=False, auto_tenant_activation=False), properties=[_Property(name='name', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='description', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='price', description=None, data_type=<DataType.NUMBER: 'number'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='in_stock', description=None, data_type=<DataType.BOOL: 'boolean'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None)], references=[], replication_config=_ReplicationConfig(factor=1, async_enabled=False, deletion_strategy=<ReplicationDeletionStrategy.NO_AUTOMATED_RESOLUTION: 'NoAutomatedResolution'>), reranker_config=None, sharding_config=_ShardingConfig(virtual_per_physical=128, desired_count=1, actual_count=1, desired_virtual_count=128, actual_virtual_count=128, key='_id', strategy='hash', function='murmur3'), vector_index_config=_VectorIndexConfigHNSW(multi_vector=None, quantizer=None, cleanup_interval_seconds=300, distance_metric=<VectorDistances.COSINE: 'cosine'>, dynamic_ef_min=100, dynamic_ef_max=500, dynamic_ef_factor=8, ef=-1, ef_construction=128, filter_strategy=<VectorFilterStrategy.SWEEPING: 'sweeping'>, flat_search_cutoff=40000, max_connections=32, skip=False, vector_cache_max_objects=1000000000000), vector_index_type=<VectorIndexType.HNSW: 'hnsw'>, vectorizer_config=None, vectorizer=<Vectorizers.NONE: 'none'>, vector_config=None)
Weaviate connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 37.72s)

**Generated Code**:
```python
import weaviate
import os
import weaviate.classes as wvc # Optional, but good practice for constants/types

# 1. Get credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Basic validation
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    exit()
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    exit()
if not openai_api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

print(f"Connecting to Weaviate at {wcd_url}...")

try:
    # 2. Connect to Weaviate Cloud using WCD URL and Key
    # The OpenAI API key is provided in the headers for the text2vec-openai module
    client = weaviate.connect_to_wcd(
        url=wcd_url,
        api_key=wcd_api_key,
        additional_headers={
            "X-OpenAI-Api-Key": openai_api_key  # Pass OpenAI key for vectorizer
        }
    )

    # Check if the connection is successful
    if not client.is_ready():
        print("Error: Weaviate client failed to connect.")
        exit()

    print("Successfully connected to Weaviate.")

    # 3. Define query parameters
    collection_name = "WineReview"
    search_query = "dessert wine"
    result_limit = 2
    return_props = ["title", "country", "price", "points"]

    print(f"\nQuerying '{collection_name}' for '{search_query}' (limit {result_limit})...")

    # 4. Get the collection object
    wine_reviews = client.collections.get(collection_name)

    # 5. Perform the vector search (nearText) query
    response = wine_reviews.query.near_text(
        query=search_query,
        limit=result_limit,
        return_properties=return_props
        # Optionally, you can request metadata like distance or certainty:
        # return_metadata=wvc.query.MetadataQuery(distance=True)
    )

    # 6. Process and print the results
    print(f"\nFound {len(response.objects)} results:")

    if not response.objects:
        print("No matching wines found.")
    else:
        for i, wine_object in enumerate(response.objects):
            properties = wine_object.properties
            print(f"\n--- Result {i+1} ---")
            print(f"  Title:   {properties.get('title', 'N/A')}")
            print(f"  Country: {properties.get('country', 'N/A')}")

            # Format price if it exists and is a number
            price = properties.get('price')
            if isinstance(price, (int, float)):
                print(f"  Price:   ${price:.2f}")
            else:
                print(f"  Price:   {price if price is not None else 'N/A'}") # Handle None or non-numeric price

            print(f"  Points:  {properties.get('points', 'N/A')}")

            # If you requested metadata, you can access it like this:
            # if wine_object.metadata:
            #     print(f"  Distance: {wine_object.metadata.distance:.4f}")


except weaviate.exceptions.WeaviateQueryError as e:
    print(f"\nQuery Error: Failed to query collection '{collection_name}'.")
    print(f"Details: {e}")
except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"\nConnection Error: Could not connect to Weaviate at {wcd_url}.")
    print(f"Details: {e}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")

finally:
    # 7. Close the connection
    # The 'connect_to_wcd' function returns a client that should be closed.
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection closed.")
```

**Output**:
```
Connecting to Weaviate at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...

An unexpected error occurred: module weaviate has no attribute connect_to_wcd

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 31.38s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import QueryNearText
import os
import sys

# 1. Get connection details and API keys from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Basic validation
if not all([wcd_url, wcd_api_key, openai_api_key]):
    print(
        "Error: Please ensure WCD_TEST_URL, WCD_TEST_KEY, and "
        "OPENAI_API_KEY environment variables are set."
    )
    sys.exit(1)

# 2. Connect to Weaviate Cloud instance
try:
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,  # Your WCD URL
        auth_credentials=Auth.api_key(wcd_api_key),  # Your WCD API key
        headers={
            # Pass the OpenAI API key for the text2vec-openai vectorizer
            "X-OpenAI-API-Key": openai_api_key
        }
    )
    client.is_ready() # Check if connection is successful
    print("Successfully connected to Weaviate.")

    # 3. Get the 'WineReview' collection
    collection_name = "WineReview"
    print(f"Accessing collection: '{collection_name}'...")
    wine_reviews = client.collections.get(collection_name)

    # 4. Define the query parameters
    search_query = "dessert wine"
    result_limit = 2
    properties_to_return = ["title", "country", "price", "points"]

    print(f"\nSearching for '{search_query}' (limit: {result_limit})...")

    # 5. Perform the nearText (semantic) search
    response = wine_reviews.query.near_text(
        query=search_query,
        limit=result_limit,
        # Specify which properties to return for each object
        return_properties=properties_to_return
    )

    # 6. Process and print the results
    print("\n--- Search Results ---")
    if not response.objects:
        print("No matching wines found.")
    else:
        print(f"Found {len(response.objects)} results:")
        for i, obj in enumerate(response.objects):
            props = obj.properties
            print(f"\nResult {i+1}:")
            print(f"  Title:   {props.get('title', 'N/A')}") # Use .get for robustness
            print(f"  Country: {props.get('country', 'N/A')}")
            # Format price nicely if it exists and is a number
            price = props.get('price')
            price_str = f"${price:.2f}" if isinstance(price, (int, float)) else 'N/A'
            print(f"  Price:   {price_str}")
            print(f"  Points:  {props.get('points', 'N/A')}")

except weaviate.exceptions.WeaviateQueryError as e:
     print(f"Query error: Could not retrieve data. Does the collection '{collection_name}' exist and have the required properties?")
     print(e)
except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Connection error: Could not connect to Weaviate.")
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # 7. Close the client connection
    if 'client' in locals() and client.is_connected():
        print("\nClosing Weaviate connection.")
        client.close()
    else:
        print("\nNo active Weaviate connection to close.")

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes.query import QueryNearText
ImportError: cannot import name 'QueryNearText' from 'weaviate.classes.query' (/usr/local/lib/python3.9/site-packages/weaviate/classes/query.py)

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 34.58s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery # Although not used for final output, good to know it exists

# --- Configuration ---
COLLECTION_NAME = "WineReview"
SEARCH_QUERY = "dessert wine"
RESULT_LIMIT = 2
PROPERTIES_TO_PRINT = ["title", "country", "price", "points"]

# --- Retrieve Credentials from Environment Variables ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
    print("Successfully retrieved environment variables.")
except KeyError as e:
    print(f"Error: Environment variable {e} not set. Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit(1)

client = None # Initialize client to None for the finally block

try:
    # --- 1. Connect to Weaviate Cloud ---
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Provide OpenAI API key for query vectorization via text2vec-openai
        additional_headers={
            "X-OpenAI-Api-Key": openai_api_key
        }
    )
    print("Connection successful.")
    print(f"Weaviate is ready: {client.is_ready()}")

    # --- 2. Get the collection handle ---
    # Check if collection exists first (optional but good practice)
    if not client.collections.exists(COLLECTION_NAME):
        print(f"Error: Collection '{COLLECTION_NAME}' does not exist.")
        # Depending on the use case, you might want to create it here or exit.
        exit(1)
    else:
        print(f"Collection '{COLLECTION_NAME}' found.")

    wine_collection = client.collections.get(COLLECTION_NAME)
    print(f"Got collection handle for '{COLLECTION_NAME}'.")

    # --- 3. Perform the Semantic Search ---
    print(f"\nSearching for wines matching '{SEARCH_QUERY}' (limit {RESULT_LIMIT})...")
    response = wine_collection.query.near_text(
        query=SEARCH_QUERY,
        limit=RESULT_LIMIT,
        # Specify which properties to return in the results
        return_properties=PROPERTIES_TO_PRINT
        # Optional: include metadata like distance if needed
        # return_metadata=MetadataQuery(distance=True)
    )

    # --- 4. Print the Results ---
    print(f"\n--- Top {len(response.objects)} Wine Results ---")
    if not response.objects:
        print("No matching wines found.")
    else:
        for i, wine_object in enumerate(response.objects):
            print(f"\nResult {i+1}:")
            properties = wine_object.properties
            print(f"  Title:   {properties.get('title', 'N/A')}") # Use .get for safety if a property might be missing
            print(f"  Country: {properties.get('country', 'N/A')}")
            print(f"  Price:   {properties.get('price', 'N/A')}")
            print(f"  Points:  {properties.get('points', 'N/A')}")
            # If you included metadata like distance:
            # if wine_object.metadata:
            #     print(f"  Distance: {wine_object.metadata.distance:.4f}")


except weaviate.exceptions.AuthenticationFailedError:
    print("\nError: Authentication failed. Check your Weaviate Cloud API key (WCD_TEST_KEY).")
except Exception as e:
    print(f"\nAn error occurred: {e}")

finally:
    # --- 5. Close the connection ---
    if client and client.is_connected():
        print("\nClosing Weaviate connection.")
        client.close()
        print("Connection closed.")
    elif client:
        print("\nClient was initialized but not connected.")
    else:
        print("\nClient connection was not established.")
```

**Output**:
```
Successfully retrieved environment variables.
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...

An error occurred: connect_to_weaviate_cloud() got an unexpected keyword argument 'additional_headers'

Client connection was not established.

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 43.34s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes as wvc
from weaviate.classes.query import Filter # Import Filter for easier use

# --- Configuration ---
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "pair with steak"
LIMIT = 5
HYBRID_ALPHA = 0.5
MAX_PRICE = 50
MIN_POINTS = 90
REQUIRED_SUBSTRINGS = ["spice", "fruit", "berry", "cherry", "honey"]

# --- 1. Get Credentials from Environment Variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if environment variables are set
missing_vars = []
if not wcd_url:
    missing_vars.append("WCD_TEST_URL")
if not wcd_api_key:
    missing_vars.append("WCD_TEST_KEY")
if not openai_api_key:
    missing_vars.append("OPENAI_API_KEY")

if missing_vars:
    print(f"Error: Required environment variables are not set: {', '.join(missing_vars)}")
    exit(1)

client = None # Initialize client to None for the finally block

try:
    # --- 2. Connect to Weaviate Cloud ---
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    auth_config = wvc.AuthApiKey(api_key=wcd_api_key)

    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=auth_config,
        headers={
            "X-OpenAI-Api-Key": openai_api_key,  # Pass OpenAI key for vectorizer
        }
    )

    # Check connection
    if not client.is_ready():
        print("Error: Weaviate client failed to connect.")
        exit(1)
    print("Connection successful!")

    # --- 3. Get the Collection Reference ---
    print(f"Accessing collection: '{COLLECTION_NAME}'")
    reviews = client.collections.get(COLLECTION_NAME)

    # --- 4. Define Filters ---
    print("Constructing filters...")
    # Price filter: price < MAX_PRICE
    price_filter = Filter.by_property("price").less_than(MAX_PRICE)

    # Points filter: points > MIN_POINTS
    points_filter = Filter.by_property("points").greater_than(MIN_POINTS)

    # Keyword filter: review_body contains at least one substring
    # We need an OR condition for the substrings using Filter.any_of
    # We use 'like "*substring*"' for substring matching
    keyword_filters = [
        Filter.by_property("review_body").like(f"*{substring}*")
        for substring in REQUIRED_SUBSTRINGS
    ]
    keyword_or_filter = Filter.any_of(keyword_filters)

    # Combine all filters using AND (Filter.all_of)
    combined_filter = Filter.all_of([
        price_filter,
        points_filter,
        keyword_or_filter
    ])
    print("Filters constructed successfully.")

    # --- 5. Perform the Hybrid Query ---
    print(f"\nPerforming hybrid search for: '{QUERY_TEXT}'")
    print(f" - Limit: {LIMIT}")
    print(f" - Alpha: {HYBRID_ALPHA}")
    print(f" - Filters: Price < {MAX_PRICE}, Points > {MIN_POINTS}, Review contains one of {REQUIRED_SUBSTRINGS}")

    response = reviews.query.hybrid(
        query=QUERY_TEXT,
        alpha=HYBRID_ALPHA,  # Balance between keyword (BM25) and vector search
        limit=LIMIT,
        filters=combined_filter,
        return_properties=[
            "title",
            "country",
            "price",
            "points",
            # "review_body" # Optional: include for debugging filter
            ]
    )

    # --- 6. Process and Print Results ---
    print("\n--- Search Results ---")
    if not response.objects:
        print("No matching wines found that meet all criteria.")
    else:
        print(f"Found {len(response.objects)} matching wines:")
        for i, obj in enumerate(response.objects):
            props = obj.properties
            price = props.get('price')
            price_str = f"${price:.2f}" if price is not None else "N/A"

            print(f"\nResult {i+1}:")
            print(f"  Title:   {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price:   {price_str}")
            print(f"  Points:  {props.get('points', 'N/A')}")
            # Optional: Print review snippet to verify keyword filter
            # review_body = props.get('review_body', '')
            # print(f"  Review Snippet: {review_body[:150]}..." if review_body else "N/A")


except weaviate.exceptions.WeaviateQueryException as e:
     print(f"Error during Weaviate query: {e}")
     # Potentially check if the collection or properties exist
     if "collection" in str(e) and COLLECTION_NAME in str(e):
         print(f"Hint: Does the collection '{COLLECTION_NAME}' exist and is it configured correctly?")
     if "property" in str(e):
         print(f"Hint: Check if properties like 'price', 'points', 'review_body', 'title', 'country' exist in the schema.")

except weaviate.exceptions.WeaviateBaseError as e:
    print(f"A Weaviate error occurred: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # --- 7. Close the Connection ---
    if client:
        print("\nClosing Weaviate connection.")
        client.close()
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
An unexpected error occurred: module 'weaviate.classes' has no attribute 'AuthApiKey'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 37.66s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os
import sys

# --- Configuration ---
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "pair with steak"
RESULT_LIMIT = 5
HYBRID_ALPHA = 0.5
MAX_PRICE = 50
MIN_POINTS = 90
REQUIRED_SUBSTRINGS = ["spice", "fruit", "berry", "cherry", "honey"]

# --- Retrieve Connection Details from Environment Variables ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_key = os.environ["WCD_TEST_KEY"]
    openai_key = os.environ["OPENAI_API_KEY"]
    print("Environment variables retrieved successfully.")
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set.")
    sys.exit(1) # Exit if essential variables are missing

# --- Connect to Weaviate Cloud ---
try:
    print(f"Connecting to Weaviate at {wcd_url}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_key),
        headers={
            # Pass the OpenAI API key for the text2vec-openai vectorizer
            "X-OpenAI-API-Key": openai_key
        },
    )
    # Check connection
    client.is_ready()
    print("Successfully connected to Weaviate Cloud.")

except Exception as e:
    print(f"Error connecting to Weaviate: {e}")
    sys.exit(1)

try:
    # --- Get the Collection Handle ---
    print(f"Accessing collection: '{COLLECTION_NAME}'")
    collection = client.collections.get(COLLECTION_NAME)

    # --- Define Filters ---
    # Note: Filters are combined using the & operator
    filters = (
        Filter.by_property("price").less_than(MAX_PRICE) &
        Filter.by_property("points").greater_than(MIN_POINTS) &
        Filter.by_property("review_body").contains_any(REQUIRED_SUBSTRINGS)
    )
    print("Filters defined:")
    print(f"  - Price < {MAX_PRICE}")
    print(f"  - Points > {MIN_POINTS}")
    print(f"  - Review body contains any of: {REQUIRED_SUBSTRINGS}")

    # --- Perform the Hybrid Search Query ---
    print(f"\nPerforming hybrid search for '{QUERY_TEXT}'...")
    print(f"  Limit: {RESULT_LIMIT}")
    print(f"  Alpha: {HYBRID_ALPHA}")

    response = collection.query.hybrid(
        query=QUERY_TEXT,
        limit=RESULT_LIMIT,
        alpha=HYBRID_ALPHA,
        filters=filters,
        # Specify only the properties needed in the output
        return_properties=["title", "country", "price", "points"]
        # Optionally include metadata like score if needed for debugging/ranking info
        # return_metadata=MetadataQuery(score=True)
    )

    # --- Process and Print Results ---
    print(f"\n--- Query Results ({len(response.objects)} found) ---")
    if not response.objects:
        print("No wines found matching all criteria.")
    else:
        for i, obj in enumerate(response.objects):
            props = obj.properties
            print(f"Result {i+1}:")
            print(f"  Title:   {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price:   ${props.get('price', 'N/A'):.2f}") # Format price
            print(f"  Points:  {props.get('points', 'N/A')}")
            # If you uncommented return_metadata above, you can print score:
            # if obj.metadata:
            #     print(f"  Score:   {obj.metadata.score:.4f}")
            print("-" * 20)

except Exception as e:
    print(f"\nAn error occurred during the query or processing: {e}")

finally:
    # --- Close the Connection ---
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Environment variables retrieved successfully.
Connecting to Weaviate at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Accessing collection: 'WineReview'
Filters defined:
  - Price < 50
  - Points > 90
  - Review body contains any of: ['spice', 'fruit', 'berry', 'cherry', 'honey']

Performing hybrid search for 'pair with steak'...
  Limit: 5
  Alpha: 0.5

--- Query Results (5 found) ---
Result 1:
  Title:   Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price:   $40.00
  Points:  92
--------------------
Result 2:
  Title:   Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price:   $49.00
  Points:  91
--------------------
Result 3:
  Title:   Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price:   $27.00
  Points:  91
--------------------
Result 4:
  Title:   Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price:   $25.00
  Points:  93
--------------------
Result 5:
  Title:   Château Rauzan-Ségla 2012  Margaux
  Country: France
  Price:   $0.00
  Points:  94
--------------------

Connection to Weaviate closed.

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 38.29s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import sys # Used for checking environment variables and exiting

# ================================
# Configuration & Environment Variables
# ================================
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_API_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COLLECTION_NAME = "WineReview" # As specified in the prompt

# Validate environment variables
if not all([WCD_URL, WCD_API_KEY, OPENAI_API_KEY]):
    print("Error: Please set the WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
    sys.exit(1)

print(f"Connecting to Weaviate Cloud at: {WCD_URL}")

# ================================
# Connect to Weaviate
# ================================
try:
    # Connect to the Weaviate Cloud instance
    # Pass OpenAI API key in headers for the text2vec-openai vectorizer
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_API_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )
    client.is_ready() # Check if connection is successful
    print("Successfully connected to Weaviate Cloud.")

except Exception as e:
    print(f"Error connecting to Weaviate: {e}")
    sys.exit(1)

# ================================
# Define Query Parameters
# ================================
query_text = "pair with steak"
result_limit = 5
hybrid_alpha = 0.5
max_price = 50
min_points = 90
required_keywords = ["spice", "fruit", "berry", "cherry", "honey"]

# Check if the collection exists
if not client.collections.exists(COLLECTION_NAME):
    print(f"Error: Collection '{COLLECTION_NAME}' does not exist.")
    print("Please ensure the collection is created with the appropriate schema,")
    print("including properties like 'title', 'country', 'price', 'points', 'review_body',")
    print("and configured with the 'text2vec-openai' vectorizer.")
    client.close()
    sys.exit(1)

# Get the collection object
try:
    wine_reviews = client.collections.get(COLLECTION_NAME)
    print(f"Successfully accessed collection: '{COLLECTION_NAME}'")
except Exception as e:
    print(f"Error accessing collection '{COLLECTION_NAME}': {e}")
    client.close()
    sys.exit(1)


# ================================
# Define Filters
# ================================
# Filter for price < 50
price_filter = Filter.by_property("price").less_than(max_price)

# Filter for points > 90
points_filter = Filter.by_property("points").greater_than(min_points)

# Filter for review_body containing any of the required keywords
# NOTE: Assumes the property name is 'review_body'. Adjust if different.
keyword_filter = Filter.by_property("review_body").contains_any(required_keywords)

# Combine all filters using logical AND (&)
combined_filter = price_filter & points_filter & keyword_filter

# ================================
# Perform Hybrid Search with Filters
# ================================
print(f"\nPerforming hybrid search for '{query_text}' with filters...")
print(f"- Limit: {result_limit}")
print(f"- Alpha: {hybrid_alpha}")
print(f"- Price < {max_price}")
print(f"- Points > {min_points}")
print(f"- Review contains any of: {required_keywords}")

try:
    response = wine_reviews.query.hybrid(
        query=query_text,
        limit=result_limit,
        alpha=hybrid_alpha,
        filters=combined_filter,
        # Specify the properties to return
        return_properties=["title", "country", "price", "points"]
    )

    # ================================
    # Print Results
    # ================================
    print("\n--- Search Results ---")
    if response.objects:
        for i, wine in enumerate(response.objects):
            props = wine.properties
            print(f"\nResult {i+1}:")
            print(f"  Title: {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price: {props.get('price', 'N/A')}")
            print(f"  Points: {props.get('points', 'N/A')}")
    else:
        print("No matching wines found for the given criteria.")

except Exception as e:
    print(f"\nAn error occurred during the query: {e}")

finally:
    # ================================
    # Close Connection
    # ================================
    print("\nClosing Weaviate connection.")
    client.close()
    print("Connection closed.")
```

**Output**:
```
Connecting to Weaviate Cloud at: https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate Cloud.
Successfully accessed collection: 'WineReview'

Performing hybrid search for 'pair with steak' with filters...
- Limit: 5
- Alpha: 0.5
- Price < 50
- Points > 90
- Review contains any of: ['spice', 'fruit', 'berry', 'cherry', 'honey']

--- Search Results ---

Result 1:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: 40.0
  Points: 92

Result 2:
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: 49.0
  Points: 91

Result 3:
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: 27.0
  Points: 91

Result 4:
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: 25.0
  Points: 93

Result 5:
  Title: Château Rauzan-Ségla 2012  Margaux
  Country: France
  Price: 0.0
  Points: 94

Closing Weaviate connection.
Connection closed.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 61.05s)

**Generated Code**:
```python
import weaviate
import os
import sys
import time  # Import time for potential delays if needed

# Import specific classes from the Weaviate v4 client
from weaviate.auth import AuthApiKey
from weaviate.classes.config import Property, DataType, Configure

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS = 50

print("Starting Weaviate batch import script...")

# --- Get Connection Details from Environment Variables ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_key = os.environ["WCD_TEST_KEY"]
    print(f"Attempting to connect to Weaviate Cloud at: {wcd_url}")
except KeyError:
    print("\nError: Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    print("Example:")
    print("  export WCD_TEST_URL='https://your-cluster-name.weaviate.network'")
    print("  export WCD_TEST_KEY='YOUR_WEAVIATE_CLOUD_API_KEY'")
    sys.exit(1)

# --- Main Script Logic ---
try:
    # Use 'with' statement for automatic connection management (connect & close)
    print("Connecting to Weaviate Cloud...")
    with weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(wcd_key),
        # Optional: Add headers if required by your setup (e.g., for module API keys)
        # headers={
        #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY", ""), # Example for OpenAI
        #     # Add other module API keys if needed
        # }
    ) as client:
        print(f"Connection successful. Client is ready: {client.is_ready()}")

        # 1. Check if collection exists and delete if it does (for a clean run)
        if client.collections.exists(COLLECTION_NAME):
            print(f"Deleting existing collection: '{COLLECTION_NAME}'...")
            client.collections.delete(COLLECTION_NAME)
            # Short pause to ensure deletion is processed, sometimes helpful in cloud envs
            time.sleep(2)
            print(f"Collection '{COLLECTION_NAME}' deleted.")

        # 2. Create the collection with specified properties
        print(f"Creating collection: '{COLLECTION_NAME}'...")
        # Use client.collections.create to define the schema
        products_collection = client.collections.create(
            name=COLLECTION_NAME,
            description="A collection to store demo product information",
            properties=[
                Property(name="name", data_type=DataType.TEXT, description="The name of the product"),
                Property(name="description", data_type=DataType.TEXT, description="A description of the product"),
            ],
            # --- Optional: Vectorizer Configuration ---
            # If you want Weaviate to generate vectors (e.g., for semantic search),
            # uncomment and configure a vectorizer. Otherwise, vectors won't be generated.
            # vectorizer_config=Configure.Vectorizer.text2vec_openai(), # Example: OpenAI
            # vectorizer_config=Configure.Vectorizer.text2vec_cohere(), # Example: Cohere
            # vectorizer_config=Configure.Vectorizer.text2vec_huggingface(
            #     model="sentence-transformers/all-MiniLM-L6-v2" # Example: HuggingFace MiniLM
            # ),
            # If you manage vectors externally or don't need them, set to None:
             vectorizer_config=Configure.Vectorizer.none(), # No automatic vectorization

            # --- Optional: Generative Module Configuration ---
            # If using generative search features (requires a vectorizer)
            # generative_config=Configure.Generative.openai() # Example
        )
        print(f"Collection '{COLLECTION_NAME}' created successfully.")

        # 3. Prepare data objects for batch import
        print(f"Preparing {NUM_OBJECTS} objects...")
        objects_to_add = []
        for i in range(NUM_OBJECTS):
            data_object = {
                "name": f"Product {i}",
                "description": f"This is the description for product number {i}."
            }
            objects_to_add.append(data_object)
        print(f"{len(objects_to_add)} objects prepared.")

        # 4. Perform batch import using the collection object
        print(f"Starting batch import into '{COLLECTION_NAME}'...")
        # The client handles batching automatically with insert_many
        # For very large imports, consider manual batching with `collection.batch.configure(...)`
        # and `with collection.batch as batch:` context manager for more control.
        # However, insert_many is simpler for moderate amounts.
        insert_result = products_collection.data.insert_many(objects_to_add)

        print("Batch import finished.")

        # Check for errors during import
        if insert_result.has_errors:
            print("\nErrors occurred during batch import:")
            error_count = 0
            for index, error in insert_result.errors.items():
                print(f" - Object index {index}: {error.message}")
                error_count += 1
            print(f"Total errors: {error_count}")
            # Decide if script should exit or continue based on errors
            # sys.exit(1) # Optional: exit if errors are critical
        else:
            # insert_result.uuids provides a dict mapping original index to generated UUID
            successful_imports = len(insert_result.uuids)
            print(f"Successfully imported {successful_imports} objects.")

        # 5. Verify the number of objects in the collection
        print(f"\nVerifying object count in '{COLLECTION_NAME}'...")
        # Use the aggregate method on the collection object
        # It's good practice to wait a moment for indexing to catch up in some cases
        time.sleep(1)
        count_response = products_collection.aggregate.over_all(total_count=True)
        total_count = count_response.total_count

        print(f"Reported number of objects in '{COLLECTION_NAME}': {total_count}")

        # Optional: Compare expected vs actual count (adjusting for potential import errors)
        expected_count = NUM_OBJECTS - (error_count if insert_result.has_errors else 0)
        if total_count == expected_count:
            print("Object count verified successfully.")
        else:
            print(f"Warning: Expected {expected_count} objects based on import results, but found {total_count}.")

    # The 'with' statement ensures client.close() is called automatically here
    print("\nConnection closed.")

# --- Error Handling for Connection and Other Issues ---
except weaviate.exceptions.AuthenticationFailedException:
    print("\nError: Authentication failed. Please check your WCD_TEST_URL and WCD_TEST_KEY.")
    sys.exit(1)
except weaviate.exceptions.WeaviateQueryException as e:
    print(f"\nError during Weaviate query/operation: {e}")
    # This can catch issues during collection creation or aggregation if parameters are wrong
    sys.exit(1)
except ConnectionError as e:
    print(f"\nError: Could not connect to Weaviate instance at {wcd_url}.")
    print(f"Details: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    # Consider logging the full traceback for debugging complex issues
    # import traceback
    # traceback.print_exc()
    sys.exit(1)

print("\nScript finished.")
```

**Output**:
```
Starting Weaviate batch import script...
Attempting to connect to Weaviate Cloud at: https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud
Connecting to Weaviate Cloud...
Connection successful. Client is ready: True
Deleting existing collection: 'DemoProducts'...
Collection 'DemoProducts' deleted.
Creating collection: 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Preparing 50 objects...
50 objects prepared.
Starting batch import into 'DemoProducts'...
Batch import finished.
Successfully imported 50 objects.

Verifying object count in 'DemoProducts'...
Reported number of objects in 'DemoProducts': 50
Object count verified successfully.

Connection closed.

Script finished.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 41.23s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc # Use alias for Weaviate classes
import os
import sys

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

# --- 1. Connect to Weaviate Cloud ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")

if not wcd_url:
    print("ERROR: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_key:
    print("ERROR: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

try:
    # Use connect_to_weaviate_cloud and AuthApiKey from weaviate.classes.init
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=wvc.init.Auth.api_key(wcd_key),
        # Optional: Add headers if your instance needs them (e.g., for API keys of models)
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY"), # Example
        # }
    )
    client.is_ready() # Check connection
    print("Successfully connected to Weaviate Cloud.")

except Exception as e:
    print(f"Error connecting to Weaviate Cloud: {e}")
    sys.exit(1)

# --- 2. Get or Create Collection ---
# Define the properties using the latest syntax (weaviate.classes.config)
properties = [
    wvc.config.Property(name="name", data_type=wvc.config.DataType.TEXT),
    wvc.config.Property(name="description", data_type=wvc.config.DataType.TEXT),
]

try:
    # Check if collection exists, delete if it does for a clean run (optional)
    # if client.collections.exists(COLLECTION_NAME):
    #     print(f"Collection '{COLLECTION_NAME}' already exists. Deleting for clean run.")
    #     client.collections.delete(COLLECTION_NAME)

    # Get or create the collection
    # Use get_or_create for convenience
    products_collection = client.collections.get_or_create(
        name=COLLECTION_NAME,
        properties=properties,
        # If you want a specific vectorizer (e.g., text2vec-openai), configure it here:
        # vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai()
        # If no vectorizer is specified, Weaviate uses its default or fails if none configured.
    )
    print(f"Collection '{COLLECTION_NAME}' is ready.")

except Exception as e:
    print(f"Error handling collection '{COLLECTION_NAME}': {e}")
    client.close()
    sys.exit(1)


# --- 3. Prepare Data for Batch Import ---
print(f"Preparing {NUM_OBJECTS_TO_IMPORT} objects for import...")
data_objects = [
    {
        "name": f"Product {i}",
        "description": f"Description for product {i}"
    } for i in range(1, NUM_OBJECTS_TO_IMPORT + 1) # Generate 50 objects
]

# --- 4. Batch Import Data ---
print(f"Starting batch import into '{COLLECTION_NAME}'...")
try:
    # Use the dynamic batch context manager
    with products_collection.batch.dynamic() as batch:
        for data_obj in data_objects:
            batch.add_object(
                properties=data_obj,
                # Weaviate generates a UUID if not provided
            )
            # Basic error check within the loop (optional, depends on needs)
            # if batch.number_errors > 0:
            #     print(f"Warning: {batch.number_errors} errors occurred during batch.")
                # Decide if you want to break early, e.g., break

    # Check for failed objects *after* the context manager exits
    if products_collection.batch.failed_objects:
        print(f"\nImport failed for {len(products_collection.batch.failed_objects)} objects.")
        # Optionally print details about the first few failures
        # for i, failed in enumerate(products_collection.batch.failed_objects[:5]):
        #     print(f"  Failed object {i+1}: {failed.message}")
        #     print(f"  Original object: {failed.original_object}")
    else:
        print("Batch import completed successfully.")

except Exception as e:
    print(f"\nError during batch import: {e}")
    client.close()
    sys.exit(1)

# --- 5. Print Object Count ---
try:
    # Use the aggregation API to get the total count
    aggregate_result = products_collection.aggregate.over_all(total_count=True)
    total_count = aggregate_result.total_count
    print(f"\nTotal number of objects in '{COLLECTION_NAME}': {total_count}")

except Exception as e:
    print(f"Error retrieving object count: {e}")


# --- 6. Close Connection ---
finally:
    # Ensure the client connection is closed
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Connection closed.")
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Error handling collection 'DemoProducts': '_Collections' object has no attribute 'get_or_create'

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 45.23s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

print("Starting Weaviate script...")

# ================================
# Connect to Weaviate Cloud
# ================================
print("Connecting to Weaviate Cloud...")

# Check for required environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

client = None # Initialize client to None for finally block
try:
    # Connect to the Weaviate Cloud instance using environment variables
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Optional: Add headers if needed, e.g., for OpenAI keys
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")
        # }
    )

    # Check connection
    client.is_ready()
    print("Successfully connected to Weaviate Cloud.")

    # ================================
    # Define Collection Details
    # ================================
    collection_name = "DemoProducts"
    print(f"Working with collection: '{collection_name}'")

    # ================================
    # Delete Existing Collection (Optional - for clean runs)
    # ================================
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it for a clean start.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # ================================
    # Create Collection
    # ================================
    print(f"Creating collection '{collection_name}'...")
    products_collection = client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
        # No vectorizer specified - Weaviate will use its default behavior
        # (often 'none' unless configured otherwise server-side)
    )
    print(f"Collection '{collection_name}' created successfully.")

    # ================================
    # Prepare Data for Batch Import
    # ================================
    num_objects_to_import = 50
    print(f"Preparing {num_objects_to_import} objects for import...")
    data_objects = [
        {
            "name": f"Product {i}",
            "description": f"This is the description for product {i}."
        }
        for i in range(num_objects_to_import)
    ]
    print("Data preparation complete.")

    # ================================
    # Batch Import Objects
    # ================================
    print(f"Starting batch import of {num_objects_to_import} objects...")
    # Get a collection object reference for batching
    # Note: products_collection from the create call could also be used
    collection = client.collections.get(collection_name)

    with collection.batch.dynamic() as batch:
        for data_obj in data_objects:
            batch.add_object(
                properties=data_obj,
                # uuid=... # Optionally specify UUIDs
            )
        # The batch context manager automatically executes the batch import upon exit

    # Optional: Check for batch import errors
    if collection.batch.failed_objects:
        print(f"Batch import encountered errors. Number of failed imports: {len(collection.batch.failed_objects)}")
        # You could inspect collection.batch.failed_objects[0] for details
    else:
        print("Batch import completed successfully.")

    # ================================
    # Verify Object Count
    # ================================
    print("Verifying the number of objects in the collection...")
    # Use the aggregate method to get the total count
    count_response = collection.aggregate.over_all(total_count=True)
    object_count = count_response.total_count

    print(f"Found {object_count} objects in the '{collection_name}' collection.")

    # As a check, assert the count if desired
    # assert object_count == num_objects_to_import

except Exception as e:
    print(f"An error occurred during the Weaviate operation: {e}")
    # Consider more specific error handling based on Weaviate exceptions if needed

finally:
    # ================================
    # Close Connection
    # ================================
    if client:
        print("Closing Weaviate connection.")
        client.close()
    else:
        print("No active Weaviate connection to close.")

print("Script finished.")
```

**Output**:
```
Starting Weaviate script...
Connecting to Weaviate Cloud...
Successfully connected to Weaviate Cloud.
Working with collection: 'DemoProducts'
Collection 'DemoProducts' already exists. Deleting it for a clean start.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Preparing 50 objects for import...
Data preparation complete.
Starting batch import of 50 objects...
Batch import completed successfully.
Verifying the number of objects in the collection...
Found 50 objects in the 'DemoProducts' collection.
Closing Weaviate connection.
Script finished.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

### gemini/gemini-2.0-flash-lite

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.52s)

**Generated Code**:
```python
import os
import weaviate

# Retrieve environment variables
url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not url or not api_key:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    exit(1)  # Exit with an error code

# Configure client
client = weaviate.Client(
    url=url,
    auth_client_secret=weaviate.AuthApiKey(api_key=api_key),
)

# Check server status
try:
    client.is_ready()
    print("Successfully connected to Weaviate Cloud and server is ready.")
except Exception as e:
    print(f"Error connecting to Weaviate Cloud or server not ready: {e}")
    exit(1) # Exit with an error code
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:14: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 2.23s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.auth import Auth

# Retrieve the URL and API key from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Check if the environment variables are set
if not cluster_url or not api_key:
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY."
    )

# Connect to the Weaviate Cloud instance
client = weaviate.Client(
    url=cluster_url,
    auth_client_secret=Auth.api_key(api_key),
)

# Check if the server is ready
if not client.is_ready():
    raise Exception("Weaviate server is not ready.")

# Optionally, close the client connection (recommended)
client.close()

print("Successfully connected to Weaviate Cloud and verified server readiness.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes.auth import Auth
ModuleNotFoundError: No module named 'weaviate.classes.auth'

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 7.63s)

**Generated Code**:
```python
import os
import weaviate

# Configuration from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    exit(1)

# Initialize the Weaviate client
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
)

# Define the class (collection) name
class_name = "DemoProducts"

# Delete the class if it exists
try:
    client.schema.delete_class(class_name)
    print(f"Deleted existing class '{class_name}'")
except weaviate.exceptions.UnexpectedStatusCodeException as e:
    if e.status_code == 404:
        print(f"Class '{class_name}' not found, proceeding to create.")
    else:
        print(f"Error deleting class '{class_name}': {e}")
        exit(1)  # Exit on other deletion errors

# Define the properties for the class
properties = [
    {
        "name": "name",
        "dataType": ["text"],
    },
    {
        "name": "description",
        "dataType": ["text"],
    },
    {
        "name": "price",
        "dataType": ["number"],
    },
    {
        "name": "in_stock",
        "dataType": ["boolean"],
    },
]

# Create the class schema
try:
    class_definition = {
        "class": class_name,
        "properties": properties,
    }
    client.schema.create_class(class_definition)
    print(f"Created class '{class_name}'")
except weaviate.exceptions.UnexpectedStatusCodeException as e:
    print(f"Error creating class '{class_name}': {e}")
    exit(1)

print("Schema creation completed successfully.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:14: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 3.13s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get environment variables for Weaviate Cloud connection
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
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
```

**Output**:
```
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 3.56s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth

# Retrieve environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url or not wcd_key:
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY."
    )

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key)
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

print(f"Collection '{collection_name}' created successfully.")

# Close connection (optional, as the client is context managed)
# client.close()
```

**Output**:
```
Collection 'DemoProducts' created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.35s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client

# Retrieve Weaviate Cloud credentials from environment variables
url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not all([url, api_key, openai_api_key]):
    raise ValueError(
        "Please set the environment variables: WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY"
    )


# Initialize the Weaviate client
client: Client = weaviate.Client(
    url=url,
    auth_client_secret=weaviate.AuthApiKey(api_key=api_key),
    additional_headers={"X-OpenAI-Api-Key": openai_api_key},
)

# Define the query
query_text = "dessert wine"

# Perform the query
try:
    result = (
        client.query.get("WineReview", ["title", "country", "price", "points"])
        .with_near_text({"concepts": [query_text]})
        .with_limit(2)
        .do()
    )

    # Print the results
    if result and result.get("data") and result["data"].get("Get") and result["data"]["Get"].get("WineReview"):
        for wine in result["data"]["Get"]["WineReview"]:
            print(f"Title: {wine.get('title')}")
            print(f"Country: {wine.get('country')}")
            print(f"Price: {wine.get('price')}")
            print(f"Points: {wine.get('points')}")
            print("-" * 20)
    else:
        print("No matching wines found.")

except Exception as e:
    print(f"An error occurred: {e}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:17: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client: Client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 17, in <module>
    client: Client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.77s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Retrieve environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Validate environment variables
if not all([cluster_url, api_key, openai_api_key]):
    raise ValueError(
        "Please set the environment variables: WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY"
    )

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
    headers={
        "X-OpenAI-API-Key": openai_api_key
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform the query
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the results
if response.objects:
    for obj in response.objects:
        properties = obj.properties
        print(f"Title: {properties.get('title')}")
        print(f"Country: {properties.get('country')}")
        print(f"Price: {properties.get('price')}")
        print(f"Points: {properties.get('points')}")
        print("-" * 20)
else:
    print("No matching wines found.")

client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
--------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
--------------------

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 6.52s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure
from weaviate.classes.query import MetadataQuery

# ================================
# Connect to Weaviate Cloud
# ================================

# Get environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not all([cluster_url, api_key, openai_api_key]):
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY"
    )

# Connect to the Weaviate Cloud instance
client = weaviate.Client(
    url=cluster_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=api_key),
    additional_headers={"X-OpenAI-Api-Key": openai_api_key},
)

# ================================
# Query the 'WineReview' collection
# ================================

collection_name = "WineReview"  # Assuming the collection exists

try:
    collection = client.collections.get(collection_name)
except weaviate.exceptions.InvalidUserInputException as e:
    print(f"Error: Collection '{collection_name}' not found.  Please create it first. Error: {e}")
    exit()  # Exit the program if the collection doesn't exist


response = collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=[
        "title",
        "country",
        "price",
        "points",
    ],
)

if response.objects:
    for obj in response.objects:
        properties = obj.properties
        print(f"Title: {properties.get('title')}")
        print(f"Country: {properties.get('country')}")
        print(f"Price: {properties.get('price')}")
        print(f"Points: {properties.get('points')}")
        print("-" * 20)
else:
    print("No matching wines found.")

# Close connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:21: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 21, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.58s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud credentials from environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Check if all required environment variables are set
if not all([WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY]):
    print("Error: Required environment variables are not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY")
    exit(1)


# Configure the Weaviate client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(WEAVIATE_API_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY}
)


# Define the query
query = "pair with steak"
limit = 5
alpha = 0.5
substrings = ["spice", "fruit", "berry", "cherry", "honey"]


try:
    # Perform the hybrid search with filters and substring check
    result = (
        client.query
        .get("WineReview", ["title", "country", "price", "points", "review_body"])
        .with_hybrid(query=query, alpha=alpha)
        .with_where(
            {
                "operator": "And",
                "operands": [
                    {"path": ["price"], "operator": "LessThan", "valueNumber": 50},
                    {"path": ["points"], "operator": "GreaterThan", "valueNumber": 90},
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueText": f"*({')|('.join(substrings)})*",  # Construct the OR-based substring filter
                    },
                ],
            }
        )
        .with_limit(limit)
        .do()
    )

    # Process and print the results
    if result and result.get("data") and result["data"].get("Get") and result["data"]["Get"].get("WineReview"):
        wine_reviews = result["data"]["Get"]["WineReview"]
        for wine in wine_reviews:
            print(f"Title: {wine.get('title')}")
            print(f"Country: {wine.get('country')}")
            print(f"Price: {wine.get('price')}")
            print(f"Points: {wine.get('points')}")
            print("-" * 20)
    else:
        print("No matching wines found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up client
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:17: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 17, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.07s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Retrieve environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
    headers={
        "X-OpenAI-API-Key": openai_api_key
    },
)

# Get the 'WineReview' collection
try:
    collection = client.collections.get("WineReview")
except Exception as e:
    print(f"Error getting 'WineReview' collection: {e}")
    client.close()
    exit()


# Perform the hybrid search
try:
    response = collection.query.hybrid(
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

    # Print the results
    for obj in response.objects:
        if obj.properties:  # Check if obj.properties is not None
            print(f"Title: {obj.properties.get('title', 'N/A')}")
            print(f"Country: {obj.properties.get('country', 'N/A')}")
            print(f"Price: {obj.properties.get('price', 'N/A')}")
            print(f"Points: {obj.properties.get('points', 'N/A')}")
            print(f"Score: {obj.metadata.score}")  # Access the score metadata
            print("-" * 20)
except Exception as e:
    print(f"Error during query: {e}")

# Close the client connection
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
Score: 0.5
--------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
Score: 0.4629642069339752
--------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Score: 0.2213282436132431
--------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Score: 0.065570168197155
--------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
Score: 0.01466419454663992
--------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.22s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery, Filter
from weaviate.classes.config import Configure

# ================================
# Connect to Weaviate
# ================================

# Get environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not all([cluster_url, api_key, openai_api_key]):
    print("Error: Missing required environment variables.")
    print("Ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set.")
    exit(1)

try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key),
    )
except Exception as e:
    print(f"Error connecting to Weaviate Cloud: {e}")
    exit(1)

# ================================
# Query the 'WineReview' collection
# ================================

collection_name = "WineReview"  # Assuming the collection name is WineReview
query_text = "pair with steak"
limit = 5
alpha = 0.5
substrings = ["spice", "fruit", "berry", "cherry", "honey"]

try:
    results = (
        client.collections.get(collection_name)
        .query.hybrid(
            query=query_text,
            alpha=alpha,
            limit=limit,
        )
        .with_additional(MetadataQuery(score=True))
        .with_where(
            (
                Filter.by_property("price").less_than(50)
                & Filter.by_property("points").greater_than(90)
                & Filter.by_property("review_body").contains_any(substrings)
            )
        )
        .fetch_objects()
    )
except Exception as e:
    print(f"Error during query: {e}")
    exit(1)

# ================================
# Print the results
# ================================

if results and results.objects:
    for result in results.objects:
        properties = result.properties
        print("-----------------------------")
        print(f"Title: {properties.get('title')}")
        print(f"Country: {properties.get('country')}")
        print(f"Price: {properties.get('price')}")
        print(f"Points: {properties.get('points')}")
        #print(f"Review Body: {properties.get('review_body')}") # Uncomment to print review body
        print(f"Score: {result.metadata.score}")
else:
    print("No matching wines found.")

# Close connection
client.close()
```

**Output**:
```
Error during query: Query call with protocol GRPC search failed with message <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2025-04-03T09:01:52.303537177+00:00", grpc_status:2, grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"}"
>.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 7.35s)

**Generated Code**:
```python
import os
import weaviate

# Environment variables for Weaviate Cloud
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Initialize the Weaviate client
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY)
)


# Define the schema for the "DemoProducts" class if it doesn't exist
class_name = "DemoProducts"
try:
    client.schema.get_class(class_name)
    print(f"Class '{class_name}' already exists.  Skipping schema creation.")

except weaviate.exceptions.UnexpectedStatusCodeException as e:
    if e.status_code == 404:  # Class doesn't exist
        schema_definition = {
            "class": class_name,
            "description": "Products demo class",
            "properties": [
                {"name": "name", "dataType": ["text"], "description": "Product name"},
                {"name": "description", "dataType": ["text"], "description": "Product description"},
            ],
        }
        client.schema.create_class(schema_definition)
        print(f"Class '{class_name}' created.")
    else:
        raise  # Re-raise other exceptions


# Batch import data
def batch_import_products(num_products):
    with client.batch(
        batch_size=100
    ) as batch:  # Use batch_size for performance.
        for i in range(num_products):
            product_data = {
                "name": f"Product {i}",
                "description": f"Description {i}",
            }
            batch.add_data_object(
                data_object=product_data,
                class_name=class_name,
            )


batch_import_products(50)
print("Batch import completed.")

# Get the number of objects in the collection
try:
    result = (
        client.query.get(class_name, ["name"])  # Get the number by counting names
        .with_limit(10000)  # get at most 10000
        .do()
    )
    count = len(result["data"]["Get"][class_name])
    print(f"Number of objects in '{class_name}': {count}")
except Exception as e:
    print(f"Error getting object count: {e}")

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 7.68s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Get Weaviate Cloud credentials from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=AuthApiKey(WCD_TEST_KEY),
)

collection_name = "DemoProducts"  # Use the specified collection name

# Create the collection if it doesn't exist
if not client.collections.exists(collection_name):
    client.collections.create(
        name=collection_name,
        properties=[
            {"name": "name", "dataType": ["text"]},
            {"name": "description", "dataType": ["text"]},
        ],
    )

# Get the collection object
collection = client.collections.get(collection_name)

# Prepare data for batch import
data_rows = [
    {"name": f"Product {i}", "description": f"Description {i}"} for i in range(50)
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed imports
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Number of objects in '{collection_name}': {len(collection)}")

# Close the connection
client.close()
```

**Output**:
```
Number of objects in 'DemoProducts': 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 5.43s)

**Generated Code**:
```python
# ================================
# Connect to Weaviate
# ================================
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Retrieve credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key=api_key)
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
    ]
)


# ================================
# Batch import
# ================================
objects_to_import = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    }
    for i in range(50)
]

collection = client.collections.get(collection_name)

with collection.batch.dynamic() as batch:
    for obj in objects_to_import:
        batch.add_object(
            properties=obj,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Number of objects in the collection: {len(collection)}")

# Close connection
client.close()
```

**Output**:
```
Number of objects in the collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

### openai/gpt-4o-2024-11-20

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.38s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Ensure the environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Create a Weaviate client
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # Optional, depending on your setup
    }
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready. Please check your configuration.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:13: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 4.97s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Ensure the environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(WCD_TEST_KEY)
)

# Check if the server is ready
assert client.is_ready(), "Weaviate server is not ready to accept requests."

# Close the client connection
client.close()
```

**Errors**:
```
/code/code.py:14: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.51s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Validate environment variables
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI modules
)

# Define the class schema for DemoProducts
demo_products_schema = {
    "class": "DemoProducts",
    "description": "A collection of demo products",
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
            "description": "The name of the product",
        },
        {
            "name": "description",
            "dataType": ["text"],
            "description": "A description of the product",
        },
        {
            "name": "price",
            "dataType": ["number"],
            "description": "The price of the product",
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"],
            "description": "Whether the product is in stock",
        },
    ],
}

# Check if the class already exists
if client.schema.exists("DemoProducts"):
    print("Class 'DemoProducts' already exists. Deleting it...")
    client.schema.delete_class("DemoProducts")
    print("Class 'DemoProducts' deleted.")

# Create the class
print("Creating class 'DemoProducts'...")
client.schema.create_class(demo_products_schema)
print("Class 'DemoProducts' created successfully.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:13: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.28s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Ensure the environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
auth_config = AuthApiKey(api_key=WCD_TEST_KEY)
client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)

# Define the collection (class) name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.schema.exists(collection_name):
    client.schema.delete_class(collection_name)

# Define the schema for the collection
schema = {
    "class": collection_name,
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
        {
            "name": "price",
            "dataType": ["number"],
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"],
        },
    ],
}

# Create the collection
client.schema.create_class(schema)

print(f"Created collection: {collection_name}")

# Close the client connection (optional, as the client will close automatically when the script ends)
client.close()
```

**Errors**:
```
/code/code.py:15: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.11s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.schema.properties import Property, DataType

# ================================
# Connect to Weaviate
# ================================
# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI vectorizer
)

# ================================
# Create a collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.schema.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it...")
    client.schema.delete_class(collection_name)

# Define the schema for the collection
schema = {
    "class": collection_name,
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
        {
            "name": "price",
            "dataType": ["number"],
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"],
        },
    ],
    "vectorizer": "text2vec-openai",  # Optional: Use OpenAI vectorizer for semantic search
}

# Create the collection
client.schema.create_class(schema)
print(f"Collection '{collection_name}' created successfully.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.schema.properties import Property, DataType
ModuleNotFoundError: No module named 'weaviate.schema'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.56s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Validate environment variables
if not weaviate_url or not weaviate_api_key or not openai_api_key:
    raise ValueError("Missing required environment variables.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=weaviate_url,
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key,  # OpenAI API key for text2vec-openai
        "Authorization": f"Bearer {weaviate_api_key}",  # Weaviate Cloud API key
    },
)

# Query the WineReview collection
query = "dessert wine"
response = client.query.get(
    "WineReview",  # Class name
    ["title", "country", "price", "points"],  # Fields to retrieve
).with_near_text({
    "concepts": [query],
}).with_limit(2).do()

# Check for errors in the response
if "errors" in response:
    print("Error:", response["errors"])
else:
    # Print the results
    results = response.get("data", {}).get("Get", {}).get("WineReview", [])
    for wine in results:
        print(f"Title: {wine.get('title')}")
        print(f"Country: {wine.get('country')}")
        print(f"Price: {wine.get('price')}")
        print(f"Points: {wine.get('points')}")
        print("-" * 40)
```

**Errors**:
```
/code/code.py:14: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.08s)

**Generated Code**:
```python
import weaviate
from weaviate.auth import AuthApiKey
import os

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

# Query the 'WineReview' collection
response = client.query.get(
    "WineReview",  # Class name
    ["title", "country", "price", "points"]  # Properties to retrieve
).with_near_text({
    "concepts": ["dessert wine"]
}).with_limit(2).do()

# Print the results
if "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
    wines = response["data"]["Get"]["WineReview"]
    for wine in wines:
        print(f"Title: {wine.get('title')}")
        print(f"Country: {wine.get('country')}")
        print(f"Price: {wine.get('price')}")
        print(f"Points: {wine.get('points')}")
        print("-" * 40)
else:
    print("No results found.")

# Close the client connection
client.close()
```

**Errors**:
```
/code/code.py:11: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 19.38s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery

# ================================
# Connect to Weaviate Cloud
# ================================
# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
)

# ================================
# Query the WineReview collection
# ================================
# Access the WineReview collection
wine_review_collection = client.collections.get("WineReview")

# Perform a semantic search using the text2vec-openai vectorizer
response = wine_review_collection.query.near_text(
    query="dessert wine",
    limit=2,  # Limit the results to 2
    return_metadata=MetadataQuery(distance=True),  # Include distance metadata
)

# ================================
# Print the results
# ================================
for wine in response.objects:
    properties = wine.properties
    print(f"Title: {properties.get('title')}")
    print(f"Country: {properties.get('country')}")
    print(f"Price: {properties.get('price')}")
    print(f"Points: {properties.get('points')}")
    print(f"Distance: {wine.metadata.distance}")
    print("-" * 40)

# Close the connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 478, in __call
    res = await _Retry(4).with_exponential_backoff(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 31, in with_exponential_backoff
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 28, in with_exponential_backoff
    return await f(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/grpc/aio/_call.py", line 327, in __await__
    raise _create_rpc_error(
grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY", grpc_status:2, created_time:"2025-04-03T09:03:27.738082305+00:00"}"
>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 27, in <module>
    response = wine_review_collection.query.near_text(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/queries/near_text/query.py", line 97, in near_text
    res = await self._query.near_text(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 490, in __call
    raise WeaviateQueryError(str(e), "GRPC search")  # pyright: ignore
weaviate.exceptions.WeaviateQueryError: Query call with protocol GRPC search failed with message <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"explorer: get class: concurrentTargetVectorSearch): explorer: get class: vectorize search vector: vectorize params: vectorize params: vectorize keywords: remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY", grpc_status:2, created_time:"2025-04-03T09:03:27.738082305+00:00"}"
>.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 17.89s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.exceptions import WeaviateException

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate environment variables
if not WCD_TEST_URL or not WCD_TEST_KEY or not OPENAI_API_KEY:
    raise ValueError("Ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set in the environment variables.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY,
        "Authorization": f"Bearer {WCD_TEST_KEY}",
    },
)

# Define the query parameters
query = "pair with steak"
limit = 5
alpha = 0.5
price_limit = 50
points_min = 90
required_substrings = ["spice", "fruit", "berry", "cherry", "honey"]

# Construct the GraphQL query
graphql_query = {
    "query": f"""
    {{
        Get {{
            WineReview(
                hybrid: {{
                    query: "{query}",
                    alpha: {alpha}
                }},
                limit: {limit},
                where: {{
                    operator: And,
                    operands: [
                        {{
                            path: ["price"],
                            operator: LessThan,
                            valueInt: {price_limit}
                        }},
                        {{
                            path: ["points"],
                            operator: GreaterThan,
                            valueInt: {points_min}
                        }},
                        {{
                            operator: Or,
                            operands: [
                                {{
                                    path: ["review_body"],
                                    operator: Like,
                                    valueText: "*spice*"
                                }},
                                {{
                                    path: ["review_body"],
                                    operator: Like,
                                    valueText: "*fruit*"
                                }},
                                {{
                                    path: ["review_body"],
                                    operator: Like,
                                    valueText: "*berry*"
                                }},
                                {{
                                    path: ["review_body"],
                                    operator: Like,
                                    valueText: "*cherry*"
                                }},
                                {{
                                    path: ["review_body"],
                                    operator: Like,
                                    valueText: "*honey*"
                                }}
                            ]
                        }}
                    ]
                }}
            ) {{
                title
                country
                price
                points
            }}
        }}
    }}
    """
}

# Execute the query
try:
    response = client.query.raw(graphql_query)
    results = response.get("data", {}).get("Get", {}).get("WineReview", [])

    # Print the results
    if results:
        print("Matching Wines:")
        for wine in results:
            print(f"Title: {wine.get('title')}")
            print(f"Country: {wine.get('country')}")
            print(f"Price: {wine.get('price')}")
            print(f"Points: {wine.get('points')}")
            print("-" * 40)
    else:
        print("No matching wines found.")
except WeaviateException as e:
    print(f"An error occurred while querying Weaviate: {e}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.exceptions import WeaviateException
ImportError: cannot import name 'WeaviateException' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.64s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    }
)

# Define the query parameters
query = "pair with steak"
limit = 5
alpha = 0.5

# Define the filters
filters = {
    "operator": "And",
    "operands": [
        {
            "path": ["price"],
            "operator": "LessThan",
            "valueInt": 50
        },
        {
            "path": ["points"],
            "operator": "GreaterThan",
            "valueInt": 90
        },
        {
            "operator": "Or",
            "operands": [
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*spice*"
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*fruit*"
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*berry*"
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*cherry*"
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*honey*"
                }
            ]
        }
    ]
}

# Perform the hybrid search query
response = client.query.get(
    "WineReview",  # Class name
    ["title", "country", "price", "points"]  # Properties to retrieve
).with_hybrid(
    query=query,
    alpha=alpha
).with_limit(
    limit
).with_where(
    filters
).do()

# Process and print the results
if "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
    results = response["data"]["Get"]["WineReview"]
    for wine in results:
        print(f"Title: {wine.get('title')}")
        print(f"Country: {wine.get('country')}")
        print(f"Price: {wine.get('price')}")
        print(f"Points: {wine.get('points')}")
        print("-" * 40)
else:
    print("No results found.")

# Close the client connection
client.close()
```

**Errors**:
```
/code/code.py:11: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.93s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# ================================
# Connect to Weaviate Cloud
# ================================
# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY)
)

# ================================
# Query the WineReview collection
# ================================
# Define the filter conditions
price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)
review_body_filter = Filter.by_property("review_body").contains_any(
    ["spice", "fruit", "berry", "cherry", "honey"]
)

# Combine filters using AND
combined_filter = price_filter & points_filter & review_body_filter

# Perform the hybrid search
wine_review_collection = client.collections.get("WineReview")
response = wine_review_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    filters=combined_filter,
    return_metadata=MetadataQuery(score=True),  # Include scores in the response
    limit=5
)

# ================================
# Print the results
# ================================
for wine in response.objects:
    properties = wine.properties
    print(f"Title: {properties.get('title')}")
    print(f"Country: {properties.get('country')}")
    print(f"Price: {properties.get('price')}")
    print(f"Points: {properties.get('points')}")
    print("-" * 40)

# Close the connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 478, in __call
    res = await _Retry(4).with_exponential_backoff(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 31, in with_exponential_backoff
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/retry.py", line 28, in with_exponential_backoff
    return await f(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/grpc/aio/_call.py", line 327, in __await__
    raise _create_rpc_error(
grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2025-04-03T09:04:10.09204188+00:00", grpc_status:2, grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"}"
>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 35, in <module>
    response = wine_review_collection.query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/queries/hybrid/query.py", line 107, in hybrid
    res = await self._query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/grpc/query.py", line 490, in __call
    raise WeaviateQueryError(str(e), "GRPC search")  # pyright: ignore
weaviate.exceptions.WeaviateQueryError: Query call with protocol GRPC search failed with message <AioRpcError of RPC that terminated with:
	status = StatusCode.UNKNOWN
	details = "remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"
	debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2025-04-03T09:04:10.09204188+00:00", grpc_status:2, grpc_message:"remote client vectorize: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY"}"
>.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 7.82s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.exceptions import WeaviateStartUpError

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Ensure the environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI module
)

# Define the schema for the "DemoProducts" collection
schema = {
    "class": "DemoProducts",
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
    ],
}

# Add the schema to Weaviate if it doesn't already exist
try:
    if not client.schema.contains(schema):
        client.schema.create_class(schema)
        print("Schema 'DemoProducts' created successfully.")
    else:
        print("Schema 'DemoProducts' already exists.")
except WeaviateStartUpError as e:
    print(f"Error creating schema: {e}")
    exit(1)

# Prepare 50 objects for batch import
objects = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}",
    }
    for i in range(1, 51)
]

# Batch import the objects
with client.batch as batch:
    batch.batch_size = 10  # Set batch size
    for obj in objects:
        batch.add_data_object(obj, "DemoProducts")
    print("Batch import completed.")

# Count the number of objects in the "DemoProducts" collection
result = client.query.aggregate("DemoProducts").with_meta_count().do()
count = result["data"]["Aggregate"]["DemoProducts"][0]["meta"]["count"]
print(f"Number of objects in 'DemoProducts': {count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:14: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.98s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI module
)

# Define the schema for the "DemoProducts" collection
class_name = "DemoProducts"
schema = {
    "class": class_name,
    "properties": [
        {
            "name": "name",
            "dataType": ["text"],
        },
        {
            "name": "description",
            "dataType": ["text"],
        },
    ],
}

# Create the schema if it doesn't already exist
if not client.schema.contains(schema):
    client.schema.create_class(schema)

# Prepare 50 objects to batch import
data_rows = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}",
    }
    for i in range(1, 51)
]

# Batch import the objects
with client.batch as batch:
    for data_row in data_rows:
        batch.add_data_object(data_object=data_row, class_name=class_name)
        if batch.errors:
            print("Batch import stopped due to errors.")
            break

# Print the number of objects in the collection
result = client.query.aggregate(class_name).with_meta_count().do()
object_count = result["data"]["Aggregate"][class_name][0]["meta"]["count"]
print(f"Number of objects in the '{class_name}' collection: {object_count}")

# Close the client connection
client.close()
```

**Errors**:
```
/code/code.py:10: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 10.63s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# ================================
# Connect to Weaviate Cloud
# ================================
# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY)
)

# ================================
# Create the "DemoProducts" collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the specified properties
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# ================================
# Batch import 50 objects
# ================================
data_rows = [
    {"name": f"Product {i+1}", "description": f"Description {i+1}"}
    for i in range(50)
]

collection = client.collections.get(collection_name)

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

# ================================
# Print the number of objects in the collection
# ================================
print(f"Number of objects in the '{collection_name}' collection: {len(collection)}")

# Close the connection
client.close()
```

**Output**:
```
Number of objects in the 'DemoProducts' collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

### openai/gpt-4o-mini-2024-07-18

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 6.70s)

**Generated Code**:
```python
import os
import weaviate

# Get the Weaviate Cloud URL and API key from environment variables
weaviate_url = os.getenv('WCD_TEST_URL')
weaviate_key = os.getenv('WCD_TEST_KEY')

# Create a Weaviate client instance
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthClientPassword(weaviate_key, "")
)

# Check if the server is ready to accept requests
try:
    client.is_ready()
    print("Weaviate server is ready to accept requests.")
except Exception as e:
    print(f"Weaviate server is not ready: {e}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthClientPassword from weaviate is deprecated. Import AuthClientPassword from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.31s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth

# Retrieve the Weaviate Cloud URL and API key from environment variables
cluster_url = os.getenv('WCD_TEST_URL')
api_key = os.getenv('WCD_TEST_KEY')

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.83s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
weaviate_url = os.getenv('WCD_TEST_URL')
weaviate_key = os.getenv('WCD_TEST_KEY')

# Initialize Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthClientPassword(username='', password=weaviate_key)
)

# Define the class schema for DemoProducts
class_name = "DemoProducts"
class_schema = {
    "class": class_name,
    "properties": [
        {
            "name": "name",
            "dataType": ["text"]
        },
        {
            "name": "description",
            "dataType": ["text"]
        },
        {
            "name": "price",
            "dataType": ["number"]
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"]
        }
    ]
}

# Check if the class already exists
if client.schema.contains(class_name):
    print(f"Class '{class_name}' already exists. Deleting it...")
    client.schema.delete_class(class_name)

# Create the new class
print(f"Creating class '{class_name}'...")
client.schema.create_class(class_schema)
print(f"Class '{class_name}' created successfully.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthClientPassword from weaviate is deprecated. Import AuthClientPassword from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 7.40s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth
from weaviate.schema import Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.Client(
    url=os.getenv("WCD_TEST_URL"),
    auth_client_secret=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Define the collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.schema.contains(collection_name):
    client.schema.delete_class(collection_name)

# Create the collection with the specified properties
client.schema.create_class(
    class_name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Created collection: {collection_name}")

# Close connection (optional, as the client will be garbage collected)
# client.close()  # Uncomment if you want to explicitly close the connection
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.schema import Property, DataType
ModuleNotFoundError: No module named 'weaviate.schema'

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 15.45s)

**Generated Code**:
```python
# ================================
# Connect to Weaviate
# ================================
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# ================================
# Create a collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the new collection with specified properties
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Collection '{collection_name}' created successfully.")

# Close connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.10s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
weaviate_url = os.getenv('WCD_TEST_URL')
weaviate_key = os.getenv('WCD_TEST_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthClientPassword(
        username=weaviate_key,
        password=""
    ),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the query
query = "dessert wine"

# Perform the query on the 'WineReview' collection
results = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    near_text={"concepts": [query]},
    limit=2
).do()

# Print the results
for result in results['data']['Get']['WineReview']:
    print(f"Title: {result['title']}, Country: {result['country']}, Price: {result['price']}, Points: {result['points']}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthClientPassword from weaviate is deprecated. Import AuthClientPassword from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:10: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.93s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-API-Key": os.getenv("OPENAI_API_KEY")
    },
)

# Define the collection name
collection_name = "WineReview"

# Query the collection for wines that match "dessert wine"
response = client.query.get(collection_name).with_near_text(
    {"concepts": ["dessert wine"]}
).with_limit(2).do()

# Print the title, country, price, and points of each matching wine
for obj in response['data']['Get'][collection_name]:
    title = obj.get('title', 'N/A')
    country = obj.get('country', 'N/A')
    price = obj.get('price', 'N/A')
    points = obj.get('points', 'N/A')
    
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 18, in <module>
    response = client.query.get(collection_name).with_near_text(
AttributeError: 'WeaviateClient' object has no attribute 'query'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 6.01s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import MetadataQuery

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Define the collection name
collection_name = "WineReview"

# Perform a semantic search for "dessert wine"
response = client.collections.get(collection_name).query.near_text(
    query="dessert wine",
    limit=2,
    return_metadata=MetadataQuery(distance=True)  # Optional: include distance in the response
)

# Print the title, country, price, and points of each matching wine
for wine in response.objects:
    title = wine.properties.get("title")
    country = wine.properties.get("country")
    price = wine.properties.get("price")
    points = wine.properties.get("points")
    
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")

# Close connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY"))
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.24s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
wcd_test_url = os.getenv('WCD_TEST_URL')
wcd_test_key = os.getenv('WCD_TEST_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize Weaviate client
client = weaviate.Client(
    url=wcd_test_url,
    auth_client_secret=weaviate.AuthClientPassword(
        username=wcd_test_key,
        password=""
    ),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the hybrid search query
query = "pair with steak"

# Perform the query
results = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    limit=5
).with_hybrid_search(
    query=query,
    alpha=0.5
).with_where(
    {
        "operator": "And",
        "operands": [
            {
                "path": ["price"],
                "operator": "LessThan",
                "valueNumber": 50
            },
            {
                "path": ["points"],
                "operator": "GreaterThan",
                "valueNumber": 90
            },
            {
                "path": ["review_body"],
                "operator": "ContainsAny",
                "valueString": ["spice", "fruit", "berry", "cherry", "honey"]
            }
        ]
    }
).do()

# Print the results
for result in results['data']['Get']['WineReview']:
    print(f"Title: {result['title']}, Country: {result['country']}, Price: {result['price']}, Points: {result['points']}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthClientPassword from weaviate is deprecated. Import AuthClientPassword from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:10: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.23s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-API-Key": os.getenv("OPENAI_API_KEY")
    },
)

# Define the collection
collection = client.collections.get("WineReview")

# Perform the hybrid search
response = collection.query.hybrid(
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

# Print the results
for obj in response.objects:
    title = obj.properties.get("title")
    country = obj.properties.get("country")
    price = obj.properties.get("price")
    points = obj.properties.get("points")
    score = obj.metadata.score

    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}, Score: {score}")

# Close the client connection
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir, Country: US, Price: 40.0, Points: 92, Score: 0.5
Title: Bink 2014 Pinot Noir (Anderson Valley), Country: US, Price: 49.0, Points: 91, Score: 0.4627816081047058
Title: Doña Silvina 2011 Malbec (Mendoza), Country: Argentina, Price: 27.0, Points: 91, Score: 0.2214958518743515
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji), Country: Hungary, Price: 25.0, Points: 93, Score: 0.0657503604888916
Title: Château Rauzan-Ségla 2012  Margaux, Country: France, Price: 0.0, Points: 94, Score: 0.014926085248589516

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.60s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, MetadataQuery

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Define the query parameters
query_text = "pair with steak"
alpha_value = 0.5
max_results = 5

# Define the substrings to check in the review_body
substrings = ["spice", "fruit", "berry", "cherry", "honey"]

# Create the filter for the query
filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(substrings)
)

# Perform the hybrid search
response = client.collections.get("WineReview").query.hybrid(
    query=query_text,
    alpha=alpha_value,
    filters=filters,
    limit=max_results,
    return_metadata=MetadataQuery(score=True)
)

# Print the results
for wine in response.objects:
    print(f"Title: {wine.properties.get('title')}, "
          f"Country: {wine.properties.get('country')}, "
          f"Price: {wine.properties.get('price')}, "
          f"Points: {wine.properties.get('points')}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY"))
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.14s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
weaviate_url = os.getenv('WCD_TEST_URL')
weaviate_key = os.getenv('WCD_TEST_KEY')

# Initialize Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthClientPassword(
        username=weaviate_key, password=""
    )
)

# Define the class for the collection if it doesn't exist
class_name = "DemoProducts"
if not client.schema.contains(class_name):
    client.schema.create_class({
        "class": class_name,
        "properties": [
            {
                "name": "name",
                "dataType": ["text"]
            },
            {
                "name": "description",
                "dataType": ["text"]
            }
        ]
    })

# Prepare objects to be added
objects_to_add = [
    {
        "class": class_name,
        "properties": {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
    }
    for i in range(50)
]

# Batch import objects
client.batch.create(objects_to_add)

# Count the number of objects in the collection
count = client.data_object.count(class_name)
print(f"Number of objects in '{class_name}': {count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthClientPassword from weaviate is deprecated. Import AuthClientPassword from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:9: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 18.83s)

**Generated Code**:
```python
import os
import weaviate

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY")),
)

# Define the collection name
collection_name = "DemoProducts"

# Create a list of 50 arbitrary objects
data_rows = [
    {
        "name": f"Product {i + 1}",
        "description": f"Description {i + 1}"
    } for i in range(50)
]

# Get the collection
collection = client.collections.get(collection_name)

# Batch import the objects
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed objects
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
object_count = len(collection)
print(f"Number of objects in the collection '{collection_name}': {object_count}")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 7, in <module>
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY")),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.18s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# ================================
# Connect to Weaviate
# ================================
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# ================================
# Create a collection
# ================================
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the specified properties
client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# ================================
# Batch import
# ================================
data_rows = [
    {"name": f"Product {i+1}", "description": f"Description {i+1}"} for i in range(50)
]

collection = client.collections.get(collection_name)

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
object_count = collection.query.count()
print(f"Number of objects in '{collection_name}': {object_count}")

# Close connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 56, in <module>
    object_count = collection.query.count()
AttributeError: '_QueryCollection' object has no attribute 'count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

