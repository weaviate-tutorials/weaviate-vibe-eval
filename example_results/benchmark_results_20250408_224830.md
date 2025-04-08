# Weaviate Benchmark Results

Generated on: 2025-04-08 22:48:30

## Summary

- **anthropic/claude-3-7-sonnet-20250219**: 9/14 tasks successful
- **anthropic/claude-3-5-sonnet-20241022**: 7/14 tasks successful
- **anthropic/claude-3-5-haiku-20241022**: 10/14 tasks successful
- **cohere/command-a-03-2025**: 3/14 tasks successful
- **cohere/command-r-plus-08-2024**: 1/14 tasks successful
- **gemini/gemini-2.5-pro-exp-03-25**: 10/14 tasks successful
- **gemini/gemini-2.0-flash-lite**: 5/14 tasks successful
- **openai/gpt-4o-2024-11-20**: 2/14 tasks successful
- **openai/gpt-4o-mini-2024-07-18**: 2/14 tasks successful
- **openai/gpt-4.5-preview-2025-02-27**: 11/14 tasks successful
- **openai/o3-mini-2025-01-31**: 2/14 tasks successful
## Detailed Results

### anthropic/claude-3-7-sonnet-20250219

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 5.89s)

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
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

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

**Status**: ✅ SUCCESS (runtime: 4.06s)

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

**Status**: ❌ FAILURE (runtime: 8.17s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType, Configure

# Get environment variables
url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate
client = weaviate.connect_to_wcs(
    cluster_url=url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key),
)

# Check if collection exists and delete it if it does
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")
    print("Existing DemoProducts collection deleted")

# Create the collection with properties
demo_products = client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ],
    vectorizer_config=Configure.Vectorizer.none()
)

print("DemoProducts collection created successfully")

# Close the client connection
client.close()
```

**Output**:
```
Existing DemoProducts collection deleted

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 27, in <module>
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

**Status**: ✅ SUCCESS (runtime: 5.07s)

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

**Status**: ❌ FAILURE (runtime: 8.53s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Check if collection exists and delete it if it does
if client.collections.exists("DemoProducts"):
    print("Collection 'DemoProducts' already exists. Deleting it...")
    client.collections.delete("DemoProducts")
    print("Collection 'DemoProducts' deleted successfully.")

# Create the DemoProducts collection with the specified properties
client.collections.create(
    "DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN)
    ]
)

print("Collection 'DemoProducts' created successfully with all required properties.")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted successfully.

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 25, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN)
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 10.82s)

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

# Clean up the client connection
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

**Status**: ✅ SUCCESS (runtime: 9.95s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth

# Connect to Weaviate Cloud using environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key),
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

# Prepare 50 arbitrary objects
data_rows = [
    {
        "name": f"Product {i+1}",
        "description": f"Description for product {i+1}. This is a sample product."
    } for i in range(50)
]

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
print(f"Number of objects in the collection: {len(collection)}")

# Close the client
client.close()
```

**Output**:
```
Number of objects in the collection: 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 10.48s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Check if collection exists and create it if it doesn't
if not client.collections.exists("DemoProducts"):
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )

# Get the collection
collection = client.collections.get("DemoProducts")

# Batch import 50 arbitrary objects
with collection.batch.dynamic() as batch:
    for i in range(1, 51):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
count = collection.aggregate.over_all().with_meta_count().do()
print(f"Number of objects in the DemoProducts collection: {count}")

# Close the client when done
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 36, in <module>
    count = collection.aggregate.over_all().with_meta_count().do()
AttributeError: 'AggregateReturn' object has no attribute 'with_meta_count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.81s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import QueryBuilder
from weaviate.connect import ConnectionParams

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Connect to Weaviate
connection_params = ConnectionParams.from_url(
    url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
)

client = weaviate.WeaviateClient(
    connection_params=connection_params,
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Query the WineReview collection
response = client.collections.get("WineReview").query.near_text(
    query="dessert wine",
    limit=2
).with_additional(["distance"]).with_fields([
    "title", 
    "country", 
    "price", 
    "points"
]).do()

# Print the results
print("Wines matching 'dessert wine':")
for wine in response.objects:
    properties = wine.properties
    print(f"Title: {properties['title']}")
    print(f"Country: {properties['country']}")
    print(f"Price: ${properties['price']}")
    print(f"Points: {properties['points']}")
    print(f"Distance: {wine.metadata.distance}")
    print("-" * 50)
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes.query import QueryBuilder
ImportError: cannot import name 'QueryBuilder' from 'weaviate.classes.query' (/usr/local/lib/python3.9/site-packages/weaviate/classes/query.py)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.99s)

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

**Status**: ✅ SUCCESS (runtime: 11.19s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Query for wines matching "dessert wine" with a limit of 2
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
print("Wines matching 'dessert wine':")
print("-" * 50)
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: ${wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print("-" * 50)

# Close the client connection
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
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88
--------------------------------------------------

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.99s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import QueryReference
from weaviate.classes.filters import Filter, FilterOperator

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Initialize Weaviate client
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
    headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Create filter for price < 50 and points > 90
price_points_filter = Filter.by_property("price").less_than(50).and_filter(
    Filter.by_property("points").greater_than(90)
)

# Create filter for review_body containing one of the specified substrings
review_body_filter = (
    Filter.by_property("review_body").contains_any("spice").or_filter(
        Filter.by_property("review_body").contains_any("fruit").or_filter(
            Filter.by_property("review_body").contains_any("berry").or_filter(
                Filter.by_property("review_body").contains_any("cherry").or_filter(
                    Filter.by_property("review_body").contains_any("honey")
                )
            )
        )
    )
)

# Combine the filters
combined_filter = price_points_filter.and_filter(review_body_filter)

# Query the collection with hybrid search
response = (
    client.collections.get("WineReview")
    .query
    .hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points", "review_body"]
    )
    .objects
)

# Print the results
if response:
    print(f"Found {len(response)} matching wines:")
    for i, wine in enumerate(response, 1):
        props = wine.properties
        print(f"\n{i}. {props['title']}")
        print(f"   Country: {props['country']}")
        print(f"   Price: ${props['price']}")
        print(f"   Points: {props['points']}")
else:
    print("No matching wines found.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.classes.filters import Filter, FilterOperator
ModuleNotFoundError: No module named 'weaviate.classes.filters'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.81s)

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
Score: 0.4630
--------------------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.2213
--------------------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.0656
--------------------------------------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
Score: 0.0147
--------------------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 13.12s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os
import re

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Define the search terms for the review body
search_terms = ["spice", "fruit", "berry", "cherry", "honey"]

# Create a regex pattern for any of the search terms
pattern = re.compile('|'.join(search_terms), re.IGNORECASE)

# Create the filter for price < 50 and points > 90
price_points_filter = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90)
)

# Perform hybrid search with alpha=0.5
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    filters=price_points_filter,
    limit=5,
    return_properties=["title", "country", "price", "points", "review_body"]
)

# Print the results, filtering for those containing at least one of the search terms
print("Wines that pair well with steak:")
print("--------------------------------")

for wine in response.objects:
    # Check if the review_body contains any of the search terms
    if "review_body" in wine.properties and pattern.search(wine.properties["review_body"]):
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: ${wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print("--------------------------------")

# Close the client connection
client.close()
```

**Output**:
```
Wines that pair well with steak:
--------------------------------
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
--------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
--------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
--------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
--------------------------------

```

---

### anthropic/claude-3-5-sonnet-20241022

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 7.08s)

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

**Status**: ✅ SUCCESS (runtime: 4.46s)

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

**Status**: ❌ FAILURE (runtime: 10.01s)

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

# Verify the collection exists and has the correct properties
collection = client.collections.get("DemoProducts")
print("\nCollection properties:")
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

**Status**: ✅ SUCCESS (runtime: 10.04s)

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

**Status**: ❌ FAILURE (runtime: 11.70s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Check if collection exists and delete it
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the DemoProducts collection with properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOLEAN)
        ]
    )
    
    print("DemoProducts collection created successfully!")

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 24, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN)
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.55s)

**Generated Code**:
```python
import weaviate
import os
from typing import List
import time

# Get environment variables
WEAVIATE_URL = os.getenv('WCD_TEST_URL')
WEAVIATE_API_KEY = os.getenv('WCD_TEST_KEY')

# Create a client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Define the collection
collection_name = "DemoProducts"

# Create the collection if it doesn't exist
if not client.collections.exists(collection_name):
    collection = client.collections.create(
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
else:
    collection = client.collections.get(collection_name)

# Prepare batch objects
def create_objects(num_objects: int) -> List[dict]:
    return [
        {
            "name": f"Product {i}",
            "description": f"Description for product number {i}"
        }
        for i in range(num_objects)
    ]

# Batch import objects
objects = create_objects(50)

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

# Get the count of objects in the collection
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

**Status**: ✅ SUCCESS (runtime: 10.92s)

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
        "description": f"Description for product {i}"
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

**Status**: ❌ FAILURE (runtime: 13.25s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

try:
    # Create the DemoProducts collection if it doesn't exist
    if not client.collections.exists("DemoProducts"):
        client.collections.create(
            "DemoProducts",
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ]
        )

    # Get the collection
    collection = client.collections.get("DemoProducts")

    # Batch import 50 objects
    with collection.batch.dynamic() as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description for product {i}"
                }
            )

    # Check if there were any failed objects
    if batch.failed_objects:
        print(f"Failed to import {len(batch.failed_objects)} objects")

    # Get the count of objects in the collection
    count = collection.aggregate.over_all().with_count().do()
    print(f"Number of objects in collection: {count}")

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 37, in <module>
    if batch.failed_objects:
AttributeError: '_BatchCollection' object has no attribute 'failed_objects'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 13.35s)

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
    auth_client_secret=weaviate.auth.AuthApiKey(weaviate_api_key),
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
    print("No results found or unexpected response format")
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

**Status**: ✅ SUCCESS (runtime: 9.65s)

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
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: ${obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
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

**Status**: ✅ SUCCESS (runtime: 14.42s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")
    
    # Perform semantic search for dessert wines
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print results
    for wine in response.objects:
        print("\nWine Details:")
        print(f"Title: {wine.properties['title']}")
        print(f"Country: {wine.properties['country']}")
        print(f"Price: ${wine.properties['price']}")
        print(f"Points: {wine.properties['points']}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```

Wine Details:
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88

Wine Details:
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.69s)

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
    print("Error: Unexpected response format")
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

**Status**: ✅ SUCCESS (runtime: 11.41s)

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

# Close the client connection
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
Relevance Score: 0.4631
--------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Relevance Score: 0.2215
--------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Relevance Score: 0.0658
--------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
Relevance Score: 0.0150
--------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 18.65s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Create filter for price, points and review_body
    review_terms = ["spice", "fruit", "berry", "cherry", "honey"]
    review_filters = [Filter.by_property("review_body").like(f"*{term}*") for term in review_terms]
    combined_review_filter = review_filters[0]
    for filter in review_filters[1:]:
        combined_review_filter = combined_review_filter | filter

    filters = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        combined_review_filter
    )

    # Perform hybrid search
    response = collection.query.hybrid(
        query="pair with steak",
        filters=filters,
        alpha=0.5,  # Equal weight between keyword and vector search
        limit=5,
        return_properties=[
            "title",
            "country",
            "price",
            "points"
        ]
    )

    # Print results
    print("\nMatching Wines:")
    print("--------------")
    for wine in response.objects:
        print(f"Title: {wine.properties['title']}")
        print(f"Country: {wine.properties['country']}")
        print(f"Price: ${wine.properties['price']}")
        print(f"Points: {wine.properties['points']}")
        print("--------------")

finally:
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
--------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
--------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
--------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
--------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
--------------

```

---

### anthropic/claude-3-5-haiku-20241022

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 4.71s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.connect import ConnectionParams

# Create connection parameters from environment variables
connection_params = ConnectionParams.from_params(
    url=os.getenv('WCD_TEST_URL'),
    api_key=os.getenv('WCD_TEST_KEY')
)

# Create Weaviate client
client = weaviate.connect_to_custom(
    connection_params=connection_params
)

# Check server readiness
try:
    client.is_ready()
    print("Weaviate server is ready.")
except Exception as e:
    print(f"Error connecting to Weaviate: {e}")
finally:
    # Close the connection
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

**Status**: ✅ SUCCESS (runtime: 4.22s)

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

**Status**: ❌ FAILURE (runtime: 10.79s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType

def create_products_collection():
    # Read Weaviate Cloud credentials from environment variables
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

**Status**: ✅ SUCCESS (runtime: 7.58s)

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

**Status**: ✅ SUCCESS (runtime: 9.95s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Delete the collection if it already exists
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")
        print("Existing 'DemoProducts' collection deleted.")

    # Create the new collection with specified properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOLEAN)
        ]
    )
    print("'DemoProducts' collection created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the client connection
    client.close()
```

**Output**:
```
Existing 'DemoProducts' collection deleted.
An error occurred: BOOLEAN

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 9.55s)

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

    # Batch import 50 objects
    with products.batch as batch:
        for i in range(50):
            batch.add_object({
                "name": f"Product {i}",
                "description": f"Description {i}"
            })

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

**Status**: ❌ FAILURE (runtime: 10.18s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=AuthApiKey(os.getenv("WCD_TEST_KEY")),
)

# Create the collection if it doesn't exist
try:
    # Remove existing collection if needed
    client.collections.delete("DemoProducts")
except Exception:
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

**Status**: ✅ SUCCESS (runtime: 11.77s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Create the collection with specified properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT)
        ]
    )

    # Get the collection
    products_collection = client.collections.get("DemoProducts")

    # Batch import 50 objects
    with products_collection.batch.dynamic() as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )

    # Print the number of objects in the collection
    object_count = products_collection.aggregate.count()
    print(f"Number of objects in DemoProducts collection: {object_count}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the client connection
    client.close()
```

**Output**:
```
An error occurred: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.73s)

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

**Status**: ✅ SUCCESS (runtime: 8.56s)

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

# Perform near_text query for dessert wines
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

**Status**: ✅ SUCCESS (runtime: 12.99s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery

# Connect to Weaviate Cloud with OpenAI API key for vectorization
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
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
        print("Wine Details:")
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: {wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print(f"Semantic Distance: {wine.metadata.distance}")
        print("---")

finally:
    # Always close the client connection
    client.close()
```

**Output**:
```
Wine Details:
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
Semantic Distance: 0.4648876190185547
---
Wine Details:
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Semantic Distance: 0.48120927810668945
---

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.35s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import HybridSearchOptions

def main():
    # Connect to Weaviate Cloud
    client = weaviate.connect_to_wcs(
        cluster_url=os.getenv('WCD_TEST_URL'),
        auth_credentials=os.getenv('WCD_TEST_KEY'),
        headers={
            "X-OpenAI-Api-Key": os.getenv('OPENAI_API_KEY')
        }
    )

    try:
        # Query the WineReview collection
        wine_collection = client.collections.get("WineReview")
        
        # Hybrid search with specific conditions
        results = wine_collection.query.hybrid(
            query="pair with steak",
            hybrid_search_options=HybridSearchOptions(alpha=0.5),
            filters=wine_collection.query.filter.where(
                # Price less than 50
                weaviate.query.Filter.less_than("price", 50)
            ).and_filter(
                # Points greater than 90
                weaviate.query.Filter.greater_than("points", 90)
            ),
            limit=5
        )

        # Filter results based on review body keywords
        matching_wines = [
            result for result in results.objects 
            if any(keyword in result.properties['review_body'].lower() 
                   for keyword in ['spice', 'fruit', 'berry', 'cherry', 'honey'])
        ]

        # Print matching wines
        for wine in matching_wines:
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

if __name__ == "__main__":
    main()
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

**Status**: ✅ SUCCESS (runtime: 8.75s)

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

**Status**: ✅ SUCCESS (runtime: 14.72s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

def main():
    # Connect to Weaviate Cloud using environment variables
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )

    try:
        # Get the WineReview collection
        wine_collection = client.collections.get("WineReview")

        # Define complex filter conditions
        review_filter = (
            Filter.by_property("price").less_than(50) &
            Filter.by_property("points").greater_than(90) &
            (
                Filter.by_property("review_body").contains_any(
                    ["spice", "fruit", "berry", "cherry", "honey"]
                )
            )
        )

        # Perform hybrid search
        response = wine_collection.query.hybrid(
            query="pair with steak",
            filters=review_filter,
            alpha=0.5,  # Balance between semantic and keyword search
            fusion_type=HybridFusion.RELATIVE_SCORE,
            limit=5
        )

        # Print results
        print(f"Found {len(response.objects)} matching wines:")
        for wine in response.objects:
            print(f"Title: {wine.properties.get('title', 'N/A')}")
            print(f"Country: {wine.properties.get('country', 'N/A')}")
            print(f"Price: ${wine.properties.get('price', 'N/A')}")
            print(f"Points: {wine.properties.get('points', 'N/A')}")
            print("---")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Always close the client
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Found 5 matching wines:
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

### cohere/command-a-03-2025

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.96s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.exceptions import WeaviateConnectionError

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Initialize the Weaviate client with API key authentication
client = Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
)

try:
    # Check if the server is ready
    if client.is_ready():
        print("Weaviate server is ready to accept requests.")
    else:
        print("Weaviate server is not ready.")
except WeaviateConnectionError as e:
    print(f"Failed to connect to Weaviate: {e}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 12, in <module>
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
NameError: name 'weaviate' is not defined

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 5.53s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not cluster_url or not api_key:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check if the server is ready
assert client.is_ready(), "Weaviate server is not ready."

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.51s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.util import get_valid_uuid

# Retrieve environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")

# Initialize the Weaviate client
client = Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
)

# Define the collection name
COLLECTION_NAME = "DemoProducts"

# Check if the collection already exists and delete it if necessary
if client.collections.exists(COLLECTION_NAME):
    client.collections.delete(COLLECTION_NAME)
    print(f"Collection '{COLLECTION_NAME}' deleted.")

# Define the properties for the collection
properties = [
    {
        "name": "name",
        "dataType": ["text"],
        "description": "Name of the product",
    },
    {
        "name": "description",
        "dataType": ["text"],
        "description": "Description of the product",
    },
    {
        "name": "price",
        "dataType": ["number"],
        "description": "Price of the product",
    },
    {
        "name": "in_stock",
        "dataType": ["boolean"],
        "description": "Whether the product is in stock",
    },
]

# Create the collection
client.collections.create(
    name=COLLECTION_NAME,
    properties=properties,
    vectorizer_config="text2vec-openai",  # Optional: specify a vectorizer
)

print(f"Collection '{COLLECTION_NAME}' created successfully.")
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

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.47s)

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

**Status**: ❌ FAILURE (runtime: 7.02s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.init import Auth

# Environment variables for Weaviate Cloud
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY)
)

# Define the collection name
COLLECTION_NAME = "DemoProducts"

# Check if the collection exists and delete it if it does
if client.collections.exists(COLLECTION_NAME):
    client.collections.delete(COLLECTION_NAME)
    print(f"Collection '{COLLECTION_NAME}' deleted.")

# Create the collection with the specified properties
client.collections.create(
    name=COLLECTION_NAME,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)

print(f"Collection '{COLLECTION_NAME}' created successfully.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 31, in <module>
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

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 10.01s)

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
try:
    client.collections.delete(collection_name)  # Delete if it already exists
except:
    pass

collection = client.collections.create(
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
with collection.batch.dynamic() as batch:
    batch.add_objects(batch_objects)

# Print the number of objects in the collection
object_count = collection.count()
print(f"Number of objects in the '{collection_name}' collection: {object_count}")
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

**Status**: ❌ FAILURE (runtime: 8.45s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Auth

# Retrieve Weaviate Cloud credentials from environment variables
CLUSTER_URL = os.getenv("WCD_TEST_URL")
API_KEY = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=CLUSTER_URL,
    auth_credentials=Auth.api_key(API_KEY),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")  # Optional: If using OpenAI for embeddings
    }
)

# Define the collection schema
collection_name = "DemoProducts"
client.collections.create(
    name=collection_name,
    properties=[
        {
            "name": "name",
            "dataType": ["text"],
            "description": "Product name"
        },
        {
            "name": "description",
            "dataType": ["text"],
            "description": "Product description"
        }
    ]
)

# Generate 50 arbitrary objects
data_rows = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    } for i in range(50)
]

# Batch import objects into the collection
collection = client.collections.get(collection_name)
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        if batch.number_of_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed imports
failed_objects = collection.batch.failed_objects
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

**Status**: ❌ FAILURE (runtime: 6.01s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.data import DataObject

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Create the "DemoProducts" collection with properties
client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT)
    ]
)

# Batch import 50 objects into the collection
collection = client.collections.get("DemoProducts")
with collection.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
object_count = collection.aggregate.total()
print(f"Number of objects in the collection: {object_count}")

# Close the client
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/sync.py", line 107, in create
    self.__loop.run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/async_.py", line 134, in create
    name = await super()._create(config._to_dict())
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/base.py", line 27, in _create
    response = await self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 550, in post
    return await self.__send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 505, in __send
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 496, in __send
    raise UnexpectedStatusCodeError(error_msg, response=res)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.32s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud
client = Client(
    url=os.getenv("WCD_TEST_URL"),
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WCD_TEST_KEY")),
    additional_headers={"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")}
)

# Define the query
query = "dessert wine"

# Perform the hybrid search (combines BM25 and vector search)
response = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    hybrid={
        "query": query,
        "alpha": 0.5  # Adjust the balance between vector and keyword search
    },
    limit=2
)

# Extract and print the results
results = response['data']['Get']['WineReview']
for wine in results:
    print(f"Title: {wine['title']}")
    print(f"Country: {wine['country']}")
    print(f"Price: {wine['price']}")
    print(f"Points: {wine['points']}")
    print("-" * 40)
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
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

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.52s)

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
    print(f"Title: {properties['title']}")
    print(f"Country: {properties['country']}")
    print(f"Price: {properties['price']}")
    print(f"Points: {properties['points']}")
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

**Status**: ✅ SUCCESS (runtime: 8.07s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import MetadataQuery
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Reference the WineReview collection
wine_collection = client.collections.get("WineReview")

# Perform a semantic search for "dessert wine" with a limit of 2 results
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for obj in response.objects:
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: {obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
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

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.43s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.util import get_valid_uuid

# Connect to Weaviate Cloud
client = Client(
    url=os.getenv("WCD_TEST_URL"),
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WCD_TEST_KEY")),
    additional_headers={"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")}
)

# Define the query
query = """
{
  Get {
    WineReview(
      hybrid: {
        query: "pair with steak"
        alpha: 0.5
      }
      where: {
        operator: And
        path: ["price", "points", "review_body"]
        valueInt: [[..50], [91..]]
        valueString: ["spice", "fruit", "berry", "cherry", "honey"]
        operator: Or
      }
      limit: 5
    ) {
      title
      country
      price
      points
    }
  }
}
"""

# Execute the query
response = client.query.raw(query)

# Extract and print the results
results = response["data"]["Get"]["WineReview"]
for wine in results:
    print(f"Title: {wine['title']}")
    print(f"Country: {wine['country']}")
    print(f"Price: ${wine['price']}")
    print(f"Points: {wine['points']}")
    print("-" * 40)
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.60s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-API-Key": os.getenv("OPENAI_API_KEY")
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Define the hybrid search query with filters
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
    wine_data = obj.properties
    print(f"Title: {wine_data['title']}")
    print(f"Country: {wine_data['country']}")
    print(f"Price: {wine_data['price']}")
    print(f"Points: {wine_data['points']}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 23, in <module>
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

**Status**: ❌ FAILURE (runtime: 7.92s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, HybridFusion
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Define the search query with filters and hybrid search
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    fusion_type=HybridFusion.RELATIVE_SCORE,
    limit=5,
    filters=Filter.by_properties(
        price=Filter.range(lt=50),
        points=Filter.range(gt=90),
        review_body=Filter.any(
            Filter.like("review_body", "*spice*"),
            Filter.like("review_body", "*fruit*"),
            Filter.like("review_body", "*berry*"),
            Filter.like("review_body", "*cherry*"),
            Filter.like("review_body", "*honey*")
        )
    )
)

# Print the results
for obj in response.objects:
    print({
        "title": obj.properties["title"],
        "country": obj.properties["country"],
        "price": obj.properties["price"],
        "points": obj.properties["points"]
    })

# Close the client
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 24, in <module>
    filters=Filter.by_properties(
AttributeError: type object 'Filter' has no attribute 'by_properties'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

### cohere/command-r-plus-08-2024

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 6.47s)

**Generated Code**:
```python
import os
from weaviate import Client

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Initialize the Weaviate client
client = Client(
    url=weaviate_url,
    additional_headers={"X-OpenAI-Api-Key": api_key},
)

# Check if the server is ready
status = client.is_ready()

if status:
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready. Please check the instance status.")
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

**Status**: ❌ FAILURE (runtime: 5.13s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.auth import AuthApiKey

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

client = Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(api_key=WCD_TEST_KEY)
)

# Check if the server is ready
assert client.is_ready(), "Weaviate server is not ready."
```

**Errors**:
```
/code/code.py:12: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 12, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.61s)

**Generated Code**:
```python
import os
from weaviate import Client

# Connect to Weaviate Cloud using environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")
client = Client(wcd_url, auth_client_secret=wcd_key)

# Check if the collection already exists and delete if necessary
if client.schema.exists("DemoProducts"):
    client.schema.delete_class("DemoProducts")

# Create the "DemoProducts" collection with the specified properties
client.schema.create_class(
    class_name="DemoProducts",
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

**Status**: ❌ FAILURE (runtime: 13.75s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)

# Collection name
collection_name = "DemoProducts"

# Check if the collection already exists and delete it
if client.data_object.exists(collection_name):
    client.schema.delete_class(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the collection with the specified properties
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
    module_config={
        "text2vec-contextionary": {
            "vectorizePropertyName": "name"
        }
    },
    id_property=generate_uuid5
)

print(f"Created collection: {collection.name}")

# Close the connection
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
  client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 6.94s)

**Generated Code**:
```python
import os
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Check if the collection already exists and delete it if necessary
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")

# Create the collection with the specified properties
client.collections.create(
    "DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 6, in <module>
    client = weaviate.connect_to_weaviate_cloud(
NameError: name 'weaviate' is not defined

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.61s)

**Generated Code**:
```python
import os
from weaviate import Client

# Connect to Weaviate Cloud using environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")
client = Client(wcd_url, auth_client_secret=wcd_key)

# Define the schema for the "DemoProducts" collection
schema = {
    "class": "DemoProducts",
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
}

# Create the collection if it doesn't exist
client.schema.create_class(schema)

# Function to add objects in batch to the collection
def batch_import_objects(objects, batch_size=10):
    for i in range(0, len(objects), batch_size):
        batch = objects[i:i+batch_size]
        client.batch.configure(batch_size=len(batch)).add_data_objects(batch).do()

# Generate 50 arbitrary objects
objects_to_import = [{"name": f"Product {i}", "description": f"Description {i}"} for i in range(50)]

# Batch import the objects into the collection
batch_import_objects(objects_to_import)

# Get the number of objects in the collection
collection_name = "DemoProducts"
collection = client.data_object.get(
    where={"path": [f"{collection_name}"]},
    with_vector=False
)
num_objects = len(collection['data']['Get'][collection_name])

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
  client = Client(wcd_url, auth_client_secret=wcd_key)
Traceback (most recent call last):
  File "/code/code.py", line 7, in <module>
    client = Client(wcd_url, auth_client_secret=wcd_key)
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 8.23s)

**Generated Code**:
```python
import os

import weaviate

# Connect to Weaviate Cloud using environment variables
client = weaviate.Client(
    url=os.environ["WCD_TEST_URL"],
    auth_client_secret=os.environ["WCD_TEST_KEY"],
)

# Get the collection or create it if it doesn't exist
collection = client.collections.get(
    "DemoProducts",
    ["name", "description"],
)

# Create a list of 50 objects with arbitrary data
data_rows = [
    {"name": f"Product {i}", "description": f"Description {i}"} for i in range(50)
]

# Batch import the objects into the collection
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )

# Check for any failed imports
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Failed to import {len(failed_objects)} objects.")
    print("First failed object:", failed_objects[0])

# Print the number of objects in the collection
print(f"Total objects in 'DemoProducts' collection: {len(collection)}")

# Close the client connection
client.close()
```

**Errors**:
```
/code/code.py:6: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 6, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.45s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.data import DataObject

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.AuthApiKey(api_key=os.environ["WCD_TEST_KEY"])
)

# Create the collection with the specified properties
client.collections.create(
    "DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT)
    ]
)

# Get the collection
collection = client.collections.get("DemoProducts")

# Batch import 50 objects into the collection
data_objects = []
for i in range(50):
    data_objects.append(DataObject(
        properties={
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
    ))

collection.data.insert_many(data_objects)

# Print the number of objects in the collection
collection_size = collection.data.count()
print(f"Number of objects in 'DemoProducts' collection: {collection_size}")

# Close the client connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/sync.py", line 107, in create
    self.__loop.run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/async_.py", line 134, in create
    name = await super()._create(config._to_dict())
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/base.py", line 27, in _create
    response = await self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 550, in post
    return await self.__send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 505, in __send
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 496, in __send
    raise UnexpectedStatusCodeError(error_msg, response=res)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 15.15s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
client = Client(WCD_TEST_URL, auth_client_secret=WCD_TEST_KEY)

# Set the class and vectorizer details
class_name = "WineReview"
vectorizer = "text2vec-openai"
api_key = os.environ["OPENAI_API_KEY"]

# Generate a unique ID for the query
query_id = generate_uuid5(class_name, vectorizer, api_key)

# Construct the query
query = {
    "class": class_name,
    "vectorizer": vectorizer,
    "properties": ["title", "country", "price", "points"],
    "query_id": query_id,
    "query_text": "dessert wine",
    "limit": 2,
    "with_distances": True,
}

# Execute the query
results = client.query.get(query)

# Print the matching wines
for result in results["data"]["Get"][class_name]:
    title = result["_additional"]["id"]
    country = result["country"]
    price = result["price"]
    points = result["points"]
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
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

**Status**: ✅ SUCCESS (runtime: 11.21s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

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

**Status**: ❌ FAILURE (runtime: 9.25s)

**Generated Code**:
```python
import os
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the 'WineReview' collection
wine_collection = client.collections.get("WineReview")

# Query for wines that match "dessert wine"
results = wine_collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the desired properties for each matching wine
for wine in results.objects:
    print("Title:", wine.properties.get("title"))
    print("Country:", wine.properties.get("country"))
    print("Price:", wine.properties.get("price"))
    print("Points:", wine.properties.get("points"))
    print()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 5, in <module>
    client = weaviate.connect_to_weaviate_cloud(
NameError: name 'weaviate' is not defined

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 14.32s)

**Generated Code**:
```python
import os
from weaviate import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud using environment variables
client = Client(
    url=os.environ["WCD_TEST_URL"],
    additional_headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"],
        "X-OpenAI-Organization": os.environ["OPENAI_ORG_KEY"],
    },
)

# Define the search parameters
params = {
    "concepts": ["pair with steak"],
    "certainty": "0.5",
    "hybrid": {"alpha": 0.5},
    "limit": 5,
    "additional": {
        "properties": [
            {"path": ["price"], "operator": "<", "valueNumber": 50},
            {"path": ["points"], "operator": ">", "valueNumber": 90},
        ],
        "nearText": {
            "concepts": [
                "spice",
                "fruit",
                "berry",
                "cherry",
                "honey",
            ],
            "certainty": 0.5,
        },
    },
}

# Generate a unique ID for the query
query_id = generate_uuid5(
    "query", f"{params['concepts']}-{params['certainty']}-{params['hybrid']}-{params['limit']}"
)

# Perform the hybrid search
results = client.query.hybrid.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    **params,
).do()

# Print the results
for result in results["data"]["Get"]["WineReview"]:
    print(
        f"Title: {result['title']}\n"
        f"Country: {result['country']}\n"
        f"Price: {result['price']}\n"
        f"Points: {result['points']}\n"
        "-------------------------\n"
    )
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    "X-OpenAI-Organization": os.environ["OPENAI_ORG_KEY"],
  File "/usr/local/lib/python3.9/os.py", line 679, in __getitem__
    raise KeyError(key) from None
KeyError: 'OPENAI_ORG_KEY'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 15.97s)

**Generated Code**:
```python
import os
from weaviate.client import Client
from weaviate.util import generate_uuid5

# Connect to Weaviate Cloud
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

client = Client(
    url=wcd_url,
    additional_headers={
        "X-OpenAI-API-Key": openai_api_key,
    },
    auth_client_secret=wcd_key,
)

# Define the collection name
collection_name = "WineReview"

# Generate a unique ID for the query
query_id = generate_uuid5(collection_name)

# Define the query and filters
query = "pair with steak"
filters = {
    "operator": "And",
    "operands": [
        {
            "operator": "And",
            "operands": [
                {"path": ["price"], "operator": "LessThan", "valueNumber": 50},
                {"path": ["points"], "operator": "GreaterThan", "valueNumber": 90},
            ],
        },
        {
            "operator": "Or",
            "operands": [
                {"path": ["review_body"], "operator": "Contains", "valueText": "spice"},
                {"path": ["review_body"], "operator": "Contains", "valueText": "fruit"},
                {"path": ["review_body"], "operator": "Contains", "valueText": "berry"},
                {"path": ["review_body"], "operator": "Contains", "valueText": "cherry"},
                {"path": ["review_body"], "operator": "Contains", "valueText": "honey"},
            ],
        },
    ],
}

# Perform the hybrid search
response = client.query.hybrid(
    query=query,
    class_name=collection_name,
    limit=5,
    alpha=0.5,
    filters=filters,
    additional={"id": query_id},
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
/code/code.py:10: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.07s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, HybridFusion

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    api_key=os.environ["WCD_TEST_KEY"],
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Perform hybrid search with filters
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    filters=Filter(
        operator="And",
        operands=[
            Filter.by_property("price").less_than(50),
            Filter.by_property("points").greater_than(90),
            Filter.by_property("review_body").contains_any_of(["spice", "fruit", "berry", "cherry", "honey"]),
        ]
    ),
    limit=5,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for obj in response.objects:
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: {obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
    print("-------------------------")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 6, in <module>
    client = weaviate.connect_to_weaviate_cloud(
TypeError: connect_to_weaviate_cloud() got an unexpected keyword argument 'api_key'

```

---

### gemini/gemini-2.5-pro-exp-03-25

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 27.21s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.exceptions import WeaviateConnectionError

# 1. Get Weaviate Cloud connection details from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# 2. Validate that environment variables are set
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

print(f"Attempting to connect to Weaviate Cloud at: {wcd_url}")

try:
    # 3. Connect to Weaviate Cloud using connect_to_wcd
    # The 'with' statement ensures the connection is automatically closed
    with weaviate.connect_to_wcd(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(api_key=wcd_api_key),
        # Optional: Add headers for specific modules like generative AI keys
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
        # }
    ) as client:

        print("Successfully initiated connection.")

        # 4. Check if the server is ready
        is_ready = client.is_ready()

        if is_ready:
            print("Weaviate server is ready to accept requests.")
        else:
            print("Connected, but Weaviate server reported it is not ready.")
            # Depending on the use case, you might want to exit or retry here
            # sys.exit(1) # Uncomment if not ready should be treated as an error

except WeaviateConnectionError as e:
    print(f"Error: Could not connect to Weaviate: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

print("Connection check complete. Connection automatically closed.")

# The script does nothing further, as requested.
```

**Output**:
```
Attempting to connect to Weaviate Cloud at: https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud
An unexpected error occurred: module weaviate has no attribute connect_to_wcd

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 24.26s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth

# 1. Get Weaviate Cloud connection details from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# 2. Check if the environment variables are set
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1) # Exit if the URL is missing

if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1) # Exit if the API key is missing

print(f"Attempting to connect to Weaviate Cloud at {wcd_url}...")

try:
    # 3. Connect to Weaviate Cloud using the obtained credentials
    # The 'with' statement ensures the client connection is automatically closed
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,                     # Use the URL from the env var
        auth_credentials=Auth.api_key(wcd_api_key) # Use the API key from the env var
    ) as client:

        # 4. Check if the Weaviate instance is ready to accept requests
        if client.is_ready():
            print("Successfully connected and Weaviate instance is ready!")
        else:
            print("Connected to Weaviate, but the instance is not ready.")
            # Optionally exit if readiness is strictly required
            # sys.exit(1)

        # The example uses assert, which is also a valid way to check readiness
        # If client.is_ready() is False, this will raise an AssertionError
        # assert client.is_ready()
        # print("Assertion passed: Weaviate instance is ready!")

except Exception as e:
    print(f"An error occurred during connection or readiness check: {e}")
    sys.exit(1)

# 5. No further actions are taken. The 'with' block handles closing the client.
print("Script finished.")

```

**Output**:
```
Attempting to connect to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected and Weaviate instance is ready!
Script finished.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 24.65s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc  # New location for classes like Property, DataType
from weaviate.auth import AuthApiKey
import os
import sys

# 1. Get Weaviate Cloud connection details from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

# Define the collection name
collection_name = "DemoProducts"

client = None  # Initialize client to None for the finally block
try:
    # 2. Connect to Weaviate Cloud (WCS) instance
    #    Using weaviate.connect_to_wcs for WCS specific connection
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(wcd_key),
        # Optional: Add headers if needed, e.g., for OpenAI keys
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
        # }
    )

    print("Successfully connected to Weaviate.")
    client.is_ready() # Optional check

    # 3. Check if the collection already exists and delete it if it does
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist. Proceeding to create.")

    # 4. Define the properties for the collection
    properties = [
        wvc.config.Property(
            name="name",
            data_type=wvc.config.DataType.TEXT,
            description="Name of the product",
            # Optional: configure tokenization, indexing, etc.
            # tokenization=wvc.config.Tokenization.WHITESPACE
        ),
        wvc.config.Property(
            name="description",
            data_type=wvc.config.DataType.TEXT,
            description="Description of the product",
        ),
        wvc.config.Property(
            name="price",
            data_type=wvc.config.DataType.NUMBER,  # Use NUMBER for floats/decimals
            description="Price of the product",
        ),
        wvc.config.Property(
            name="in_stock",
            data_type=wvc.config.DataType.BOOL,
            description="Whether the product is currently in stock",
        ),
    ]

    # 5. Create the collection
    print(f"Creating collection '{collection_name}'...")
    collection = client.collections.create(
        name=collection_name,
        properties=properties,
        # Optional: Specify vectorizer, module configs, replication, sharding etc.
        # vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),
        # generative_config=wvc.config.Configure.Generative.openai(),
        # replication_config=wvc.config.Configure.replication(factor=1)
    )

    print(f"Successfully created collection '{collection.name}'.") # Use collection.name from returned object

except Exception as e:
    print(f"An error occurred: {e}")
    # Potentially log the error or raise it depending on context
    # raise e

finally:
    # 6. Close the connection
    if client:
        print("Closing Weaviate connection.")
        client.close()

```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Successfully created collection 'DemoProducts'.
Closing Weaviate connection.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 26.08s)

**Generated Code**:
```python
import os
import sys  # Used for exiting if env vars are missing
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure # Import Configure if vectorizer needed

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"

# --- 1. Get Connection Details from Environment Variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# --- 2. Validate Environment Variables ---
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)  # Exit the script if the URL is missing

if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)  # Exit the script if the API key is missing

print(f"Attempting to connect to Weaviate Cloud at {wcd_url}...")

# Initialize client to None for the finally block
client = None

try:
    # --- 3. Connect to Weaviate Cloud ---
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Optional: Add headers if needed, e.g., for generative AI module API keys
        # headers={
        #    "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY"), # Example for OpenAI
        # }
    )
    print("Successfully connected to Weaviate Cloud.")
    client.is_ready() # Optional check

    # --- 4. Check if Collection Exists and Delete if Necessary ---
    print(f"Checking for existing collection '{COLLECTION_NAME}'...")
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' found. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted successfully.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to creation.")

    # --- 5. Define Collection Properties ---
    properties_definition = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER), # Use NUMBER for floats/decimals
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    # --- 6. Create the Collection ---
    print(f"Creating collection '{COLLECTION_NAME}'...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=properties_definition,
        # Optional: Add vectorizer configuration if needed for semantic search
        # vectorizer_config=Configure.Vectorizer.text2vec_openai() # Example
        # Or Configure.Vectorizer.none() if you manage vectors manually
    )

    print(f"Successfully created collection: {products_collection.name}")
    # You can also inspect the created config:
    # config = client.collections.get(COLLECTION_NAME).config.get()
    # print("\nCollection Configuration:")
    # print(config)


except weaviate.exceptions.AuthenticationFailedException as auth_err:
    print(f"Authentication failed: {auth_err}")
    print("Please check your WCD_TEST_URL and WCD_TEST_KEY.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # --- 7. Close the Connection ---
    if client:
        print("Closing Weaviate connection.")
        client.close()
    else:
        print("No Weaviate connection was established.")

```

**Output**:
```
Attempting to connect to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Checking for existing collection 'DemoProducts'...
Collection 'DemoProducts' found. Deleting it...
Collection 'DemoProducts' deleted successfully.
Creating collection 'DemoProducts'...
Successfully created collection: DemoProducts
Closing Weaviate connection.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 26.50s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure

# 1. Get Weaviate Cloud connection details from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    exit(1)

collection_name = "DemoProducts"

# 2. Connect to Weaviate Cloud instance
# Using a try...finally block to ensure the client is closed
client = None
try:
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Add any necessary headers, e.g., for API keys of inference services
        # headers={
        #     "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
        # }
    )
    print("Successfully connected to Weaviate Cloud.")

    # Check client readiness
    if not client.is_ready():
       print("Weaviate client is not ready!")
       exit(1)

    # 3. Check if the collection already exists and delete it if it does
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it...")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist. Proceeding to create.")

    # 4. Define the properties for the new collection
    properties_to_create = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER), # Use NUMBER for float/int
        Property(name="in_stock", data_type=DataType.BOOL), # Use BOOL for boolean
    ]

    # 5. Create the collection
    print(f"Creating collection '{collection_name}'...")
    new_collection = client.collections.create(
        name=collection_name,
        properties=properties_to_create,
        # If you need vectorization, uncomment and configure the following:
        # vectorizer_config=Configure.Vectorizer.text2vec_openai()
        # If you don't need vectorization (e.g., only keyword search or filtering):
        vectorizer_config=Configure.Vectorizer.none() # Explicitly disable vectorization
    )

    print(f"Successfully created collection '{collection_name}' with properties:")
    # You can inspect the created collection's config if needed
    config = new_collection.config.get()
    for prop in config.properties:
        print(f"  - Name: {prop.name}, DataType: {prop.data_type.name}") # Accessing DataType enum name

except weaviate.exceptions.AuthenticationFailedException:
    print(f"Authentication failed. Check your WCD_TEST_URL and WCD_TEST_KEY.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # 6. Close the client connection
    if client:
        print("Closing Weaviate client connection.")
        client.close()

print("Script finished.")

# Example usage:
# Make sure WCD_TEST_URL and WCD_TEST_KEY are set in your environment
# export WCD_TEST_URL="your-weaviate-cloud-url"
# export WCD_TEST_KEY="your-weaviate-api-key"
# python your_script_name.py
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Successfully created collection 'DemoProducts' with properties:
  - Name: name, DataType: TEXT
  - Name: description, DataType: TEXT
  - Name: price, DataType: NUMBER
  - Name: in_stock, DataType: BOOL
Closing Weaviate client connection.
Script finished.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 55.79s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc # Alias for weaviate.classes
from weaviate.auth import AuthApiKey
import os
import sys
import time # To potentially wait for collection readiness if needed

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

def main():
    """Connects to Weaviate, creates a collection, batches imports data, and counts objects."""

    # 1. Get Weaviate Cloud Credentials from Environment Variables
    wcd_url = os.getenv("WCD_TEST_URL")
    wcd_key = os.getenv("WCD_TEST_KEY")

    if not wcd_url or not wcd_key:
        print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
        print("Please set these variables with your Weaviate Cloud instance URL and API key.")
        sys.exit(1)

    print(f"Attempting to connect to Weaviate Cloud at: {wcd_url}")

    client = None # Initialize client to None for finally block
    try:
        # 2. Connect to Weaviate Cloud using API Key Authentication
        client = weaviate.connect_to_wcs(
            cluster_url=wcd_url,
            auth_credentials=AuthApiKey(wcd_key),
            # Optional: Add headers for module API keys if needed, e.g.:
            # headers={
            #    "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
            # }
        )

        # Check if connection is successful
        if not client.is_ready():
             raise ConnectionError("Weaviate client failed to connect.")

        print("Successfully connected to Weaviate Cloud.")
        print(f"Weaviate version: {client.get_meta()['version']}")


        # 3. Recreate the Collection (Delete if exists, then Create)
        # This ensures a clean state for the demo script.
        if client.collections.exists(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
            client.collections.delete(COLLECTION_NAME)
            print(f"Collection '{COLLECTION_NAME}' deleted.")
            # Optional: Short pause to ensure deletion completes in the cluster
            # time.sleep(2)

        print(f"Creating collection '{COLLECTION_NAME}'...")
        products_collection = client.collections.create(
            name=COLLECTION_NAME,
            description="A collection to store demo product information",
            properties=[
                wvc.config.Property(
                    name="name",
                    data_type=wvc.config.DataType.TEXT,
                    description="Name of the product",
                    # Optional: Specify tokenization if needed for keyword search later
                    # tokenization=wvc.config.Tokenization.WORD
                ),
                wvc.config.Property(
                    name="description",
                    data_type=wvc.config.DataType.TEXT,
                    description="Description of the product",
                ),
            ],
            # Define vectorizer settings (or disable if not needed)
            # For this example, we'll disable vectorization as it wasn't requested
            vectorizer_config=wvc.config.Configure.Vectorizer.none(),

            # Define inverted index settings (important for filtering/keyword search)
            # Using default settings is usually fine to start
            inverted_index_config=wvc.config.Configure.inverted_index(
                 index_timestamps=False # Often not needed unless filtering/sorting by creation time
            )
            # Generative configuration (if using generative search) - not needed here
            # generative_config=wvc.config.Configure.Generative.openai() # Example
        )
        print(f"Collection '{COLLECTION_NAME}' created successfully.")


        # 4. Generate Data Objects
        print(f"Generating {NUM_OBJECTS_TO_IMPORT} data objects...")
        data_objects = []
        for i in range(NUM_OBJECTS_TO_IMPORT):
            data_objects.append(
                {
                    "name": f"Product {i}",
                    "description": f"This is the description for product number {i}. It's quite generic."
                }
            )
        print(f"Generated {len(data_objects)} objects.")


        # 5. Batch Import Data
        print(f"Starting batch import into '{COLLECTION_NAME}'...")
        # Use the collection object obtained during creation (products_collection)
        # Access the batch manager through the collection's data attribute
        with products_collection.data.batch() as batch:
            for data_obj in data_objects:
                batch.add_object(
                    properties=data_obj
                    # Weaviate automatically generates a UUID if 'uuid' is not provided
                )

        # The 'with' block automatically handles sending the batch when exiting.
        # The v4 client batch manager raises exceptions on errors during the process.
        # For more granular error checking, you would examine the result if using
        # non-context-manager batching methods (less common in v4).
        print(f"Successfully imported {len(data_objects)} objects.")
        # Optional: Add a small delay to ensure objects are indexed if querying immediately
        # print("Waiting a moment for indexing...")
        # time.sleep(2)

        # 6. Verify the number of objects in the collection
        print(f"Counting objects in '{COLLECTION_NAME}'...")

        # Use the aggregate query method on the collection object
        aggregate_result = products_collection.aggregate.over_all(total_count=True)

        object_count = aggregate_result.total_count
        print(f"Found {object_count} objects in the collection '{COLLECTION_NAME}'.")

        # Verify count matches expected number
        if object_count == NUM_OBJECTS_TO_IMPORT:
            print("Verification successful: Object count matches the number imported.")
        else:
            print(f"Warning: Object count ({object_count}) does not match expected count ({NUM_OBJECTS_TO_IMPORT}).")


    except weaviate.exceptions.AuthenticationFailedError as auth_err:
        print(f"Authentication Error: {auth_err}")
        print("Please check your WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        # You might want to log the full traceback in a real application
        # import traceback
        # traceback.print_exc()
        sys.exit(1) # Indicate failure

    finally:
        # 7. Close the connection
        if client and client.is_connected():
            client.close()
            print("Weaviate connection closed.")
        elif client:
            print("Client was initialized but connection failed or was already closed.")
        else:
            print("Client was not initialized.")

if __name__ == "__main__":
    main()
```

**Output**:
```
Attempting to connect to Weaviate Cloud at: https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate Cloud.
Weaviate version: 1.29.1
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Generating 50 data objects...
Generated 50 objects.
Starting batch import into 'DemoProducts'...

An unexpected error occurred: '_DataCollection' object has no attribute 'batch'
Weaviate connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 40.80s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc # New standard alias for weaviate.classes
from weaviate.auth import AuthApiKey # Correct import for Auth
import os
import sys

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

# --- Get Weaviate Cloud credentials from environment variables ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Error: WCD_TEST_URL or WCD_TEST_KEY environment variables not set.")
    print("Please set these variables to connect to your Weaviate Cloud instance.")
    sys.exit(1) # Exit if credentials are not found

# --- Initialize Weaviate Client ---
client = None # Initialize client to None for finally block
try:
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(wcd_api_key),
        # Optional: Add headers if needed, e.g., for OpenAI keys
        # headers={
        #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_APIKEY", "")
        # }
    )
    client.wait_for_ready(timeout=30) # Wait up to 30 seconds for Weaviate to be ready
    print("Connection successful!")

    # --- Check if collection exists and delete if it does (for a clean demo run) ---
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it for demo purposes.")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    # --- Create the collection ---
    print(f"Creating collection '{COLLECTION_NAME}'...")
    client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            wvc.config.Property(name="name", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="description", data_type=wvc.config.DataType.TEXT),
        ],
        # Optional: Specify vectorizer, module config, etc.
        # vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai()
        # generative_config=wvc.config.Configure.Generative.openai()
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # --- Get the collection object ---
    products_collection = client.collections.get(COLLECTION_NAME)

    # --- Prepare data for batch import ---
    print(f"Preparing {NUM_OBJECTS_TO_IMPORT} objects for import...")
    data_to_import = [
        {
            "name": f"Product {i}",
            "description": f"This is the description for product number {i}. It's an amazing item!"
        } for i in range(NUM_OBJECTS_TO_IMPORT)
    ]
    print("Data preparation complete.")

    # --- Batch import the data ---
    print(f"Starting batch import of {len(data_to_import)} objects...")
    # Use dynamic batching context manager
    with products_collection.batch.dynamic() as batch:
        for i, data_row in enumerate(data_to_import):
            batch.add_object(
                properties=data_row,
                # Optionally add a UUID: uuid=generate_uuid5(data_row)
            )
            # Optional: Check for errors periodically within the loop
            # if (i + 1) % 100 == 0: # Example check every 100 objects
            #     if batch.number_errors > 0:
            #         print(f"Warning: {batch.number_errors} errors occurred during import (checked at object {i+1}).")

    print("Batch import process finished.")

    # --- Check for failed objects ---
    # Note: The failed_objects list might grow large if many objects fail.
    # Accessing batch.failed_objects *after* the 'with' block is correct.
    if products_collection.batch.failed_objects:
         print(f"\nNumber of failed imports: {len(products_collection.batch.failed_objects)}")
         # Print details of the first few failures for debugging
         for i, failed in enumerate(products_collection.batch.failed_objects):
             if i >= 5: # Limit printing details for brevity
                 print("... (more failures not shown)")
                 break
             print(f"  - Failed object index (approx): {i}, Error: {failed.message}") # Adjust based on actual failed object structure if needed
    else:
        print("All objects imported successfully.")


    # --- Get and print the number of objects in the collection ---
    # Using aggregate for the canonical v4 way
    aggregate_result = products_collection.aggregate.over_all(total_count=True)
    object_count = aggregate_result.total_count

    # Or using the len() shortcut (which internally calls aggregate.over_all)
    # object_count = len(products_collection) # This also works in v4 as a shortcut

    print(f"\nNumber of objects in collection '{COLLECTION_NAME}': {object_count}")

    # --- Verify count matches expected ---
    if object_count == NUM_OBJECTS_TO_IMPORT:
        print("Object count matches the number of imported items.")
    else:
        print(f"Warning: Object count ({object_count}) does not match expected ({NUM_OBJECTS_TO_IMPORT}). Check logs or failed objects.")


except weaviate.exceptions.WeaviateQueryError as e:
    print(f"An error occurred during Weaviate query/operation: {e}")
except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Could not connect to Weaviate: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- Close the client connection ---
    if client:
        print("Closing Weaviate client connection.")
        client.close()
    else:
        print("Client was not initialized, skipping close.")
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
An unexpected error occurred: 'WeaviateClient' object has no attribute 'wait_for_ready'
Closing Weaviate client connection.

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 30.08s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
import os
import time # Added for potential delays if needed

# --- Configuration ---
COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

# --- 1. Get Weaviate Cloud Credentials ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Error: Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

# --- 2. Connect to Weaviate Cloud ---
try:
    # Use a context manager for automatic connection closing
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        # Add headers if needed for specific inference APIs, e.g.:
        # headers={
        #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY", "")
        # }
    ) as client:

        print("Successfully connected to Weaviate.")

        # --- 3. Check Connection ---
        if not client.is_ready():
            print("Error: Weaviate client is not ready.")
            exit(1)
        print("Client is ready.")

        # --- 4. (Optional but Recommended) Delete Existing Collection ---
        if client.collections.exists(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
            client.collections.delete(COLLECTION_NAME)
            # Small delay to ensure deletion is processed if running immediately after
            time.sleep(2)
            print(f"Collection '{COLLECTION_NAME}' deleted.")

        # --- 5. Create the Collection ---
        print(f"Creating collection '{COLLECTION_NAME}'...")
        client.collections.create(
            name=COLLECTION_NAME,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
                # If you wanted vectorization, you'd add vectorizer_config here
                # e.g., vectorizer_config=Configure.Vectorizer.text2vec_openai()
            ],
            # Ensure vectorizer is explicitly None if not using one
            vectorizer_config=Configure.Vectorizer.none()
        )
        print(f"Collection '{COLLECTION_NAME}' created successfully.")

        # --- 6. Get the Collection Object ---
        products_collection = client.collections.get(COLLECTION_NAME)
        print(f"Got collection object for '{COLLECTION_NAME}'.")

        # --- 7. Prepare Data for Batch Import ---
        print(f"Preparing {NUM_OBJECTS_TO_IMPORT} objects for batch import...")
        objects_to_add = []
        for i in range(NUM_OBJECTS_TO_IMPORT):
            objects_to_add.append({
                "name": f"Product {i+1}",  # Start naming from 1
                "description": f"This is the description for product {i+1}."
            })
        print("Data preparation complete.")

        # --- 8. Batch Import Objects ---
        print(f"Starting batch import of {len(objects_to_add)} objects...")

        # Use the dynamic batching context manager
        with products_collection.batch.dynamic() as batch:
            for data_object in objects_to_add:
                batch.add_object(
                    properties=data_object
                    # No vector needed since vectorizer is None
                )

        print("Batch import process finished.")

        # --- Check for Batch Errors ---
        if products_collection.batch.number_errors > 0:
            print(f"WARNING: Encountered {products_collection.batch.number_errors} errors during batch import.")
            # You can access failed objects if needed:
            # failed_objs = products_collection.batch.failed_objects
            # for failed in failed_objs:
            #     print(f"Failed object: {failed.message}, Original: {failed.original_object}")
        else:
            print("Batch import completed successfully with no errors.")

        # --- 9. Verify the Number of Objects ---
        print(f"Verifying the number of objects in '{COLLECTION_NAME}'...")

        # Use aggregate query to get the count
        aggregate_result = products_collection.aggregate.over_all(total_count=True)

        print(f"Total number of objects in '{COLLECTION_NAME}': {aggregate_result.total_count}")

        if aggregate_result.total_count == NUM_OBJECTS_TO_IMPORT:
            print("Verification successful: Correct number of objects found.")
        else:
            print(f"Verification failed: Expected {NUM_OBJECTS_TO_IMPORT} objects, but found {aggregate_result.total_count}.")

except weaviate.exceptions.AuthenticationFailedError:
    print("Authentication failed. Please check your WCD_TEST_URL and WCD_TEST_KEY.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Script finished.")
    # Connection is automatically closed by the 'with' statement

```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate.
Client is ready.
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Got collection object for 'DemoProducts'.
Preparing 50 objects for batch import...
Data preparation complete.
Starting batch import of 50 objects...
Batch import process finished.
An unexpected error occurred: '_BatchCollectionWrapper' object has no attribute 'number_errors'
Script finished.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 30.22s)

**Generated Code**:
```python
import weaviate
import os
import sys
from dotenv import load_dotenv

# --- Configuration ---
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "dessert wine"
RESULT_LIMIT = 2

# --- Load Environment Variables ---
load_dotenv()

wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# --- Validate Environment Variables ---
if not all([wcd_url, wcd_api_key, openai_api_key]):
    print("ERROR: Missing environment variables.")
    print("Please ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set.")
    sys.exit(1) # Exit if credentials are missing

# --- Prepare Connection Headers ---
# The OpenAI API key needs to be passed in the headers for text2vec-openai
headers = {"X-OpenAI-Api-Key": openai_api_key}

# --- Connect to Weaviate Cloud (WCD) ---
print(f"Connecting to Weaviate Cloud at {wcd_url}...")
try:
    # Use connect_to_wcs for Weaviate Cloud Service connection in v4
    # Pass authentication and necessary headers (like OpenAI key)
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(api_key=wcd_api_key),
        headers=headers
    )
    client.wait_for_ready(timeout_seconds=30) # Wait up to 30s for readiness
    print("Connection successful!")

    # --- Get a reference to the collection ---
    wine_reviews = client.collections.get(COLLECTION_NAME)

    # --- Perform the nearText query ---
    print(f"\nSearching for '{QUERY_TEXT}' in '{COLLECTION_NAME}' (limit {RESULT_LIMIT})...")
    response = wine_reviews.query.near_text(
        query=QUERY_TEXT,
        limit=RESULT_LIMIT,
        return_properties=["title", "country", "price", "points"]
        # We don't need to specify the vectorizer here,
        # Weaviate uses the one defined in the collection's schema.
    )

    # --- Process and Print Results ---
    print("\nQuery Results:")
    if not response.objects:
        print("No matching wines found.")
    else:
        for i, obj in enumerate(response.objects):
            props = obj.properties
            print(f"\n--- Result {i+1} ---")
            print(f"  Title:   {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price:   {props.get('price', 'N/A')}") # Assuming price is stored directly
            print(f"  Points:  {props.get('points', 'N/A')}")
            # Optionally print distance/certainty if needed
            # print(f"  Distance: {obj.metadata.distance}") # v4 uses obj.metadata

except weaviate.exceptions.WeaviateQueryException as e:
     print(f"\nERROR: Query failed! Collection '{COLLECTION_NAME}' might not exist or schema mismatch.")
     print(f"Details: {e}")
except weaviate.exceptions.WeaviateException as e:
    print(f"\nERROR: Could not connect to or query Weaviate: {e}")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
finally:
    # --- Close the connection ---
    if 'client' in locals() and client.is_connected():
        print("\nClosing Weaviate connection.")
        client.close()
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...

Closing Weaviate connection.

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 38, in <module>
    client.wait_for_ready(timeout_seconds=30) # Wait up to 30s for readiness
AttributeError: 'WeaviateClient' object has no attribute 'wait_for_ready'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 72, in <module>
    except weaviate.exceptions.WeaviateException as e:
AttributeError: module 'weaviate.exceptions' has no attribute 'WeaviateException'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 24.93s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import QueryReference
import os
import sys # Used for sys.exit

# --- Configuration ---
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "dessert wine"
RESULT_LIMIT = 2
REQUESTED_PROPERTIES = ["title", "country", "price", "points"]

# --- 1. Get Connection Details from Environment Variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# --- Basic Validation ---
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)
if not openai_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

# --- 2. Connect to Weaviate Cloud ---
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_key),
        headers={
            "X-OpenAI-API-Key": openai_key  # Pass OpenAI key for vectorization
        },
    )
    print("Successfully connected to Weaviate.")

    # --- 3. Get the Collection ---
    print(f"Getting collection: {COLLECTION_NAME}")
    wine_reviews = client.collections.get(COLLECTION_NAME)

    # --- 4. Perform the nearText Query ---
    print(f"Querying for '{QUERY_TEXT}' (limit: {RESULT_LIMIT})...")
    response = wine_reviews.query.near_text(
        query=QUERY_TEXT,
        limit=RESULT_LIMIT,
        return_properties=REQUESTED_PROPERTIES # Specify desired properties
    )

    # --- 5. Process and Print Results ---
    print("\n--- Query Results ---")
    if response.objects:
        for i, obj in enumerate(response.objects):
            print(f"\nResult {i+1}:")
            # Access properties using .get() for safety in case a property is missing
            print(f"  Title:   {obj.properties.get('title', 'N/A')}")
            print(f"  Country: {obj.properties.get('country', 'N/A')}")
            print(f"  Price:   {obj.properties.get('price', 'N/A')}")
            print(f"  Points:  {obj.properties.get('points', 'N/A')}")
            # You can also print metadata like distance/certainty if needed:
            # print(f"  Distance: {obj.metadata.distance}") # If available
            # print(f"  Certainty: {obj.metadata.certainty}") # If available
    else:
        print("No matching wines found.")

    print("\n--- End of Results ---")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- 6. Close the Connection ---
    if 'client' in locals() and client.is_connected():
        print("Closing Weaviate connection.")
        client.close()
    else:
        print("Client was not connected or doesn't exist.")

```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate.
Getting collection: WineReview
Querying for 'dessert wine' (limit: 2)...

--- Query Results ---

Result 1:
  Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price:   24.0
  Points:  88

Result 2:
  Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price:   40.0
  Points:  88

--- End of Results ---
Closing Weaviate connection.

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 32.71s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery # Import needed for optional metadata
import os
import sys

# --- Configuration ---
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "dessert wine"
RESULT_LIMIT = 2
RETURN_PROPERTIES = ["title", "country", "price", "points"]

# --- Retrieve Connection Details from Environment Variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# --- Validate Environment Variables ---
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)
if not openai_api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("       This is required for the text2vec-openai vectorizer.")
    sys.exit(1)

# --- Define Connection Parameters ---
# Note: The OpenAI API key is passed via headers for inference tasks like vectorization
headers = {
    "X-OpenAI-Api-Key": openai_api_key
}

print(f"Attempting to connect to Weaviate Cloud at {wcd_url}...")

# --- Connect to Weaviate Cloud using a context manager ---
try:
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers=headers
    ) as client:

        print("Successfully connected to Weaviate Cloud.")
        print(f"Checking if collection '{COLLECTION_NAME}' exists...")

        # --- Check if collection exists ---
        if not client.collections.exists(COLLECTION_NAME):
            print(f"Error: Collection '{COLLECTION_NAME}' does not exist.")
            print("Please ensure the collection has been created with the text2vec-openai vectorizer.")
            sys.exit(1)

        print(f"Collection '{COLLECTION_NAME}' found.")

        # --- Get the collection ---
        wine_reviews = client.collections.get(COLLECTION_NAME)

        print(f"\nPerforming semantic search for '{QUERY_TEXT}' in '{COLLECTION_NAME}'...")

        # --- Perform the near_text (semantic) search ---
        response = wine_reviews.query.near_text(
            query=QUERY_TEXT,
            limit=RESULT_LIMIT,
            return_properties=RETURN_PROPERTIES,
            # Optionally include metadata like distance if needed:
            # return_metadata=MetadataQuery(distance=True)
        )

        # --- Process and print the results ---
        print(f"\nFound {len(response.objects)} results (limit was {RESULT_LIMIT}):")

        if not response.objects:
            print("No matching wines found.")
        else:
            for i, wine in enumerate(response.objects):
                print(f"\n--- Result {i+1} ---")
                properties = wine.properties
                print(f"  Title:   {properties.get('title', 'N/A')}")
                print(f"  Country: {properties.get('country', 'N/A')}")
                print(f"  Price:   {properties.get('price', 'N/A')}") # Price might be None or missing
                print(f"  Points:  {properties.get('points', 'N/A')}")

                # If you requested metadata, you could print it like this:
                # if wine.metadata:
                #     print(f"  Distance: {wine.metadata.distance:.4f}") # Example for distance

except Exception as e:
    print(f"\nAn error occurred during the Weaviate operation:")
    print(e)
    # For detailed debugging, uncomment the next line
    # import traceback
    # traceback.print_exc()
    sys.exit(1)

print("\nScript finished.")
```

**Output**:
```
Attempting to connect to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.
Checking if collection 'WineReview' exists...
Collection 'WineReview' found.

Performing semantic search for 'dessert wine' in 'WineReview'...

Found 2 results (limit was 2):

--- Result 1 ---
  Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price:   24.0
  Points:  88

--- Result 2 ---
  Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price:   40.0
  Points:  88

Script finished.

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 28.18s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc
import os
import json # Import json for pretty printing if needed

# --- Configuration ---
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "pair with steak"
RESULT_LIMIT = 5
HYBRID_ALPHA = 0.5
MAX_PRICE = 50
MIN_POINTS = 90
REQUIRED_SUBSTRINGS = ["spice", "fruit", "berry", "cherry", "honey"]

# --- Retrieve credentials from environment variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# --- Check if environment variables are set ---
if not wcd_url:
    raise ValueError("WCD_TEST_URL environment variable not set.")
if not wcd_api_key:
    raise ValueError("WCD_TEST_KEY environment variable not set.")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# --- Define connection parameters ---
auth_credentials = wvc.auth.AuthApiKey(api_key=wcd_api_key)
openai_headers = {"X-OpenAI-Api-Key": openai_api_key}

client = None
try:
    # --- Connect to Weaviate Cloud ---
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=auth_credentials,
        headers=openai_headers  # Pass OpenAI key for vectorizer authentication
    )
    print("Connection successful!")

    # --- Get the collection object ---
    print(f"Accessing collection: {COLLECTION_NAME}")
    reviews = client.collections.get(COLLECTION_NAME)

    # --- Define the filters ---
    print(f"Building filters: price < {MAX_PRICE}, points > {MIN_POINTS}, review_body contains one of {REQUIRED_SUBSTRINGS}")

    # Filter for price less than MAX_PRICE
    price_filter = wvc.query.Filter.by_property("price").less_than(MAX_PRICE)

    # Filter for points greater than MIN_POINTS
    points_filter = wvc.query.Filter.by_property("points").greater_than(MIN_POINTS)

    # Filter for review_body containing at least one of the required substrings
    # Using contains_any for efficient OR logic on substrings within the text property
    substring_filter = wvc.query.Filter.by_property("review_body").contains_any(REQUIRED_SUBSTRINGS)

    # Combine all filters using logical AND
    combined_filter = wvc.query.Filter.all_of([
        price_filter,
        points_filter,
        substring_filter
    ])

    # --- Perform the hybrid search query ---
    print(f"Performing hybrid search for '{QUERY_TEXT}' with alpha={HYBRID_ALPHA}, limit={RESULT_LIMIT}...")
    response = reviews.query.hybrid(
        query=QUERY_TEXT,
        limit=RESULT_LIMIT,
        alpha=HYBRID_ALPHA,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points"] # Specify properties to return
    )

    # --- Process and print the results ---
    print("\n--- Query Results ---")
    if response.objects:
        for i, wine_object in enumerate(response.objects):
            properties = wine_object.properties
            print(f"\nResult {i+1}:")
            print(f"  Title:   {properties.get('title', 'N/A')}")
            print(f"  Country: {properties.get('country', 'N/A')}")
            print(f"  Price:   {properties.get('price', 'N/A'):.2f}") # Format price nicely
            print(f"  Points:  {properties.get('points', 'N/A')}")
            # Optional: Print score or other metadata if needed
            # print(f"  Score:   {wine_object.metadata.score}") # Example if score is needed
    else:
        print("No matching wines found.")

except weaviate.exceptions.WeaviateQueryError as e:
        print(f"Query error: {e}")
        print(f"Original gRPC error details: {e.grpc_ BATCH_DELETE_FAILED}") # Example of accessing gRPC details if available
except weaviate.exceptions.WeaviateBaseError as e:
    print(f"An error occurred with Weaviate: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- Close the client connection ---
    if client:
        print("\nClosing Weaviate client connection.")
        client.close()
```

**Errors**:
```
  File "/code/code.py", line 94
    (e.grpc_ BATCH_DELETE_FAILED)
             ^
SyntaxError: f-string: invalid syntax

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 35.69s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter # MetadataQuery is not needed for the requested output
import os
import sys

# 1. Get credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# 2. Check if environment variables are set
if not wcd_url:
    print("Error: WCD_TEST_URL environment variable not set.")
    sys.exit(1)
if not wcd_api_key:
    print("Error: WCD_TEST_KEY environment variable not set.")
    sys.exit(1)
if not openai_api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

# Define constants for the query
COLLECTION_NAME = "WineReview"
QUERY_TEXT = "pair with steak"
RESULT_LIMIT = 5
HYBRID_ALPHA = 0.5
PRICE_LIMIT = 50
POINTS_THRESHOLD = 90
REQUIRED_SUBSTRINGS = ["spice", "fruit", "berry", "cherry", "honey"]
# Specify only the properties we need in the output
RETURN_PROPS = ["title", "country", "price", "points"]

try:
    # 3. Connect to Weaviate Cloud using a 'with' statement for automatic connection closing
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            "X-OpenAI-API-Key": openai_api_key
        },
        # Optional: configure timeouts
        # startup_period=120 # seconds to wait for Weaviate to start before checking readiness
    ) as client:

        print("Connection successful.")
        # Optional: Check if the client is ready
        if not client.is_ready():
             print("Error: Weaviate client is not ready.")
             sys.exit(1)

        # 4. Get the collection object
        print(f"Accessing collection: {COLLECTION_NAME}")
        wine_reviews = client.collections.get(COLLECTION_NAME)

        # 5. Define the filters based on the requirements
        print("Defining query filters...")
        filters = (
            Filter.by_property("price").less_than(PRICE_LIMIT) &
            Filter.by_property("points").greater_than(POINTS_THRESHOLD) &
            Filter.by_property("review_body").contains_any(REQUIRED_SUBSTRINGS)
        )

        # 6. Perform the hybrid query
        print(f"Performing hybrid search for '{QUERY_TEXT}' with limit {RESULT_LIMIT}, alpha {HYBRID_ALPHA}...")
        response = wine_reviews.query.hybrid(
            query=QUERY_TEXT,
            limit=RESULT_LIMIT,
            alpha=HYBRID_ALPHA,
            filters=filters,
            # Specify only the properties needed to optimize the response
            return_properties=RETURN_PROPS
            # Metadata is not requested in the output, so we omit return_metadata
            # return_metadata=MetadataQuery(score=True) # Use this if you need the score
        )

        # 7. Process and print the results
        print(f"\n--- Query Results (Max {RESULT_LIMIT}) ---")
        if not response.objects:
            print("No wines found matching all criteria.")
        else:
            print(f"Found {len(response.objects)} matching wines:")
            for i, wine_object in enumerate(response.objects):
                props = wine_object.properties
                print(f"\nResult {i+1}:")
                print(f"  Title:   {props.get('title', 'N/A')}")
                print(f"  Country: {props.get('country', 'N/A')}")
                print(f"  Price:   ${props.get('price', 'N/A'):.2f}") # Format price nicely
                print(f"  Points:  {props.get('points', 'N/A')}")
                # If you added return_metadata=MetadataQuery(score=True) above, you could print score:
                # print(f"  Score:   {wine_object.metadata.score:.4f}")

except weaviate.exceptions.WeaviateQueryException as e:
        print(f"Error during Weaviate query: {e}")
        # This could indicate issues like the collection not existing, property names being wrong, etc.
except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Error connecting to Weaviate: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

print("\nScript finished.")
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
Connection successful.
Accessing collection: WineReview
Defining query filters...
Performing hybrid search for 'pair with steak' with limit 5, alpha 0.5...

--- Query Results (Max 5) ---
Found 5 matching wines:

Result 1:
  Title:   Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price:   $40.00
  Points:  92

Result 2:
  Title:   Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price:   $49.00
  Points:  91

Result 3:
  Title:   Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price:   $27.00
  Points:  91

Result 4:
  Title:   Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price:   $25.00
  Points:  93

Result 5:
  Title:   Château Rauzan-Ségla 2012  Margaux
  Country: France
  Price:   $0.00
  Points:  94

Script finished.

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 30.26s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# --- Configuration ---
# Get connection details and API keys from environment variables
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COLLECTION_NAME = "WineReview"

# Check if environment variables are set
if not WCD_URL:
    raise ValueError("WCD_TEST_URL environment variable not set.")
if not WCD_KEY:
    raise ValueError("WCD_TEST_KEY environment variable not set.")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# --- Define Query Parameters ---
search_query = "pair with steak"
result_limit = 5
hybrid_alpha = 0.5 # 0 = BM25 only, 1 = vector only, 0.5 = equal weight
max_price = 50
min_points = 90
required_keywords = ["spice", "fruit", "berry", "cherry", "honey"]
return_props = ["title", "country", "price", "points"]

# --- Connect to Weaviate ---
print(f"Connecting to Weaviate Cloud at {WCD_URL}...")
client = None # Initialize client to None for finally block
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )
    client.wait_for_ready()
    print("Connection successful.")

    # --- Get Collection Handle ---
    print(f"Accessing collection: {COLLECTION_NAME}")
    if not client.collections.exists(COLLECTION_NAME):
        print(f"Error: Collection '{COLLECTION_NAME}' does not exist.")
        exit()
    wine_reviews = client.collections.get(COLLECTION_NAME)

    # --- Define Filters ---
    # Note: We use Filter.all_of([...]) to combine multiple filters with AND logic.
    # Alternatively, you can chain filters using the & operator: filter1 & filter2 & filter3
    filters = Filter.all_of([
        Filter.by_property("price").less_than(max_price),
        Filter.by_property("points").greater_than(min_points),
        Filter.by_property("review_body").contains_any(required_keywords)
    ])
    print("Filters defined:")
    print(f"- Price < {max_price}")
    print(f"- Points > {min_points}")
    print(f"- Review body contains any of: {required_keywords}")


    # --- Perform Hybrid Search ---
    print(f"\nPerforming hybrid search for: '{search_query}'")
    print(f"Limit: {result_limit}, Alpha: {hybrid_alpha}")

    response = wine_reviews.query.hybrid(
        query=search_query,
        alpha=hybrid_alpha,
        limit=result_limit,
        filters=filters,
        return_properties=return_props
        # fusion_type=HybridFusion.RELATIVE_SCORE # Default fusion type
    )

    # --- Process and Print Results ---
    print("\n--- Search Results ---")
    if response.objects:
        print(f"Found {len(response.objects)} matching wines:")
        for i, wine in enumerate(response.objects):
            props = wine.properties
            print(f"\nResult {i+1}:")
            print(f"  Title:   {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price:   ${props.get('price', 'N/A'):.2f}") # Format price
            print(f"  Points:  {props.get('points', 'N/A')}")
    else:
        print("No matching wines found with the specified criteria.")

except weaviate.exceptions.WeaviateQueryException as e:
      print(f"An error occurred during the query: {e}")
      # Potentially inspect e.message or specific attributes if needed
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # --- Close Connection ---
    if client and client.is_connected():
        print("\nClosing Weaviate connection.")
        client.close()
    else:
        print("\nNo active Weaviate connection to close.")
```

**Output**:
```
Connecting to Weaviate Cloud at https://vzpf5e8otq6123jmttpiga.c0.europe-west3.gcp.weaviate.cloud...
An unexpected error occurred: 'WeaviateClient' object has no attribute 'wait_for_ready'

Closing Weaviate connection.

```

---

### gemini/gemini-2.0-flash-lite

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 2.26s)

**Generated Code**:
```python
import os
import weaviate

# Get the Weaviate Cloud credentials from environment variables
url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not url or not api_key:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set")

# Initialize the Weaviate client
client = weaviate.Client(
    url=url,
    auth_client_secret=weaviate.AuthApiKey(api_key=api_key),
)

# Check if the server is ready
try:
    client.is_ready()
    print("Weaviate server is ready!")
except Exception as e:
    print(f"Weaviate server is not ready: {e}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:12: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 12, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 2.69s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Get the URL and API key from environment variables
wcd_test_url = os.environ.get("WCD_TEST_URL")
wcd_test_key = os.environ.get("WCD_TEST_KEY")

if not wcd_test_url or not wcd_test_key:
    raise ValueError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )


# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_test_url,
    auth_credentials=Auth.api_key(wcd_test_key),
)

# Check that the server is ready
try:
    assert client.is_ready()
    print("Weaviate server is ready to accept requests.")
except Exception as e:
    print(f"Weaviate server is not ready: {e}")
finally:
    client.close()
```

**Output**:
```
Weaviate server is ready to accept requests.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 7.98s)

**Generated Code**:
```python
import os
import weaviate

# Retrieve Weaviate Cloud credentials from environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")

if not WEAVIATE_URL or not WEAVIATE_API_KEY:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    exit(1)

# Initialize the Weaviate client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
)


collection_name = "DemoProducts"

# 1. Delete the collection if it exists
try:
    client.schema.delete_class(collection_name)
    print(f"Collection '{collection_name}' deleted (if it existed).")
except weaviate.exceptions.UnexpectedStatusCodeException as e:
    if e.status_code == 404:
        print(f"Collection '{collection_name}' not found, no deletion needed.")
    else:
        print(f"Error deleting collection '{collection_name}': {e}")
        exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)


# 2. Define the schema properties
class_definition = {
    "class": collection_name,
    "properties": [
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
        {"name": "price", "dataType": ["number"]},
        {"name": "in_stock", "dataType": ["boolean"]},
    ],
}

# 3. Create the collection
try:
    client.schema.create_class(class_definition)
    print(f"Collection '{collection_name}' created successfully.")
except weaviate.exceptions.UnexpectedStatusCodeException as e:
    print(f"Error creating collection '{collection_name}': {e}")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)


# Close the client connection (optional, but good practice)
client.close()
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

**Status**: ❌ FAILURE (runtime: 3.06s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.config import CollectionConfig
from weaviate.classes.init import Auth

# Get Weaviate Cloud credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not cluster_url or not api_key:
    raise ValueError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )

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
    CollectionConfig(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
    )
)

print(f"Created collection: {products_collection.name}")

# Close connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.classes.config import CollectionConfig
ImportError: cannot import name 'CollectionConfig' from 'weaviate.classes.config' (/usr/local/lib/python3.9/site-packages/weaviate/classes/config.py)

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.87s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.init import Auth
import os

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

if not wcd_url or not wcd_key:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    exit(1)


# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key),
)

# Collection name
collection_name = "DemoProducts"

try:
    # Delete the collection if it exists
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)
        print(f"Deleted collection '{collection_name}'")

    # Create the collection
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOLEAN),
        ],
    )
    print(f"Created collection '{collection_name}'")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    client.close()
```

**Output**:
```
Deleted collection 'DemoProducts'
An error occurred: BOOLEAN

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 8.37s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")

if not WEAVIATE_URL or not WEAVIATE_API_KEY:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    exit(1)


# Initialize the client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
)


# Define the class schema (if it doesn't exist)
class_name = "DemoProducts"
try:
    client.schema.get_class(class_name)
    print(f"Class '{class_name}' already exists. Skipping schema creation.")
except weaviate.exceptions.UnexpectedStatusCodeException as e:
    if e.status_code == 404:
        class_object = {
            "class": class_name,
            "description": "A collection of demo products",
            "properties": [
                {
                    "name": "name",
                    "dataType": ["text"],
                    "description": "The product name",
                },
                {
                    "name": "description",
                    "dataType": ["text"],
                    "description": "The product description",
                },
            ],
            "vectorIndexConfig": {
              "distance": "cosine" # Adjust distance metric if necessary
            },
        }

        client.schema.create_class(class_object)
        print(f"Class '{class_name}' created.")
    else:
        print(f"Error checking/creating class '{class_name}': {e}")
        exit(1)


# Batch import objects
batch_size = 50
with client.batch(batch_size=batch_size) as batch:
    for i in range(batch_size):
        object_data = {
            "name": f"Product {i}",
            "description": f"Description {i}",
        }
        batch.add_data_object(data_object=object_data, class_name=class_name)

print(f"Batch import of {batch_size} objects complete.")


# Count the number of objects in the collection
try:
    result = client.query.aggregate(class_name).with_meta_count().do()
    object_count = result["data"]["Aggregate"][class_name][0]["meta"]["count"]
    print(f"Number of objects in '{class_name}': {object_count}")
except Exception as e:
    print(f"Error counting objects: {e}")
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

**Status**: ✅ SUCCESS (runtime: 9.71s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Retrieve Weaviate Cloud connection details from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Error: Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY.")
    exit(1)

try:
    # Initialize the client
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=AuthApiKey(WCD_TEST_KEY),
    )

    # Get or create the collection
    collection_name = "DemoProducts"
    try:
        collection = client.collections.get(collection_name)
    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        if e.status_code == 404:
            # Create the collection if it doesn't exist
            collection = client.collections.create(
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
                ],
            )
        else:
            raise  # Re-raise other exceptions

    # Prepare data for batch import
    data_rows = [
        {
            "name": f"Product {i}",
            "description": f"Description {i}",
        }
        for i in range(50)
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

    # Handle potential import errors
    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        print(f"First failed object: {failed_objects[0]}")

    # Print the number of objects in the collection
    print(f"Number of objects in collection '{collection_name}': {len(collection)}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'client' in locals() and client is not None:
        client.close()
```

**Output**:
```
Number of objects in collection 'DemoProducts': 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 7.03s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Configure, Property, DataType
import os

# 1. Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

# 2. Create the collection (if it doesn't exist)
try:
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
    )
except weaviate.exceptions.UnexpectedStatusCodeException as e:
    # If the collection already exists, it will throw an error.  Catch it and move on.
    if e.status_code != 409:  # 409 is "Conflict" - collection already exists
        raise e
    else:
        print("Collection 'DemoProducts' already exists.  Skipping creation.")

# 3. Batch import objects
collection = client.collections.get("DemoProducts")
with collection.batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}",
            }
        )

# 4. Print the number of objects in the collection
count = collection.aggregate.over_all().object_count
print(f"Number of objects in 'DemoProducts': {count}")

# 5. Close the connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.52s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud credentials from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    raise ValueError(
        "Please set the following environment variables: WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY"
    )


# Initialize the Weaviate client
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
)

try:
    # Perform the vector search
    result = (
        client.query
        .get("WineReview", ["title", "country", "price", "points"])
        .with_near_text({"concepts": ["dessert wine"]})
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
/code/code.py:16: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 16, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.01s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Retrieve environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Check if all required environment variables are set
if not all([cluster_url, api_key, openai_api_key]):
    raise ValueError(
        "Please set the following environment variables: WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY"
    )


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
    print(f"Error getting collection 'WineReview': {e}")
    client.close()
    exit()

# Query for dessert wines
try:
    response = collection.query.near_text(
        query="dessert wine",
        limit=2
    )
except Exception as e:
    print(f"Error querying Weaviate: {e}")
    client.close()
    exit()


# Print the results
if response and response.objects:
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

**Status**: ❌ FAILURE (runtime: 4.68s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import MetadataQuery

# 1. Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# 2. Query the 'WineReview' collection
collection = client.collections.get("WineReview")

response = collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"],
    return_metadata=MetadataQuery(distance=True) # Optionally include distance
)

# 3. Print the results
if response.objects:
    for obj in response.objects:
        print(f"Title: {obj.properties.get('title')}")
        print(f"Country: {obj.properties.get('country')}")
        print(f"Price: {obj.properties.get('price')}")
        print(f"Points: {obj.properties.get('points')}")
        print(f"Distance: {obj.metadata.distance}") # Print distance if available
        print("-" * 20)
else:
    print("No matching wines found.")

# 4. Close the client (optional, but good practice)
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.35s)

**Generated Code**:
```python
import os
import weaviate

# Environment variables for Weaviate Cloud
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Initialize the Weaviate client
client = weaviate.Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
)

# Define the query
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
            "valueNumber": 50,
        },
        {
            "path": ["points"],
            "operator": "GreaterThan",
            "valueNumber": 90,
        },
        {
            "operator": "Or",
            "operands": [
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*spice*",
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*fruit*",
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*berry*",
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*cherry*",
                },
                {
                    "path": ["review_body"],
                    "operator": "Like",
                    "valueText": "*honey*",
                },
            ],
        },
    ],
}

# Perform the hybrid search
try:
    result = (
        client.query
        .get("WineReview", ["title", "country", "price", "points"])
        .with_hybrid(query=query, alpha=alpha)
        .with_limit(limit)
        .with_where(filters)
        .do()
    )
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Print the results
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.79s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Retrieve API keys from environment variables
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

# Get the collection
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
if response.objects:
    for obj in response.objects:
        properties = obj.properties
        if properties:
            print(f"Title: {properties.get('title')}")
            print(f"Country: {properties.get('country')}")
            print(f"Price: {properties.get('price')}")
            print(f"Points: {properties.get('points')}")
            print(f"Score: {obj.metadata.score}")
            print("-" * 20)
else:
    print("No matching wines found.")

# Close the client
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

**Status**: ❌ FAILURE (runtime: 6.74s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.query import HybridFusion, Filter
import os

# 1. Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Add inference API keys as needed
    }
)


# 2. Define the query
query = "pair with steak"
limit = 5
alpha = 0.5
keywords = ["spice", "fruit", "berry", "cherry", "honey"]
collection_name = "WineReview"

# 3. Execute the hybrid search with filters
try:
    response = client.collections.get(collection_name).query.hybrid(
        query=query,
        alpha=alpha,
        limit=limit,
        filters=(
            Filter.by_property("price").less_than(50) &
            Filter.by_property("points").greater_than(90) &
            (
                Filter.by_property("review_body").like(f"*{keywords[0]}*") |
                Filter.by_property("review_body").like(f"*{keywords[1]}*") |
                Filter.by_property("review_body").like(f"*{keywords[2]}*") |
                Filter.by_property("review_body").like(f"*{keywords[3]}*") |
                Filter.by_property("review_body").like(f"*{keywords[4]}*")
            )
        )
    )
    # 4. Print the results
    if response.objects:
        for obj in response.objects:
            if obj.properties:
                print(f"Title: {obj.properties.get('title')}")
                print(f"Country: {obj.properties.get('country')}")
                print(f"Price: {obj.properties.get('price')}")
                print(f"Points: {obj.properties.get('points')}")
                print("-" * 20)
    else:
        print("No matching wines found.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 9, in <module>
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

### openai/gpt-4o-2024-11-20

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 6.70s)

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

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, depending on your setup
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

**Status**: ❌ FAILURE (runtime: 4.32s)

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
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    raise ConnectionError("Weaviate server is not ready.")

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

**Status**: ❌ FAILURE (runtime: 12.43s)

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
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI module
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

**Status**: ❌ FAILURE (runtime: 7.82s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.schema.properties import Property, DataType

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Validate environment variables
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
auth_config = AuthApiKey(api_key=WCD_TEST_KEY)
client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)

# Define the collection (class) name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.schema.contains(collection_name):
    client.schema.delete_class(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Define the schema for the collection
collection_schema = {
    "class": collection_name,
    "properties": [
        {"name": "name", "dataType": [DataType.TEXT]},
        {"name": "description", "dataType": [DataType.TEXT]},
        {"name": "price", "dataType": [DataType.NUMBER]},
        {"name": "in_stock", "dataType": [DataType.BOOLEAN]},
    ],
}

# Create the collection
client.schema.create_class(collection_schema)
print(f"Created collection: {collection_name}")

# Close the client connection (optional, but good practice)
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

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.05s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

# Define the collection name
collection_name = "DemoProducts"

# Check if the collection already exists
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it...")
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")

# Create the collection with the specified properties
print(f"Creating collection '{collection_name}'...")
client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ],
    vectorizer_config=Configure.Vectorizer.text2vec_openai(),  # Optional vectorizer
)

print(f"Collection '{collection_name}' created successfully.")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 29, in <module>
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

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 8.69s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.exceptions import WeaviateStartUpError

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to Weaviate Cloud instance
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI module
)

# Create the schema for the "DemoProducts" collection
class_name = "DemoProducts"
schema = {
    "class": class_name,
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
            "description": "The description of the product",
        },
    ],
}

# Add the schema to Weaviate if it doesn't already exist
if not client.schema.contains(schema):
    client.schema.create_class(schema)

# Batch import 50 objects into the "DemoProducts" collection
with client.batch as batch:
    batch.batch_size = 10  # Set batch size
    for i in range(1, 51):  # Create 50 objects
        obj = {
            "name": f"Product {i}",
            "description": f"Description {i}",
        }
        batch.add_data_object(obj, class_name)

# Wait for the batch to complete
batch.flush()

# Count the number of objects in the "DemoProducts" collection
result = client.query.aggregate(class_name).with_meta_count().do()
count = result["data"]["Aggregate"][class_name][0]["meta"]["count"]

# Print the number of objects in the collection
print(f"Number of objects in the '{class_name}' collection: {count}")
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

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 8.95s)

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
if not client.schema.contains({"class": class_name}):
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
    batch.batch_size = 10  # Set batch size
    for data_row in data_rows:
        batch.add_data_object(data_object=data_row, class_name=class_name)

# Wait for the batch process to complete
client.batch.flush()

# Count the number of objects in the "DemoProducts" collection
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

**Status**: ✅ SUCCESS (runtime: 12.61s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

# Step 1: Create the "DemoProducts" collection with the required properties
collection_name = "DemoProducts"

# Check if the collection already exists
if not client.collections.exists(collection_name):
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        vectorizer_config=Configure.Vectorizer.text2vec_openai(),  # Optional vectorizer
    )
    print(f"Collection '{collection_name}' created.")
else:
    print(f"Collection '{collection_name}' already exists.")

# Step 2: Batch import 50 objects into the collection
collection = client.collections.get(collection_name)

# Use dynamic batching for efficient imports
with collection.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}",
            }
        )

# Step 3: Print the number of objects in the collection
# Use the iterator to count objects
object_count = sum(1 for _ in collection.iterator())
print(f"Number of objects in the '{collection_name}' collection: {object_count}")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists.
Number of objects in the 'DemoProducts' collection: 50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 6.39s)

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
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Query the WineReview collection
query = "dessert wine"
response = client.query.get(
    "WineReview",  # Class name
    ["title", "country", "price", "points"]  # Fields to retrieve
).with_near_text({
    "concepts": [query]
}).with_limit(2).do()

# Process and print the results
if "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
    results = response["data"]["Get"]["WineReview"]
    for wine in results:
        title = wine.get("title", "N/A")
        country = wine.get("country", "N/A")
        price = wine.get("price", "N/A")
        points = wine.get("points", "N/A")
        print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
else:
    print("No results found or an error occurred.")
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

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.18s)

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

# Query the WineReview collection
response = client.query.get(
    "WineReview",  # The name of the collection
    ["title", "country", "price", "points"]  # Fields to retrieve
).with_near_text({
    "concepts": ["dessert wine"]
}).with_limit(2).do()

# Print the results
if "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
    for wine in response["data"]["Get"]["WineReview"]:
        print(f"Title: {wine.get('title', 'N/A')}")
        print(f"Country: {wine.get('country', 'N/A')}")
        print(f"Price: {wine.get('price', 'N/A')}")
        print(f"Points: {wine.get('points', 'N/A')}")
        print("-" * 40)
else:
    print("No results found or an error occurred.")

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

**Status**: ❌ FAILURE (runtime: 7.77s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],  # Weaviate Cloud instance URL
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),  # Weaviate Cloud API key
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # OpenAI API key for text2vec-openai
    }
)

# Query the 'WineReview' collection for wines matching "dessert wine"
response = client.query.collection("WineReview").near_text(
    query="dessert wine",  # Semantic search query
    limit=2  # Limit the results to 2
).fetch_objects(return_properties=["title", "country", "price", "points"])

# Print the results
if response.objects:
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title')}")
        print(f"Country: {wine.properties.get('country')}")
        print(f"Price: {wine.properties.get('price')}")
        print(f"Points: {wine.properties.get('points')}")
        print("-" * 40)
else:
    print("No matching wines found.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    response = client.query.collection("WineReview").near_text(
AttributeError: 'WeaviateClient' object has no attribute 'query'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.31s)

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
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the query
query = """
{
  Get {
    WineReview(
      hybrid: {
        query: "pair with steak",
        alpha: 0.5
      },
      where: {
        operator: And,
        operands: [
          {
            operator: LessThan,
            path: ["price"],
            valueNumber: 50
          },
          {
            operator: GreaterThan,
            path: ["points"],
            valueNumber: 90
          },
          {
            operator: Or,
            operands: [
              {
                operator: Like,
                path: ["review_body"],
                valueText: "*spice*"
              },
              {
                operator: Like,
                path: ["review_body"],
                valueText: "*fruit*"
              },
              {
                operator: Like,
                path: ["review_body"],
                valueText: "*berry*"
              },
              {
                operator: Like,
                path: ["review_body"],
                valueText: "*cherry*"
              },
              {
                operator: Like,
                path: ["review_body"],
                valueText: "*honey*"
              }
            ]
          }
        ]
      },
      limit: 5
    ) {
      title
      country
      price
      points
    }
  }
}
"""

# Execute the query
response = client.query.raw(query)

# Parse and print the results
if "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
    results = response["data"]["Get"]["WineReview"]
    for wine in results:
        print(f"Title: {wine.get('title')}")
        print(f"Country: {wine.get('country')}")
        print(f"Price: {wine.get('price')}")
        print(f"Points: {wine.get('points')}")
        print("-" * 40)
else:
    print("No results found or an error occurred.")
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 20.57s)

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
    auth_client_secret=AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
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
                {"path": ["review_body"], "operator": "Like", "valueString": "*spice*"},
                {"path": ["review_body"], "operator": "Like", "valueString": "*fruit*"},
                {"path": ["review_body"], "operator": "Like", "valueString": "*berry*"},
                {"path": ["review_body"], "operator": "Like", "valueString": "*cherry*"},
                {"path": ["review_body"], "operator": "Like", "valueString": "*honey*"},
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
        title = wine.get("title", "N/A")
        country = wine.get("country", "N/A")
        price = wine.get("price", "N/A")
        points = wine.get("points", "N/A")
        print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
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

**Status**: ✅ SUCCESS (runtime: 14.48s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Define the query parameters
query_text = "pair with steak"
alpha = 0.5
limit = 5
price_limit = 50
points_min = 90
review_keywords = ["spice", "fruit", "berry", "cherry", "honey"]

# Build the filter for price, points, and review_body
filter_conditions = (
    Filter.by_property("price").less_than(price_limit) &
    Filter.by_property("points").greater_than(points_min) &
    Filter.by_property("review_body").like(f"*{'* OR *'.join(review_keywords)}*")
)

# Perform the hybrid search
response = client.collections.get("WineReview").query.hybrid(
    query=query_text,
    alpha=alpha,
    filters=filter_conditions,
    limit=limit,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
if response.objects:
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title')}")
        print(f"Country: {wine.properties.get('country')}")
        print(f"Price: {wine.properties.get('price')}")
        print(f"Points: {wine.properties.get('points')}")
        print("-" * 40)
else:
    print("No matching wines found.")

# Close the client connection
client.close()
```

**Output**:
```
No matching wines found.

```

---

### openai/gpt-4o-mini-2024-07-18

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 9.52s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
weaviate_url = os.getenv('WCD_TEST_URL')
weaviate_key = os.getenv('WCD_TEST_KEY')

# Create a Weaviate client instance
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthClientPassword(weaviate_key, "")
)

# Check if the server is ready
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

**Status**: ✅ SUCCESS (runtime: 4.84s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve the Weaviate Cloud URL and API key from environment variables
cluster_url = os.getenv('WCD_TEST_URL')
api_key = os.getenv('WCD_TEST_KEY')

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check if the server is ready to accept requests
assert client.is_ready()

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.14s)

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

# Define the class name
class_name = "DemoProducts"

# Check if the class already exists
if client.schema.contains(class_name):
    print(f"Class '{class_name}' already exists. Deleting it...")
    client.schema.delete_class(class_name)

# Define the schema for the new class
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

# Create the new class
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

**Status**: ❌ FAILURE (runtime: 6.93s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Auth, Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
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

# Close connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate import Auth, Property, DataType
ImportError: cannot import name 'Auth' from 'weaviate' (/usr/local/lib/python3.9/site-packages/weaviate/__init__.py)

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.52s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Define the collection name
collection_name = "DemoProducts"

# Check if the collection already exists
if client.collections.exists(collection_name):
    # Delete the existing collection
    client.collections.delete(collection_name)

# Create the new collection with the specified properties
client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN)
    ]
)

print(f"Collection '{collection_name}' created successfully.")

# Close the client when done
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 27, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN)
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.85s)

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
        username=weaviate_key,
        password=""
    )
)

# Define the class schema if it doesn't exist
class_name = "DemoProducts"
schema = {
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
}

# Check if the class already exists, if not, create it
if not client.schema.contains(class_name):
    client.schema.create_class(schema)

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

# Print the number of objects in the collection
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

**Status**: ❌ FAILURE (runtime: 9.12s)

**Generated Code**:
```python
import os
import weaviate

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.Auth.api_key(os.getenv("WCD_TEST_KEY")),
)

# Get the collection
collection = client.collections.get("DemoProducts")

# Prepare data rows
data_rows = [
    {
        "name": f"Product {i + 1}",
        "description": f"Description {i + 1}"
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
object_count = len(collection.get_all())
print(f"Number of objects in the collection: {object_count}")

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

**Status**: ❌ FAILURE (runtime: 8.04s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Define the collection name and properties
collection_name = "DemoProducts"

# Create the collection with the specified properties
client.collections.create(
    collection_name,
    properties=[
        weaviate.classes.config.Property(name="name", data_type=weaviate.classes.config.DataType.TEXT),
        weaviate.classes.config.Property(name="description", data_type=weaviate.classes.config.DataType.TEXT),
    ]
)

# Batch import 50 arbitrary objects into the collection
with client.collections.get(collection_name).batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
count = client.collections.get(collection_name).data.count()
print(f"Number of objects in '{collection_name}': {count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/sync.py", line 107, in create
    self.__loop.run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 42, in run_until_complete
    return fut.result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 446, in result
    return self.__get_result()
  File "/usr/local/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result
    raise self._exception
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/async_.py", line 134, in create
    name = await super()._create(config._to_dict())
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/base.py", line 27, in _create
    response = await self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 550, in post
    return await self.__send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 505, in __send
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 496, in __send
    raise UnexpectedStatusCodeError(error_msg, response=res)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.12s)

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

# Define the query
query = "dessert wine"

# Perform the query
results = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    near_text={"concepts": [query]},
    limit=2
).do()

# Print the results
for wine in results['data']['Get']['WineReview']:
    print(f"Title: {wine['title']}, Country: {wine['country']}, Price: {wine['price']}, Points: {wine['points']}")
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

**Status**: ❌ FAILURE (runtime: 11.46s)

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

# Query for wines that match "dessert wine"
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

**Status**: ❌ FAILURE (runtime: 6.46s)

**Generated Code**:
```python
import weaviate
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Add inference API keys as needed
    }
)

# Query the 'WineReview' collection for wines matching "dessert wine"
response = client.data.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    limit=2
).with_near_text(
    {"concepts": ["dessert wine"]}
).do()

# Print the results
for obj in response['data']['Get']['WineReview']:
    print(f"Title: {obj['title']}, Country: {obj['country']}, Price: {obj['price']}, Points: {obj['points']}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 7, in <module>
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.48s)

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

# Perform the hybrid search
results = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    limit=5
).with_hybrid(query=query, alpha=0.5).with_where(
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
                "operator": "Or",
                "operands": [
                    {
                        "path": ["review_body"],
                        "operator": "Contains",
                        "valueString": "spice"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Contains",
                        "valueString": "fruit"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Contains",
                        "valueString": "berry"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Contains",
                        "valueString": "cherry"
                    },
                    {
                        "path": ["review_body"],
                        "operator": "Contains",
                        "valueString": "honey"
                    }
                ]
            }
        ]
    }
).do()

# Print the results
for wine in results['data']['Get']['WineReview']:
    print(f"Title: {wine['title']}, Country: {wine['country']}, Price: {wine['price']}, Points: {wine['points']}")
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

**Status**: ✅ SUCCESS (runtime: 8.40s)

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

# Define the collection name
collection_name = "WineReview"

# Perform the hybrid query
response = client.collections.get(collection_name).query.hybrid(
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
Title: Bink 2014 Pinot Noir (Anderson Valley), Country: US, Price: 49.0, Points: 91, Score: 0.4632064700126648
Title: Doña Silvina 2011 Malbec (Mendoza), Country: Argentina, Price: 27.0, Points: 91, Score: 0.22124573588371277
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji), Country: Hungary, Price: 25.0, Points: 93, Score: 0.06578859686851501
Title: Château Rauzan-Ségla 2012  Margaux, Country: France, Price: 0.0, Points: 94, Score: 0.0148789556697011

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.27s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import Filter

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Define the query
query = "pair with steak"

# Define the substrings to look for in the review_body
substrings = ["spice", "fruit", "berry", "cherry", "honey"]

# Create the filter for review_body
review_body_filter = Filter.or_(
    *[Filter.by_property("review_body").like(f"*{substring}*") for substring in substrings]
)

# Perform the hybrid search
response = client.data.query.hybrid(
    query=query,
    alpha=0.5,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        review_body_filter
    ),
    limit=5
)

# Print the results
for obj in response.objects:
    print(f"Title: {obj.properties['title']}, Country: {obj.properties['country']}, Price: {obj.properties['price']}, Points: {obj.properties['points']}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

### openai/gpt-4.5-preview-2025-02-27

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 21.07s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Retrieve Weaviate Cloud URL and API key from environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud instance
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=AuthApiKey(api_key=weaviate_api_key)
)

# Check if the server is ready
is_ready = client.is_ready()
print(f"Weaviate server ready: {is_ready}")
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

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 16.93s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve credentials from environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check if the server is ready
assert client.is_ready()

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 53.29s)

**Generated Code**:
```python
import weaviate
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY"))
)

# Delete the collection if it already exists
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")

# Define and create the collection with specified properties
client.collections.create(
    name="DemoProducts",
    properties=[
        weaviate.classes.Property(name="name", data_type=weaviate.classes.DataType.TEXT),
        weaviate.classes.Property(name="description", data_type=weaviate.classes.DataType.TEXT),
        weaviate.classes.Property(name="price", data_type=weaviate.classes.DataType.NUMBER),
        weaviate.classes.Property(name="in_stock", data_type=weaviate.classes.DataType.BOOL),
    ]
)

print("Collection 'DemoProducts' created successfully.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 18, in <module>
    weaviate.classes.Property(name="name", data_type=weaviate.classes.DataType.TEXT),
AttributeError: module 'weaviate.classes' has no attribute 'Property'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 56.60s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY)
)

# Define collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

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

# Close the connection
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

**Status**: ✅ SUCCESS (runtime: 58.53s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Delete the collection if it already exists
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")
    print("Deleted existing 'DemoProducts' collection.")

# Create the 'DemoProducts' collection with specified properties
client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print("Created 'DemoProducts' collection successfully.")

# Close the client connection
client.close()
```

**Output**:
```
Deleted existing 'DemoProducts' collection.
Created 'DemoProducts' collection successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 67.68s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY"))
)

# Define the collection schema if it doesn't exist
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")  # Optional: delete existing collection to start fresh

demo_products = client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# Batch import 50 arbitrary objects
with demo_products.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
count = demo_products.aggregate.over_all(total_count=True)
print(f"Number of objects in 'DemoProducts': {count.total_count}")

# Close the client connection
client.close()
```

**Output**:
```
Number of objects in 'DemoProducts': 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 65.52s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=AuthApiKey(os.getenv("WCD_TEST_KEY")),
)

# Get the collection named "DemoProducts"
collection = client.collections.get("DemoProducts")

# Prepare 50 arbitrary objects
data_rows = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    }
    for i in range(50)
]

# Batch import objects into the collection
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(properties=data_row)
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for failed imports
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(f"Total objects in collection: {len(collection)}")

# Close the client connection
client.close()
```

**Output**:
```
Total objects in collection: 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 82.36s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# Create the "DemoProducts" collection if it doesn't exist
if not client.collections.exists("DemoProducts"):
    client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        vectorizer_config=Configure.Vectorizer.text2vec_openai()  # Optional: add vectorizer if needed
    )

# Get the collection
collection = client.collections.get("DemoProducts")

# Batch import 50 arbitrary objects
with collection.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
response = collection.aggregate.over_all(total_count=True)
print(f"Number of objects in 'DemoProducts': {response.total_count}")

# Close the client connection
client.close()
```

**Output**:
```
Number of objects in 'DemoProducts': 50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 30.73s)

**Generated Code**:
```python
import weaviate
import os

# Connect to Weaviate Cloud instance using environment variables
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Perform a vector search query for "dessert wine"
response = (
    client.collections.get("WineReview")
    .query.near_text(
        query="dessert wine",
        limit=2
    )
)

# Print the results
for wine in response.objects:
    properties = wine.properties
    print(f"Title: {properties.get('title')}")
    print(f"Country: {properties.get('country')}")
    print(f"Price: {properties.get('price')}")
    print(f"Points: {properties.get('points')}")
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

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 34.37s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-API-Key": os.getenv("OPENAI_API_KEY")
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Query the collection for wines matching "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the title, country, price, and points of each matching wine
for obj in response.objects:
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
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

**Status**: ✅ SUCCESS (runtime: 42.52s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Perform a semantic search for "dessert wine" with a limit of 2 results
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for wine in response.objects:
    props = wine.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
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

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 70.29s)

**Generated Code**:
```python
import weaviate
import os

# Connect to Weaviate Cloud instance
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Perform hybrid search query with filters
response = (
    client.collections.get("WineReview")
    .query.hybrid(
        query="pair with steak",
        alpha=0.5,
        query_properties=["review_body"],
        filters=(
            weaviate.classes.Filter("price").less_than(50)
            & weaviate.classes.Filter("points").greater_than(90)
            & (
                weaviate.classes.Filter("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
            )
        ),
        limit=5
    )
)

# Print the results
for wine in response.objects:
    props = wine.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 21, in <module>
    weaviate.classes.Filter("price").less_than(50)
AttributeError: module 'weaviate.classes' has no attribute 'Filter'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 54.17s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-API-Key": os.getenv("OPENAI_API_KEY")
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform hybrid search with filters
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
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 40)

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
----------------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
Score: 0.4629642069339752
----------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Score: 0.2213282436132431
----------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Score: 0.065570168197155
----------------------------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
Score: 0.01466419454663992
----------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 88.77s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion
import os

# Connect to Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_reviews = client.collections.get("WineReview")

# Define the filter conditions
price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)

# Define substring filters for review_body
substring_filters = (
    Filter.by_property("review_body").like("*spice*") |
    Filter.by_property("review_body").like("*fruit*") |
    Filter.by_property("review_body").like("*berry*") |
    Filter.by_property("review_body").like("*cherry*") |
    Filter.by_property("review_body").like("*honey*")
)

# Combine all filters
combined_filter = price_filter & points_filter & substring_filters

# Perform hybrid search
response = wine_reviews.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    fusion_type=HybridFusion.RELATIVE_SCORE,
    filters=combined_filter,
    limit=5,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for wine in response.objects:
    props = wine.properties
    print(f"Title: {props['title']}")
    print(f"Country: {props['country']}")
    print(f"Price: ${props['price']}")
    print(f"Points: {props['points']}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
----------------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
----------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
----------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
----------------------------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: $0.0
Points: 94
----------------------------------------

```

---

### openai/o3-mini-2025-01-31

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 5.57s)

**Generated Code**:
```python
#!/usr/bin/env python3
import os
import weaviate
from weaviate.auth import APIKey

client = weaviate.Client(
    url=os.environ["WCD_TEST_URL"],
    auth_client_secret=APIKey(os.environ["WCD_TEST_KEY"]),
)

if client.is_ready():
    print("Server is ready to accept requests.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.auth import APIKey
ImportError: cannot import name 'APIKey' from 'weaviate.auth' (/usr/local/lib/python3.9/site-packages/weaviate/auth.py)

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 3.14s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

assert client.is_ready()

client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 13.27s)

**Generated Code**:
```python
Below is an example Python script that uses the latest Weaviate client syntax to connect to Weaviate Cloud (using the WCD_TEST_URL and WCD_TEST_KEY environment variables), delete the "DemoProducts" collection if it already exists, and then create it with the specified properties.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

def main():
    # Get Weaviate Cloud instance URL and API key from environment variables
    weaviate_url = os.getenv("WCD_TEST_URL")
    api_key = os.getenv("WCD_TEST_KEY")

    if not weaviate_url or not api_key:
        raise ValueError("Both WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

    # Initialize the Weaviate client with the necessary API key header
    client = weaviate.Client(
        url=weaviate_url,
        additional_headers={
            "X-API-KEY": api_key
        }
    )
    
    class_name = "DemoProducts"

    # Check if the collection already exists; if so, delete it first.
    current_schema = client.schema.get()
    classes = current_schema.get("classes", [])
    
    for cls in classes:
        if cls.get("class") == class_name:
            print(f"Deleting existing class: {class_name}")
            client.schema.delete_class(class_name)
            break

    # Define the new class (collection) schema with the required properties.
    demo_products_class = {
        "class": class_name,
        "description": "A collection for demo products",
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

    # Create the new class in Weaviate.
    client.schema.create_class(demo_products_class)
    print(f"Created class: {class_name}")

if __name__ == "__main__":
    main()

------------------------------------------------------------

Explanation:
1. The script imports os and weaviate, and reads the Weaviate Cloud URL and API key from the environment variables WCD_TEST_URL and WCD_TEST_KEY.
2. It then initializes the Weaviate client with the API key passed as an HTTP header (X-API-KEY).
3. The script retrieves the current schema and checks if a class named "DemoProducts" already exists. If found, it deletes it.
4. It then defines the new "DemoProducts" class with the properties: name (text), description (text), price (number), and in_stock (boolean), and creates it using client.schema.create_class.
5. Finally, the script prints confirmation messages to indicate progress.

This code adheres to the latest Weaviate client syntax and meets the specified requirements.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that uses the latest Weaviate client syntax to connect to Weaviate Cloud (using the WCD_TEST_URL and WCD_TEST_KEY environment variables), delete the "DemoProducts" collection if it already exists, and then create it with the specified properties.
                ^
SyntaxError: invalid syntax

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 11.59s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Read the Weaviate Cloud URL and API key from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Define the collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the specified properties
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

# Close the connection (optional cleanup)
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

**Status**: ❌ FAILURE (runtime: 14.85s)

**Generated Code**:
```python
Below is an example Python script that connects to a Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, deletes the collection “DemoProducts” if it already exists, and then creates it with the desired properties.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    # Read connection info from environment variables
    weaviate_url = os.environ.get("WCD_TEST_URL")
    weaviate_api_key = os.environ.get("WCD_TEST_KEY")

    if not weaviate_url or not weaviate_api_key:
        raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key)
    )

    collection_name = "DemoProducts"

    # If the collection already exists, delete it first
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
    
    # Define the class (collection) with the desired properties
    properties = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]

    # Create the collection
    client.collections.create(collection_name, properties=properties)
    print(f"Collection '{collection_name}' has been created with the specified properties.")

    # Close the client connection when done
    client.close()

if __name__ == "__main__":
    main()
------------------------------------------------------------

Explanation:

1. The script reads the Weaviate Cloud URL and API key from the environment variables.
2. It connects to the cloud instance via the weaviate.connect_to_weaviate_cloud() provided in the latest client.
3. If the “DemoProducts” collection already exists, it deletes it.
4. It then creates a collection “DemoProducts” with four properties:
   • name (text)
   • description (text)
   • price (number)
   • in_stock (boolean)
5. Finally, it closes the client.

This script should work under the latest Weaviate Python client syntax.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to a Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, deletes the collection “DemoProducts” if it already exists, and then creates it with the desired properties.
                ^
SyntaxError: invalid syntax

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 16.34s)

**Generated Code**:
```python
Below is a complete Python script that uses the latest Weaviate client syntax to connect to a Weaviate Cloud instance (using the environment variables WCD_TEST_URL and WCD_TEST_KEY), creates a “DemoProducts” class (if it does not already exist) with two text properties (“name” and “description”), batch-imports 50 objects, and then prints the total number of objects in the DemoProducts collection.

Note: Before running the script, make sure you’ve installed the Weaviate client (e.g. via pip install weaviate-client) and that the WCD_TEST_URL and WCD_TEST_KEY environment variables are set.

──────────────────────────────
#!/usr/bin/env python3
import os
import weaviate

# Get connection info from environment variables
wcd_test_url = os.environ.get("WCD_TEST_URL")
wcd_test_key = os.environ.get("WCD_TEST_KEY")

if not wcd_test_url or not wcd_test_key:
    raise EnvironmentError("WCD_TEST_URL and WCD_TEST_KEY must be set in your environment.")

# Connect to Weaviate Cloud using API key authentication
client = weaviate.Client(
    url=wcd_test_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=wcd_test_key)
)

# (Optional) Create the DemoProducts schema if it does not already exist
class_name = "DemoProducts"
if not client.schema.exists(class_name):
    product_schema = {
        "class": class_name,
        "description": "A collection of demo product objects",
        "properties": [
            {
                "name": "name",
                "dataType": ["text"],
            },
           
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is a complete Python script that uses the latest Weaviate client syntax to connect to a Weaviate Cloud instance (using the environment variables WCD_TEST_URL and WCD_TEST_KEY), creates a “DemoProducts” class (if it does not already exist) with two text properties (“name” and “description”), batch-imports 50 objects, and then prints the total number of objects in the DemoProducts collection.
               ^
SyntaxError: invalid syntax

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 13.84s)

**Generated Code**:
```python
Below is an example Python script that connects to Weaviate Cloud using environment variables, retrieves a collection named "DemoProducts", and then batch-imports 50 objects with a name and description into it. Finally, it prints the total number of objects in the collection.

Note that this example assumes that the "DemoProducts" class (collection) already exists in your Weaviate instance with at least the properties "name" (text) and "description" (text).

--------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.auth import AuthApiKey

# Retrieve connection parameters from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Both WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

# Connect to Weaviate Cloud using the provided credentials
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=AuthApiKey(api_key)
)

# Retrieve the "DemoProducts" collection
collection = client.collections.get("DemoProducts")

# Prepare 50 arbitrary objects, each with "name" and "description"
data_rows = [
    {"name": f"Product {i}", "description": f"Description {i}"}
    for i in range(50)
]

# Batch import the objects
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(properties=data_row)
        # Stop the batch if errors exceed 10 to avoid runaway issues.
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Check for any failed objects during the batch import
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print("Total number of objects in the collection:", len(collection))

# Always clean up the client connection
client.close()

--------------------------------------------------

Explanation:

1. The script reads the Weaviate Cloud URL and API key from the environment.  
2. It uses weaviate.connect_to_weaviate_cloud with an AuthApiKey instance to connect.  
3. It retrieves the collection ("DemoProducts") via client.collections.get.  
4. Then, it constructs a list of 50 objects where each object has a "name" and "description".  
5. The objects are imported in batch mode within a context manager. The script also checks for errors during import and stops if more than 10 errors occur.  
6. Finally, it prints the number of objects available in the collection and closes the client connection.

Make sure the Weaviate Python client library is installed (e.g. via pip install weaviate-client) and that your schema in Weaviate includes the "DemoProducts" class with the required properties.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to Weaviate Cloud using environment variables, retrieves a collection named "DemoProducts", and then batch-imports 50 objects with a name and description into it. Finally, it prints the total number of objects in the collection.
                ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 16.80s)

**Generated Code**:
```python
Below is an example Python script that uses the latest Weaviate client to connect to Weaviate Cloud (using the environment variables WCD_TEST_URL and WCD_TEST_KEY), creates a collection called "DemoProducts" (with text properties “name” and “description”), batch-imports 50 objects, and finally prints the number of objects in that collection.

You can run the code as a standalone script (after installing the Weaviate client with pip install weaviate-client) and by making sure the environment variables WCD_TEST_URL and WCD_TEST_KEY are set.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    # -----------------------------
    # 1. CONNECT TO WEAVIATE CLOUD
    # -----------------------------
    # The WCD_TEST_URL should be your Weaviate Cloud instance URL.
    # The WCD_TEST_KEY should be your Weaviate Cloud API key.
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
    )

    # ---------------------------------------------
    # 2. CREATE 'DemoProducts' COLLECTION (if needed)
    # ---------------------------------------------
    collection_name = "DemoProducts"
    if not client.collections.exists(collection_name):
        client.collections.create(
            collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT)
            ]
        )
        print(f"Collection '{collection_name}' created.")
    else:
        print(f"Collection '{collection_name}' already exists.")

    # Retrieve the collection
    demo_products = client.collections.get(collection_name)

    # ---------------------------------------------
    # 3. BATCH IMPORT 50 OBJECTS INTO 'DemoProducts'
    # ---------------------------------------------
    with demo_products.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )
    print("Batch import completed.")

    # ---------------------------------------------
    # 4. COUNT THE NUMBER OF OBJECTS IN COLLECTION
    # ---------------------------------------------
    # We can iterate over the collection objects and count them.
    count = 0
    for _ in demo_products.iterator():
        count += 1

    print(f"Number of objects in collection '{collection_name}': {count}")

    # Always close the client when done
    client.close()

if __name__ == "__main__":
    main()

------------------------------------------------------------

Explanation of the key sections:

1. The script starts by connecting to We
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that uses the latest Weaviate client to connect to Weaviate Cloud (using the environment variables WCD_TEST_URL and WCD_TEST_KEY), creates a collection called "DemoProducts" (with text properties “name” and “description”), batch-imports 50 objects, and finally prints the number of objects in that collection.
                ^
SyntaxError: invalid syntax

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 14.63s)

**Generated Code**:
```python
Below is an example Python script that uses the latest Weaviate client syntax. It connects to Weaviate Cloud (using environment variables for the URL and API key), sets the OpenAI API key as an additional header (for the text2vec-openai vectorizer), runs a nearText query on the WineReview collection with the query "dessert wine" and a limit of 2 results, and then prints the title, country, price, and points for each matching wine.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

def main():
    # Retrieve environment variables
    wc_url = os.environ.get("WCD_TEST_URL")
    wc_api_key = os.environ.get("WCD_TEST_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    if not wc_url or not wc_api_key or not openai_api_key:
        raise ValueError("One or more necessary environment variables (WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY) are not set.")

    # Create the Weaviate client with API key auth and add the OpenAI API key as an additional header.
    client = weaviate.Client(
        url=wc_url,
        auth_client_secret=weaviate.AuthApiKey(api_key=wc_api_key),
        additional_headers={"X-OpenAI-Api-Key": openai_api_key}
    )

    # Build and execute the nearText query.
    query = (
        client.query.get("WineReview", ["title", "country", "price", "points"])
        .with_near_text({"concepts": ["dessert wine"]})
        .with_limit(2)
    )
    
    try:
        result = query.do()
    except Exception as e:
        print("Query failed:", e)
        return
    
    # Extract and print results. The response is typically structured as:
    # { "data": { "Get": { "WineReview": [ ... ] } } }
    reviews = result.get("data", {}).get("Get", {}).get("WineReview", [])
    if not reviews:
        print("No matching wines found.")
        return

    for wine in reviews:
        title = wine.get("title", "N/A")
        country = wine.get("country", "N/A")
        price = wine.get("price", "N/A")
        points = wine.get("points", "N/A")
        print(f"Title: {title}\nCountry: {country}\nPrice: {price}\nPoints: {points}\n{'-'*40}")

if __name__ == "__main__":
    main()

------------------------------------------------------------

Explanation:
1. The script reads the URL and API keys from the environment.
2. It instantiates a Weaviate client with the necessary authentication. The OpenAI API key is passed via the additional_headers so that the text2vec-openai vectorizer can use it.
3. It performs a nearText query searching for wines matching "dessert wine" in the WineReview collection, limiting results to 2.
4. It prints the title, country, price, and points for each returned wine.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that uses the latest Weaviate client syntax. It connects to Weaviate Cloud (using environment variables for the URL and API key), sets the OpenAI API key as an additional header (for the text2vec-openai vectorizer), runs a nearText query on the WineReview collection with the query "dessert wine" and a limit of 2 results, and then prints the title, country, price, and points for each matching wine.
                ^
SyntaxError: invalid syntax

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 16.09s)

**Generated Code**:
```python
Below is an example Python script using the latest Weaviate client syntax to query the WineReview collection. It connects to Weaviate Cloud using the environment variables WCD_TEST_URL and WCD_TEST_KEY and passes along the OpenAI API key (stored in OPENAI_API_KEY) via the HTTP header. The near_text query is used with the concept "dessert wine" and the results are limited to 2 items. Each matching wine’s title, country, price, and points are printed.

-----------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.auth import AuthApiKey

# Retrieve environment variables
wcd_test_url = os.environ.get("WCD_TEST_URL")
wcd_test_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not (wcd_test_url and wcd_test_key and openai_api_key):
    raise Exception("One or more required environment variables (WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY) are not set.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=wcd_test_url,
    auth_client_secret=AuthApiKey(wcd_test_key),
    additional_headers={
        "X-OpenAI-API-Key": openai_api_key
    }
)

# Build the near_text search query for 'dessert wine'. 
# The properties list limits the returned properties to title, country, price, and points.
result = (
    client.query
    .get("WineReview", properties=["title", "country", "price", "points"])
    .with_near_text({"concepts": ["dessert wine"]})
    .with_limit(2)
    .do()
)

# Parse and print the results.
# The data is nested under data -> Get -> WineReview
wines = result.get('data', {}).get('Get', {}).get('WineReview', [])
if not wines:
    print("No matching wines found.")
else:
    for wine in wines:
        title = wine.get("title", "N/A")
        country = wine.get("country", "N/A")
        price = wine.get("price", "N/A")
        points = wine.get("points", "N/A")
        print(f"Title: {title}\n  Country: {country}\n  Price: {price}\n  Points: {points}\n{'-'*40}")

# Optionally, close the client connection if needed (depending on your client version/setup)
client.close()

-----------------------------------------------------------

Explanation:
1. The script retrieves connection details and API keys from the environment.
2. It creates a client instance using AuthApiKey for the Weaviate Cloud API key and passes the OpenAI API key via headers.
3. The query uses the near_text operator with the concept “dessert wine” and limits results to 2.
4. Finally, it prints out the title, country, price, and points of each matching wine.

Make sure to run this script in an environment where the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script using the latest Weaviate client syntax to query the WineReview collection. It connects to Weaviate Cloud using the environment variables WCD_TEST_URL and WCD_TEST_KEY and passes along the OpenAI API key (stored in OPENAI_API_KEY) via the HTTP header. The near_text query is used with the concept "dessert wine" and the results are limited to 2 items. Each matching wine’s title, country, price, and points are printed.
                ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.46s)

**Generated Code**:
```python
Below is an example Python script that connects to Weaviate Cloud using your environment variables, then queries the "WineReview" collection with a near_text query for "dessert wine", limits the results to 2, and prints out the title, country, price, and points for each matching wine.

------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve the necessary environment variables
CLOUD_URL = os.environ["WCD_TEST_URL"]
CLOUD_API_KEY = os.environ["WCD_TEST_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Connect to Weaviate Cloud with API key authentication and the OpenAI header
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=CLOUD_URL,
    auth_credentials=Auth.api_key(CLOUD_API_KEY),
    headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
)

# Get the "WineReview" collection
wine_reviews = client.collections.get("WineReview")

# Use a near_text query to find wines matching "dessert wine" with a limit of 2 results.
query_response = wine_reviews.query.near_text(
    query="dessert wine",
    limit=2
)

# Iterate over the results and print the desired properties.
for obj in query_response.objects:
    properties = obj.properties
    title = properties.get("title", "N/A")
    country = properties.get("country", "N/A")
    price = properties.get("price", "N/A")
    points = properties.get("points", "N/A")
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")

# Optionally, close the client when done.
client.close()

------------------------

Explanation:
1. The script first imports the needed libraries and retrieves the connection/API keys from your environment.
2. It connects to Weaviate Cloud using the latest syntax with Auth.api_key and the appropriate headers including the OpenAI API key.
3. The "WineReview" collection is fetched and used to execute a near_text search for "dessert wine" with a maximum of 2 results.
4. Finally, it loops through each returned object, extracts the "title", "country", "price", and "points" properties, and prints them.

Make sure you have the latest Weaviate Python client installed (e.g., via pip install weaviate-client) and that your environment variables (WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY) are set before running this script.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to Weaviate Cloud using your environment variables, then queries the "WineReview" collection with a near_text query for "dessert wine", limits the results to 2, and prints out the title, country, price, and points for each matching wine.
                ^
SyntaxError: invalid syntax

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.93s)

**Generated Code**:
```python
Below is one complete Python example that uses the latest weaviate client syntax. Make sure you have installed the weaviate-client package (for example, via pip install weaviate-client) before running the code.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

# Retrieve environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not (WCD_TEST_URL and WCD_TEST_KEY and OPENAI_API_KEY):
    raise ValueError("Missing one or more required environment variables: WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY")

# Configure the Weaviate client for Weaviate Cloud: include the API key in additional headers.
client = weaviate.Client(
    url=WCD_TEST_URL,
    additional_headers={
        "X-API-KEY": WCD_TEST_KEY
    }
)

# Note: The WineReview collection uses the text2vec-openai vectorizer.
# OpenAI API key is used internally by Weaviate for the vectorization if configured.
# The following hybrid search query seeks wines that best match "pair with steak"
# while using a blend of vector search and keyword matching (alpha=0.5), and
# filters out wines with price < 50, points > 90, and review_body containing at least
# one of the substrings "spice", "fruit", "berry", "cherry", or "honey".

# Define the WHERE filter:
where_filter = {
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
}

# Execute the query:
result = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query="pair with steak", alpha=0.5)
    .with_where(where_filter)
    .with_limit(5)
    .do()
)

# Parse and print results:
# Depending on your Weaviate version, the results structure may be nested.
# Typically, the objects are under data -> Get -> WineReview.
try:
    wines = result["data"]["Get"]["WineReview"]
except KeyError:
    raise ValueError("Unexpected result format: " + str(result))

if not wines:
    print("No matching wines found.")
else:
    for wine in wines:
        title = wine.get("title", "N/A")
        country = wine.get("country", "N/A")
        price = wine.get("price", "N/A")
        points = wine.get("points", "N/A")
        print(f"Title: {title}\nCountry: {country}\nPrice: {price}\nPoints: {points}\n{'-'*40}")
------------------------------------------------------------

Explanation of the key parts:
1. The Weaviate client is connected to the Weaviate Cloud instance using WCD_TEST_URL and WCD_TEST_KEY.
2. The query uses the hybrid search capability (with the query "pair with steak" and alpha=0.5) and limits the results to 5.
3. The WHERE filter combines three constraints:
   • Price is less than 50.
   • Points are greater than 90.
   • The review_body must contain at least one of the substrings "spice", "fruit", "berry", "cherry", or "honey".
4. Finally, the code prints out the title, country, price, and points fields from each returned wine.

This should serve as a complete example that meets your requirements.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is one complete Python example that uses the latest weaviate client syntax. Make sure you have installed the weaviate-client package (for example, via pip install weaviate-client) before running the code.
                 ^
SyntaxError: invalid syntax

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.56s)

**Generated Code**:
```python
Below is an example Python script that uses the latest Weaviate client syntax to perform the requested query:

------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Get credentials and URLs from environment variables
wcd_url = os.environ["WCD_TEST_URL"]            # URL of the Weaviate Cloud instance
wcd_api_key = os.environ["WCD_TEST_KEY"]          # API key for the Weaviate Cloud instance
openai_api_key = os.environ["OPENAI_API_KEY"]       # OpenAI API Key (for text2vec-openai)

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_api_key),
    headers={"X-OpenAI-API-Key": openai_api_key},
)

# Query the "WineReview" collection
collection = client.collections.get("WineReview")

# Build the hybrid search filters:
# • price < 50
# • points > 90
# • review_body contains at least one of the substrings in the list below.
wine_filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
)

# Perform a hybrid search for wines that best match "pair with steak"
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=wine_filters,
    return_metadata=MetadataQuery(score=True)
)

# Print title, country, price, and points of each matching wine
for obj in response.objects:
    props = obj.properties
    title = props.get("title")
    country = props.get("country")
    price = props.get("price")
    points = props.get("points")
    print(f"Title: {title}")
    print(f"Country: {country}")
    print(f"Price: {price}")
    print(f"Points: {points}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 40)

# Close the connection
client.close()

------------------------------------------------

How it works:

1. It reads the Weaviate Cloud URL and API keys (both for Weaviate and OpenAI) from your environment variables (WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY).

2. It connects to the Weaviate Cloud instance using the latest client method, specifying the OpenAI API key in the headers.

3. It accesses the "WineReview" collection and runs a hybrid search query with the query term "pair with steak". The search is hybrid (with alpha=0.5) and limited to a maximum of 5 results.

4. The filters ensure that:
   • The price is less than 50.
   • The points are greater than 90.
   • The review_body field contains at least one of the specified substrings.

5. For each result, it prints the title, country, price, points, and the computed score.

You may run this code as a script (after setting up the required environment variables) to perform the query and display the results.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that uses the latest Weaviate client syntax to perform the requested query:
                ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 13.20s)

**Generated Code**:
```python
Below is an example Python script that connects to your Weaviate Cloud instance (using WCD_TEST_URL and WCD_TEST_KEY), then runs a hybrid search on the “WineReview” collection for wines matching the query “pair with steak” with alpha=0.5 and a limit of 5. The search applies a filter to return only results with price < 50, points > 90, and where the review_body contains at least one of the substrings “spice”, “fruit”, “berry”, “cherry”, or “honey”.

Save the code to a file (for example, query_wine_review.py) and run it—with the required environment variables set (OPENAI_API_KEY, WCD_TEST_URL, and WCD_TEST_KEY).

--------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to your Weaviate Cloud instance (using WCD_TEST_URL and WCD_TEST_KEY), then runs a hybrid search on the “WineReview” collection for wines matching the query “pair with steak” with alpha=0.5 and a limit of 5. The search applies a filter to return only results with price < 50, points > 90, and where the review_body contains at least one of the substrings “spice”, “fruit”, “berry”, “cherry”, or “honey”.
                ^
SyntaxError: invalid syntax

```

---

