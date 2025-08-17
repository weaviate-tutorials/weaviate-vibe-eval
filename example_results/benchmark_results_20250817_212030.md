# Weaviate Benchmark Results

Generated on: 2025-08-17 21:20:30

## Summary

- **anthropic/claude-3-7-sonnet-20250219**: 9/14 tasks successful
- **anthropic/claude-3-5-haiku-20241022**: 9/14 tasks successful
- **openai/gpt-4.1-mini-2025-04-14**: 7/14 tasks successful
- **cohere/command-a-03-2025**: 5/14 tasks successful
- **anthropic/claude-sonnet-4-20250514**: 13/14 tasks successful
- **anthropic/claude-opus-4-20250514**: 10/14 tasks successful
- **gemini/gemini-2.5-pro**: 13/14 tasks successful
- **gemini/gemini-2.5-flash**: 9/14 tasks successful
- **gemini/gemini-2.5-flash-lite**: 6/14 tasks successful
- **openai/gpt-5-2025-08-07**: 8/14 tasks successful
- **openai/gpt-5-mini-2025-08-07**: 5/14 tasks successful
- **openai/gpt-5-nano-2025-08-07**: 2/14 tasks successful
## Detailed Results

### anthropic/claude-3-7-sonnet-20250219

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 7.23s)

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
is_ready = client.is_ready()
print(f"Weaviate server is ready: {is_ready}")
```

**Output**:
```
Weaviate server is ready: True

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.74s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Get environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.42s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType, Configure

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables")

# Connect to Weaviate
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
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
    ],
    vectorizer_config=Configure.Vectorizer.none(),
)

print(f"Collection '{collection_name}' created successfully with the specified properties.")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' exists. Deleting it...
Collection 'DemoProducts' deleted.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
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

**Status**: ✅ SUCCESS (runtime: 5.26s)

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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 7.96s)

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
    client.collections.delete("DemoProducts")

# Create the DemoProducts collection with the specified properties
client.collections.create(
    "DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL)
    ]
)

# Verify the collection was created
if client.collections.exists("DemoProducts"):
    print("DemoProducts collection created successfully!")
else:
    print("Failed to create DemoProducts collection.")

# Close the client connection
client.close()
```

**Output**:
```
DemoProducts collection created successfully!

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 8.32s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.batch import Batch

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
    collection = client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    print("Collection 'DemoProducts' created")
else:
    collection = client.collections.get("DemoProducts")
    print("Collection 'DemoProducts' already exists")

# Batch import 50 objects
with collection.batch.dynamic() as batch:
    for i in range(1, 51):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
object_count = collection.aggregate.over_all().total_count
print(f"Number of objects in the collection: {object_count}")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.classes.batch import Batch
ImportError: cannot import name 'Batch' from 'weaviate.classes.batch' (/usr/local/lib/python3.9/site-packages/weaviate/classes/batch.py)

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 10.10s)

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
            {
                "name": "name",
                "dataType": ["text"]
            },
            {
                "name": "description",
                "dataType": ["text"]
            }
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
print(f"Number of objects in the collection: {len(collection)}")

# Close the client
client.close()
```

**Output**:
```
Number of objects in the collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.09s)

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
with collection.batch.fixed_size(batch_size=10) as batch:
    for i in range(1, 51):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
count = collection.query.fetch_objects(limit=0).total_count
print(f"Number of objects in the DemoProducts collection: {count}")

# Close the client when done
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 36, in <module>
    count = collection.query.fetch_objects(limit=0).total_count
AttributeError: 'QueryReturn' object has no attribute 'total_count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.10s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import QueryReference
from weaviate.embedded import EmbeddedOptions

# Get environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the Weaviate client
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
    headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Query the WineReview collection
response = (
    client.collections.get("WineReview")
    .query.near_text(
        query="dessert wine",
        limit=2
    )
    .with_additional(["distance"])
    .with_fields(["title", "country", "price", "points"])
    .do()
)

# Print the results
print("Matching wines for 'dessert wine':")
for wine in response.objects:
    properties = wine.properties
    print(f"Title: {properties['title']}")
    print(f"Country: {properties['country']}")
    print(f"Price: ${properties['price']}")
    print(f"Points: {properties['points']}")
    print(f"Distance: {wine.metadata.distance}")
    print("-" * 50)

# Close the client connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 22, in <module>
    client.collections.get("WineReview")
AttributeError: 'QueryReturn' object has no attribute 'with_additional'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.34s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Get environment variables
openai_api_key = os.environ.get("OPENAI_API_KEY")
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

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
    print("-" * 40)

# Close the client
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88
----------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88
----------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.46s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import MetadataQuery
import os

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
    
    # Query for wines that match "dessert wine"
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print the results
    print("Wines matching 'dessert wine':")
    for wine in response.objects:
        print(f"Title: {wine.properties['title']}")
        print(f"Country: {wine.properties['country']}")
        print(f"Price: ${wine.properties['price']}")
        print(f"Points: {wine.properties['points']}")
        print("-" * 50)
        
finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Wines matching 'dessert wine':
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.13s)

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
client = weaviate.connect_to_weaviate(
    url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Create filter for price < 50 and points > 90
price_points_filter = Filter.by_property("price").less_than(50).and_filter(
    Filter.by_property("points").greater_than(90)
)

# Create filter for review_body containing at least one of the specified substrings
review_filter = (
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
combined_filter = price_points_filter.and_filter(review_filter)

# Query the collection
response = (
    client.collections.get("WineReview")
    .query
    .hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=combined_filter
    )
    .with_additional(["certainty", "distance"])
    .with_fields(["title", "country", "price", "points", "review_body"])
    .do()
)

# Print the results
print("Wines that pair well with steak:")
print("-" * 50)

if response.objects:
    for i, wine in enumerate(response.objects, 1):
        props = wine.properties
        print(f"{i}. {props['title']}")
        print(f"   Country: {props['country']}")
        print(f"   Price: ${props['price']}")
        print(f"   Points: {props['points']}")
        print(f"   Certainty: {wine.metadata.certainty:.4f}")
        print("-" * 50)
else:
    print("No matching wines found.")

# Close the client
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

**Status**: ✅ SUCCESS (runtime: 6.90s)

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
print(f"Found {len(response.objects)} matching wines:")
for obj in response.objects:
    print(f"\nTitle: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: ${obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
    print(f"Score: {obj.metadata.score}")

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
Score: 0.5

Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Score: 0.3765353560447693

Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.04513849690556526

Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.016171861439943314

Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
Score: 0.0010482011130079627

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 14.67s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os
import re

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
    wine_collection = client.collections.get("WineReview")
    
    # Define the regex pattern to match any of the required substrings
    pattern = re.compile(r'spice|fruit|berry|cherry|honey', re.IGNORECASE)
    
    # Create a filter for price < 50 and points > 90
    price_points_filter = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90)
    )
    
    # Perform hybrid search with alpha=0.5
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Balance between keyword and vector search
        filters=price_points_filter,
        limit=5,
        return_metadata=MetadataQuery(distance=True, score=True)
    )
    
    # Process and print results, filtering for those containing required substrings
    print("Wines that pair well with steak:")
    print("================================")
    
    for obj in response.objects:
        # Check if review_body contains any of the required substrings
        review_body = obj.properties.get("review_body", "")
        if pattern.search(review_body):
            print(f"Title: {obj.properties.get('title', 'N/A')}")
            print(f"Country: {obj.properties.get('country', 'N/A')}")
            print(f"Price: ${obj.properties.get('price', 'N/A')}")
            print(f"Points: {obj.properties.get('points', 'N/A')}")
            print(f"Score: {obj.metadata.score:.4f}")
            print("--------------------------------")
    
finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Wines that pair well with steak:
================================
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
Score: 0.5000
--------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Score: 0.3765
--------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.0451
--------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.0162
--------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### anthropic/claude-3-5-haiku-20241022

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 4.79s)

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

**Status**: ✅ SUCCESS (runtime: 4.15s)

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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 11.59s)

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

**Status**: ✅ SUCCESS (runtime: 8.71s)

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

# Delete the collection if it already exists (for testing purposes)
try:
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)
except Exception as e:
    print(f"Error checking/deleting existing collection: {e}")

# Create the collection
try:
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
except Exception as e:
    print(f"Error creating collection: {e}")

# Close connection
client.close()
```

**Output**:
```
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 8.75s)

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

# Delete the collection if it already exists
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")

# Create the DemoProducts collection
client.collections.create(
    "DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL)
    ]
)

# Close the client connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 9.29s)

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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.86s)

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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
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

**Status**: ❌ FAILURE (runtime: 9.48s)

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
    # Create the collection with name and description properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT)
        ]
    )

    # Get the collection
    collection = client.collections.get("DemoProducts")

    # Batch import 50 objects
    with collection.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )

    # Print the number of objects in the collection
    object_count = collection.aggregate.count()
    print(f"Number of objects in the collection: {object_count}")

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
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

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.36s)

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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.25s)

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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.39s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

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

    # Perform near_text search for "dessert wine"
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2
    )

    # Print details for each matching wine
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: {wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print("---")

finally:
    # Always close the client connection
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.01s)

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
        result = client.collections.get("WineReview").query.hybrid(
            query="pair with steak",
            hybrid_search_options=HybridSearchOptions(alpha=0.5),
            filters=[
                # Price less than 50
                client.collections.get("WineReview").filter.less_than(path="price", value=50),
                # Points greater than 90
                client.collections.get("WineReview").filter.greater_than(path="points", value=90)
            ],
            limit=5
        )

        # Filter results based on review body keywords
        matching_wines = [
            wine for wine in result.objects 
            if any(keyword in wine.properties['review_body'].lower() 
                   for keyword in ['spice', 'fruit', 'berry', 'cherry', 'honey'])
        ]

        # Print matching wines
        for wine in matching_wines:
            print(f"Title: {wine.properties['title']}")
            print(f"Country: {wine.properties['country']}")
            print(f"Price: ${wine.properties['price']}")
            print(f"Points: {wine.properties['points']}")
            print("---")

    finally:
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

**Status**: ✅ SUCCESS (runtime: 9.34s)

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
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
---

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 14.08s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

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

    # Perform hybrid search with complex filtering
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Balance between semantic and keyword search
        fusion_type=HybridFusion.RELATIVE_SCORE,
        filters=(
            # Price less than 50
            Filter.by_property("price").less_than(50) &
            # Points greater than 90
            Filter.by_property("points").greater_than(90) &
            # Review body contains one of the specified substrings
            Filter.by_property("review_body").contains_any(
                ["spice", "fruit", "berry", "cherry", "honey"]
            )
        ),
        limit=5
    )

    # Print results
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: ${wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print("---")

finally:
    # Always close the client
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
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
---

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### openai/gpt-4.1-mini-2025-04-14

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 1.82s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Initialize Weaviate client with API key authentication
client = weaviate.Client(
    url,
    auth_client_secret=weaviate.AuthApiKey(api_key),
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready.")
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
TypeError: __init__() got an unexpected keyword argument 'auth_client_secret'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 2.92s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Read environment variables
cluster_url = os.environ["WCD_TEST_URL"]
api_key = os.environ["WCD_TEST_KEY"]

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check if the server is ready
assert client.is_ready()

client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.02s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

# Create Weaviate client with API key authentication
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # sometimes needed for OpenAI modules, remove if not needed
    }
)

class_name = "DemoProducts"

# Delete class if it exists
if client.schema.contains(class_name):
    client.schema.delete_class(class_name)

# Define the schema for the class
demo_products_class = {
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

# Create the class
client.schema.create_class(demo_products_class)

print(f"Class '{class_name}' created successfully.")
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

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 4.38s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Read environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY)
)

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

# Close connection
client.close()
```

**Output**:
```
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 4.44s)

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

collection_name = "DemoProducts"

# If the collection exists, delete it first
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the specified properties
client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ],
)

print(f"Collection '{collection_name}' created successfully.")
```

**Output**:
```
Collection 'DemoProducts' created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.01s)

**Generated Code**:
```python
import os
import weaviate

def main():
    # Get environment variables
    url = os.environ.get("WCD_TEST_URL")
    api_key = os.environ.get("WCD_TEST_KEY")

    if not url or not api_key:
        raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

    # Connect to Weaviate Cloud
    client = weaviate.Client(
        url=url,
        auth_client_secret=weaviate.AuthApiKey(api_key),
        additional_headers={
            "X-OpenAI-Api-Key": api_key  # sometimes needed if using OpenAI modules, but not required here
        }
    )

    # Define the schema for the class "DemoProducts"
    class_obj = {
        "class": "DemoProducts",
        "description": "A collection of demo products",
        "properties": [
            {
                "name": "name",
                "dataType": ["text"],
                "description": "Name of the product"
            },
            {
                "name": "description",
                "dataType": ["text"],
                "description": "Description of the product"
            }
        ]
    }

    # Check if class exists, if not create it
    schema = client.schema.get()
    classes = [c["class"] for c in schema.get("classes", [])]
    if "DemoProducts" not in classes:
        client.schema.create_class(class_obj)

    # Batch import 50 objects
    with client.batch as batch:
        batch.batch_size = 20  # batch size can be tuned
        for i in range(1, 51):
            obj = {
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
            batch.add_data_object(obj, "DemoProducts")

    # Count objects in the class
    result = client.query.aggregate("DemoProducts").with_meta_count().do()
    count = result.get("data", {}).get("Aggregate", {}).get("DemoProducts", [{}])[0].get("meta", {}).get("count", 0)

    print(f"Number of objects in 'DemoProducts': {count}")

if __name__ == "__main__":
    main()
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
  File "/code/code.py", line 62, in <module>
    main()
  File "/code/code.py", line 13, in main
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 10.24s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

def main():
    # Read environment variables
    WCD_TEST_URL = os.getenv("WCD_TEST_URL")
    WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

    if not WCD_TEST_URL or not WCD_TEST_KEY:
        raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=AuthApiKey(api_key=WCD_TEST_KEY),
    )

    # Define the class schema for "DemoProducts" if it doesn't exist
    class_name = "DemoProducts"
    schema = client.schema.get()
    classes = [c["class"] for c in schema.get("classes", [])]

    if class_name not in classes:
        class_obj = {
            "class": class_name,
            "description": "A demo product class",
            "properties": [
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
            ],
        }
        client.schema.create_class(class_obj)

    # Prepare 50 arbitrary objects
    data_rows = [
        {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
        for i in range(1, 51)
    ]

    # Batch import objects
    with client.batch as batch:
        batch.batch_size = 20  # You can adjust batch size if you want
        for data_row in data_rows:
            batch.add_data_object(
                data_object=data_row,
                class_name=class_name,
            )
            if batch.number_errors > 10:
                print("Batch import stopped due to excessive errors.")
                break

    # Print number of objects in the collection
    # Weaviate does not have a direct collection.count() method,
    # so we do a count query
    result = client.query.aggregate(class_name).with_meta_count().do()
    count = 0
    try:
        count = result["data"]["Aggregate"][class_name][0]["meta"]["count"]
    except (KeyError, IndexError):
        pass

    print(f"Number of objects in '{class_name}': {count}")

    client.close()


if __name__ == "__main__":
    main()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 80, in <module>
    main()
  File "/code/code.py", line 21, in main
    schema = client.schema.get()
AttributeError: 'WeaviateClient' object has no attribute 'schema'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 8.13s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType

def main():
    # Connect to Weaviate Cloud using environment variables
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    )

    # Check if collection "DemoProducts" exists, if not create it
    if not client.collections.exists("DemoProducts"):
        client.collections.create(
            "DemoProducts",
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            # Use a vectorizer suitable for text properties (optional, recommended)
            vector_config=Configure.Vectors.text2vec_weaviate()
        )

    # Get the collection object
    collection = client.collections.get("DemoProducts")

    # Batch import 50 arbitrary objects
    with collection.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )

    # Fetch the number of objects in the collection
    count = collection.data.count()
    print(f"Number of objects in 'DemoProducts': {count}")

    # Close client connection
    client.close()

if __name__ == "__main__":
    main()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 45, in <module>
    main()
  File "/code/code.py", line 38, in main
    count = collection.data.count()
AttributeError: '_DataCollection' object has no attribute 'count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.45s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Initialize Weaviate client with authentication
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY,
    },
)

# Define the query string
query_text = "dessert wine"

# Perform a vector search using the text2vec-openai vectorizer
result = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({"concepts": [query_text]})
    .with_limit(2)
    .do()
)

# Extract and print results
for wine in result.get("data", {}).get("Get", {}).get("WineReview", []):
    title = wine.get("title")
    country = wine.get("country")
    price = wine.get("price")
    points = wine.get("points")
    print(f"Title: {title}\nCountry: {country}\nPrice: {price}\nPoints: {points}\n")
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

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.04s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    # Load environment variables
    WCD_TEST_URL = os.environ["WCD_TEST_URL"]
    WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

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

    # Query for "dessert wine" with max 2 results
    response = collection.query.near_text(
        query="dessert wine",
        limit=2
    )

    # Print title, country, price, and points for each result
    for obj in response.objects:
        props = obj.properties
        title = props.get("title", "N/A")
        country = props.get("country", "N/A")
        price = props.get("price", "N/A")
        points = props.get("points", "N/A")
        print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")

    client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)), Country: US, Price: 24.0, Points: 88
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast), Country: US, Price: 40.0, Points: 88

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 9.62s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    # Read environment variables
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    openai_api_key = os.environ["OPENAI_API_KEY"]

    # Connect to Weaviate Cloud with API key and OpenAI inference key in headers
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            "X-OpenAI-Api-Key": openai_api_key
        }
    )

    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Perform semantic search with near_text for "dessert wine", limit 2
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the results
    for obj in response.objects:
        props = obj.properties
        print(f"Title: {props.get('title')}")
        print(f"Country: {props.get('country')}")
        print(f"Price: {props.get('price')}")
        print(f"Points: {props.get('points')}")
        print("-" * 40)

    # Close client connection
    client.close()

if __name__ == "__main__":
    main()
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.72s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Initialize Weaviate client with API key authentication
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
)

# Define the query string
query_text = "pair with steak"

# Define the substrings to filter in review_body
substr_filters = ["spice", "fruit", "berry", "cherry", "honey"]

# Build the filter for review_body containing at least one of the substrings
# Using "or" operator with "operator": "Like" (case-insensitive substring match)
review_body_filter = {
    "operator": "Or",
    "operands": [
        {
            "path": ["review_body"],
            "operator": "Like",
            "valueString": f"*{substr}*"
        } for substr in substr_filters
    ]
}

# Build the full filter combining price < 50, points > 90, and review_body substring filter
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
        review_body_filter
    ]
}

# Perform the hybrid query with alpha=0.5 and limit=5
response = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query_text, alpha=0.5)
    .with_limit(5)
    .with_where(where_filter)
    .do()
)

# Extract results
results = response.get("data", {}).get("Get", {}).get("WineReview", [])

# Print the results
for i, wine in enumerate(results, 1):
    title = wine.get("title", "N/A")
    country = wine.get("country", "N/A")
    price = wine.get("price", "N/A")
    points = wine.get("points", "N/A")
    print(f"{i}. Title: {title}\n   Country: {country}\n   Price: {price}\n   Points: {points}\n")
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

**Status**: ✅ SUCCESS (runtime: 11.95s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Read environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

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

# Build the filter:
# price < 50 AND points > 90 AND review_body contains any of the substrings
filter_ = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
)

# Perform the hybrid query
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=filter_,
    return_metadata=MetadataQuery(score=True)
)

# Print the requested fields for each matching wine
for obj in response.objects:
    props = obj.properties
    title = props.get("title", "<no title>")
    country = props.get("country", "<no country>")
    price = props.get("price", "<no price>")
    points = props.get("points", "<no points>")
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")

client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir, Country: US, Price: 40.0, Points: 92
Title: Bink 2014 Pinot Noir (Anderson Valley), Country: US, Price: 49.0, Points: 91
Title: Doña Silvina 2011 Malbec (Mendoza), Country: Argentina, Price: 27.0, Points: 91
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji), Country: Hungary, Price: 25.0, Points: 93
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico), Country: Italy, Price: 0.0, Points: 92

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.62s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter

# Connect to Weaviate Cloud with API key and OpenAI API key in headers
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.AuthApiKey(api_key=os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Build the filter:
# price < 50 AND points > 90 AND review_body contains at least one of the substrings
price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)

# For review_body substrings, use any_of with like filters (wildcard substring match)
review_substrings = ["spice", "fruit", "berry", "cherry", "honey"]
review_filters = [
    Filter.by_property("review_body").like(f"*{substr}*")
    for substr in review_substrings
]
review_filter = Filter.any_of(review_filters)

# Combine all filters with AND
combined_filter = price_filter & points_filter & review_filter

# Perform hybrid search with alpha=0.5, limit=5, with the filter
response = collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    limit=5,
    filters=combined_filter,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for obj in response.objects:
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
    print("-" * 40)

# Close client when done
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
----------------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
----------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
----------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
----------------------------------------
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
----------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### cohere/command-a-03-2025

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 3.89s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import WeaviateClient
from weaviate.util import get_valid_uuid

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client: WeaviateClient = weaviate.connect_to_wcs(
    cluster_url=WCD_TEST_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WCD_TEST_KEY),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY", "")  # Optional: If using OpenAI modules
    }
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready.")
```

**Output**:
```
Weaviate server is ready to accept requests.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 3.53s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Ensure environment variables are set
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.33s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.util import generate_uuid5

# Retrieve environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")

# Initialize the Weaviate client
client = Client(
    url=WEAVIATE_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    additional_headers={"X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")}  # Optional, if using OpenAI
)

# Define the collection name
collection_name = "DemoProducts"

# Check if the collection exists and delete it if it does
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")

# Define the schema for the collection
schema = {
    "classes": [
        {
            "class": collection_name,
            "description": "A collection of demo products",
            "properties": [
                {
                    "name": "name",
                    "dataType": ["text"],
                    "description": "The name of the product"
                },
                {
                    "name": "description",
                    "dataType": ["text"],
                    "description": "The description of the product"
                },
                {
                    "name": "price",
                    "dataType": ["number"],
                    "description": "The price of the product"
                },
                {
                    "name": "in_stock",
                    "dataType": ["boolean"],
                    "description": "Whether the product is in stock"
                }
            ]
        }
    ]
}

# Create the collection with the defined schema
client.collections.create(schema)
print(f"Collection '{collection_name}' created successfully.")
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

**Status**: ❌ FAILURE (runtime: 4.90s)

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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
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

**Status**: ❌ FAILURE (runtime: 5.06s)

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

# Check if the collection exists and delete it if necessary
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the specified properties
client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOLEAN),
    ]
)

# Close the client connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 26, in <module>
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

**Status**: ❌ FAILURE (runtime: 4.80s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.classes.config import Property, DataType
from weaviate.collections.classes.batch import BatchObjectReturn

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

demo_products = client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ],
)

# Prepare batch objects
batch_objects = []
for i in range(50):
    obj = {
        "name": f"Product {i}",
        "description": f"Description {i}",
    }
    batch_objects.append(obj)

# Batch import objects
with demo_products.batch.dynamic() as batch:
    batch.add_objects(batch_objects)

# Print the number of objects in the collection
object_count = demo_products.aggregate.over_all().total_count()
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
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 6.00s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Auth

# Retrieve Weaviate Cloud credentials from environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY", "")  # Optional: for hybrid search
    }
)

# Define the collection schema
collection_name = "DemoProducts"
client.collections.create(
    name=collection_name,
    properties=[
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
    ],
)

# Prepare 50 arbitrary objects for batch import
data_objects = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    }
    for i in range(50)
]

# Batch import objects into the collection
with client.collections.get(collection_name).batch.dynamic() as batch:
    for obj in data_objects:
        batch.add_object(properties=obj)
        if batch.number_errors > 0:
            print(f"Errors occurred during batch import: {batch.errors}")
            break

# Check for failed objects
failed_objects = client.collections.get(collection_name).batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
object_count = client.collections.get(collection_name).aggregate.total()
print(f"Number of objects in {collection_name}: {object_count}")

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

**Status**: ❌ FAILURE (runtime: 6.21s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Client
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.data import DataObject

# Connect to Weaviate Cloud
client = Client(
    url=os.environ["WCD_TEST_URL"],
    auth_client_secret=weaviate.AuthApiKey(os.environ["WCD_TEST_KEY"]),
)

# Create the "DemoProducts" collection
client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ],
    vector_config=Configure.Vectors.text2vec_openai(),  # Optional: Add vectorization
)

# Batch import 50 objects
demo_products = client.collections.get("DemoProducts")
with demo_products.batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}",
            }
        )

# Print the number of objects in the collection
count = demo_products.aggregate.over_all().total_count
print(f"Number of objects in the collection: {count}")

# Close the client
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:8: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 8, in <module>
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.16s)

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
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")  # Pass OpenAI API key
    }
)

# Define the query
query = "dessert wine"

# Perform the hybrid search (combines BM25 and vector search)
response = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    hybrid={
        "query": query,
        "alpha": 0.5  # Balance between vector and keyword search
    },
    limit=2  # Limit to 2 results
)

# Extract and print the results
for result in response["data"]["Get"]["WineReview"]:
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

**Status**: ✅ SUCCESS (runtime: 5.60s)

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
    limit=2,
    return_properties=["title", "country", "price", "points"]  # Specify properties to return
)

# Print the desired properties of each matching wine
for obj in response.objects:
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: {obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 5.93s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import MetadataQuery
from weaviate.classes.config import Configure

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"]),
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
    return_metadata=MetadataQuery(distance=True)
)

# Print the results
for obj in response.objects:
    properties = obj.properties
    print(f"Title: {properties['title']}")
    print(f"Country: {properties['country']}")
    print(f"Price: {properties['price']}")
    print(f"Points: {properties['points']}")
    print(f"Distance: {obj.metadata.distance}\n")

# Close the client
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
Distance: 0.4766477346420288

Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Distance: 0.4812379479408264


```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.59s)

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
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Define the query
query = """
{
  Get {
    WineReview(
      hybrid: { query: "pair with steak", alpha: 0.5 }
      where: {
        operator: And
        path: ["price", "points", "review_body"]
        value: [
          { operator: LessThan, value: 50 },
          { operator: GreaterThan, value: 90 },
          {
            operator: Like
            value: ["spice", "fruit", "berry", "cherry", "honey"]
            operator: Or
          }
        ]
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

# Extract and print results
results = response["data"]["Get"]["WineReview"]
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.82s)

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
        [
            Filter.by_property("price").less_than(50),
            Filter.by_property("points").greater_than(90),
            Filter.by_property("review_body").contains_any(
                ["spice", "fruit", "berry", "cherry", "honey"]
            ),
        ]
    ).as_operator(Filter.Operator.AND),
    return_metadata=True,
)

# Print the results
for obj in response.objects:
    wine = obj.properties
    print(f"Title: {wine['title']}")
    print(f"Country: {wine['country']}")
    print(f"Price: {wine['price']}")
    print(f"Points: {wine['points']}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 40)

# Close the client
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
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

**Status**: ✅ SUCCESS (runtime: 11.12s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import Filter, HybridFusion
from weaviate.classes.config import Configure
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Define the hybrid search query with filters
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    fusion_type=HybridFusion.RELATIVE_SCORE,
    limit=5,
    filters=Filter.by_property("price").less_than(50) &
           Filter.by_property("points").greater_than(90) &
           (Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])),
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: {wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print("---")

# Close the client
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
---
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
---

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### anthropic/claude-sonnet-4-20250514

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 6.06s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=weaviate.auth.AuthApiKey(wcd_key)
)

try:
    # Check if the server is ready
    if client.is_ready():
        print("Weaviate server is ready to accept requests!")
    else:
        print("Weaviate server is not ready.")
        
except Exception as e:
    print(f"Error checking server readiness: {e}")
    
finally:
    # Close the connection
    client.close()
```

**Output**:
```
Weaviate server is ready to accept requests!

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.45s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 8.84s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY"))
)

try:
    # Check if collection exists and delete it if it does
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")
        print("Existing 'DemoProducts' collection deleted.")
    
    # Create the DemoProducts collection with specified properties
    client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL)
        ]
    )
    
    print("'DemoProducts' collection created successfully!")
    
    # Verify the collection was created
    collection = client.collections.get("DemoProducts")
    print(f"Collection '{collection.name}' is ready to use.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Existing 'DemoProducts' collection deleted.
'DemoProducts' collection created successfully!
Collection 'DemoProducts' is ready to use.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 6.68s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Create the collection
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the new collection with the specified properties
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
Deleted existing collection: DemoProducts
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.28s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Check if the collection already exists and delete it if it does
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
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )
    
    print("Collection 'DemoProducts' created successfully with properties:")
    print("- name (text)")
    print("- description (text)")
    print("- price (number)")
    print("- in_stock (boolean)")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted successfully.
Collection 'DemoProducts' created successfully with properties:
- name (text)
- description (text)
- price (number)
- in_stock (boolean)

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 12.08s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.config import Configure

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY"))
)

try:
    # Create the collection with the specified properties
    collection = client.collections.create(
        name="DemoProducts",
        properties=[
            weaviate.classes.config.Property(
                name="name",
                data_type=weaviate.classes.config.DataType.TEXT
            ),
            weaviate.classes.config.Property(
                name="description", 
                data_type=weaviate.classes.config.DataType.TEXT
            )
        ]
    )
    print("Collection 'DemoProducts' created successfully!")
    
    # Get reference to the collection
    demo_products = client.collections.get("DemoProducts")
    
    # Prepare 50 objects for batch import
    objects_to_insert = []
    for i in range(1, 51):
        objects_to_insert.append({
            "name": f"Product {i}",
            "description": f"Description {i}"
        })
    
    # Batch import the objects
    response = demo_products.data.insert_many(objects_to_insert)
    
    # Check for any errors during insertion
    if response.has_errors:
        print("Some objects failed to insert:")
        for error in response.errors:
            print(f"Error: {error}")
    else:
        print(f"Successfully inserted {len(objects_to_insert)} objects!")
    
    # Print the number of objects in the collection
    total_objects = demo_products.aggregate.over_all(total_count=True)
    print(f"Total number of objects in 'DemoProducts' collection: {total_objects.total_count}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
An error occurred: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 12.16s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
)

try:
    # Create the collection if it doesn't exist
    if not client.collections.exists("DemoProducts"):
        client.collections.create(
            name="DemoProducts",
            properties=[
                weaviate.classes.Property(name="name", data_type=weaviate.classes.DataType.TEXT),
                weaviate.classes.Property(name="description", data_type=weaviate.classes.DataType.TEXT),
            ]
        )
        print("Collection 'DemoProducts' created.")
    else:
        print("Collection 'DemoProducts' already exists.")

    # Get the collection
    collection = client.collections.get("DemoProducts")

    # Create 50 arbitrary objects
    data_rows = [
        {
            "name": f"Product {i}",
            "description": f"Description {i}"
        } for i in range(1, 51)
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
    else:
        print("All objects imported successfully!")

    # Print the number of objects in the collection
    print(f"Number of objects in collection: {len(collection)}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists.
All objects imported successfully!
Number of objects in collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.74s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Create the DemoProducts collection with name and description properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    
    # Get the collection
    collection = client.collections.get("DemoProducts")
    
    # Batch import 50 objects using fixed_size batch (recommended approach)
    with collection.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )
    
    # Check for any batch errors
    if collection.batch.failed_objects:
        print(f"Number of failed objects: {len(collection.batch.failed_objects)}")
    
    # Get the total count of objects in the collection
    response = collection.query.fetch_objects(limit=0)  # limit=0 to get count without objects
    total_count = len(list(collection.iterator()))  # Use iterator to get accurate count
    
    print(f"Number of objects in DemoProducts collection: {total_count}")

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
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

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.02s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import MetadataQuery

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

try:
    # Get the WineReview collection
    wine_reviews = client.collections.get("WineReview")
    
    # Perform a vector search for "dessert wine"
    response = wine_reviews.query.near_text(
        query="dessert wine",
        limit=2,
        return_metadata=MetadataQuery(distance=True)
    )
    
    # Print the results
    print(f"Found {len(response.objects)} matching wines:\n")
    
    for i, wine in enumerate(response.objects, 1):
        print(f"Wine {i}:")
        print(f"  Title: {wine.properties.get('title', 'N/A')}")
        print(f"  Country: {wine.properties.get('country', 'N/A')}")
        print(f"  Price: ${wine.properties.get('price', 'N/A')}")
        print(f"  Points: {wine.properties.get('points', 'N/A')}")
        print(f"  Distance: {wine.metadata.distance:.4f}")
        print()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Found 2 matching wines:

Wine 1:
  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: $24.0
  Points: 88
  Distance: 0.4766

Wine 2:
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: $40.0
  Points: 88
  Distance: 0.4812


```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 11.15s)

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

# Query for wines that best match "dessert wine"
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 11.72s)

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
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Required for text2vec-openai vectorizer
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Perform semantic search for "dessert wine" with limit of 2 results
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print the results
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: {wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print("-" * 40)

finally:
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 13.03s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import HybridFusion

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY")),
    headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Perform hybrid search with filters
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        where=weaviate.classes.query.Filter.by_property("price").less_than(50) &
              weaviate.classes.query.Filter.by_property("points").greater_than(90) &
              (weaviate.classes.query.Filter.by_property("review_body").contains_any(["spice"]) |
               weaviate.classes.query.Filter.by_property("review_body").contains_any(["fruit"]) |
               weaviate.classes.query.Filter.by_property("review_body").contains_any(["berry"]) |
               weaviate.classes.query.Filter.by_property("review_body").contains_any(["cherry"]) |
               weaviate.classes.query.Filter.by_property("review_body").contains_any(["honey"]))
    )
    
    # Print results
    print(f"Found {len(response.objects)} matching wines:\n")
    
    for i, wine in enumerate(response.objects, 1):
        print(f"{i}. Title: {wine.properties.get('title', 'N/A')}")
        print(f"   Country: {wine.properties.get('country', 'N/A')}")
        print(f"   Price: ${wine.properties.get('price', 'N/A')}")
        print(f"   Points: {wine.properties.get('points', 'N/A')}")
        print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    client.close()
```

**Output**:
```
An error occurred: hybrid() got an unexpected keyword argument 'where'

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 9.88s)

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
print(f"Found {len(response.objects)} matching wines:\n")

for obj in response.objects:
    properties = obj.properties
    print(f"Title: {properties.get('title', 'N/A')}")
    print(f"Country: {properties.get('country', 'N/A')}")
    print(f"Price: ${properties.get('price', 'N/A')}")
    print(f"Points: {properties.get('points', 'N/A')}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 50)

# Close the connection
client.close()
```

**Output**:
```
Found 5 matching wines:

Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.0
Points: 92
Score: 0.5
--------------------------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Score: 0.3765353560447693
--------------------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.04513849690556526
--------------------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.016171861439943314
--------------------------------------------------
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
Score: 0.0010482011130079627
--------------------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 17.26s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # For text2vec-openai vectorizer
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Perform hybrid search with filters
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Balance between keyword and vector search
        limit=5,
        # Apply filters for price, points, and review_body content
        filters=Filter.all_of([
            # Price must be less than 50
            Filter.by_property("price").less_than(50),
            # Points must be greater than 90
            Filter.by_property("points").greater_than(90),
            # Review body must contain at least one of the specified substrings
            Filter.any_of([
                Filter.by_property("review_body").like("*spice*"),
                Filter.by_property("review_body").like("*fruit*"),
                Filter.by_property("review_body").like("*berry*"),
                Filter.by_property("review_body").like("*cherry*"),
                Filter.by_property("review_body").like("*honey*")
            ])
        ]),
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print the results
    print(f"Found {len(response.objects)} wines that pair well with steak:\n")
    
    for i, wine in enumerate(response.objects, 1):
        props = wine.properties
        print(f"{i}. Title: {props.get('title', 'N/A')}")
        print(f"   Country: {props.get('country', 'N/A')}")
        print(f"   Price: ${props.get('price', 'N/A')}")
        print(f"   Points: {props.get('points', 'N/A')}")
        print()

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Found 5 wines that pair well with steak:

1. Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
   Country: US
   Price: $40.0
   Points: 92

2. Title: Bink 2014 Pinot Noir (Anderson Valley)
   Country: US
   Price: $49.0
   Points: 91

3. Title: Doña Silvina 2011 Malbec (Mendoza)
   Country: Argentina
   Price: $27.0
   Points: 91

4. Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
   Country: Hungary
   Price: $25.0
   Points: 93

5. Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
   Country: Italy
   Price: $0.0
   Points: 92


```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### anthropic/claude-opus-4-20250514

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 12.67s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=AuthApiKey(wcd_key)
)

try:
    # Check if the server is ready
    if client.is_ready():
        print("Weaviate server is ready to accept requests")
    else:
        print("Weaviate server is not ready")
finally:
    # Close the connection
    client.close()
```

**Output**:
```
Weaviate server is ready to accept requests

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 19.22s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Get environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 38.45s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=weaviate.auth.AuthApiKey(wcd_key)
)

try:
    # Check if collection exists and delete it
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")
        print("Existing 'DemoProducts' collection deleted.")
    
    # Create the collection with properties
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
                data_type=DataType.BOOL
            )
        ]
    )
    
    print("Collection 'DemoProducts' created successfully!")
    
    # Verify the collection was created
    collection = client.collections.get("DemoProducts")
    print(f"\nCollection name: {collection.name}")
    print("Properties:")
    for prop in collection.config.get().properties:
        print(f"  - {prop.name}: {prop.data_type}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Existing 'DemoProducts' collection deleted.
Collection 'DemoProducts' created successfully!

Collection name: DemoProducts
Properties:
  - name: text
  - description: text
  - price: number
  - in_stock: boolean

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 18.54s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

try:
    # Create the collection
    collection_name = "DemoProducts"

    # Delete the collection if it already exists (for testing purposes)
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

finally:
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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 33.01s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Check if the collection already exists and delete it if it does
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")
        print("Existing 'DemoProducts' collection deleted.")
    
    # Create the DemoProducts collection with specified properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL)
        ]
    )
    
    print("Collection 'DemoProducts' created successfully!")
    
    # Verify the collection was created
    if client.collections.exists("DemoProducts"):
        print("Collection confirmed to exist.")
        
        # Optional: Get the collection to verify its configuration
        collection = client.collections.get("DemoProducts")
        print(f"Collection name: {collection.name}")

finally:
    # Always close the client connection
    client.close()
```

**Output**:
```
Existing 'DemoProducts' collection deleted.
Collection 'DemoProducts' created successfully!
Collection confirmed to exist.
Collection name: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 28.40s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.data import DataObject

# Get environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=weaviate.auth.AuthApiKey(wcd_key)
)

try:
    # Create or get the collection
    if client.collections.exists("DemoProducts"):
        collection = client.collections.get("DemoProducts")
    else:
        collection = client.collections.create(
            name="DemoProducts",
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT)
            ]
        )
    
    # Prepare batch data
    products = []
    for i in range(50):
        products.append(
            DataObject(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )
        )
    
    # Batch import the objects
    collection.data.insert_many(products)
    
    # Get and print the number of objects in the collection
    response = collection.aggregate.over_all(total_count=True)
    print(f"Number of objects in the collection: {response.total_count}")
    
finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Number of objects in the collection: 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 32.49s)

**Generated Code**:
```python
import weaviate
from weaviate.auth import Auth
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

# Get the collection
collection = client.collections.get("DemoProducts")

# Create 50 product objects
data_rows = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
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

# Check for failed imports
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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 37.48s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Create the DemoProducts collection with properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    
    # Get the collection
    collection = client.collections.get("DemoProducts")
    
    # Batch import 50 products using fixed size batch
    with collection.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )
    
    # Check if there were any errors during batch import
    if collection.batch.failed_objects:
        print(f"Warning: {len(collection.batch.failed_objects)} objects failed to import")
    
    # Get the count of objects in the collection
    # Using aggregate query to count objects
    response = collection.aggregate.over_all(total_count=True)
    
    print(f"Number of objects in the collection: {response.total_count}")
    
finally:
    # Always close the client connection
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
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

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 32.57s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import MetadataQuery
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.auth.AuthApiKey(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Perform near_text search for "dessert wine"
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_metadata=MetadataQuery(distance=True)
    )
    
    # Print the results
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: {wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print(f"Distance: {wine.metadata.distance}")
        print("-" * 50)
        
finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
Distance: 0.476643443107605
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Distance: 0.4812176823616028
--------------------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 26.95s)

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
        "X-OpenAI-API-Key": os.environ["OPENAI_API_KEY"]
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Query for wines that match "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the results
for obj in response.objects:
    print(f"Title: {obj.properties.get('title', 'N/A')}")
    print(f"Country: {obj.properties.get('country', 'N/A')}")
    print(f"Price: {obj.properties.get('price', 'N/A')}")
    print(f"Points: {obj.properties.get('points', 'N/A')}")
    print("-" * 50)

# Close the client connection
client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
--------------------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 35.46s)

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
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Required for text2vec-openai
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Query for dessert wines using semantic search
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2
    )
    
    # Print the results
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: {wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
        print("-" * 50)
        
finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
--------------------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 40.67s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import Filter
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.auth.AuthApiKey(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Perform hybrid search with filters
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        where=(
            Filter.by_property("price").less_than(50) &
            Filter.by_property("points").greater_than(90) &
            (
                Filter.by_property("review_body").contains_any(["spice"]) |
                Filter.by_property("review_body").contains_any(["fruit"]) |
                Filter.by_property("review_body").contains_any(["berry"]) |
                Filter.by_property("review_body").contains_any(["cherry"]) |
                Filter.by_property("review_body").contains_any(["honey"])
            )
        ),
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print results
    print(f"Found {len(response.objects)} wines that pair well with steak:\n")
    
    for i, wine in enumerate(response.objects, 1):
        print(f"{i}. {wine.properties['title']}")
        print(f"   Country: {wine.properties['country']}")
        print(f"   Price: ${wine.properties['price']}")
        print(f"   Points: {wine.properties['points']}")
        print()

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 19, in <module>
    response = wine_collection.query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 41, in run_until_complete
    fut = asyncio.run_coroutine_threadsafe(f(*args, **kwargs), self.loop)
TypeError: hybrid() got an unexpected keyword argument 'where'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 38.16s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-API-Key": os.environ["OPENAI_API_KEY"]
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform hybrid search
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    where=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    ),
    return_metadata=MetadataQuery(score=True)
)

# Print results
for obj in response.objects:
    print(f"Title: {obj.properties.get('title', 'N/A')}")
    print(f"Country: {obj.properties.get('country', 'N/A')}")
    print(f"Price: ${obj.properties.get('price', 'N/A')}")
    print(f"Points: {obj.properties.get('points', 'N/A')}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 50)

# Close the client connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 19, in <module>
    response = collection.query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 41, in run_until_complete
    fut = asyncio.run_coroutine_threadsafe(f(*args, **kwargs), self.loop)
TypeError: hybrid() got an unexpected keyword argument 'where'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 60.83s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # For text2vec-openai vectorizer
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Create filters for price < 50 and points > 90
    price_filter = Filter.by_property("price").less_than(50)
    points_filter = Filter.by_property("points").greater_than(90)
    
    # Create filter for review_body containing at least one of the specified substrings
    # Using wildcard patterns for substring matching
    review_filter = Filter.any_of([
        Filter.by_property("review_body").like("*spice*"),
        Filter.by_property("review_body").like("*fruit*"),
        Filter.by_property("review_body").like("*berry*"),
        Filter.by_property("review_body").like("*cherry*"),
        Filter.by_property("review_body").like("*honey*")
    ])
    
    # Combine all filters
    combined_filter = price_filter & points_filter & review_filter
    
    # Perform hybrid search with alpha=0.5
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Balance between keyword and vector search
        where=combined_filter,
        limit=5,
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print the results
    print(f"Found {len(response.objects)} wines that pair well with steak:\n")
    
    for i, wine in enumerate(response.objects, 1):
        print(f"Wine {i}:")
        print(f"  Title: {wine.properties.get('title', 'N/A')}")
        print(f"  Country: {wine.properties.get('country', 'N/A')}")
        print(f"  Price: ${wine.properties.get('price', 'N/A')}")
        print(f"  Points: {wine.properties.get('points', 'N/A')}")
        print()

finally:
    # Close the client connection
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 37, in <module>
    response = wine_collection.query.hybrid(
  File "/usr/local/lib/python3.9/site-packages/weaviate/syncify.py", line 23, in sync_method
    return _EventLoopSingleton.get_instance().run_until_complete(
  File "/usr/local/lib/python3.9/site-packages/weaviate/event_loop.py", line 41, in run_until_complete
    fut = asyncio.run_coroutine_threadsafe(f(*args, **kwargs), self.loop)
TypeError: hybrid() got an unexpected keyword argument 'where'

```

---

### gemini/gemini-2.5-pro

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 21.19s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey

# 1. Get Weaviate Cloud credentials from environment variables
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("🔴 Error: Make sure WCD_TEST_URL and WCD_TEST_KEY environment variables are set.")
    exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

try:
    # 2. Connect to the Weaviate Cloud instance
    # The 'with' statement ensures the connection is closed automatically
    with weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(wcd_api_key),
    ) as client:
        # 3. Check if the server is ready to accept requests
        is_ready = client.is_ready()

        # 4. Report the status
        if is_ready:
            print("✅ Weaviate server is ready to accept requests.")
        else:
            print("🟡 Weaviate server is NOT ready.")

except Exception as e:
    print(f"🔴 An error occurred during connection: {e}")

```

**Output**:
```
Connecting to Weaviate Cloud at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
✅ Weaviate server is ready to accept requests.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 23.09s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Get Weaviate credentials from environment variables
# WCD_TEST_URL is the URL of your Weaviate Cloud instance
# WCD_TEST_KEY is the API key for your Weaviate Cloud instance
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if the environment variables are set
if not wcd_url or not wcd_api_key:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
else:
    client = None  # Initialize client to ensure it's defined for the finally block
    try:
        # Connect to your Weaviate Cloud instance using the environment variables
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=wcd_url,
            auth_credentials=Auth.api_key(wcd_api_key)
        )

        # Check if the connection is successful and the server is ready.
        # The is_ready() method will return True or raise an exception on failure.
        if client.is_ready():
            print(f"Successfully connected and Weaviate is ready at {wcd_url}")

    except Exception as e:
        print(f"An error occurred during connection: {e}")

    finally:
        # Close the connection to Weaviate
        if client:
            client.close()
            print("Connection to Weaviate closed.")

```

**Output**:
```
Successfully connected and Weaviate is ready at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 30.14s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc
import os

# --- 1. Configuration and Connection ---
# Retrieve connection details from environment variables
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_KEY = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("FATAL: You must set WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

COLLECTION_NAME = "DemoProducts"

# Connect to Weaviate Cloud
# The connect_to_wcs method is a helper for Weaviate Cloud Services
client = weaviate.connect_to_wcs(
    cluster_url=WCD_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WCD_KEY),
)

print("Successfully connected to Weaviate.")

try:
    # --- 2. Delete Collection if it exists ---
    # This is useful for repeatedly running the script to ensure a clean start
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it.")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    # --- 3. Create the Collection ---
    print(f"Creating collection '{COLLECTION_NAME}'...")
    
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        
        # Define the properties of the collection objects
        properties=[
            wvc.config.Property(
                name="name",
                data_type=wvc.config.DataType.TEXT,
                description="The name of the product",
            ),
            wvc.config.Property(
                name="description",
                data_type=wvc.config.DataType.TEXT,
                description="A detailed description of the product",
            ),
            wvc.config.Property(
                name="price",
                data_type=wvc.config.DataType.NUMBER,
                description="The price of the product",
            ),
            wvc.config.Property(
                name="in_stock",
                data_type=wvc.config.DataType.BOOL,
                description="Whether the product is currently in stock",
            ),
        ],

        # Define vectorizer settings.
        # We use a default transformer model from HuggingFace, which is a good
        # starting point if you don't have an OpenAI/Cohere API key.
        # If your instance doesn't have a text2vec module, use:
        # vectorizer_config=wvc.config.Configure.Vectorizer.none()
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_transformers()
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully!")
    
    # You can inspect the created collection configuration
    # config = client.collections.get(COLLECTION_NAME).config.get()
    # print("\nCollection Config:")
    # print(config)

finally:
    # --- 4. Close the connection ---
    # It's a good practice to close the client connection
    client.close()
    print("Connection closed.")

```

**Output**:
```
Successfully connected to Weaviate.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 36, in <module>
    products_collection = client.collections.create(
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
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'vectorizer: no module with name "text2vec-transformers" present'}]}.

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 30.63s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# --- Get Weaviate Cloud credentials from environment variables ---
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_API_KEY = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables not set.")
    sys.exit(1)


client = None  # Initialize client to None
try:
    # --- 1. Connect to Weaviate Cloud ---
    # The client connects to your Weaviate instance using the provided URL and API key.
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_API_KEY)
    )
    print("Successfully connected to Weaviate.")

    collection_name = "DemoProducts"

    # --- 2. Delete the collection if it already exists ---
    # This is useful for running the script multiple times to ensure a clean start.
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # --- 3. Create the collection ---
    # The collection is created with a specific name and a list of properties.
    # Each property has a name and a data type.
    print(f"Creating collection '{collection_name}'...")
    products_collection = client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )

    print(f"\nSuccessfully created collection: '{products_collection.name}'")
    # You can optionally inspect the created collection's configuration
    config = products_collection.config.get()
    print("Collection schema:")
    print(config.properties)


except Exception as e:
    print(f"\nAn error occurred: {e}")

finally:
    # --- 4. Close the connection ---
    # It's important to close the connection to release resources.
    if client:
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate.
Creating collection 'DemoProducts'...

Successfully created collection: 'DemoProducts'
Collection schema:
[_Property(name='name', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='description', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='price', description=None, data_type=<DataType.NUMBER: 'number'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='in_stock', description=None, data_type=<DataType.BOOL: 'boolean'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None)]

Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 14.37s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# This script assumes you have the following environment variables set:
# WCD_TEST_URL: The URL of your Weaviate Cloud instance.
# WCD_TEST_KEY: The API key for your Weaviate Cloud instance.

# Define the collection name
COLLECTION_NAME = "DemoProducts"

try:
    # Connect to Weaviate Cloud
    # For more information, see the Python Client library page: https://www.docs.weaviate.io/weaviate/client-libraries/python
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    )
    print("Successfully connected to Weaviate.")

    # Check if the collection already exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it.")
        # Delete the existing collection
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    # Create the "DemoProducts" collection with specified properties
    # For more information, see the How-to Manage Collections page: https://docs.weaviate.io/weaviate/manage-data/collections
    print(f"Creating collection '{COLLECTION_NAME}'...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully.")
    print("Collection schema:")
    # You can inspect the collection's configuration like this:
    config = products_collection.config.get()
    print(config)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the client is closed
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Client closed.")
```

**Output**:
```
Successfully connected to Weaviate.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Collection schema:
_CollectionConfig(name='DemoProducts', description=None, generative_config=None, inverted_index_config=_InvertedIndexConfig(bm25=_BM25Config(b=0.75, k1=1.2), cleanup_interval_seconds=60, index_null_state=False, index_property_length=False, index_timestamps=False, stopwords=_StopwordsConfig(preset=<StopwordsPreset.EN: 'en'>, additions=None, removals=None)), multi_tenancy_config=_MultiTenancyConfig(enabled=False, auto_tenant_creation=False, auto_tenant_activation=False), properties=[_Property(name='name', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='description', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='price', description=None, data_type=<DataType.NUMBER: 'number'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None), _Property(name='in_stock', description=None, data_type=<DataType.BOOL: 'boolean'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer='none', vectorizer_configs=None)], references=[], replication_config=_ReplicationConfig(factor=1, async_enabled=False, deletion_strategy=<ReplicationDeletionStrategy.NO_AUTOMATED_RESOLUTION: 'NoAutomatedResolution'>), reranker_config=None, sharding_config=_ShardingConfig(virtual_per_physical=128, desired_count=1, actual_count=1, desired_virtual_count=128, actual_virtual_count=128, key='_id', strategy='hash', function='murmur3'), vector_index_config=_VectorIndexConfigHNSW(multi_vector=None, quantizer=None, cleanup_interval_seconds=300, distance_metric=<VectorDistances.COSINE: 'cosine'>, dynamic_ef_min=100, dynamic_ef_max=500, dynamic_ef_factor=8, ef=-1, ef_construction=128, filter_strategy=<VectorFilterStrategy.SWEEPING: 'sweeping'>, flat_search_cutoff=40000, max_connections=32, skip=False, vector_cache_max_objects=1000000000000), vector_index_type=<VectorIndexType.HNSW: 'hnsw'>, vectorizer_config=None, vectorizer=<Vectorizers.NONE: 'none'>, vector_config=None)
Client closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 33.61s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes as wvc

# 1. Get credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"

# Check if the environment variables are set
if not wcd_url or not wcd_api_key:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    exit(1)

# The client is the main entry point to Weaviate
# This code will connect to your Weaviate Cloud (WCS) instance
client = None
try:
    # 2. Connect to Weaviate Cloud
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(wcd_api_key),
    )
    print("Connection successful.")

    # For a clean run, we delete the collection if it already exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it.")
        client.collections.delete(COLLECTION_NAME)

    # 3. Create the "DemoProducts" collection
    print(f"Creating collection '{COLLECTION_NAME}'...")
    products = client.collections.create(
        name=COLLECTION_NAME,
        # Define the properties of the objects in this collection
        properties=[
            wvc.config.Property(name="name", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="description", data_type=wvc.config.DataType.TEXT),
        ],
        # By default, a vectorizer is configured. For this simple example,
        # you can explicitly set it to None if you don't need vectors.
        # If you have a vectorizer module enabled (e.g., text2vec-openai),
        # Weaviate will automatically create vectors for the text properties.
        # vectorizer_config=wvc.config.Configure.Vectorizer.none()
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")


    # 4. Prepare objects for batch import
    print("Preparing 50 objects for batch import...")
    objects_to_add = []
    for i in range(1, 51):  # Create 50 objects
        objects_to_add.append({
            "name": f"Product {i}",
            "description": f"This is the description for product number {i}."
        })

    # 5. Batch import the objects
    print(f"Starting batch import of {len(objects_to_add)} objects...")
    # The `insert_many` method handles batching automatically.
    batch_result = products.data.insert_many(objects_to_add)

    # Check for errors
    if batch_result.has_errors:
        print("There were errors during the batch import:")
        for item in batch_result.errors:
            print(f"  - At index {item['index']}: {item['message']}")
    else:
        print("Batch import completed successfully.")

    # 6. Get and print the number of objects in the collection
    # The aggregate query is the modern way to get counts and other stats
    aggregate_response = products.aggregate.over_all(total_count=True)

    print("-" * 20)
    print(f"Total number of objects in '{COLLECTION_NAME}': {aggregate_response.total_count}")
    print("-" * 20)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 7. Close the connection to Weaviate
    if client:
        client.close()
        print("Connection to Weaviate closed.")

```

**Output**:
```
Connecting to Weaviate Cloud at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
Connection successful.
Collection 'DemoProducts' already exists. Deleting it.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Preparing 50 objects for batch import...
Starting batch import of 50 objects...
Batch import completed successfully.
--------------------
Total number of objects in 'DemoProducts': 50
--------------------
Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 31.96s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc
from weaviate.auth import AuthApiKey
import os
import sys

# --- 1. Get Connection Details from Environment Variables ---
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_API_KEY = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("You must set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    sys.exit(1)

# --- 2. Connect to Weaviate Cloud ---
print(f"Connecting to Weaviate at {WCD_URL}...")
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_URL,
    auth_credentials=AuthApiKey(api_key=WCD_API_KEY),
)

try:
    # Define the collection name
    collection_name = "DemoProducts"

    # --- 3. Recreate the Collection ---
    # To ensure the script is runnable multiple times, we first delete the collection
    # if it already exists.
    if client.collections.exists(collection_name):
        print(f"Deleting existing collection: '{collection_name}'")
        client.collections.delete(collection_name)

    print(f"Creating new collection: '{collection_name}'")
    # Create the collection with the specified properties
    products = client.collections.create(
        name=collection_name,
        properties=[
            wvc.config.Property(name="name", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="description", data_type=wvc.config.DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created successfully.")

    # --- 4. Generate Data for Batch Import ---
    print("Generating 50 objects for import...")
    data_objects = [
        {
            "name": f"Product {i+1}",
            "description": f"This is the description for product number {i+1}."
        }
        for i in range(50)
    ]

    # --- 5. Batch Import the Objects ---
    print("Starting batch import...")
    # Use the collection's batch context manager for efficient importing
    with products.batch.dynamic() as batch:
        for data_obj in data_objects:
            batch.add_object(
                properties=data_obj
            )

    # Check for any errors during the batch import
    if products.batch.failed_objects:
        print(f"Number of failed imports: {len(products.batch.failed_objects)}")
        print(f"First failed object: {products.batch.failed_objects[0].message}")
    else:
        print("Batch import completed successfully.")

    # --- 6. Print the Number of Objects in the Collection ---
    # The modern way to get a count is using the aggregate API
    response = products.aggregate.over_all(total_count=True)

    print("-" * 20)
    print(f"Total number of objects in '{collection_name}': {response.total_count}")
    print("-" * 20)

finally:
    # --- 7. Close the Connection ---
    print("Closing the client connection.")
    client.close()

```

**Output**:
```
Connecting to Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
Deleting existing collection: 'DemoProducts'
Creating new collection: 'DemoProducts'
Collection 'DemoProducts' created successfully.
Generating 50 objects for import...
Starting batch import...
Batch import completed successfully.
--------------------
Total number of objects in 'DemoProducts': 50
--------------------
Closing the client connection.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 18.76s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get Weaviate Cloud connection details from environment variables
# WCD_TEST_URL is the URL of your Weaviate Cloud instance
# WCD_TEST_KEY is the API key for your Weaviate Cloud instance
try:
    url = os.environ["WCD_TEST_URL"]
    api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

# Define the collection name
COLLECTION_NAME = "DemoProducts"

# Connect to Weaviate Cloud
# For more information on client instantiation, see:
# https://weaviate.io/developers/weaviate/client-libraries/python
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=url,
    auth_credentials=Auth.api_key(api_key),
)

print("Client connected to Weaviate Cloud.")

try:
    # 1. Create the collection
    # For more information on collection management, see:
    # https://weaviate.io/developers/weaviate/manage-data/collections
    
    # Clean up previous runs by deleting the collection if it exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Deleting existing collection: {COLLECTION_NAME}")
        client.collections.delete(COLLECTION_NAME)

    print(f"Creating collection: {COLLECTION_NAME}")
    products = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )

    # 2. Batch import 50 objects
    # For more information on batch importing, see:
    # https://weaviate.io/developers/weaviate/manage-data/import
    print("Starting batch import of 50 objects...")

    # Use a context manager for batching. It will automatically send the batch
    # when the batch size is reached or when the context manager exits.
    with products.batch.fixed_size(batch_size=10) as batch:
        for i in range(50):
            product_object = {
                "name": f"Product {i}",
                "description": f"This is the description for product {i}."
            }
            batch.add_object(
                properties=product_object
            )

    print("Batch import completed.")

    # 3. Get the total number of objects in the collection
    # For more information on aggregations, see:
    # https://weaviate.io/developers/weaviate/search/aggregate
    response = products.aggregate.over_all(total_count=True)
    
    # Print the result
    print(f"\nNumber of objects in '{COLLECTION_NAME}': {response.total_count}")

finally:
    # Close the client connection
    client.close()
    print("\nClient connection closed.")
```

**Output**:
```
Client connected to Weaviate Cloud.
Deleting existing collection: DemoProducts
Creating collection: DemoProducts
Starting batch import of 50 objects...
Batch import completed.

Number of objects in 'DemoProducts': 50

Client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 28.63s)

**Generated Code**:
```python
import os
import weaviate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Connection setup ---
# Check for necessary environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

if not all([wcd_url, wcd_key, openai_key]):
    print(
        "Error: Missing environment variables."
        "Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY."
    )
    exit(1)

# The headers are used to pass the OpenAI API key to the text2vec-openai module
# Weaviate will use this key to vectorize the query "dessert wine".
headers = {
    "X-OpenAI-Api-Key": openai_key
}

# Connect to Weaviate Cloud
# The latest client syntax uses `weaviate.connect_to_wcs` for cloud instances
try:
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(api_key=wcd_key),
        headers=headers
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- Query Execution ---
    # Get a reference to the 'WineReview' collection
    reviews = client.collections.get("WineReview")

    # Define the search query
    query_text = "dessert wine"
    print(f"\nSearching for wines similar to: '{query_text}'...")

    # Execute the vector search (near_text) query
    response = reviews.query.near_text(
        query=query_text,
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # --- Print Results ---
    print(f"Found {len(response.objects)} matching wines:\n")

    if not response.objects:
        print("No results found.")
    else:
        for i, wine in enumerate(response.objects):
            # The properties of each object are in the .properties attribute
            properties = wine.properties
            print(f"--- Result {i+1} ---")
            print(f"  Title:   {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            print(f"  Price:   ${properties.get('price'):.2f}" if properties.get('price') else "Price: N/A")
            print(f"  Points:  {properties.get('points')}")
            print("-" * 15 + "\n")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection to Weaviate
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Connection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate Cloud.

Searching for wines similar to: 'dessert wine'...
Found 2 matching wines:

--- Result 1 ---
  Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price:   $24.00
  Points:  88
---------------

--- Result 2 ---
  Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price:   $40.00
  Points:  88
---------------

Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 21.24s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# --- Load environment variables ---
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_API_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit(1)

# Define client and collection name for use in the script
client = None
collection_name = "WineReview"

try:
    # --- Connect to Weaviate Cloud ---
    # The Weaviate client requires the OpenAI API key in the headers
    # to access the text2vec-openai vectorizer module.
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_API_KEY),
        headers={
            "X-OpenAI-API-Key": OPENAI_API_KEY
        }
    )

    print("Successfully connected to Weaviate.")

    # --- Get the collection object ---
    reviews = client.collections.get(collection_name)
    
    query_text = "dessert wine"

    # --- Perform the nearText query ---
    response = reviews.query.near_text(
        query=query_text,
        limit=2
    )

    # --- Print the results ---
    print(f"\nTop {len(response.objects)} results for '{query_text}':\n")

    if not response.objects:
        print("No results found.")
    else:
        for item in response.objects:
            # Access the properties of each returned object
            properties = item.properties
            
            print(f"  Title: {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            
            # Format price nicely, handling cases where it might be missing
            price = properties.get('price')
            price_str = f"${price:.2f}" if price is not None else "N/A"
            print(f"  Price: {price_str}")
            
            print(f"  Points: {properties.get('points')}")
            print("-" * 25)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- Close the connection ---
    # It's good practice to close the connection when you're done.
    if client:
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Output**:
```
Successfully connected to Weaviate.

Top 2 results for 'dessert wine':

  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: $24.00
  Points: 88
-------------------------
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: $40.00
  Points: 88
-------------------------

Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 25.51s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Get environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if all required environment variables are set
if not all([wcd_url, wcd_api_key, openai_api_key]):
    print("Error: Make sure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables are set.")
    exit(1)

try:
    # Connect to your Weaviate Cloud instance
    # The 'with' statement ensures the client is closed automatically
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            # The API key for the vectorizer, in this case text2vec-openai
            "X-OpenAI-Api-Key": openai_api_key,
        }
    ) as client:

        # Get a reference to the WineReview collection
        wine_reviews = client.collections.get("WineReview")

        # Perform a semantic search using near_text for "dessert wine"
        # For more information on semantic search, see: https://weaviate.io/developers/weaviate/search/semantic
        response = wine_reviews.query.near_text(
            query="dessert wine",
            limit=2
        )

        # Print the results
        print("Top 2 wine matches for 'dessert wine':")
        if not response.objects:
            print("No results found.")
        else:
            for item in response.objects:
                # Access the properties of each wine review object
                wine = item.properties
                print(f"\n  - Title: {wine.get('title')}")
                print(f"    Country: {wine.get('country')}")
                
                price = wine.get('price')
                # Format price if it exists
                price_str = f"${price:.2f}" if price is not None else "N/A"
                print(f"    Price: {price_str}")
                
                print(f"    Points: {wine.get('points')}")

except Exception as e:
    print(f"An error occurred: {e}")

```

**Output**:
```
Top 2 wine matches for 'dessert wine':

  - Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
    Country: US
    Price: $24.00
    Points: 88

  - Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
    Country: US
    Price: $40.00
    Points: 88

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 34.27s)

**Generated Code**:
```python
import weaviate
import weaviate.classes.query as wvc # Alias for convenience
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- 1. Get credentials and check for their existence ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not all([wcd_url, wcd_api_key, openai_api_key]):
    print("Error: Missing one or more environment variables.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit()

# --- 2. Connect to Weaviate Cloud ---
try:
    # Use weaviate.auth.AuthApiKey for API key authentication
    auth_config = weaviate.auth.AuthApiKey(api_key=wcd_api_key)

    # Instantiate the client
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=auth_config,
        # Pass the OpenAI API key in the headers for the text2vec-openai vectorizer
        headers={
            "X-OpenAI-Api-Key": openai_api_key
        }
    )
    print("Successfully connected to Weaviate Cloud.")
    print(f"Client is ready: {client.is_ready()}")

    # --- 3. Get a handle to the 'WineReview' collection ---
    reviews = client.collections.get("WineReview")

    # --- 4. Define the filters ---
    # We need to combine multiple conditions using AND (all_of) and OR (any_of)

    # Filter for review_body containing one of the specified substrings.
    # The 'like' operator with wildcards (*) is used for substring matching.
    review_body_filter = wvc.Filter.any_of([
        wvc.Filter.by_property("review_body").like("*spice*"),
        wvc.Filter.by_property("review_body").like("*fruit*"),
        wvc.Filter.by_property("review_body").like("*berry*"),
        wvc.Filter.by_property("review_body").like("*cherry*"),
        wvc.Filter.by_property("review_body").like("*honey*"),
    ])

    # Combine all filters with an AND condition
    combined_filter = wvc.Filter.all_of([
        wvc.Filter.by_property("price").less_than(50),
        wvc.Filter.by_property("points").greater_than(90),
        review_body_filter
    ])


    # --- 5. Execute the hybrid query ---
    print("\nExecuting hybrid query for 'pair with steak'...\n")
    response = reviews.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Equal weight to vector (semantic) and keyword (BM25) search
        limit=5,
        filters=combined_filter,
        # Specify which properties to return for efficiency
        return_properties=["title", "country", "price", "points"]
    )

    # --- 6. Print the results ---
    if not response.objects:
        print("No matching wines found with the specified criteria.")
    else:
        print("Found matching wines:")
        print("--------------------")
        for item in response.objects:
            # Access properties through the .properties attribute
            properties = item.properties
            print(f"  Title: {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            print(f"  Price: ${properties.get('price'):.2f}")
            print(f"  Points: {properties.get('points')}")
            print("--------------------")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- 7. Close the connection ---
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Output**:
```
Successfully connected to Weaviate Cloud.
Client is ready: True

Executing hybrid query for 'pair with steak'...

Found matching wines:
--------------------
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.00
  Points: 92
--------------------
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.00
  Points: 91
--------------------
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.00
  Points: 91
--------------------
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.00
  Points: 93
--------------------
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.00
  Points: 92
--------------------

Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 34.21s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os
import sys

# --- 1. Connect to Weaviate Cloud ---
# Get credentials from environment variables
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
except KeyError:
    print("Error: Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
    sys.exit(1)

try:
    # Connect to your Weaviate instance
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_KEY),
        headers={
            # The 'text2vec-openai' vectorizer requires the OpenAI API key
            "X-OpenAI-API-Key": OPENAI_API_KEY
        },
    )

    # --- 2. Get the 'WineReview' collection ---
    wine_reviews = client.collections.get("WineReview")

    # --- 3. Define the filters for the query ---
    # We combine multiple conditions using the '&' (AND) operator.
    wine_filters = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    )

    # --- 4. Execute the hybrid search query ---
    response = wine_reviews.query.hybrid(
        query="pair with steak",
        limit=5,
        alpha=0.5,  # 0.5 means an equal balance between vector and keyword search
        filters=wine_filters,
    )

    # --- 5. Print the results ---
    print("Found wines that pair with steak (price < 50, points > 90):")
    if not response.objects:
        print("No matching wines found.")
    else:
        for i, item in enumerate(response.objects):
            # Access the properties of each returned object
            properties = item.properties
            print(f"\n--- Result {i+1} ---")
            print(f"  Title: {properties.get('title', 'N/A')}")
            print(f"  Country: {properties.get('country', 'N/A')}")
            
            # Safely get and format the price
            price = properties.get('price')
            if price is not None:
                print(f"  Price: ${price:.2f}")
            else:
                print("  Price: N/A")
            
            print(f"  Points: {properties.get('points', 'N/A')}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- 6. Close the connection ---
    # It's a good practice to close the connection when you're done
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Output**:
```
Found wines that pair with steak (price < 50, points > 90):

--- Result 1 ---
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.00
  Points: 92

--- Result 2 ---
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.00
  Points: 91

--- Result 3 ---
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.00
  Points: 91

--- Result 4 ---
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.00
  Points: 93

--- Result 5 ---
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.00
  Points: 92

Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 27.78s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

# This script performs a hybrid search on a 'WineReview' collection in Weaviate.
# It finds up to 5 wines that are a good match for "pair with steak",
# applying specific filters on price, points, and review content.

# Ensure your environment variables are set before running the script:
# os.environ["WCD_TEST_URL"] = "YOUR_WCD_URL"
# os.environ["WCD_TEST_KEY"] = "YOUR_WCD_API_KEY"
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

try:
    # 1. Connect to Weaviate Cloud
    # The client connects to the Weaviate instance specified by the WCD_TEST_URL
    # and authenticates with the WCD_TEST_KEY.
    # The OpenAI API key is passed in the headers for the text2vec-openai vectorizer.
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WCD_TEST_URL"),
        auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY")),
        headers={
            "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
        }
    )
    print("Successfully connected to Weaviate.")

    # 2. Get the 'WineReview' collection object
    # For more information on collections, see:
    # https://weaviate.io/developers/weaviate/manage-data/collections
    wine_reviews = client.collections.get("WineReview")

    # 3. Define the search filters
    # The query requires multiple conditions to be met. We build a filter for each
    # and then combine them.
    # For more information on filtering, see:
    # https://weaviate.io/developers/weaviate/search/filters

    # Filter for price less than 50
    price_filter = Filter.by_property("price").less_than(50)

    # Filter for points greater than 90
    points_filter = Filter.by_property("points").greater_than(90)

    # Create a list of keyword filters for the review body.
    # The `like` operator with wildcards (*) allows for substring matching.
    keyword_filters = [
        Filter.by_property("review_body").like("*spice*"),
        Filter.by_property("review_body").like("*fruit*"),
        Filter.by_property("review_body").like("*berry*"),
        Filter.by_property("review_body").like("*cherry*"),
        Filter.by_property("review_body").like("*honey*"),
    ]
    # Combine the keyword filters using an OR condition with `Filter.any_of`.
    # This means an object will be included if its review_body matches AT LEAST ONE of these patterns.
    review_body_filter = Filter.any_of(keyword_filters)

    # Combine all individual filters using an AND condition with `Filter.all_of`.
    # An object must satisfy the price, points, AND review body conditions to be returned.
    combined_filter = Filter.all_of([
        price_filter,
        points_filter,
        review_body_filter
    ])

    # 4. Execute the hybrid search query
    # Hybrid search combines vector search (semantic) and keyword search (BM25).
    # The `alpha` parameter balances the two: alpha=0 is pure keyword, alpha=1 is pure vector.
    # For more information on hybrid search, see:
    # https://weaviate.io/developers/weaviate/search/hybrid
    response = wine_reviews.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points"]
    )

    # 5. Print the results
    print("\n--- Query Results ---")
    print("Wines that pair with steak (price < 50, points > 90):")

    if not response.objects:
        print("No matching wines found.")
    else:
        for i, obj in enumerate(response.objects):
            properties = obj.properties
            print(f"\nResult {i+1}:")
            print(f"  Title: {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            print(f"  Price: ${properties.get('price')}")
            print(f"  Points: {properties.get('points')}")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check your environment variables (WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY) and collection name.")

finally:
    # 6. Close the client connection
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate.

--- Query Results ---
Wines that pair with steak (price < 50, points > 90):

Result 1:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.0
  Points: 92

Result 2:
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.0
  Points: 91

Result 3:
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.0
  Points: 91

Result 4:
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.0
  Points: 93

Result 5:
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.0
  Points: 92

Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### gemini/gemini-2.5-flash

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 7.99s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.exceptions import WeaviateConnectionError

print("Attempting to connect to Weaviate Cloud...")

# Retrieve environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

# --- Input Validation ---
if not weaviate_url:
    print("Error: Environment variable WCD_TEST_URL is not set.")
    exit(1)
if not weaviate_api_key:
    print("Error: Environment variable WCD_TEST_KEY is not set.")
    exit(1)

# --- Connect to Weaviate Cloud ---
try:
    # Use the 'with' statement for automatic resource management (closing the connection)
    with weaviate.connect(
        cluster_url=weaviate_url,
        auth_credentials=AuthApiKey(weaviate_api_key)
    ) as client:
        print("\nSuccessfully connected to Weaviate!")

        # --- Check Server Readiness ---
        if client.is_ready():
            print("Weaviate server is ready to accept requests.")
        else:
            print("Weaviate server is NOT ready to accept requests.")

except WeaviateConnectionError as e:
    print(f"\nFailed to connect to Weaviate: {e}")
    print("Please check your WCD_TEST_URL, WCD_TEST_KEY, and network connection.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")

print("\nScript finished.")
```

**Output**:
```
Attempting to connect to Weaviate Cloud...

An unexpected error occurred: 'module' object is not callable

Script finished.

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.48s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve Weaviate Cloud credentials from environment variables
weaviate_cloud_url = os.getenv("WCD_TEST_URL")
weaviate_cloud_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_cloud_url:
    raise ValueError("Environment variable WCD_TEST_URL not set.")
if not weaviate_cloud_key:
    raise ValueError("Environment variable WCD_TEST_KEY not set.")

client = None  # Initialize client to None for the finally block

try:
    # Connect to the Weaviate Cloud instance
    print(f"Attempting to connect to Weaviate Cloud at URL: {weaviate_cloud_url}")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_cloud_url,
        auth_credentials=Auth.api_key(weaviate_cloud_key)
    )

    # Check if the server is ready to accept requests
    if client.is_ready():
        print("Weaviate server is ready to accept requests.")
    else:
        print("Weaviate server is NOT ready.")
        # Optionally, raise an error if not ready
        # raise ConnectionError("Weaviate server did not report as ready.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure your WCD_TEST_URL and WCD_TEST_KEY are correct and the instance is running.")

finally:
    # Always close the client connection
    if client:
        print("Closing Weaviate client connection.")
        client.close()
    else:
        print("Client was not initialized, no connection to close.")

```

**Output**:
```
Attempting to connect to Weaviate Cloud at URL: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Weaviate server is ready to accept requests.
Closing Weaviate client connection.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 12.83s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType, Collection

# --- Configuration ---
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"

# --- Pre-check environment variables ---
if not WEAVIATE_URL or not WEAVIATE_API_KEY:
    print("Error: Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY.")
    print("Example: export WCD_TEST_URL='YOUR_WEAVIATE_CLOUD_URL'")
    print("Example: export WCD_TEST_KEY='YOUR_WEAVIATE_CLOUD_API_KEY'")
    exit(1)

print(f"Attempting to connect to Weaviate at: {WEAVIATE_URL}")

client = None # Initialize client to None for the finally block

try:
    # --- 1. Connect to Weaviate Cloud ---
    client = weaviate.connect_to_wcs(
        url=WEAVIATE_URL,
        auth_credentials=weaviate.classes.Auth.api_key(WEAVIATE_API_KEY),
        # You can add a `timeout_config` here if needed, e.g., (10, 60)
    )
    print("Successfully connected to Weaviate!")

    # --- 2. If the collection already exists, delete it first ---
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to create.")

    # --- 3. Define the collection schema ---
    # Using weaviate.classes.config.Collection for schema definition
    # and weaviate.classes.config.Property for individual properties.
    products_collection_definition = Collection(
        name=COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
        # You can also add vectorizer_config, generatative_config, etc. here if needed.
        # For simplicity, we'll use default vectorizer (text2vec-contextionary or similar based on cloud setup)
        # and no generative module for this example.
    )

    # --- 4. Create the collection ---
    client.collections.create(products_collection_definition)
    print(f"Collection '{COLLECTION_NAME}' created successfully with specified properties.")

    # --- Optional: Verify the collection creation ---
    # You can uncomment this section to inspect the created schema
    # print("\nVerifying collection schema:")
    # collection_object = client.collections.get(COLLECTION_NAME)
    # print(f"Collection Name: {collection_object.name}")
    # print("Properties:")
    # for prop in collection_object.properties:
    #     print(f"  - Name: {prop.name}, DataType: {prop.data_type}")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Weaviate connection error: {e}")
except weaviate.exceptions.WeaviateGRPCError as e:
    print(f"Weaviate gRPC error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- 5. Close the client connection ---
    if client:
        client.close()
        print("Weaviate client connection closed.")

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.classes.config import Property, DataType, Collection
ImportError: cannot import name 'Collection' from 'weaviate.classes.config' (/usr/local/lib/python3.9/site-packages/weaviate/classes/config.py)

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.89s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# 1. Retrieve Weaviate Cloud URL and API key from environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not WCD_TEST_URL:
    print("Error: WCD_TEST_URL environment variable not set.")
    exit(1)
if not WCD_TEST_KEY:
    print("Error: WCD_TEST_KEY environment variable not set.")
    exit(1)

# Connect to the Weaviate Cloud instance
print(f"Connecting to Weaviate Cloud at: {WCD_TEST_URL}")
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY)
    )
    print("Successfully connected to Weaviate Cloud.")
except Exception as e:
    print(f"Failed to connect to Weaviate Cloud: {e}")
    exit(1)

# Define the collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (as per requirement)
print(f"Checking if collection '{collection_name}' already exists...")
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it...")
    try:
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting collection '{collection_name}': {e}")
        client.close()
        exit(1)
else:
    print(f"Collection '{collection_name}' does not exist. Proceeding to create.")

# Define the properties for the collection
properties_to_add = [
    Property(name="name", data_type=DataType.TEXT),
    Property(name="description", data_type=DataType.TEXT),
    Property(name="price", data_type=DataType.NUMBER),
    Property(name="in_stock", data_type=DataType.BOOL),
]

# Create the collection
print(f"Creating collection '{collection_name}' with specified properties...")
try:
    products_collection = client.collections.create(
        name=collection_name, # Use 'name' parameter for collection name
        properties=properties_to_add
    )
    print(f"Collection '{products_collection.name}' created successfully!")
    print("Properties created:")
    for prop in properties_to_add:
        print(f"  - Name: {prop.name}, DataType: {prop.data_type}")

except weaviate.exceptions.WeaviateBaseError as e:
    print(f"Error creating collection: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close connection
    print("Closing Weaviate connection.")
    client.close()

```

**Output**:
```
Connecting to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate Cloud.
Checking if collection 'DemoProducts' already exists...
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted successfully.
Creating collection 'DemoProducts' with specified properties...
Collection 'DemoProducts' created successfully!
Properties created:
An unexpected error occurred: 'Property' object has no attribute 'data_type'
Closing Weaviate connection.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 7.72s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

# Define environment variables (replace with your actual values if not set)
# For demonstration purposes, you might want to uncomment and set them directly
# if running outside an environment where they are pre-configured.
# os.environ["WCD_TEST_URL"] = "YOUR_WEAVIATE_CLOUD_URL"
# os.environ["WCD_TEST_KEY"] = "YOUR_WEAVIATE_API_KEY"

# Ensure the environment variables are set
try:
    WEAVIATE_URL = os.environ["WCD_TEST_URL"]
    WEAVIATE_API_KEY = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY.")
    print("Example: export WCD_TEST_URL='https://YOUR_CLUSTER_URL.weaviate.cloud'")
    print("Example: export WCD_TEST_KEY='YOUR_API_KEY'")
    exit(1)

COLLECTION_NAME = "DemoProducts"

# Connect to Weaviate Cloud using the environment variables
print(f"Connecting to Weaviate Cloud at {WEAVIATE_URL}...")
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
)

try:
    # Check if the collection already exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding to create.")

    # Define the properties for the "DemoProducts" collection
    product_properties = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    # Create the "DemoProducts" collection
    # We will use a default vectorizer (e.g., text2vec-weaviate) which is often
    # suitable for basic text properties if not specified, or you can explicitly
    # configure one if needed. For this example, we'll keep it simple as the
    # prompt didn't specify vectorizer requirements.
    # If a vectorizer is required, add `vector_config=Configure.Vectors.text2vec_weaviate()` or similar.
    client.collections.create(
        name=COLLECTION_NAME,
        properties=product_properties,
        # Optional: You can add a vectorizer here if desired, e.g.:
        # vector_config=Configure.Vectors.text2vec_weaviate(),
        # For a collection focusing on product data, a text-based vectorizer
        # would typically be used on 'name' and 'description' properties.
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully with specified properties.")

    # Verify the creation by listing collections or getting the collection details
    print("\nVerifying collection creation:")
    if client.collections.exists(COLLECTION_NAME):
        collection_obj = client.collections.get(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' exists.")
        print("Properties:")
        # Note: The `properties` attribute of `collection_obj.config` directly gives a list of `Property` objects
        # from which you can extract name and data_type.
        for prop in collection_obj.config.get().properties:
            print(f"- Name: {prop.name}, Data Type: {prop.data_type}")
    else:
        print(f"Failed to find collection '{COLLECTION_NAME}' after creation attempt.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the client connection is closed
    if client.is_connected():
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Collection 'DemoProducts' created successfully with specified properties.

Verifying collection creation:
Collection 'DemoProducts' exists.
Properties:
- Name: name, Data Type: text
- Name: description, Data Type: text
- Name: price, Data Type: number
- Name: in_stock, Data Type: boolean

Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 13.44s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.exceptions import WeaviateCollectionAlreadyExistsError

# --- Configuration ---
WEAVIATE_CLUSTER_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

# --- Validate Environment Variables ---
if not WEAVIATE_CLUSTER_URL:
    print("Error: WCD_TEST_URL environment variable not set.")
    exit(1)
if not WEAVIATE_API_KEY:
    print("Error: WCD_TEST_KEY environment variable not set.")
    exit(1)

print(f"Connecting to Weaviate Cloud at: {WEAVIATE_CLUSTER_URL[:30]}...")

client = None # Initialize client to None for finally block

try:
    # --- Connect to Weaviate Cloud ---
    # The new client syntax uses connect_to_weaviate_cloud for WCD instances
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_CLUSTER_URL,
        api_key=WEAVIATE_API_KEY
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- Define and Create Collection ---
    # Check if the collection already exists and delete it for a clean run
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    print(f"Creating collection '{COLLECTION_NAME}'...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT)
        ],
        # You can add vectorizer_config, generative_config etc. here if needed
        # vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_contextionary(),
        # generative_config=weaviate.classes.config.Configure.Generative.palm()
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # --- Prepare Objects for Batch Import ---
    data_objects_to_import = []
    for i in range(NUM_OBJECTS_TO_IMPORT):
        data_objects_to_import.append({
            "name": f"Product {i + 1}",
            "description": f"This is the description for Product number {i + 1}. It is an arbitrary product for demonstration purposes."
        })

    print(f"Preparing to batch import {len(data_objects_to_import)} objects...")

    # --- Batch Import Objects ---
    # Use insert_many for efficient batch importing
    inserted_uuids = products_collection.data.insert_many(data_objects_to_import)
    print(f"Batch import completed. Inserted {len(inserted_uuids)} objects.")
    # print(f"UUIDs of inserted objects: {inserted_uuids}") # Uncomment to see UUIDs

    # --- Get and Print Number of Objects ---
    # Use the aggregate method to get collection statistics like total count
    aggregate_results = products_collection.query.aggregate()
    total_objects = aggregate_results.total_count

    print(f"\n--- Import Summary ---")
    print(f"Total number of objects in '{COLLECTION_NAME}': {total_objects}")

except WeaviateCollectionAlreadyExistsError:
    print(f"Error: Collection '{COLLECTION_NAME}' already exists and could not be deleted/recreated. "
          "Please ensure the client has necessary permissions or manually delete it.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # --- Close the client connection ---
    if client and client.is_connected():
        client.close()
        print("Weaviate client connection closed.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.exceptions import WeaviateCollectionAlreadyExistsError
ImportError: cannot import name 'WeaviateCollectionAlreadyExistsError' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.04s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.exceptions import WeaviateClosedError

# 1. Get Weaviate Cloud credentials from environment variables
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_URL or not WCD_KEY:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    print("Please set them before running the script.")
    exit(1)

COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

client = None  # Initialize client to None for finally block

try:
    # 2. Connect to Weaviate Cloud
    print(f"Connecting to Weaviate Cloud at: {WCD_URL}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=weaviate.Auth.api_key(WCD_KEY),
    )
    print("Connection successful!")

    # 3. Handle the collection: Delete if it exists, then create it
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    print(f"Creating collection '{COLLECTION_NAME}'...")
    collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            weaviate.CollectionProperty(name="name", data_type=weaviate.config.DataType.TEXT),
            weaviate.CollectionProperty(name="description", data_type=weaviate.config.DataType.TEXT),
        ],
        # Example: Disable vector indexing if not needed for this collection type
        # vectorizer_config=weaviate.collections.classes.config.Configure.Vectorizer.none(),
        # inverted_index_config=weaviate.collections.classes.config.Configure.inverted_index(
        #     bm25_token_weights_for_properties=["name", "description"]
        # )
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # 4. Prepare arbitrary objects for import
    print(f"Preparing {NUM_OBJECTS_TO_IMPORT} objects for import...")
    data_rows = [
        {
            "name": f"Product {i+1}",
            "description": f"This is the description for Product {i+1}. It's a fantastic item!"
        }
        for i in range(NUM_OBJECTS_TO_IMPORT)
    ]

    # 5. Batch import objects
    print(f"Starting batch import of {NUM_OBJECTS_TO_IMPORT} objects...")
    with collection.batch.dynamic() as batch:
        for i, data_row in enumerate(data_rows):
            batch.add_object(
                properties=data_row,
                # You can also add a UUID explicitly if needed, e.g., uuid=generate_uuid_from_string(f"product-{i}")
            )
            if batch.number_errors > 0 and batch.number_errors > NUM_OBJECTS_TO_IMPORT * 0.1: # Stop if more than 10% errors
                print(f"Batch import stopped due to excessive errors ({batch.number_errors} errors).")
                break
        print(f"Batching complete. Number of objects added to batch: {batch.number_objects_added}.")
    
    # Check for failed objects after the batch is processed (context manager handles flushing)
    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"\n--- Batch Import Summary ---")
        print(f"Number of objects successfully imported: {batch.number_objects_added - len(failed_objects)}")
        print(f"Number of failed imports: {len(failed_objects)}")
        if len(failed_objects) > 0:
            print(f"First failed object: {failed_objects[0]}")
    else:
        print(f"\nAll {batch.number_objects_added} objects seem to have been imported successfully.")


    # 6. Print the number of objects in the collection
    print(f"\nRetrieving total count of objects in '{COLLECTION_NAME}'...")
    total_objects = len(collection)
    print(f"Total number of objects in '{COLLECTION_NAME}': {total_objects}")

except WeaviateClosedError as e:
    print(f"Error: The Weaviate client connection was already closed. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # 7. Close the client connection
    if client:
        print("Closing Weaviate client connection...")
        client.close()
        print("Client connection closed.")
    else:
        print("Client was not initialized, no connection to close.")

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 3, in <module>
    from weaviate.exceptions import WeaviateClosedError
ImportError: cannot import name 'WeaviateClosedError' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 16.96s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
import os

# --- Configuration ---
# Connect to Weaviate Cloud using environment variables
# Ensure WCD_TEST_URL and WCD_TEST_KEY are set in your environment
# Example:
# export WCD_TEST_URL="https://YOUR_CLUSTER_URL.weaviate.cloud"
# export WCD_TEST_KEY="YOUR_API_KEY"

try:
    WEAVIATE_URL = os.environ["WCD_TEST_URL"]
    WEAVIATE_API_KEY = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    print("Please set these variables before running the script.")
    print("Example: export WCD_TEST_URL='YOUR_CLUSTER_URL' && export WCD_TEST_KEY='YOUR_API_KEY'")
    exit(1)

COLLECTION_NAME = "DemoProducts"
NUM_OBJECTS_TO_IMPORT = 50

# --- Weaviate Client Connection ---
# Using a context manager ensures the client connection is automatically closed
# when exiting the 'with' block.
with weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
) as client:
    print(f"Connected to Weaviate Cloud at: {WEAVIATE_URL}")

    # --- Collection Management: Create or Recreate Collection ---
    # Check if the collection already exists and delete it to ensure a clean slate
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    print(f"Creating collection '{COLLECTION_NAME}'...")
    client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        # It's good practice to configure a vectorizer for text properties.
        # text2vec-weaviate is a convenient choice for Weaviate Cloud as it's often
        # built-in and doesn't require additional API keys.
        vector_config=Configure.Vectors.text2vec_weaviate()
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # Get a reference to the collection for data operations
    demo_products_collection = client.collections.get(COLLECTION_NAME)

    # --- Data Operations: Batch Import Objects ---
    print(f"Starting batch import of {NUM_OBJECTS_TO_IMPORT} objects into '{COLLECTION_NAME}'...")

    # Using 'fixed_size' batching for efficient data import.
    # The 'batch_size' determines how many objects are sent in one request.
    with demo_products_collection.batch.fixed_size(batch_size=20) as batch:
        for i in range(1, NUM_OBJECTS_TO_IMPORT + 1):
            properties = {
                "name": f"Product {i}",
                "description": f"This is the description for Product {i}. It details its features and benefits."
            }
            batch.add_object(properties=properties)

    print("Batch import process finished.")

    # Check for any errors during the batch import
    if demo_products_collection.batch.failed_objects:
        print(f"WARNING: {len(demo_products_collection.batch.failed_objects)} objects failed to import.")
        for error in demo_products_collection.batch.failed_objects:
            print(f"- {error.message} (Object properties: {error.object_.properties})")
    else:
        print("All objects successfully imported in the batch.")

    # --- Query: Print Number of Objects ---
    print(f"Retrieving the number of objects in '{COLLECTION_NAME}'...")
    try:
        # Use the aggregate API to get collection-level statistics, including total count.
        # `total_count=True` specifically requests the object count.
        results = demo_products_collection.aggregate.over_all(total_count=True)
        object_count = results.total_count
        print(f"\nTotal number of objects in '{COLLECTION_NAME}' collection: {object_count}")
    except Exception as e:
        print(f"An error occurred while trying to get the object count: {e}")

print("Client connection closed automatically.")
```

**Output**:
```
Connected to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 51, in <module>
    vector_config=Configure.Vectors.text2vec_weaviate()
AttributeError: type object 'Configure' has no attribute 'Vectors'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.46s)

**Generated Code**:
```python
import weaviate
import os

# 1. Load environment variables for Weaviate Cloud and OpenAI API Key
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Check if all necessary environment variables are set
if not all([WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY]):
    print("Error: Missing one or more required environment variables.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    print("\nExample (Bash/Zsh):")
    print("export WCD_TEST_URL='YOUR_WEAVIATE_CLUSTER_URL'")
    print("export WCD_TEST_KEY='YOUR_WEAVIATE_API_KEY'")
    print("export OPENAI_API_KEY='YOUR_OPENAI_API_KEY'")
    exit(1)

client = None
try:
    # 2. Connect to Weaviate Cloud
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_wcs(
        cluster_url=WEAVIATE_URL,
        api_key=WEAVIATE_API_KEY,
        # Pass OpenAI API key in headers as required by text2vec-openai vectorizer
        headers={"X-OpenAI-Api-Key": OPENAI_API_KEY}
    )
    print("Successfully connected to Weaviate.")

    # 3. Define the collection and query parameters
    collection_name = "WineReview"
    query_text = "dessert wine"
    limit_results = 2
    # Properties to retrieve from the matching objects
    properties_to_return = ["title", "country", "price", "points"]

    # 4. Get the collection object
    print(f"\nAccessing collection: '{collection_name}'...")
    wine_review_collection = client.collections.get(collection_name)

    # 5. Perform the near_text query
    print(f"Searching for wines best matching '{query_text}' (limit: {limit_results})...")
    response = wine_review_collection.query.near_text(
        query=query_text,
        limit=limit_results,
        return_properties=properties_to_return
    )

    # 6. Process and print the results
    if response.objects:
        print(f"\nFound {len(response.objects)} matching wines:")
        for i, obj in enumerate(response.objects):
            print(f"\n--- Result {i+1} ---")
            print(f"Title: {obj.properties.get('title', 'N/A')}")
            print(f"Country: {obj.properties.get('country', 'N/A')}")
            # Handle cases where 'price' might be None or missing
            price = obj.properties.get('price')
            print(f"Price: ${price:.2f}" if isinstance(price, (int, float)) else "Price: N/A")
            print(f"Points: {obj.properties.get('points', 'N/A')}")
    else:
        print("\nNo matching wines found for the query.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Error connecting to Weaviate: {e}")
except weaviate.exceptions.WeaviateGRPCError as e:
    print(f"Weaviate GRPC error during query: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # 7. Close the Weaviate connection
    if client:
        print("\nClosing Weaviate connection...")
        client.close()
        print("Connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 23, in <module>
    client = weaviate.connect_to_wcs(
TypeError: connect_to_wcs() got an unexpected keyword argument 'api_key'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 66, in <module>
    except weaviate.exceptions.WeaviateGRPCError as e:
AttributeError: module 'weaviate.exceptions' has no attribute 'WeaviateGRPCError'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.89s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# 1. Get Weaviate Cloud and OpenAI API keys from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Ensure all necessary environment variables are set
if not WCD_TEST_URL:
    raise ValueError("WCD_TEST_URL environment variable not set.")
if not WCD_TEST_KEY:
    raise ValueError("WCD_TEST_KEY environment variable not set.")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please set it to your OpenAI API key.")

client = None # Initialize client to None for the finally block

try:
    # 2. Connect to Weaviate Cloud
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-API-Key": OPENAI_API_KEY # Pass OpenAI API key for text2vec-openai vectorizer
        },
    )
    print("Successfully connected to Weaviate.")

    # 3. Get the 'WineReview' collection
    print("Accessing 'WineReview' collection...")
    wine_collection = client.collections.get("WineReview")
    print("Collection 'WineReview' accessed.")

    # 4. Define the query parameters
    query_text = "dessert wine"
    max_results = 2
    # Specify which properties to return for each object
    properties_to_return = ["title", "country", "price", "points"]

    print(f"\nQuerying the 'WineReview' collection for wines matching '{query_text}'...")
    print(f"Limiting results to {max_results} and returning properties: {', '.join(properties_to_return)}.")

    # 5. Perform the near_text query
    response = wine_collection.query.near_text(
        query=query_text,
        limit=max_results,
        return_properties=properties_to_return # Return only specified properties
    )

    # 6. Print the results
    if response.objects:
        print("\n--- Matching Wines ---")
        for i, obj in enumerate(response.objects):
            props = obj.properties # obj.properties will contain only the returned properties
            print(f"\nResult {i+1}:")
            print(f"  Title: {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            
            # Format price if it's a number, otherwise print as is
            price_val = props.get('price')
            if isinstance(price_val, (int, float)):
                print(f"  Price: ${price_val:.2f}")
            else:
                print(f"  Price: {price_val if price_val is not None else 'N/A'}")
            
            print(f"  Points: {props.get('points', 'N/A')}")
            print("-" * 30)
    else:
        print("\nNo matching wines found for your query.")

except Exception as e:
    print(f"\nAn error occurred: {e}")

finally:
    # 7. Close the Weaviate client connection
    if client:
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate.
Accessing 'WineReview' collection...
Collection 'WineReview' accessed.

Querying the 'WineReview' collection for wines matching 'dessert wine'...
Limiting results to 2 and returning properties: title, country, price, points.

--- Matching Wines ---

Result 1:
  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: $24.00
  Points: 88
------------------------------

Result 2:
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: $40.00
  Points: 88
------------------------------

Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 6.21s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType # Not strictly needed for query, but good for context

# 1. Connect to Weaviate Cloud
# The API key for Weaviate Cloud is WCD_TEST_KEY
# The URL for Weaviate Cloud is WCD_TEST_URL
# The OpenAI API key for text2vec-openai is OPENAI_API_KEY
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )

    # 2. Get the 'WineReview' collection
    wine_review_collection = client.collections.get("WineReview")

    # 3. Query the collection for wines matching "dessert wine"
    #    - Use near_text for semantic search.
    #    - Limit the results to 2.
    #    - Return specific properties: title, country, price, points.
    print("Searching for wines that best match 'dessert wine'...")
    response = wine_review_collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # 4. Print the details of each matching wine
    if response.objects:
        print(f"\nFound {len(response.objects)} matching wines:")
        for i, wine in enumerate(response.objects):
            print(f"\n--- Wine {i+1} ---")
            print(f"Title: {wine.properties.get('title', 'N/A')}")
            print(f"Country: {wine.properties.get('country', 'N/A')}")
            print(f"Price: ${wine.properties.get('price', 'N/A')}")
            print(f"Points: {wine.properties.get('points', 'N/A')}")
    else:
        print("\nNo matching wines found.")

except KeyError as e:
    print(f"Error: Environment variable not set. Please ensure {e} is set.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the client connection is closed
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Searching for wines that best match 'dessert wine'...

Found 2 matching wines:

--- Wine 1 ---
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88

--- Wine 2 ---
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88

Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 17.04s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter
from weaviate.auth import AuthApiKey

# Load environment variables
# Ensure these are set in your environment before running the script
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if environment variables are set
if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    raise ValueError(
        "Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables."
        "Example: export WCD_TEST_URL='YOUR_WEAVIATE_CLUSTER_URL'"
        "         export WCD_TEST_KEY='YOUR_WEAVIATE_API_KEY'"
        "         export OPENAI_API_KEY='YOUR_OPENAI_API_KEY'"
    )

client = None  # Initialize client to None for finally block

try:
    # Connect to Weaviate Cloud
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_wcs(
        cluster_url=WCD_TEST_URL,
        auth_credentials=AuthApiKey(WCD_TEST_KEY),
        # Pass OpenAI API key as a header for the text2vec-openai vectorizer
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )
    print("Successfully connected to Weaviate.")

    # Get the WineReview collection object
    wine_review_collection = client.collections.get("WineReview")

    # Define the query parameters
    query_text = "pair with steak"
    limit_results = 5
    properties_to_return = ["title", "country", "price", "points"]

    # Define the filters
    # 1. Price less than 50
    filter_price = Filter.by_property("price").less_than(50)

    # 2. Points greater than 90
    filter_points = Filter.by_property("points").greater_than(90)

    # 3. Review body contains at least one of the specified substrings
    # The 'contains_any' method checks for any of the given strings as substrings.
    filter_review_body = Filter.by_property("review_body").contains_any(
        ["spice", "fruit", "berry", "cherry", "honey"]
    )

    # Combine all filters with AND logic using the & operator
    combined_filter = filter_price & filter_points & filter_review_body

    # Perform the hybrid search
    print(f"\nSearching for wines matching '{query_text}' with hybrid search (alpha=0.5)...")
    print(f"Applying filters: Price < 50, Points > 90, Review contains 'spice', 'fruit', 'berry', 'cherry', or 'honey'.")
    print(f"Maximum {limit_results} results.")

    response = wine_review_collection.query.hybrid(
        query=query_text,
        alpha=0.5,  # 0.5 for balanced hybrid search (keyword + vector)
        filters=combined_filter,
        limit=limit_results,
        return_properties=properties_to_return
    )

    # Process and print the results
    if response.objects:
        print(f"\nFound {len(response.objects)} matching wines:")
        for i, wine in enumerate(response.objects):
            print(f"\n--- Result {i+1} ---")
            print(f"Title: {wine.properties['title']}")
            print(f"Country: {wine.properties['country']}")
            print(f"Price: ${wine.properties['price']:.2f}")
            print(f"Points: {wine.properties['points']}")
    else:
        print("\nNo wines found matching the specified criteria.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the client connection is closed
    if client:
        client.close()
        print("\nWeaviate connection closed.")
```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate.

Searching for wines matching 'pair with steak' with hybrid search (alpha=0.5)...
Applying filters: Price < 50, Points > 90, Review contains 'spice', 'fruit', 'berry', 'cherry', or 'honey'.
Maximum 5 results.

Found 5 matching wines:

--- Result 1 ---
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.00
Points: 92

--- Result 2 ---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.00
Points: 91

--- Result 3 ---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.00
Points: 91

--- Result 4 ---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.00
Points: 93

--- Result 5 ---
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.00
Points: 92

Weaviate connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.91s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# --- 1. Get Weaviate and OpenAI API keys from environment variables ---
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Ensure all required environment variables are set
if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    print("Error: Please set the following environment variables:")
    print("  - WCD_TEST_URL (Weaviate Cloud URL)")
    print("  - WCD_TEST_KEY (Weaviate Cloud API Key)")
    print("  - OPENAI_API_KEY (OpenAI API Key for text2vec-openai vectorizer)")
    exit(1)

client = None  # Initialize client to None for safe cleanup in finally block

try:
    # --- 2. Connect to Weaviate Cloud ---
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-API-Key": OPENAI_API_KEY
        },
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- 3. Get the 'WineReview' collection ---
    # Ensure the collection name matches your Weaviate schema
    collection = client.collections.get("WineReview")
    print(f"Targeting collection: '{collection.name}'")

    # --- 4. Perform the hybrid search query ---
    print("\nSearching for wines that 'pair with steak' under specific criteria...")
    response = collection.query.hybrid(
        query="pair with steak",
        limit=5,  # Limit results to a maximum of 5
        alpha=0.5, # Hybrid search alpha value
        filters=(
            # Price less than 50
            Filter.by_property("price").less_than(50) &
            # Points greater than 90
            Filter.by_property("points").greater_than(90) &
            # Review body contains any of the specified keywords
            Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
        ),
        # Explicitly request only the properties needed for output
        return_properties=["title", "country", "price", "points"]
    )

    # --- 5. Print the results ---
    if response.objects:
        print("\n--- Matching Wines (Top 5 Results) ---")
        for i, obj in enumerate(response.objects):
            props = obj.properties
            print(f"\nResult {i+1}:")
            print(f"  Title: {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price: ${props.get('price', 'N/A')}")
            print(f"  Points: {props.get('points', 'N/A')}")
    else:
        print("\nNo wines found matching all specified criteria.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Error: Could not connect to Weaviate. Check your URL and network. Details: {e}")
except weaviate.exceptions.WeaviateAuthError as e:
    print(f"Error: Authentication failed. Check your Weaviate API key or OpenAI API key. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- 6. Close the Weaviate client connection ---
    if client and client.is_connected():
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate Cloud.
Targeting collection: 'WineReview'

Searching for wines that 'pair with steak' under specific criteria...

--- Matching Wines (Top 5 Results) ---

Result 1:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.0
  Points: 92

Result 2:
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.0
  Points: 91

Result 3:
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.0
  Points: 91

Result 4:
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.0
  Points: 93

Result 5:
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.0
  Points: 92

Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 9.82s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

# Ensure environment variables are set
# Example:
# os.environ['WCD_TEST_URL'] = 'YOUR_WEAVIATE_CLUSTER_URL'
# os.environ['WCD_TEST_KEY'] = 'YOUR_WEAVIATE_API_KEY'
# os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'

# 1. Connect to Weaviate Cloud
client = None
try:
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )
    print("Successfully connected to Weaviate Cloud.")

    # 2. Get the 'WineReview' collection
    wine_collection = client.collections.get("WineReview")
    print("Accessing 'WineReview' collection.")

    # Define the search query
    query_text = "pair with steak"
    limit_results = 5
    hybrid_alpha = 0.5 # Balance between keyword and vector search

    # 3. Define the filters
    # Filter for price less than 50 and points greater than 90
    price_and_points_filter = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90)
    )

    # Filter for review_body containing specific substrings
    review_body_keywords_filter = Filter.any_of(
        filters=[
            Filter.by_property("review_body").like("*spice*"),
            Filter.by_property("review_body").like("*fruit*"),
            Filter.by_property("review_body").like("*berry*"),
            Filter.by_property("review_body").like("*cherry*"),
            Filter.by_property("review_body").like("*honey*")
        ]
    )

    # Combine all filters using logical AND
    combined_filters = price_and_points_filter & review_body_keywords_filter

    print(f"\nSearching for wines matching '{query_text}' with the following criteria:")
    print(f"- Price < 50, Points > 90")
    print(f"- Review body contains 'spice', 'fruit', 'berry', 'cherry', or 'honey'")
    print(f"- Hybrid search (alpha={hybrid_alpha}), max {limit_results} results")

    # 4. Perform the hybrid search with filters and desired return properties
    response = wine_collection.query.hybrid(
        query=query_text,
        alpha=hybrid_alpha,
        limit=limit_results,
        filters=combined_filters,
        return_properties=["title", "country", "price", "points", "review_body"] # Include review_body to verify filter
    )

    # 5. Print the results
    if response.objects:
        print("\n--- Matching Wines ---")
        for i, obj in enumerate(response.objects):
            print(f"\nResult {i+1}:")
            print(f"  Title: {obj.properties.get('title', 'N/A')}")
            print(f"  Country: {obj.properties.get('country', 'N/A')}")
            print(f"  Price: {obj.properties.get('price', 'N/A')}")
            print(f"  Points: {obj.properties.get('points', 'N/A')}")
            # Optional: Print the relevant part of review_body for verification
            # print(f"  Review Body Snippet: {obj.properties.get('review_body', 'N/A')[:150]}...")
    else:
        print("\nNo wines found matching the specified criteria.")

except KeyError as e:
    print(f"Error: Environment variable {e} not set. Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if client:
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate Cloud.
Accessing 'WineReview' collection.

Searching for wines matching 'pair with steak' with the following criteria:
- Price < 50, Points > 90
- Review body contains 'spice', 'fruit', 'berry', 'cherry', or 'honey'
- Hybrid search (alpha=0.5), max 5 results

--- Matching Wines ---

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
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: 0.0
  Points: 92

Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### gemini/gemini-2.5-flash-lite

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 1.90s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud credentials from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise EnvironmentError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
)

# Check if the server is ready
try:
    if client.is_ready():
        print("Weaviate server is ready to accept requests.")
    else:
        print("Weaviate server is not ready.")
except Exception as e:
    print(f"An error occurred while checking server readiness: {e}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:15: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 2.20s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Get the Weaviate Cloud URL and API key from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Check if the environment variables are set
if not cluster_url:
    raise ValueError("WCD_TEST_URL environment variable not set.")
if not api_key:
    raise ValueError("WCD_TEST_KEY environment variable not set.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the client connection
client.close()

print("Successfully connected to Weaviate Cloud and confirmed server readiness.")
```

**Output**:
```
Successfully connected to Weaviate Cloud and confirmed server readiness.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 6.39s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud connection details from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_key = os.environ.get("WCD_TEST_KEY")

if not weaviate_url or not weaviate_key:
    raise EnvironmentError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(weaviate_key),
)

collection_name = "DemoProducts"

# 1. Check if the collection exists and delete it if it does
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it.")
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")
else:
    print(f"Collection '{collection_name}' does not exist.")

# 2. Define the schema for the "DemoProducts" collection
collection_schema = {
    "name": collection_name,
    "properties": [
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
        {"name": "price", "dataType": ["number"]},
        {"name": "in_stock", "dataType": ["boolean"]},
    ],
    "vectorizer": "text2vec-contextionary",  # Or another preferred vectorizer
    "moduleConfig": {
        "text2vec-contextionary": {
            "vectorizer": "text2vec-contextionary",
            "vectorIndexType": "hnsw",
        }
    },
}

# 3. Create the collection
try:
    client.collections.create(collection_schema)
    print(f"Collection '{collection_name}' created successfully.")
except Exception as e:
    print(f"Error creating collection: {e}")

# Optional: Verify the collection creation
if client.collections.exists(collection_name):
    print(f"Verification: Collection '{collection_name}' exists.")
else:
    print(f"Verification: Collection '{collection_name}' does not exist.")

# Optional: Print the schema of the created collection
try:
    schema = client.collections.get(collection_name)
    print(f"\nSchema of '{collection_name}':")
    print(schema)
except Exception as e:
    print(f"Error getting schema for '{collection_name}': {e}")
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

**Status**: ✅ SUCCESS (runtime: 2.91s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Retrieve Weaviate Cloud URL and API key from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Define the collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    print(f"Deleting existing collection: {collection_name}")
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")

# Create the collection with specified properties
print(f"Creating collection: {collection_name}")
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Collection '{products_collection.name}' created successfully.")

# Close connection
client.close()
print("Connection to Weaviate closed.")
```

**Output**:
```
Creating collection: DemoProducts
Collection 'DemoProducts' created successfully.
Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 3.97s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth
import os

# Retrieve Weaviate Cloud URL and API key from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

# Define the collection name
collection_name = "DemoProducts"

# 1. Client Instantiation
# Connect to Weaviate Cloud using environment variables
if WCD_TEST_URL and WCD_TEST_KEY:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
    )
else:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

# Use a try-finally block to ensure the client is closed
try:
    # 2. Collection Management
    # Check if the collection already exists and delete it if it does
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # Create the "DemoProducts" collection with specified properties
    print(f"Creating collection '{collection_name}'...")
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )
    print(f"Collection '{collection_name}' created successfully.")

    # Optional: Verify the collection was created
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' now exists.")
        collection_config = client.collections.get(collection_name).config
        print("Collection configuration:")
        print(f"  Name: {collection_config.name}")
        print("  Properties:")
        for prop in collection_config.properties:
            print(f"    - Name: {prop.name}, Data Type: {prop.data_type}")
    else:
        print(f"Failed to verify creation of collection '{collection_name}'.")

finally:
    # Close the client connection
    client.close()
    print("Weaviate client connection closed.")

```

**Output**:
```
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Collection 'DemoProducts' now exists.
Collection configuration:
Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 50, in <module>
    print(f"  Name: {collection_config.name}")
AttributeError: '_ConfigCollection' object has no attribute 'name'

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 3.73s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud credentials from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

if not weaviate_url or not weaviate_api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
)

# Define the collection schema
class_name = "DemoProducts"
schema = {
    "classes": [
        {
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
    ]
}

# Create the collection if it doesn't exist
if not client.schema.exists(class_name):
    client.schema.create(schema)
    print(f"Collection '{class_name}' created.")
else:
    print(f"Collection '{class_name}' already exists.")

# Generate and batch import 50 arbitrary objects
objects_to_import = []
for i in range(50):
    objects_to_import.append({
        "name": f"Product {i+1}",
        "description": f"This is the description for product {i+1}.",
    })

# Use the batch client for efficient importing
with client.batch.configure(
    batch_size=10,  # Adjust batch size as needed
    # Other potential configurations:
    # dynamic=True, # If properties can change
    # update_frequency=10,
    # alphanumeric_fallback=True,
) as batch:
    for obj in objects_to_import:
        batch.add_object(obj, class_name=class_name)

print(f"Batch imported {len(objects_to_import)} objects into '{class_name}'.")

# Print the number of objects in the collection
try:
    total_objects = client.query.aggregate(class_name).with_total_count().do()
    if total_objects and "data" in total_objects and "Get" in total_objects["data"] and class_name in total_objects["data"]["Get"] and "totalNumberOfObjects" in total_objects["data"]["Get"][class_name]:
        count = total_objects["data"]["Get"][class_name]["totalNumberOfObjects"]
        print(f"Number of objects in '{class_name}': {count}")
    else:
        print(f"Could not retrieve the total number of objects in '{class_name}'. The result was: {total_objects}")
except Exception as e:
    print(f"An error occurred while fetching the object count: {e}")

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

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 3.63s)

**Generated Code**:
```python
import weaviate
import os

# Get Weaviate Cloud credentials from environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise EnvironmentError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to Weaviate Cloud
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=weaviate.Auth.api_key(WCD_TEST_KEY),
    )
except Exception as e:
    print(f"Error connecting to Weaviate Cloud: {e}")
    exit()

collection_name = "DemoProducts"

# Check if the collection exists, create it if not
try:
    if not client.collections.exists(collection_name):
        client.collections.create(
            collection_name,
            properties=[
                weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
                weaviate.Property(name="description", data_type=weaviate.DataType.TEXT),
            ],
        )
        print(f"Collection '{collection_name}' created.")
    else:
        print(f"Collection '{collection_name}' already exists.")
except Exception as e:
    print(f"Error creating or checking collection: {e}")
    client.close()
    exit()

# Get the collection
try:
    collection = client.collections.get(collection_name)
except Exception as e:
    print(f"Error getting collection '{collection_name}': {e}")
    client.close()
    exit()

# Generate 50 arbitrary objects
data_rows = [
    {"name": f"Product {i+1}", "description": f"This is a description for Product {i+1}"}
    for i in range(50)
]

# Batch import objects
print("Starting batch import of 50 objects...")
try:
    with collection.batch.dynamic() as batch:
        for data_row in data_rows:
            batch.add_object(
                properties=data_row,
            )
            # Optional: Add a check for errors to stop early if needed
            # if batch.number_errors > 10:
            #     print("Batch import stopped due to excessive errors.")
            #     break
    print("Batch import completed.")

    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        # Print the first failed object if any
        if failed_objects:
            print(f"First failed object: {failed_objects[0]}")
except Exception as e:
    print(f"An error occurred during batch import: {e}")


# Print the number of objects in the collection
try:
    num_objects = len(collection)
    print(f"Number of objects in the '{collection_name}' collection: {num_objects}")
except Exception as e:
    print(f"Error getting the count of objects: {e}")

# Close the client connection
client.close()
print("Weaviate client connection closed.")
```

**Output**:
```
Error connecting to Weaviate Cloud: module weaviate has no attribute Auth

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 3.31s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud using environment variables
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    )
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL and WCD_TEST_KEY to connect to Weaviate Cloud.")
    exit()

collection_name = "DemoProducts"

# Define the collection schema
client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# Get the collection object
collection = client.collections.get(collection_name)

# Batch import 50 arbitrary objects
batch_size = 50
objects_to_import = []
for i in range(batch_size):
    objects_to_import.append(
        {
            "name": f"Product {i}",
            "description": f"Description for product {i}"
        }
    )

# Use the batch.add_objects method for efficient batch import
# The fixed_size batcher is generally recommended for predictable performance
with collection.batch.fixed_size(batch_size=batch_size) as batch:
    for obj_data in objects_to_import:
        batch.add_object(properties=obj_data)

# Print the number of objects in the collection
count_response = client.query.aggregate(collection_name).with_fields("totalNumberOfObjects").do()
total_objects = count_response["data"]["Aggregate"][collection_name][0]["totalNumberOfObjects"]

print(f"Number of objects in the '{collection_name}' collection: {total_objects}")

# Close the client connection
client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
Traceback (most recent call last):
  File "/code/code.py", line 20, in <module>
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

**Status**: ❌ FAILURE (runtime: 8.55s)

**Generated Code**:
```python
import os
import weaviate

def query_wine_reviews():
    """
    Queries the 'WineReview' collection in Weaviate for dessert wines
    and prints the details of the best matching results.
    """

    # Get Weaviate Cloud connection details from environment variables
    weaviate_url = os.environ.get("WCD_TEST_URL")
    weaviate_api_key = os.environ.get("WCD_TEST_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    if not all([weaviate_url, weaviate_api_key, openai_api_key]):
        print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
        return

    # Initialize Weaviate client
    client = weaviate.Client(
        url=weaviate_url,
        auth_client_secret=weaviate.AuthApiKey(weaviate_api_key),
        additional_headers={
            "X-OpenAI-Api-Key": openai_api_key,
        }
    )

    # Define the query and the collection name
    query_text = "dessert wine"
    collection_name = "WineReview"

    try:
        # Build the GraphQL query
        response = (
            client.query
            .get(collection_name, ["title", "country", "price", "points"])
            .with_near_text({"concepts": [query_text]})
            .with_limit(2)
            .do()
        )

        # Process and print the results
        if "data" in response and "Get" in response["data"] and collection_name in response["data"]["Get"]:
            wines = response["data"]["Get"][collection_name]
            if wines:
                print(f"Top {len(wines)} wines matching '{query_text}':\n")
                for wine in wines:
                    print(f"Title: {wine.get('title', 'N/A')}")
                    print(f"Country: {wine.get('country', 'N/A')}")
                    print(f"Price: {wine.get('price', 'N/A')}")
                    print(f"Points: {wine.get('points', 'N/A')}")
                    print("-" * 20)
            else:
                print(f"No wines found matching '{query_text}'.")
        else:
            print("Error: Unexpected response format from Weaviate.")
            print(response)

    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print(f"An error occurred: {e}")
        print("Please ensure the collection 'WineReview' exists and is configured with text2vec-openai.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    query_wine_reviews()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:20: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 66, in <module>
    query_wine_reviews()
  File "/code/code.py", line 20, in query_wine_reviews
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.70s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Retrieve Weaviate Cloud connection details from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

# Retrieve OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Check if all required environment variables are set
if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    raise ValueError("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")

try:
    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-API-Key": OPENAI_API_KEY
        },
    )

    # Get the 'WineReview' collection
    collection = client.collections.get("WineReview")

    # Query the collection for wines that best match "dessert wine"
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        # Specify which properties to retrieve in the response
        include_vector=False,  # We don't need the vector for this query
        return_properties=["title", "country", "price", "points"],
    )

    # Print the title, country, price, and points of each matching wine
    if response.objects:
        print("Matching wines:")
        for obj in response.objects:
            print(f"- Title: {obj.properties.get('title')}")
            print(f"  Country: {obj.properties.get('country')}")
            print(f"  Price: {obj.properties.get('price')}")
            print(f"  Points: {obj.properties.get('points')}")
    else:
        print("No matching wines found.")

except weaviate.UnexpectedStatusCodeException as e:
    print(f"Weaviate client error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the client connection
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Weaviate client connection closed.")
```

**Output**:
```
Matching wines:
- Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: 24.0
  Points: 88
- Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: 40.0
  Points: 88
Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 2.96s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import Query  # Import Query explicitly if needed for type hinting, though not strictly necessary here
import os

# Connect to Weaviate Cloud
# Ensure WCD_TEST_URL and WCD_TEST_KEY environment variables are set
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        # Inject the OpenAI API key for the text2vec-openai vectorizer
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Define the query and limit
search_query = "dessert wine"
max_results = 2

# Get the 'WineReview' collection
wine_reviews_collection = client.collections.get("WineReview")

# Perform a semantic search
# The text2vec-openai vectorizer will be used to generate embeddings for the search query
response = wine_reviews_collection.query.near_text(
    query=search_query,
    limit=max_results,
    # Specify which properties to return for each matching wine
    return_properties=["title", "country", "price", "points"]
)

# Print the results
if response.objects:
    print(f"Found {len(response.objects)} wines matching '{search_query}':\n")
    for wine in response.objects:
        properties = wine.properties
        print(f"Title: {properties.get('title', 'N/A')}")
        print(f"Country: {properties.get('country', 'N/A')}")
        print(f"Price: {properties.get('price', 'N/A')}")
        print(f"Points: {properties.get('points', 'N/A')}")
        print("-" * 20)
else:
    print(f"No wines found matching '{search_query}'.")

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 2, in <module>
    from weaviate.classes.query import Query  # Import Query explicitly if needed for type hinting, though not strictly necessary here
ImportError: cannot import name 'Query' from 'weaviate.classes.query' (/usr/local/lib/python3.9/site-packages/weaviate/classes/query.py)

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 3.27s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud connection details from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not all([weaviate_url, weaviate_key, openai_api_key]):
    raise ValueError(
        "Please set the following environment variables: "
        "WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY"
    )

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(weaviate_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key,
    },
)

# Define the query
query_text = "pair with steak"
limit = 5
alpha = 0.5

# Construct the GraphQL query
# We use a hybrid search with the query text and specify the `bm25` and `vector` searches.
# The `alpha` parameter controls the weighting between BM25 and vector search.
# We also apply filters for price and points, and a where filter for substrings in the review_body.
graphql_query = {
    "query": """
    {
      Get {
        WineReview(
          limit: %d,
          hybrid: {
            query: "%s",
            alpha: %.1f
          },
          where: {
            and: [
              {
                path: ["price"],
                operator: LessThan,
                value_number: 50
              },
              {
                path: ["points"],
                operator: GreaterThan,
                value_number: 90
              },
              {
                operator: Or,
                operands: [
                  {
                    path: ["review_body"],
                    operator: ContainsAny,
                    valueText: ["spice"]
                  },
                  {
                    path: ["review_body"],
                    operator: ContainsAny,
                    valueText: ["fruit"]
                  },
                  {
                    path: ["review_body"],
                    operator: ContainsAny,
                    valueText: ["berry"]
                  },
                  {
                    path: ["review_body"],
                    operator: ContainsAny,
                    valueText: ["cherry"]
                  },
                  {
                    path: ["review_body"],
                    operator: ContainsAny,
                    valueText: ["honey"]
                  }
                ]
              }
            ]
          }
        ) {
          title
          country
          price
          points
          review_body
        }
      }
    }
    """ % (limit, query_text, alpha)
}

# Execute the query
try:
    result = client.query.raw(graphql_query)

    # Print the results
    if "data" in result and "Get" in result["data"] and "WineReview" in result["data"]["Get"]:
        wines = result["data"]["Get"]["WineReview"]
        if wines:
            print(f"Found {len(wines)} wines matching your criteria:")
            for wine in wines:
                print(f"- Title: {wine['title']}, Country: {wine['country']}, Price: ${wine['price']}, Points: {wine['points']}")
        else:
            print("No wines found matching your criteria.")
    else:
        print("An error occurred during the query execution.")
        print(result)

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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.62s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Retrieve credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not all([cluster_url, api_key, openai_api_key]):
    raise ValueError("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")

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

# Define the hybrid search query
query_text = "pair with steak"
max_results = 5
alpha_value = 0.5

# Perform the hybrid search with filters
response = collection.query.hybrid(
    query=query_text,
    limit=max_results,
    alpha=alpha_value,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    ),
    # Request specific properties to be returned
    return_properties=["title", "country", "price", "points"]
)

# Print the results
if response.objects:
    for obj in response.objects:
        print(f"Title: {obj.properties['title']}")
        print(f"Country: {obj.properties['country']}")
        print(f"Price: {obj.properties['price']}")
        print(f"Points: {obj.properties['points']}")
        # Optionally print the score if you included return_metadata=MetadataQuery(score=True)
        # print(f"Score: {obj.metadata.score}")
        print("-" * 20)
else:
    print("No matching wines found.")

# Close the client connection
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
--------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
--------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
--------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
--------------------
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
--------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 4.56s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import Filter, HybridFusion
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud using environment variables
# WCD_TEST_URL should be set to your Weaviate Cloud instance URL
# WCD_TEST_KEY should be set to your Weaviate API key
# OPENAI_API_KEY should be set to your OpenAI API key
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_reviews = client.collections.get("WineReview")

# Define the search query and filters
query = "pair with steak"
max_results = 5
alpha_value = 0.5
keywords_to_check = ["spice", "fruit", "berry", "cherry", "honey"]

# Construct the filter for review_body
# This filter checks if the review_body contains at least one of the specified keywords
review_body_filter = Filter.by_property("review_body").contains_any(keywords_to_check)

# Perform the hybrid search
response = wine_reviews.query.hybrid(
    query=query,
    alpha=alpha_value,
    limit=max_results,
    filters=Filter.all_of([
        Filter.by_property("price").less_than(50),
        Filter.by_property("points").greater_than(90),
        review_body_filter  # Add the review_body keyword filter
    ]),
    return_properties=["title", "country", "price", "points", "review_body"]
)

# Print the results
if response.objects:
    print(f"Found {len(response.objects)} wines matching your query:")
    for wine in response.objects:
        properties = wine.properties
        print(f"  Title: {properties['title']}")
        print(f"  Country: {properties['country']}")
        print(f"  Price: ${properties['price']}")
        print(f"  Points: {properties['points']}")
        print("-" * 20)
else:
    print("No wines found matching your criteria.")

# Close the client connection
client.close()
```

**Output**:
```
Found 5 wines matching your query:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.0
  Points: 92
--------------------
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.0
  Points: 91
--------------------
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.0
  Points: 91
--------------------
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.0
  Points: 93
--------------------
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.0
  Points: 92
--------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### openai/gpt-5-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 22.80s)

**Generated Code**:
```python

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 10.17s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

assert client.is_ready()

client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 29.71s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure

WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

with weaviate.connect_to_wcs(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
) as client:
    # Delete the collection if it already exists
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the collection with the requested properties
    client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
        # Use no vectorizer to avoid requiring any embedding module
        vectorizer_config=Configure.Vectorizer.none(),
    )

    print("Collection 'DemoProducts' created successfully.")
```

**Output**:
```
Collection 'DemoProducts' created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 17.48s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    cluster_url = os.getenv("WCD_TEST_URL")
    api_key = os.getenv("WCD_TEST_KEY")

    if not cluster_url or not api_key:
        raise EnvironmentError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key),
    )

    try:
        collection_name = "DemoProducts"

        # Delete the collection if it already exists
        if client.collections.exists(collection_name):
            client.collections.delete(collection_name)

        # Create the collection
        products_collection = client.collections.create(
            collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
                Property(name="price", data_type=DataType.NUMBER),
                Property(name="in_stock", data_type=DataType.BOOL),
            ],
        )

        print(f"Created collection: {products_collection.name}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 20.52s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

try:
    # Delete the collection if it already exists
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the collection
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
        # Use the built-in Weaviate vectorizer (no external API key required)
        vector_config=Configure.Vectors.text2vec_weaviate(),
    )
finally:
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 26, in <module>
    vector_config=Configure.Vectors.text2vec_weaviate(),
AttributeError: type object 'Configure' has no attribute 'Vectors'

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 28.67s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 20.09s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 35.10s)

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

try:
    # Create the collection if it doesn't exist
    if not client.collections.exists("DemoProducts"):
        client.collections.create(
            name="DemoProducts",
            vector_config=Configure.Vectors.text2vec_weaviate(),  # Works in Weaviate Cloud without 3rd-party API keys
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
        )

    # Get the collection
    products = client.collections.get("DemoProducts")

    # Batch import 50 objects
    with products.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}",
                }
            )

    # Print the number of objects in the collection
    agg = products.aggregate.over_all(total_count=True)
    print(agg.total_count)

finally:
    client.close()
```

**Output**:
```
50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 18.32s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

def main():
    client = weaviate.connect_to_wcs(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=AuthApiKey(os.environ["WCD_TEST_KEY"]),
        headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
    )

    try:
        collection = client.collections.get("WineReview")

        result = collection.query.near_text(
            query="dessert wine",
            limit=2,
            return_properties=["title", "country", "price", "points"],
        )

        for obj in result.objects or []:
            props = obj.properties or {}
            print(f"Title: {props.get('title')}")
            print(f"Country: {props.get('country')}")
            print(f"Price: {props.get('price')}")
            print(f"Points: {props.get('points')}")
            print("-" * 40)
    finally:
        client.close()

if __name__ == "__main__":
    main()
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.92s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Read environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_key = os.getenv("WCD_TEST_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key),
    headers={
        "X-OpenAI-API-Key": openai_key,
    },
)

# Get the collection
collection = client.collections.get("WineReview")

# Query for best matches to "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2,
)

# Print requested properties
for obj in response.objects:
    props = obj.properties or {}
    print(f"Title: {props.get('title')}, Country: {props.get('country')}, Price: {props.get('price')}, Points: {props.get('points')}")

client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)), Country: US, Price: 24.0, Points: 88
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast), Country: US, Price: 40.0, Points: 88

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 24.82s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud with OpenAI vectorizer key
with weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
) as client:
    collection = client.collections.get("WineReview")

    # Semantic search for "dessert wine" with max 2 results
    resp = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"],
    )

    # Print desired fields
    for obj in resp.objects:
        props = obj.properties or {}
        print(f"Title: {props.get('title')}")
        print(f"Country: {props.get('country')}")
        print(f"Price: {props.get('price')}")
        print(f"Points: {props.get('points')}")
        print()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88

Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88


```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 25.18s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 21.76s)

**Generated Code**:
```python

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 29.57s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

# Connect to Weaviate Cloud with OpenAI key for text2vec-openai
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    collection = client.collections.get("WineReview")

    # Build filters:
    # - price < 50
    # - points > 90
    # - review_body contains any of the substrings: spice, fruit, berry, cherry, honey
    text_filter = Filter.any_of(
        filters=[
            Filter.by_property("review_body").like("*spice*"),
            Filter.by_property("review_body").like("*fruit*"),
            Filter.by_property("review_body").like("*berry*"),
            Filter.by_property("review_body").like("*cherry*"),
            Filter.by_property("review_body").like("*honey*"),
        ]
    )
    numeric_filter = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90)
    )
    combined_filters = numeric_filter & text_filter

    # Hybrid search
    resp = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=combined_filters,
        return_properties=["title", "country", "price", "points"],
    )

    # Print results
    for obj in resp.objects:
        p = obj.properties
        print(f"{p.get('title')} | {p.get('country')} | ${p.get('price')} | {p.get('points')} pts")

finally:
    client.close()
```

**Output**:
```
Soléna 2009 Guadalupe Vineyard Pinot Noir | US | $40.0 | 92 pts
Bink 2014 Pinot Noir (Anderson Valley) | US | $49.0 | 91 pts
Doña Silvina 2011 Malbec (Mendoza) | Argentina | $27.0 | 91 pts
Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji) | Hungary | $25.0 | 93 pts
Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico) | Italy | $0.0 | 92 pts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### openai/gpt-5-mini-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 9.92s)

**Generated Code**:
```python
import os
import weaviate

# Read environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise RuntimeError("Both WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

# Create client for Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
)

# Check that the server is ready to accept requests
if client.is_ready():
    print("Weaviate server is ready.")
else:
    raise RuntimeError("Weaviate server is not ready.")
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

**Status**: ❌ FAILURE (runtime: 8.49s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Read credentials from environment
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise RuntimeError("Both WCD_TEST_URL and WCD_TEST_KEY environment variables must be set")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(api_key=WCD_TEST_KEY)
)

# Check that the server is ready to accept requests
assert client.is_ready(), "Weaviate server is not ready"

# Close the client
client.close()
```

**Errors**:
```
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

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 15.58s)

**Generated Code**:
```python
import os
import sys
import weaviate

def main():
    # Read env vars
    url = os.getenv("WCD_TEST_URL")
    api_key = os.getenv("WCD_TEST_KEY")
    if not url or not api_key:
        sys.exit("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables")

    # Connect to Weaviate Cloud
    client = weaviate.Client(
        url=url,
        auth_client_secret=weaviate.AuthApiKey(api_key),
    )

    # Optional: ensure the instance is reachable
    if not client.is_ready():
        sys.exit("Weaviate instance is not ready / reachable")

    class_name = "DemoProducts"

    # If the class exists, delete it first
    schema = client.schema.get()
    existing = [c.get("class") for c in schema.get("classes", [])]
    if class_name in existing:
        client.schema.delete_class(class_name)
        print(f"Deleted existing class '{class_name}'")

    # Define the class schema
    class_schema = {
        "class": class_name,
        "properties": [
            {"name": "name", "dataType": ["text"]},
            {"name": "description", "dataType": ["text"]},
            {"name": "price", "dataType": ["number"]},
            {"name": "in_stock", "dataType": ["boolean"]},
        ],
        # Use "none" if you don't rely on a vectorizer module for this class.
        # Change to an available vectorizer module name if you want automatic vectorization.
        "vectorizer": "none",
    }

    # Create the class
    client.schema.create_class(class_schema)
    print(f"Created class '{class_name}' with properties: name, description, price, in_stock")

if __name__ == "__main__":
    main()
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
  File "/code/code.py", line 50, in <module>
    main()
  File "/code/code.py", line 13, in main
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 21.06s)

**Generated Code**:
```python
import os
import sys
import weaviate

# Read connection info from environment
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.", file=sys.stderr)
    sys.exit(1)

# Connect to Weaviate Cloud using API key auth
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=WCD_TEST_KEY),
)

collection_name = "DemoProducts"

# If the collection (class) already exists, delete it first
schema = client.schema.get()
existing_classes = {c.get("class") for c in schema.get("classes", [])}
if collection_name in existing_classes:
    client.schema.delete_class(collection_name)
    print(f"Deleted existing collection/class: {collection_name}")

# Define the class (collection) schema
demo_products_class = {
    "class": collection_name,
    "properties": [
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
        {"name": "price", "dataType": ["number"]},
        {"name": "in_stock", "dataType": ["boolean"]},
    ],
}

# Create the class
client.schema.create_class(demo_products_class)
print(f"Created collection/class: {collection_name}")

# Close connection
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

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 14.10s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

def main():
    # Read connection info from environment
    cluster_url = os.environ["WCD_TEST_URL"]
    api_key = os.environ["WCD_TEST_KEY"]

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key)
    )

    try:
        collection_name = "DemoProducts"

        # If the collection exists, delete it first
        if client.collections.exists(collection_name):
            print(f"Collection '{collection_name}' exists — deleting it...")
            client.collections.delete(collection_name)
            print("Deleted.")

        # Define properties
        properties = [
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]

        # Create the collection
        client.collections.create(
            collection_name,
            properties=properties
        )

        print(f"Collection '{collection_name}' created with properties: name, description, price, in_stock")

    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection 'DemoProducts' exists — deleting it...
Deleted.
Collection 'DemoProducts' created with properties: name, description, price, in_stock

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 23.31s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 19.15s)

**Generated Code**:
```python
import os
import sys
import weaviate

# Read environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    sys.exit(1)

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
)

try:
    # Get the collection (class) named "DemoProducts"
    collection = client.collections.get("DemoProducts")

    # Prepare 50 objects
    data_rows = [
        {"name": f"Product {i+1}", "description": f"Description {i+1}"}
        for i in range(50)
    ]

    # Batch import
    with collection.batch.dynamic() as batch:
        for data_row in data_rows:
            batch.add_object(properties=data_row)
            # optional safety: stop if too many errors
            if batch.number_errors > 10:
                print("Batch import stopped due to excessive errors.")
                break

    # Report failed objects, if any
    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        print("First failed object:", failed_objects[0])

    # Print total number of objects in the collection
    print("Total objects in 'DemoProducts':", len(collection))

finally:
    client.close()
```

**Output**:
```
Total objects in 'DemoProducts': 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 16.80s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

def main():
    # Read cloud credentials from environment
    wc_url = os.environ.get("WCD_TEST_URL")
    wc_key = os.environ.get("WCD_TEST_KEY")
    if not wc_url or not wc_key:
        raise RuntimeError("Set WCD_TEST_URL and WCD_TEST_KEY environment variables")

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wc_url,
        auth_credentials=Auth.api_key(wc_key)
    )

    try:
        class_name = "DemoProducts"

        # Create collection (class) if it doesn't exist
        if not client.collections.exists(class_name):
            client.collections.create(
                class_name,
                properties=[
                    Property(name="name", data_type=DataType.TEXT),
                    Property(name="description", data_type=DataType.TEXT),
                ]
            )
            print(f"Created collection '{class_name}'")
        else:
            print(f"Collection '{class_name}' already exists")

        # Get the collection handle
        collection = client.collections.get(class_name)

        # Batch import 50 objects
        with collection.batch.fixed_size(batch_size=50) as batch:
            for i in range(50):
                batch.add_object(
                    properties={
                        "name": f"Product {i}",
                        "description": f"Description {i}"
                    }
                )

        # Count objects by iterating (suitable for small counts; for large datasets consider an aggregate API)
        count = sum(1 for _ in collection.iterator())
        print(f"Number of objects in '{class_name}': {count}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection 'DemoProducts' already exists
Number of objects in 'DemoProducts': 50

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 14.23s)

**Generated Code**:
```python
# Requires: pip install weaviate-client
import os
import weaviate

def main():
    # Read environment variables
    wcd_url = os.environ.get("WCD_TEST_URL")
    wcd_key = os.environ.get("WCD_TEST_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")

    if not (wcd_url and wcd_key and openai_key):
        raise RuntimeError("Please set WCD_TEST_URL, WCD_TEST_KEY and OPENAI_API_KEY environment variables")

    # Connect to Weaviate Cloud and pass the OpenAI API key as an additional header
    client = weaviate.Client(
        url=wcd_url,
        auth_client_secret=weaviate.AuthApiKey(api_key=wcd_key),
        additional_headers={"X-OpenAI-Api-Key": openai_key},
    )

    query_text = "dessert wine"

    # Query the WineReview class using nearText (text2vec-openai vectorizer)
    response = (
        client.query
        .get("WineReview", ["title", "country", "price", "points"])
        .with_near_text({"concepts": [query_text]})
        .with_limit(2)
        .do()
    )

    items = response.get("data", {}).get("Get", {}).get("WineReview", [])
    if not items:
        print("No matching wines found.")
        return

    for i, item in enumerate(items, start=1):
        title = item.get("title")
        country = item.get("country")
        price = item.get("price")
        points = item.get("points")
        print(f"Result {i}:")
        print(f"  Title:   {title}")
        print(f"  Country: {country}")
        print(f"  Price:   {price}")
        print(f"  Points:  {points}")
        print()

if __name__ == "__main__":
    main()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:15: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 50, in <module>
    main()
  File "/code/code.py", line 15, in main
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 24.09s)

**Generated Code**:
```python
import os
import weaviate

def main():
    # Load credentials from environment
    cluster_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    openai_api_key = os.environ["OPENAI_API_KEY"]

    # Connect to Weaviate Cloud (passes the OpenAI key in headers so text2vec-openai can be used)
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=weaviate.AuthApiKey(api_key=wcd_api_key),
        headers={
            "X-OpenAI-API-Key": openai_api_key
        },
    )

    try:
        # Run a near-text/vector search for "dessert wine" on the WineReview class,
        # requesting the fields title, country, price and points, limited to 2 results.
        res = (
            client.query
            .get("WineReview", ["title", "country", "price", "points"])
            .with_near_text({"concepts": ["dessert wine"]})
            .with_limit(2)
            .do()
        )

        # Extract results
        items = res.get("data", {}).get("Get", {}).get("WineReview", [])
        if not items:
            print("No matching wines found.")
            return

        # Print requested fields for each result
        for i, item in enumerate(items, start=1):
            title = item.get("title")
            country = item.get("country")
            price = item.get("price")
            points = item.get("points")
            print(f"Result {i}:")
            print(f"  Title:   {title}")
            print(f"  Country: {country}")
            print(f"  Price:   {price}")
            print(f"  Points:  {points}")
            print()

    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(
Traceback (most recent call last):
  File "/code/code.py", line 53, in <module>
    main()
  File "/code/code.py", line 23, in main
    client.query
AttributeError: 'WeaviateClient' object has no attribute 'query'

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 15.46s)

**Generated Code**:
```python
#!/usr/bin/env python3
import os
import sys
import weaviate
from weaviate.classes.init import Auth

# Read required environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY or not OPENAI_API_KEY:
    sys.exit(
        "Missing required environment variables. Make sure WCD_TEST_URL, WCD_TEST_KEY and OPENAI_API_KEY are set."
    )

# Connect to Weaviate Cloud, pass OpenAI API key as header for the text2vec-openai vectorizer
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Semantic search for "dessert wine", limit to maximum 2 results
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"],
    )

    # Print requested fields for each matching wine
    if not response.objects:
        print("No matching wines found.")
    else:
        for i, obj in enumerate(response.objects, start=1):
            props = obj.properties or {}
            title = props.get("title")
            country = props.get("country")
            price = props.get("price")
            points = props.get("points")
            print(f"Result {i}:")
            print(f"  Title  : {title}")
            print(f"  Country: {country}")
            print(f"  Price  : {price}")
            print(f"  Points : {points}")
            print()
finally:
    client.close()
```

**Output**:
```
Result 1:
  Title  : Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price  : 24.0
  Points : 88

Result 2:
  Title  : Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price  : 40.0
  Points : 88


```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 24.63s)

**Generated Code**:
```python
import os
import weaviate

# Read environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
# OPENAI_API_KEY is expected to be set on the Weaviate Cloud instance (server-side),
# not required by the client here.

# Create Weaviate client for cloud instance
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    timeout_config=(5, 60),
)

# Build the Where filter:
# - price < 50
# - points > 90
# - review_body contains at least one of the listed substrings
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
                {"path": ["review_body"], "operator": "Like", "valueText": "%spice%"},
                {"path": ["review_body"], "operator": "Like", "valueText": "%fruit%"},
                {"path": ["review_body"], "operator": "Like", "valueText": "%berry%"},
                {"path": ["review_body"], "operator": "Like", "valueText": "%cherry%"},
                {"path": ["review_body"], "operator": "Like", "valueText": "%honey%"},
            ],
        },
    ],
}

# Perform hybrid search with alpha=0.5, query "pair with steak", limit 5
response = (
    client.query.get("WineReview", ["title", "country", "price", "points", "review_body"])
    .with_hybrid("pair with steak", alpha=0.5)
    .with_where(where_filter)
    .with_limit(5)
    .do()
)

# Extract results and print requested fields
items = response.get("data", {}).get("Get", {}).get("WineReview", [])

if not items:
    print("No matching wines found.")
else:
    for idx, item in enumerate(items, start=1):
        title = item.get("title")
        country = item.get("country")
        price = item.get("price")
        points = item.get("points")
        print(f"{idx}. Title: {title} | Country: {country} | Price: {price} | Points: {points}")
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 31.12s)

**Generated Code**:
```python

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 20.50s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# Ensure required environment variables exist
WCD_URL = os.environ.get("WCD_TEST_URL")
WCD_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

if not all([WCD_URL, WCD_KEY, OPENAI_KEY]):
    raise RuntimeError(
        "Missing required environment variables. Make sure WCD_TEST_URL, WCD_TEST_KEY and OPENAI_API_KEY are set."
    )

# Connect to Weaviate Cloud (include OpenAI API key in headers for text2vec-openai)
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_URL,
    auth_credentials=Auth.api_key(WCD_KEY),
    headers={"X-OpenAI-Api-Key": OPENAI_KEY},
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Build text-substring filter: review_body contains at least one of the substrings
    review_substrings_filter = (
        Filter.by_property("review_body").like("*spice*")
        | Filter.by_property("review_body").like("*fruit*")
        | Filter.by_property("review_body").like("*berry*")
        | Filter.by_property("review_body").like("*cherry*")
        | Filter.by_property("review_body").like("*honey*")
    )

    # Numeric filters: price < 50 and points > 90
    numeric_filters = (
        Filter.by_property("price").less_than(50)
        & Filter.by_property("points").greater_than(90)
    )

    combined_filter = numeric_filters & review_substrings_filter

    # Perform hybrid search with alpha=0.5, limit up to 5 results
    response = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        fusion_type=HybridFusion.RELATIVE_SCORE,
        filters=combined_filter,
        limit=5,
        return_properties=["title", "country", "price", "points"],
    )

    # Print results
    if not response.objects:
        print("No matching wines found.")
    else:
        for obj in response.objects:
            props = obj.properties or {}
            title = props.get("title")
            country = props.get("country")
            price = props.get("price")
            points = props.get("points")
            print(f"Title: {title} | Country: {country} | Price: {price} | Points: {points}")

finally:
    client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir | Country: US | Price: 40.0 | Points: 92
Title: Bink 2014 Pinot Noir (Anderson Valley) | Country: US | Price: 49.0 | Points: 91
Title: Doña Silvina 2011 Malbec (Mendoza) | Country: Argentina | Price: 27.0 | Points: 91
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji) | Country: Hungary | Price: 25.0 | Points: 93
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico) | Country: Italy | Price: 0.0 | Points: 92

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

### openai/gpt-5-nano-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 9.40s)

**Generated Code**:
```python

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 8.34s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    cluster_url = os.environ["WCD_TEST_URL"]
    api_key = os.environ["WCD_TEST_KEY"]

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key)
    )

    assert client.is_ready()

    client.close()

if __name__ == "__main__":
    main()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.13s)

**Generated Code**:
```python

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.15s)

**Generated Code**:
```python

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.89s)

**Generated Code**:
```python

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.70s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.96s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.53s)

**Generated Code**:
```python

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.22s)

**Generated Code**:
```python

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.51s)

**Generated Code**:
```python

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.74s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

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

        # Semantic search: find wines most similar to "dessert wine"
        response = wine_collection.query.near_text(
            query="dessert wine",
            limit=2
        )

        # Print desired fields: title, country, price, and points
        for obj in response.objects:
            props = obj.properties
            title = props.get("title")
            country = props.get("country")
            price = props.get("price")
            points = props.get("points")
            print(title, country, price, points)
    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)) US 24.0 88
Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast) US 40.0 88

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:133: DeprecationWarning: Dep005: You are using weaviate-client version 4.11.3. The latest version is 4.16.7.
            Consider upgrading to the latest version. See https://weaviate.io/developers/weaviate/client-libraries/python for details.
  warnings.warn(

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.08s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.03s)

**Generated Code**:
```python

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.51s)

**Generated Code**:
```python

```

---

