# Weaviate Benchmark Results

Generated on: 2025-08-17 22:11:08

## Summary

- **anthropic/claude-3-7-sonnet-20250219**: 9/14 tasks successful
- **anthropic/claude-3-5-haiku-20241022**: 11/14 tasks successful
- **openai/gpt-4.1-mini-2025-04-14**: 7/14 tasks successful
- **cohere/command-a-03-2025**: 4/14 tasks successful
- **anthropic/claude-sonnet-4-20250514**: 13/14 tasks successful
- **anthropic/claude-opus-4-20250514**: 11/14 tasks successful
- **gemini/gemini-2.5-pro**: 14/14 tasks successful
- **gemini/gemini-2.5-flash**: 8/14 tasks successful
- **gemini/gemini-2.5-flash-lite**: 8/14 tasks successful
- **openai/gpt-5-2025-08-07**: 10/14 tasks successful
- **openai/gpt-5-mini-2025-08-07**: 6/14 tasks successful
- **openai/gpt-5-nano-2025-08-07**: 3/14 tasks successful
## Detailed Results

### anthropic/claude-3-7-sonnet-20250219

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 5.84s)

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

**Errors**:
```
/code/code.py:14: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.67s)

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

**Status**: ❌ FAILURE (runtime: 8.91s)

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

# Create collection with properties
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

**Output**:
```
Collection 'DemoProducts' exists. Deleting it...
Collection 'DemoProducts' deleted.

```

**Errors**:
```
/code/code.py:14: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
Traceback (most recent call last):
  File "/code/code.py", line 35, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN),
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 51974), raddr=('34.111.245.21', 443)>

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 4.92s)

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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 8.11s)

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

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.07s)

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
try:
    collection = client.collections.get("DemoProducts")
    print("Collection 'DemoProducts' already exists")
except weaviate.exceptions.WeaviateQueryError:
    # Create collection with properties
    collection = client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        vectorizer_config=Configure.Vectorizer.none(),  # No vectorization needed for this example
    )
    print("Created collection 'DemoProducts'")

# Batch import 50 objects
with collection.batch.dynamic() as batch:
    for i in range(1, 51):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description for product {i}. This is a sample product."
            }
        )

# Print the number of objects in the collection
count = collection.aggregate.over_all().count()
print(f"Number of objects in the collection: {count}")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists

```

**Errors**:
```
/code/code.py:11: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
Traceback (most recent call last):
  File "/code/code.py", line 43, in <module>
    count = collection.aggregate.over_all().count()
AttributeError: 'AggregateReturn' object has no attribute 'count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 54416), raddr=('34.111.245.21', 443)>

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 9.74s)

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

**Status**: ❌ FAILURE (runtime: 9.10s)

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
print(f"Number of objects in the collection: {count}")

# Close the client when done
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 36, in <module>
    count = collection.query.fetch_objects(limit=0).total_count
AttributeError: 'QueryReturn' object has no attribute 'total_count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 52568), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.28s)

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
client = weaviate.connect_to_weaviate(
    url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
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
Traceback (most recent call last):
  File "/code/code.py", line 12, in <module>
    client = weaviate.connect_to_weaviate(
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 145, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute connect_to_weaviate

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.05s)

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

**Status**: ✅ SUCCESS (runtime: 7.85s)

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

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.83s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, MetadataQuery
import weaviate.classes.query as wvc

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

# Define the query
response = (
    client.collections.get("WineReview")
    .query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=Filter.and_operator(
            Filter.less_than(path=["price"], value=50),
            Filter.greater_than(path=["points"], value=90),
            Filter.or_operator(
                Filter.contains_any_substring(path=["review_body"], values=["spice", "fruit", "berry", "cherry", "honey"])
            )
        ),
        return_metadata=MetadataQuery(distance=True, score=True)
    )
    .objects
)

# Print the results
print(f"Found {len(response)} matching wines:\n")
for wine in response:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: ${wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print(f"Distance: {wine.metadata.distance}")
    print(f"Score: {wine.metadata.score}")
    print("-" * 50)

# Close the client
client.close()
```

**Errors**:
```
/code/code.py:12: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
Traceback (most recent call last):
  File "/code/code.py", line 27, in <module>
    filters=Filter.and_operator(
AttributeError: type object 'Filter' has no attribute 'and_operator'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 47028), raddr=('34.111.245.21', 443)>

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.17s)

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
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: ${obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
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
Score: 0.3765
--------------------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.0451
--------------------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.0162
--------------------------------------------------
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
Score: 0.0010
--------------------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.85s)

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

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Define the review patterns to match
review_patterns = ["spice", "fruit", "berry", "cherry", "honey"]
pattern_regex = "|".join(review_patterns)

# Create a filter for price < 50 and points > 90
# Also filter for reviews containing at least one of the required substrings
price_points_filter = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").like(f"*({pattern_regex})*")
)

# Perform hybrid search with alpha=0.5
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,  # Balance between keyword and vector search
    filters=price_points_filter,
    limit=5,
    return_properties=["title", "country", "price", "points", "review_body"],
    return_metadata=MetadataQuery(distance=True, score=True)
)

# Print the results
print("Wines that pair well with steak:")
print("-" * 50)
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: ${wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print("-" * 50)

# Close the client
client.close()
```

**Output**:
```
Wines that pair well with steak:
--------------------------------------------------

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

**Status**: ✅ SUCCESS (runtime: 4.46s)

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

**Status**: ✅ SUCCESS (runtime: 11.64s)

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

**Output**:
```
Deleting existing DemoProducts collection...
An error occurred: BOOLEAN

```

**Errors**:
```
/code/code.py:11: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 7.66s)

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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.01s)

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

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 10.23s)

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
/code/code.py:10: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 12.63s)

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
    # Remove the collection if it already exists (optional)
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")
    
    # Create the collection with specified properties
    client.collections.create(
        name="DemoProducts",
        properties=[
            weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
            weaviate.Property(name="description", data_type=weaviate.DataType.TEXT)
        ]
    )
except Exception as e:
    print(f"Error creating collection: {e}")

# Get the collection
collection = client.collections.get("DemoProducts")

# Batch import 50 objects
try:
    with collection.batch.dynamic() as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i+1}",
                    "description": f"Description for Product {i+1}"
                }
            )
        
        # Check for any batch import errors
        if batch.number_errors > 0:
            print(f"Number of failed imports: {batch.number_errors}")
            for error in batch.failed_objects:
                print(f"Failed object: {error}")

    # Print the number of objects in the collection
    print(f"Number of objects in the collection: {len(collection)}")

except Exception as e:
    print(f"Error during batch import: {e}")

# Close the client connection
client.close()
```

**Output**:
```
Error creating collection: module weaviate has no attribute Property
Number of objects in the collection: 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.46s)

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

# Create the collection with properties
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

# Close the client
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 240, in create
    return self.__create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 104, in __create
    result = self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 822, in post
    return self._send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 716, in _send
    return executor.execute(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 99, in execute
    return cast(T, exception_callback(e))
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 714, in exc
    self.__handle_exceptions(e, error_msg)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 670, in __handle_exceptions
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 95, in execute
    resp_call = response_callback(call)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 711, in resp
    return self.__handle_response(res, error_msg, status_codes)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 681, in __handle_response
    raise UnexpectedStatusCodeError(error_msg, response)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 46604), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.48s)

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
/code/code.py:6: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.15s)

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

**Status**: ✅ SUCCESS (runtime: 11.04s)

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

    # Print details of matching wines
    for wine in response.objects:
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

**Status**: ❌ FAILURE (runtime: 10.40s)

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
        wine_reviews = client.collections.get("WineReview")
        
        # Hybrid search with specific filters
        results = wine_reviews.query.hybrid(
            query="pair with steak",
            hybrid_search_options=HybridSearchOptions(alpha=0.5),
            filters=wine_reviews.query.filter(
                # Price less than 50
                weaviate.Filter.less_than(path="price", value=50)
                # Points greater than 90
                & weaviate.Filter.greater_than(path="points", value=90)
            ),
            limit=5
        )

        # Filter results to include specific review body keywords
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

**Status**: ✅ SUCCESS (runtime: 9.39s)

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

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 13.42s)

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
        print(f"Title: {wine.properties['title']}")
        print(f"Country: {wine.properties['country']}")
        print(f"Price: ${wine.properties['price']}")
        print(f"Points: {wine.properties['points']}")
        print("---")

finally:
    # Always close the client connection
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

---

### openai/gpt-4.1-mini-2025-04-14

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 3.66s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Initialize Weaviate client with API key authentication
client = weaviate.Client(
    url=url,
    auth_client_secret=weaviate.AuthApiKey(api_key),
    additional_headers={
        "X-OpenAI-Api-Key": api_key  # sometimes needed, but only if using OpenAI module; omit if not
    }
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 2.99s)

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

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 3.97s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

# Initialize Weaviate client with API key authentication
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # sometimes needed for OpenAI integration, remove if not needed
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
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 4.64s)

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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.10s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

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
    ]
)

print(f'Collection "{collection_name}" created successfully.')

# Close the client when done
client.close()
```

**Output**:
```
Collection "DemoProducts" created successfully.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 6.42s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # sometimes needed, but optional here
    }
)

# Define the schema for the class "DemoProducts"
class_obj = {
    "class": "DemoProducts",
    "description": "A demo product class",
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

# Prepare batch import of 50 objects
with client.batch as batch:
    batch.batch_size = 20  # optional, default is 100
    for i in range(1, 51):
        obj = {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
        batch.add_data_object(obj, "DemoProducts")

# Query to count objects in DemoProducts
result = client.query.aggregate("DemoProducts").with_meta_count().do()

count = 0
try:
    count = result["data"]["Aggregate"]["DemoProducts"][0]["meta"]["count"]
except (KeyError, IndexError):
    pass

print(f"Number of objects in 'DemoProducts': {count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 6.79s)

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

    # Define the class schema for "DemoProducts"
    class_obj = {
        "class": "DemoProducts",
        "description": "A demo product collection",
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

    # Get the collection (class) object for batch import
    collection = client.collections.get("DemoProducts")

    # Prepare 50 arbitrary objects
    data_rows = [
        {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
        for i in range(1, 51)
    ]

    # Batch import
    with collection.batch.dynamic() as batch:
        for data_row in data_rows:
            batch.add_object(properties=data_row)
            if batch.number_errors > 10:
                print("Batch import stopped due to excessive errors.")
                break

    # Check for failed objects
    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        print(f"First failed object: {failed_objects[0]}")

    # Print number of objects in the collection
    print(f"Number of objects in 'DemoProducts': {len(collection)}")

    client.close()

if __name__ == "__main__":
    main()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 75, in <module>
    main()
  File "/code/code.py", line 38, in main
    schema = client.schema.get()
AttributeError: 'WeaviateClient' object has no attribute 'schema'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 49316), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 6.74s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType

def main():
    # Connect to Weaviate Cloud using environment variables
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"])
    )

    # Check if collection "DemoProducts" exists, if not create it
    if not client.collections.exists("DemoProducts"):
        client.collections.create(
            "DemoProducts",
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            # Use a vectorizer suitable for text, e.g. Weaviate's built-in text2vec_weaviate
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
    # Using the iterator and counting objects
    count = 0
    for _ in collection.iterator():
        count += 1

    print(f"Number of objects in 'DemoProducts': {count}")

    # Close the client connection
    client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Number of objects in 'DemoProducts': 50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 4.15s)

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
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
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
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 5.05s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

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

# Print title, country, price, and points of each matching wine
for obj in response.objects:
    props = obj.properties
    print(
        f"Title: {props.get('title')}, "
        f"Country: {props.get('country')}, "
        f"Price: {props.get('price')}, "
        f"Points: {props.get('points')}"
    )

client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)), Country: US, Price: 24.0, Points: 88
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast), Country: US, Price: 40.0, Points: 88

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 6.26s)

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

    # Connect to Weaviate Cloud with OpenAI API key in headers for text2vec-openai vectorizer
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            "X-OpenAI-Api-Key": openai_api_key
        }
    )

    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Perform semantic search with near_text for "dessert wine", limit 2 results
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

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 6.74s)

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

# Define the filter for price < 50 and points > 90
filter_obj = {
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
                },
            ]
        }
    ]
}

# Perform the hybrid query
result = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query_text, alpha=0.5)
    .with_limit(5)
    .with_where(filter_obj)
    .do()
)

# Extract and print results
wines = result.get("data", {}).get("Get", {}).get("WineReview", [])
for wine in wines:
    title = wine.get("title", "N/A")
    country = wine.get("country", "N/A")
    price = wine.get("price", "N/A")
    points = wine.get("points", "N/A")
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 6.24s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

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
        return_metadata=MetadataQuery(score=True),
        properties=["title", "country", "price", "points"]
    )

    # Print the results
    for obj in response.objects:
        props = obj.properties
        print(f"Title: {props.get('title', 'N/A')}")
        print(f"Country: {props.get('country', 'N/A')}")
        print(f"Price: {props.get('price', 'N/A')}")
        print(f"Points: {props.get('points', 'N/A')}")
        print(f"Score: {obj.metadata.score:.4f}")
        print("-" * 40)

    client.close()

if __name__ == "__main__":
    main()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 55, in <module>
    main()
  File "/code/code.py", line 33, in main
    response = collection.query.hybrid(
TypeError: hybrid() got an unexpected keyword argument 'properties'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 48788), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 6.31s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter

# Connect to Weaviate Cloud with API key and OpenAI API key in headers
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Build the filter:
# price < 50 AND points > 90 AND review_body contains at least one of the substrings
# "spice", "fruit", "berry", "cherry", or "honey"
# We use Filter.any_of for the substrings in review_body with like("*substring*")

price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)

review_body_substrings = ["spice", "fruit", "berry", "cherry", "honey"]
review_body_filters = [
    Filter.by_property("review_body").like(f"*{substr}*") for substr in review_body_substrings
]
review_body_filter = Filter.any_of(review_body_filters)

combined_filter = Filter.all_of([
    price_filter,
    points_filter,
    review_body_filter
])

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

# Close the client connection when done
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

---

### cohere/command-a-03-2025

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 3.90s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.exceptions import WeaviateConnectionError

# Retrieve environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Initialize the Weaviate client with API key authentication
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
)

# Check if the server is ready
try:
    client.is_ready()
    print("Weaviate server is ready to accept requests.")
except WeaviateConnectionError as e:
    print(f"Failed to connect to Weaviate: {e}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 3.39s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

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

**Status**: ❌ FAILURE (runtime: 4.72s)

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

# Check if the collection already exists and delete it if it does
if client.schema.exists(COLLECTION_NAME):
    client.schema.delete_class(COLLECTION_NAME)
    print(f"Collection '{COLLECTION_NAME}' deleted.")

# Define the schema for the collection
schema = {
    "classes": [
        {
            "class": COLLECTION_NAME,
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
    ]
}

# Create the collection
client.schema.create(schema)
print(f"Collection '{COLLECTION_NAME}' created successfully.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 5.38s)

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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 40062), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.47s)

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

# Delete the collection if it already exists
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
Traceback (most recent call last):
  File "/code/code.py", line 26, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN),
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 38296), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 4.45s)

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
object_count = demo_products.count()
print(f"Number of objects in the '{collection_name}' collection: {object_count}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 5.97s)

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
        if batch.number_errors > 10:
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

**Status**: ❌ FAILURE (runtime: 6.42s)

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
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# Batch import 50 objects into the collection
collection = client.collections.get("DemoProducts")
with collection.batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
object_count = collection.aggregate.over_all().total_count
print(f"Number of objects in the collection: {object_count}")

# Close the client
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 13, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 240, in create
    return self.__create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 104, in __create
    result = self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 822, in post
    return self._send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 716, in _send
    return executor.execute(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 99, in execute
    return cast(T, exception_callback(e))
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 714, in exc
    self.__handle_exceptions(e, error_msg)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 670, in __handle_exceptions
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 95, in execute
    resp_call = response_callback(call)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 711, in resp
    return self.__handle_response(res, error_msg, status_codes)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 681, in __handle_response
    raise UnexpectedStatusCodeError(error_msg, response)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 56654), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.22s)

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

# Perform the hybrid search (combines vector and keyword search)
response = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query=query)
    .with_limit(2)
    .do()
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
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 5.73s)

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

**Status**: ✅ SUCCESS (runtime: 6.26s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import MetadataQuery

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.classes.init.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Perform a semantic search for "dessert wine" with a limit of 2 results
response = collection.query.near_text(
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
    print(f"Distance: {obj.metadata.distance}")
    print("---")

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
---
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Distance: 0.4812379479408264
---

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.97s)

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
        operator: AND
        path: ["price", "points", "review_body"]
        valueInt: [50, 90]
        valueStringType: ["spice", "fruit", "berry", "cherry", "honey"]
        operator: [LessThan, GreaterThan, ContainsAny]
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
    print(f"Price: {wine['price']}")
    print(f"Points: {wine['points']}")
    print("-" * 40)
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 5.50s)

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
    ).to_where(),
    return_metadata=weaviate.classes.query.MetadataQuery(score=True),
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
Traceback (most recent call last):
  File "/code/code.py", line 28, in <module>
    filters=Filter.by_properties(
AttributeError: type object 'Filter' has no attribute 'by_properties'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 58080), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 6.97s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, HybridFusion
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

# Define the search query with filters and hybrid search
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
for obj in response.objects:
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: {obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
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

---

### anthropic/claude-sonnet-4-20250514

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 6.38s)

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

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.62s)

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

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 31.48s)

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

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 6.51s)

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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 11.17s)

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

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 11.64s)

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
    
    # Prepare 50 objects for batch import
    objects_to_insert = []
    for i in range(1, 51):
        objects_to_insert.append({
            "name": f"Product {i}",
            "description": f"Description {i}"
        })
    
    # Batch import the objects
    demo_products = client.collections.get("DemoProducts")
    response = demo_products.data.insert_many(objects_to_insert)
    
    print(f"Batch import completed! Inserted {len(objects_to_insert)} objects.")
    
    # Check for any errors during insertion
    if response.has_errors:
        print("Some errors occurred during insertion:")
        for error in response.errors:
            print(f"Error: {error}")
    
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

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 11.88s)

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
        print("Collection 'DemoProducts' created successfully.")
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

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.56s)

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
    
    # Get and print the total number of objects in the collection
    response = collection.query.fetch_objects(limit=1)  # Just to get the total count
    total_count = len(list(collection.iterator()))  # Count all objects using iterator
    
    print(f"Total number of objects in DemoProducts collection: {total_count}")

finally:
    # Always close the client connection
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 240, in create
    return self.__create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 104, in __create
    result = self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 822, in post
    return self._send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 716, in _send
    return executor.execute(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 99, in execute
    return cast(T, exception_callback(e))
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 714, in exc
    self.__handle_exceptions(e, error_msg)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 670, in __handle_exceptions
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 95, in execute
    resp_call = response_callback(call)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 711, in resp
    return self.__handle_response(res, error_msg, status_codes)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 681, in __handle_response
    raise UnexpectedStatusCodeError(error_msg, response)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.38s)

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

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.29s)

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

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.87s)

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
    
    # Query for wines that best match "dessert wine" using semantic search
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

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.07s)

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
    print(f"Found {len(response.objects)} wines that pair well with steak:\n")
    
    for i, wine in enumerate(response.objects, 1):
        print(f"{i}. Title: {wine.properties.get('title', 'N/A')}")
        print(f"   Country: {wine.properties.get('country', 'N/A')}")
        print(f"   Price: ${wine.properties.get('price', 'N/A')}")
        print(f"   Points: {wine.properties.get('points', 'N/A')}")
        print("-" * 50)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
An error occurred: hybrid() got an unexpected keyword argument 'where'

```

**Errors**:
```
/code/code.py:6: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.01s)

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

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 19.78s)

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
    
    # Create filters for the requirements
    # Price less than 50 AND points greater than 90
    price_points_filter = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90)
    )
    
    # Filter for review_body containing at least one of the specified substrings
    # Using like with wildcards to match substrings
    flavor_filter = Filter.any_of([
        Filter.by_property("review_body").like("*spice*"),
        Filter.by_property("review_body").like("*fruit*"),
        Filter.by_property("review_body").like("*berry*"),
        Filter.by_property("review_body").like("*cherry*"),
        Filter.by_property("review_body").like("*honey*")
    ])
    
    # Combine all filters
    combined_filter = price_points_filter & flavor_filter
    
    # Perform hybrid search with alpha=0.5
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Balance between keyword and vector search
        filters=combined_filter,
        limit=5,
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print the results
    print(f"Found {len(response.objects)} wines that pair well with steak:")
    print("-" * 80)
    
    for wine in response.objects:
        props = wine.properties
        print(f"Title: {props.get('title', 'N/A')}")
        print(f"Country: {props.get('country', 'N/A')}")
        print(f"Price: ${props.get('price', 'N/A')}")
        print(f"Points: {props.get('points', 'N/A')}")
        print("-" * 40)
    
    if len(response.objects) == 0:
        print("No wines found matching the specified criteria.")

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Found 5 wines that pair well with steak:
--------------------------------------------------------------------------------
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
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
----------------------------------------

```

---

### anthropic/claude-opus-4-20250514

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 25.47s)

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

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 16.34s)

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

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 31.33s)

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

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 31.67s)

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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 42.75s)

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

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 38.04s)

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

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 29.10s)

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

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 39.84s)

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
Traceback (most recent call last):
  File "/code/code.py", line 14, in <module>
    client.collections.create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 240, in create
    return self.__create(
  File "/usr/local/lib/python3.9/site-packages/weaviate/collections/collections/executor.py", line 104, in __create
    result = self._connection.post(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 822, in post
    return self._send(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 716, in _send
    return executor.execute(
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 99, in execute
    return cast(T, exception_callback(e))
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 714, in exc
    self.__handle_exceptions(e, error_msg)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 670, in __handle_exceptions
    raise e
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/executor.py", line 95, in execute
    resp_call = response_callback(call)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 711, in resp
    return self.__handle_response(res, error_msg, status_codes)
  File "/usr/local/lib/python3.9/site-packages/weaviate/connect/v4.py", line 681, in __handle_response
    raise UnexpectedStatusCodeError(error_msg, response)
weaviate.exceptions.UnexpectedStatusCodeError: Collection may not have been created properly.! Unexpected status code: 422, with response body: {'error': [{'message': 'class name DemoProducts already exists'}]}.

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 33.79s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import MetadataQuery

# Get environment variables
wcd_url = os.environ["WCD_TEST_URL"]
wcd_key = os.environ["WCD_TEST_KEY"]
openai_key = os.environ["OPENAI_API_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=weaviate.auth.AuthApiKey(wcd_key),
    headers={
        "X-OpenAI-Api-Key": openai_key
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
Distance: 0.4766477346420288
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Distance: 0.4812379479408264
--------------------------------------------------

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 18.51s)

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

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 37.77s)

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
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print the results
    print("Found wines matching 'dessert wine':\n")
    for i, wine in enumerate(response.objects, 1):
        print(f"Wine {i}:")
        print(f"  Title: {wine.properties.get('title', 'N/A')}")
        print(f"  Country: {wine.properties.get('country', 'N/A')}")
        print(f"  Price: ${wine.properties.get('price', 'N/A')}")
        print(f"  Points: {wine.properties.get('points', 'N/A')}")
        print()

finally:
    # Always close the client connection
    client.close()
```

**Output**:
```
Found wines matching 'dessert wine':

Wine 1:
  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: $24.0
  Points: 88

Wine 2:
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: $40.0
  Points: 88


```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 40.57s)

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
Traceback (most recent call last):
  File "/code/code.py", line 19, in <module>
    response = wine_collection.query.hybrid(
TypeError: hybrid() got an unexpected keyword argument 'where'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 34.41s)

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
Traceback (most recent call last):
  File "/code/code.py", line 19, in <module>
    response = collection.query.hybrid(
TypeError: hybrid() got an unexpected keyword argument 'where'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 52832), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 56.48s)

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
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Create filters for price < 50 and points > 90
    price_filter = Filter.by_property("price").less_than(50)
    points_filter = Filter.by_property("points").greater_than(90)
    
    # Create filter for review_body containing at least one of the specified substrings
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
        filters=combined_filter,
        limit=5,
        return_properties=["title", "country", "price", "points"]
    )
    
    # Print results
    print(f"Found {len(response.objects)} wines that pair well with steak:\n")
    
    for i, wine in enumerate(response.objects, 1):
        print(f"Wine {i}:")
        print(f"  Title: {wine.properties['title']}")
        print(f"  Country: {wine.properties['country']}")
        print(f"  Price: ${wine.properties['price']}")
        print(f"  Points: {wine.properties['points']}")
        print()

finally:
    # Close the client connection
    client.close()
```

**Output**:
```
Found 5 wines that pair well with steak:

Wine 1:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.0
  Points: 92

Wine 2:
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.0
  Points: 91

Wine 3:
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.0
  Points: 91

Wine 4:
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.0
  Points: 93

Wine 5:
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.0
  Points: 92


```

---

### gemini/gemini-2.5-pro

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 20.35s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.auth

# 1. Get connection details from environment variables
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("❗️ Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

print(f"Connecting to Weaviate Cloud at {wcd_url}...")

try:
    # 2. Connect to Weaviate Cloud
    # The 'with' statement ensures the connection is closed automatically
    with weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(api_key=wcd_key)
    ) as client:

        print("✅ Successfully connected to Weaviate.")

        # 3. Check if the server is ready to accept requests
        if client.is_ready():
            print("✅ Weaviate server is ready.")
        else:
            print("❌ Weaviate server is NOT ready.")

except Exception as e:
    print(f"❌ An error occurred during connection: {e}")

```

**Output**:
```
Connecting to Weaviate Cloud at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
✅ Successfully connected to Weaviate.
✅ Weaviate server is ready.

```

**Errors**:
```
/code/code.py:18: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  with weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 17.63s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Get the Weaviate Cloud URL and API key from environment variables
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

print(f"Connecting to Weaviate at {wcd_url}...")

try:
    # The 'with' statement ensures the client is closed automatically
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key)
    ) as client:
        # Check if the connection is successful and the server is ready
        if client.is_ready():
            print("Successfully connected to Weaviate Cloud!")
            print("The server is ready to accept requests.")
        else:
            print("Could not connect to Weaviate Cloud or server is not ready.")

except Exception as e:
    print(f"An error occurred during connection: {e}")

```

**Output**:
```
Connecting to Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud!
The server is ready to accept requests.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 24.64s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.classes.config import Property, DataType

# 1. Get connection details from environment variables
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_API_KEY = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("❌ Error: Make sure WCD_TEST_URL and WCD_TEST_KEY environment variables are set.")
    exit(1)

COLLECTION_NAME = "DemoProducts"
client = None  # Initialize client to None

try:
    # 2. Connect to Weaviate Cloud
    # The connect_to_wcs method is a helper for Weaviate Cloud Services
    client = weaviate.connect_to_wcs(
        cluster_url=WCD_URL,
        auth_credentials=AuthApiKey(api_key=WCD_API_KEY),
        # Optional: Add headers for your specific API provider (e.g., OpenAI, Cohere)
        # headers={
        #     "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        # }
    )
    print(f"✅ Successfully connected to Weaviate at {WCD_URL}")

    # 3. Check if the collection exists and delete it if it does
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it.")
        client.collections.delete(COLLECTION_NAME)
        print(f"🗑️ Collection '{COLLECTION_NAME}' deleted.")

    # 4. Create the new collection with the specified schema
    print(f"Creating collection '{COLLECTION_NAME}'...")
    
    # Using the latest syntax with weaviate.classes.config
    properties = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    client.collections.create(
        name=COLLECTION_NAME,
        properties=properties,
        # You can also configure the vectorizer here if needed
        # vectorizer_config=Configure.Vectorizer.text2vec_openai()
    )

    print(f"✅ Collection '{COLLECTION_NAME}' created successfully!")
    
    # Verify by listing all collections
    all_collections = client.collections.list_all()
    print("\nAvailable collections in your cluster:")
    for name, collection in all_collections.items():
        print(f"- {name}")


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 5. Close the connection
    if client:
        client.close()
        print("\nℹ️ Connection to Weaviate closed.")
```

**Output**:
```
✅ Successfully connected to Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Collection 'DemoProducts' already exists. Deleting it.
🗑️ Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
✅ Collection 'DemoProducts' created successfully!

Available collections in your cluster:
- DemoProducts
- WineReview

ℹ️ Connection to Weaviate closed.

```

**Errors**:
```
/code/code.py:20: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 19.72s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# --- 1. Get Weaviate credentials from environment variables ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("ERROR: Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

# --- 2. Connect to the Weaviate Cloud instance ---
# The try...finally block ensures that the client connection is closed
# even if an error occurs.
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_key)
    )
    print("Successfully connected to Weaviate.")

    # --- 3. Define the collection and delete if it exists ---
    collection_name = "DemoProducts"

    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # --- 4. Create the collection with the specified properties ---
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

    print(f"Successfully created collection: {products_collection.name}")
    print("Collection properties:")
    # You can inspect the created collection's config
    config = client.collections.get(collection_name).config.get()
    for prop in config.properties:
        print(f"- {prop.name}: {prop.data_type}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- 5. Close the connection ---
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Connection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Successfully created collection: DemoProducts
Collection properties:
- name: text
- description: text
- price: number
- in_stock: boolean
Connection to Weaviate closed.

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 20.82s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get Weaviate connection details from environment variables
# WCD_TEST_URL is the URL of the Weaviate Cloud instance,
# and WCD_TEST_KEY is the API key for the Weaviate Cloud instance.
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url or not wcd_api_key:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

collection_name = "DemoProducts"

# Connect to Weaviate Cloud using a context manager.
# This ensures the connection is closed automatically.
# For more information, see: https://weaviate.io/developers/weaviate/client-libraries/python
with weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_api_key)
) as client:
    print(f"Connected to Weaviate at {wcd_url}")

    # Check if the collection already exists
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        # Delete the collection if it exists
        client.collections.delete(collection_name)

    # Create the collection with the specified properties.
    # For more information, see: https://weaviate.io/developers/weaviate/manage-data/collections
    print(f"Creating collection '{collection_name}'...")
    products = client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )

    print(f"Collection '{collection_name}' created successfully.")

print("Client connection closed.")
```

**Output**:
```
Connected to Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Collection 'DemoProducts' already exists. Deleting it.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Client connection closed.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 27.85s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.classes.config import Property, DataType

# --- 1. Connect to Weaviate Cloud ---
# Get connection details from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
collection_name = "DemoProducts"

# Check if environment variables are set
if not wcd_url or not wcd_api_key:
    raise ValueError(
        "WCD_TEST_URL and WCD_TEST_KEY environment variables must be set."
    )

print("Connecting to Weaviate Cloud...")

# Use a context manager to ensure the connection is closed automatically
try:
    # Connect to your WCS instance
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(wcd_api_key),
    )
    print("Connection successful.")

    # --- 2. Create the Collection ---
    # To ensure the script is repeatable, we first delete the collection if it exists.
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)

    print(f"Creating collection '{collection_name}'...")
    # Create the collection with the specified properties
    client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created successfully.")

    # --- 3. Prepare and Batch Import Data ---
    print("Generating 50 sample objects...")
    data_objects = [
        {
            "name": f"Product {i}",
            "description": f"This is the description for product number {i}.",
        }
        for i in range(50)
    ]

    # Get a reference to the collection
    products_collection = client.collections.get(collection_name)

    print("Starting batch import of 50 objects...")
    # Use the batch context manager for efficient importing
    # .batch.dynamic() automatically handles batch size and rate limiting.
    with products_collection.batch.dynamic() as batch:
        for item in data_objects:
            batch.add_object(properties=item)

    print("Batch import completed.")

    # --- 4. Verify the number of objects ---
    # Fetch the total count of objects in the collection
    response = products_collection.aggregate.over_all(total_count=True)

    print("\n--- Verification ---")
    print(f"Number of objects in '{collection_name}': {response.total_count}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # The 'weaviate.connect_to_wcs' doesn't require a manual close() in a script,
    # but if you were using weaviate.Client, you'd call client.close() here.
    # The connection will be gracefully terminated when the script exits.
    print("\nScript finished.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Connection successful.
Collection 'DemoProducts' already exists. Deleting it.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Generating 50 sample objects...
Starting batch import of 50 objects...
Batch import completed.

--- Verification ---
Number of objects in 'DemoProducts': 50

Script finished.

```

**Errors**:
```
/code/code.py:23: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 38042), raddr=('34.111.245.21', 443)>

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 39.39s)

**Generated Code**:
```python
import weaviate
import weaviate.classes.config as wvc_config
import os
import sys

# Get Weaviate Cloud credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if the environment variables are set
if not wcd_url or not wcd_api_key:
    print("Error: Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    sys.exit(1)

# Define the collection name
COLLECTION_NAME = "DemoProducts"
client = None  # Initialize client to None for the finally block

try:
    # 1. Connect to Weaviate Cloud
    # Replace with your actual cluster URL and API key
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(api_key=wcd_api_key),
        headers={
            "X-Python-Client-Version": weaviate.__version__
        }
    )
    print("Successfully connected to Weaviate.")

    # 2. Recreate the collection to ensure a clean state
    # This deletes the collection if it exists and creates a new one.
    if client.collections.exists(COLLECTION_NAME):
        client.collections.delete(COLLECTION_NAME)
        print(f"Deleted existing collection '{COLLECTION_NAME}'.")

    products = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            wvc_config.Property(name="name", data_type=wvc_config.DataType.TEXT),
            wvc_config.Property(name="description", data_type=wvc_config.DataType.TEXT),
        ],
        # By default, a vectorizer is not set up.
        # If you need vectorization, uncomment and configure the following line:
        # vectorizer_config=wvc_config.Configure.Vectorizer.text2vec_openai(),
    )
    print(f"Successfully created collection '{COLLECTION_NAME}'.")

    # 3. Prepare 50 arbitrary objects for import
    print("Preparing 50 objects for import...")
    data_objects = [
        {
            "name": f"Product {i}",
            "description": f"This is the description for product number {i}."
        }
        for i in range(1, 51)  # Create 50 objects from 1 to 50
    ]

    # 4. Batch import the objects
    print("Starting batch import...")
    # Get the collection object
    products_collection = client.collections.get(COLLECTION_NAME)

    with products_collection.batch.dynamic() as batch:
        for obj in data_objects:
            batch.add_object(
                properties=obj
            )
    print("Batch import finished.")

    # Check for failed objects
    if products_collection.batch.failed_objects:
        print(f"Failed to import {len(products_collection.batch.failed_objects)} objects.")
        # You can inspect the failed_objects list for details, e.g.:
        # for failed in products_collection.batch.failed_objects:
        #     print(f"Failed object: {failed.message}")
    else:
        print("All 50 objects imported successfully.")

    # 5. Get the total number of objects in the collection
    aggregate_result = products_collection.aggregate.over_all(total_count=True)

    # Print the count
    print(f"\nTotal number of objects in '{COLLECTION_NAME}': {aggregate_result.total_count}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. Close the connection
    if client:
        client.close()
        print("Connection to Weaviate closed.")

```

**Output**:
```
Successfully connected to Weaviate.
Deleted existing collection 'DemoProducts'.
Successfully created collection 'DemoProducts'.
Preparing 50 objects for import...
Starting batch import...
Batch import finished.
All 50 objects imported successfully.

Total number of objects in 'DemoProducts': 50
Connection to Weaviate closed.

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 24.50s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# This script requires the WCD_TEST_URL and WCD_TEST_KEY environment variables
# to be set, for example in a .env file.
# WCD_TEST_URL is the URL of the Weaviate Cloud instance
# WCD_TEST_KEY is the API key for the Weaviate Cloud instance
#
# e.g., from a .env file:
# WCD_TEST_URL="https://your-weaviate-instance.weaviate.network"
# WCD_TEST_KEY="your-weaviate-api-key"

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv not installed, skipping load_dotenv()")

# Get Weaviate credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if the environment variables are set
if not wcd_url or not wcd_api_key:
    print("Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    exit(1)

# Connect to Weaviate Cloud using the latest client syntax
# For more information, see: https://weaviate.io/developers/weaviate/client-libraries/python
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_api_key),
    # You can add headers for third-party API keys here, e.g., for OpenAI
    # headers={
    #     "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    # }
)

try:
    # Define the collection name
    collection_name = "DemoProducts"

    # =================================================
    # 1. Create the collection
    # =================================================
    # For more information, see: https://weaviate.io/developers/weaviate/manage-data/collections
    
    # Delete the collection if it already exists to ensure a clean run
    if client.collections.exists(collection_name):
        print(f"Deleting existing collection '{collection_name}'...")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    print(f"Creating collection '{collection_name}'...")
    products_collection = client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created successfully.")

    # =================================================
    # 2. Batch import 50 objects
    # =================================================
    # For more information, see: https://weaviate.io/developers/weaviate/manage-data/import
    
    print("Starting batch import of 50 objects...")
    # Using a context manager for batching is recommended.
    # It automatically handles sending batches when the batch size is reached
    # or when the context is exited.
    with products_collection.batch.fixed_size(batch_size=20) as batch:
        for i in range(1, 51):
            product_object = {
                "name": f"Product {i}",
                "description": f"This is the description for product {i}."
            }
            batch.add_object(properties=product_object)
    
    print("Batch import completed.")

    # You can check for failed objects after the batch import
    if len(products_collection.batch.failed_objects) > 0:
        print(f"Failed to import {len(products_collection.batch.failed_objects)} objects.")
    else:
        print("All objects imported successfully.")

    # =================================================
    # 3. Print the number of objects in the collection
    # =================================================
    # For more information on aggregations: https://weaviate.io/developers/weaviate/search/aggregate
    
    # Use the aggregate method to get the total count of objects
    aggregate_response = products_collection.aggregate.over_all(
        total_count=True
    )
    
    # The result is in the `total_count` attribute of the response
    object_count = aggregate_response.total_count
    
    print(f"\nNumber of objects in '{collection_name}': {object_count}")

finally:
    # Close the connection to Weaviate
    print("Closing Weaviate connection.")
    client.close()
```

**Output**:
```
Deleting existing collection 'DemoProducts'...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Starting batch import of 50 objects...
Batch import completed.
All objects imported successfully.

Number of objects in 'DemoProducts': 50
Closing Weaviate connection.

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 26.74s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc
import os

# --- Configuration ---
# Get environment variables for Weaviate Cloud and OpenAI
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_API_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Check for missing environment variables ---
if not all([WCD_URL, WCD_API_KEY, OPENAI_API_KEY]):
    print(
        "Error: Please set the WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY "
        "environment variables."
    )
    exit(1)

try:
    # Use a 'with' statement for automatic connection management
    # This connects to your Weaviate Cloud (WCS) instance
    with weaviate.connect_to_wcs(
        cluster_url=WCD_URL,
        auth_credentials=wvc.auth.AuthApiKey(WCD_API_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY  # Pass OpenAI key for vectorization
        }
    ) as client:

        print("Successfully connected to Weaviate Cloud.")
        print(f"Weaviate client is ready: {client.is_ready()}")

        # Get a handle to the 'WineReview' collection
        reviews = client.collections.get("WineReview")

        # Perform the vector search (semantic search)
        # The 'near_text' method vectorizes the query "dessert wine" and
        # finds the two most similar items in the collection.
        response = reviews.query.near_text(
            query="dessert wine",
            limit=2,
            return_properties=["title", "country", "price", "points"]
        )

        # Print the results in a user-friendly format
        print("\nTop 2 wine reviews matching 'dessert wine':")
        if not response.objects:
            print("No results found.")
        else:
            for item in response.objects:
                wine = item.properties
                # Handle potentially missing price for cleaner output
                price_str = f"${wine.get('price'):.2f}" if wine.get('price') is not None else "N/A"

                print("-" * 30)
                print(f"  Title:   {wine.get('title')}")
                print(f"  Country: {wine.get('country')}")
                print(f"  Price:   {price_str}")
                print(f"  Points:  {wine.get('points')}")

except Exception as e:
    print(f"\nAn error occurred: {e}")

```

**Output**:
```

An error occurred: module 'weaviate.classes' has no attribute 'auth'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 22.66s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# --- 1. Get environment variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if all required environment variables are set
if not all([wcd_url, wcd_api_key, openai_api_key]):
    print("ERROR: Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
    exit(1)

client = None
try:
    # --- 2. Connect to Weaviate Cloud ---
    # The OpenAI API key is passed in the headers for the text2vec-openai vectorizer.
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            "X-OpenAI-API-Key": openai_api_key
        },
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- 3. Get the 'WineReview' collection ---
    collection = client.collections.get("WineReview")
    print("Successfully retrieved the 'WineReview' collection.")

    # --- 4. Perform the near_text query ---
    query_text = "dessert wine"
    response = collection.query.near_text(
        query=query_text,
        limit=2
    )

    # --- 5. Print the results ---
    print(f"\nTop 2 wine results for '{query_text}':")
    print("-" * 40)

    if not response.objects:
        print("No results found.")
    else:
        for obj in response.objects:
            # Access the properties of each returned object
            properties = obj.properties
            print(f"  Title:   {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            print(f"  Price:   ${properties.get('price'):.2f}" if properties.get('price') is not None else "N/A")
            print(f"  Points:  {properties.get('points')}")
            print("-" * 40)

finally:
    # --- 6. Close the connection ---
    if client:
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate Cloud.
Successfully retrieved the 'WineReview' collection.

Top 2 wine results for 'dessert wine':
----------------------------------------
  Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price:   $24.00
  Points:  88
----------------------------------------
  Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price:   $40.00
  Points:  88
----------------------------------------

Connection to Weaviate closed.

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.56s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# This script performs a semantic search on the 'WineReview' collection
# to find wines similar to "dessert wine".

# Ensure the required environment variables are set.
# These variables are necessary to connect to Weaviate Cloud and OpenAI.
required_env_vars = ["WCD_TEST_URL", "WCD_TEST_KEY", "OPENAI_API_KEY"]
for var in required_env_vars:
    if var not in os.environ:
        raise ValueError(f"Environment variable '{var}' is not set. Please set it before running the script.")

# Connect to a Weaviate Cloud instance
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],  # URL of your Weaviate instance
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),  # API key for your Weaviate instance
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Pass the OpenAI API key
        }
    )
    print("Successfully connected to Weaviate.")

    # Get a handle to the 'WineReview' collection
    # For more information on collections, see: https://docs.weaviate.io/weaviate/manage-data/collections
    reviews = client.collections.get("WineReview")

    # Perform a semantic search (near_text) to find wines matching the query.
    # The 'text2vec-openai' vectorizer will convert the query into a vector
    # and find the most similar items in the collection.
    # For more information on searching, see: https://docs.weaviate.io/weaviate/search
    response = reviews.query.near_text(
        query="dessert wine",
        limit=2
    )

    print("\nTop 2 wine reviews matching 'dessert wine':\n")
    # Check if any results were returned
    if not response.objects:
        print("No results found.")
    else:
        # Print the title, country, price, and points for each matching wine
        for item in response.objects:
            # Access the properties of each returned object
            properties = item.properties
            print(f"  Title: {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            print(f"  Price: ${properties.get('price')}")
            print(f"  Points: {properties.get('points')}")
            print("-" * 20)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection to Weaviate
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate.

Top 2 wine reviews matching 'dessert wine':

  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: $24.0
  Points: 88
--------------------
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: $40.0
  Points: 88
--------------------

Connection to Weaviate closed.

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 28.21s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes as wvc
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Get environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if all environment variables are set
if not all([wcd_url, wcd_api_key, openai_api_key]):
    print("Error: Required environment variables WCD_TEST_URL, WCD_TEST_KEY, or OPENAI_API_KEY are not set.")
    exit(1)

# --- Connection and Query Logic ---
client = None
try:
    # 2. Connect to Weaviate Cloud
    # The Weaviate client uses the OpenAI API key for vectorization at query time.
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(wcd_api_key),
        headers={
            "X-OpenAI-Api-Key": openai_api_key
        }
    )
    print("Successfully connected to Weaviate.")

    # Get a reference to the 'WineReview' collection
    reviews = client.collections.get("WineReview")
    print("Collection 'WineReview' retrieved.")

    # 3. Define the filters for the query
    # Filter for price < 50
    price_filter = wvc.query.Filter.by_property("price").less_than(50)

    # Filter for points > 90
    points_filter = wvc.query.Filter.by_property("points").greater_than(90)

    # Filter for at least one keyword in the review_body.
    # We use a list comprehension and Filter.any_of() for an OR condition.
    review_keywords = ["spice", "fruit", "berry", "cherry", "honey"]
    review_body_filters = [
        wvc.query.Filter.by_property("review_body").like(f"*{keyword}*") for keyword in review_keywords
    ]
    or_filter_for_review = wvc.query.Filter.any_of(review_body_filters)

    # Combine all filters with an AND condition
    final_filters = wvc.query.Filter.all_of([
        price_filter,
        points_filter,
        or_filter_for_review
    ])
    
    # 4. Execute the hybrid query
    print("\nExecuting hybrid search for 'pair with steak'...")
    response = reviews.query.hybrid(
        query="pair with steak",
        limit=5,
        alpha=0.5,  # 0.5 for an even blend of keyword and vector search
        filters=final_filters,
        return_properties=[
            "title",
            "country",
            "price",
            "points"
        ]
    )

    # 5. Print the results
    print("\n--- Query Results ---")
    if not response.objects:
        print("No matching wines found.")
    else:
        for item in response.objects:
            wine = item.properties
            print(f"  Title: {wine.get('title')}")
            print(f"  Country: {wine.get('country')}")
            print(f"  Price: ${wine.get('price')}")
            print(f"  Points: {wine.get('points')}")
            print("-" * 20)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. Close the connection
    if client:
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Output**:
```
Successfully connected to Weaviate.
Collection 'WineReview' retrieved.

Executing hybrid search for 'pair with steak'...

--- Query Results ---
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

Connection to Weaviate closed.

```

**Errors**:
```
/code/code.py:24: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 26.65s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os
import sys

# --- 1. Check for and retrieve environment variables ---
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_API_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"FATAL: Missing environment variable '{e.args[0]}'. Please set it before running the script.")
    sys.exit(1)

# --- 2. Connect to Weaviate Cloud ---
try:
    # Use a 'with' statement for automatic connection closing
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_API_KEY),
        headers={
            "X-OpenAI-API-Key": OPENAI_API_KEY
        },
    ) as client:

        print("Successfully connected to Weaviate.")

        # --- 3. Get a handle to the 'WineReview' collection ---
        collection_name = "WineReview"
        reviews = client.collections.get(collection_name)

        # --- 4. Define the filters to be applied ---
        # The query will only consider objects that meet all these conditions.
        wine_filter = (
            Filter.by_property("price").less_than(50) &
            Filter.by_property("points").greater_than(90) &
            Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
        )

        # --- 5. Execute the hybrid query ---
        response = reviews.query.hybrid(
            query="pair with steak",
            limit=5,
            alpha=0.5,
            filters=wine_filter
        )

        # --- 6. Print the results ---
        print("\n--- Query Results ---")
        print("Top 5 wines that pair with steak (price < $50, points > 90):\n")

        if not response.objects:
            print("No matching wines found.")
        else:
            for item in response.objects:
                wine = item.properties
                # Using .get() provides a default value if a key is missing
                print(
                    f"- Title: {wine.get('title', 'N/A')}\n"
                    f"  Country: {wine.get('country', 'N/A')}\n"
                    f"  Price: ${wine.get('price', 0)}\n"
                    f"  Points: {wine.get('points', 0)}\n"
                )

except Exception as e:
    print(f"An error occurred: {e}")

```

**Output**:
```
Successfully connected to Weaviate.

--- Query Results ---
Top 5 wines that pair with steak (price < $50, points > 90):

- Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.0
  Points: 92

- Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.0
  Points: 91

- Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.0
  Points: 91

- Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.0
  Points: 93

- Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.0
  Points: 92


```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 22.35s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

# This script assumes you have a .env file with the following variables:
# WCD_TEST_URL="your-weaviate-cloud-url"
# WCD_TEST_KEY="your-weaviate-cloud-api-key"
# OPENAI_API_KEY="your-openai-api-key"
#
# If you don't have a .env file, you can set these environment variables manually.
# for example:
# export WCD_TEST_URL="your-weaviate-cloud-url"
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv not installed, proceeding with environment variables.")


# 1. Connect to Weaviate Cloud
# For more information, see: https://docs.weaviate.io/weaviate/client-libraries/python#weaviate-cloud
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Required for text2vec-openai
        }
    )
    print("Successfully connected to Weaviate.")

    # 2. Get the 'WineReview' collection
    # For more information, see: https://docs.weaviate.io/weaviate/manage-data/collections
    reviews = client.collections.get("WineReview")

    # 3. Define the filter conditions
    # For more information on filtering, see: https://docs.weaviate.io/weaviate/search/filters
    
    # Filter for price < 50 and points > 90
    price_and_points_filter = Filter.all_of([
        Filter.by_property("price").less_than(50),
        Filter.by_property("points").greater_than(90),
    ])

    # Filter for at least one of the specified substrings in the review_body
    # The `like` operator with wildcards (*) is used for substring matching.
    keyword_filter = Filter.any_of([
        Filter.by_property("review_body").like("*spice*"),
        Filter.by_property("review_body").like("*fruit*"),
        Filter.by_property("review_body").like("*berry*"),
        Filter.by_property("review_body").like("*cherry*"),
        Filter.by_property("review_body").like("*honey*"),
    ])
    
    # Combine all filters using the AND logic
    combined_filters = Filter.all_of([
        price_and_points_filter,
        keyword_filter
    ])

    # 4. Perform the hybrid search
    # For more information on hybrid search, see: https://docs.weaviate.io/weaviate/search/hybrid
    response = reviews.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Equal weighting between vector and keyword search
        limit=5,
        filters=combined_filters,
        # Specify the properties to be returned for each result
        return_properties=["title", "country", "price", "points"]
    )

    # 5. Print the results
    print("\nFound wines matching 'pair with steak' (price < 50, points > 90):")
    if len(response.objects) > 0:
        for wine in response.objects:
            print("-" * 20)
            print(f"Title: {wine.properties['title']}")
            print(f"Country: {wine.properties['country']}")
            print(f"Price: ${wine.properties['price']:.2f}")
            print(f"Points: {wine.properties['points']}")
    else:
        print("No matching wines found.")

except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection to Weaviate
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate.

Found wines matching 'pair with steak' (price < 50, points > 90):
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

Connection to Weaviate closed.

```

---

### gemini/gemini-2.5-flash

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 10.35s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.exceptions import WeaviateConnectionError

# Retrieve environment variables
# WCD_TEST_URL should be something like "https://YOUR_CLUSTER_URL.weaviate.cloud"
# WCD_TEST_KEY should be your Weaviate API key
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

# --- Input Validation ---
if not weaviate_url:
    print("Error: WCD_TEST_URL environment variable is not set.", file=sys.stderr)
    print("Please set it to your Weaviate Cloud URL (e.g., 'https://your-cluster-1234.weaviate.cloud').", file=sys.stderr)
    sys.exit(1)

if not weaviate_api_key:
    print("Error: WCD_TEST_KEY environment variable is not set.", file=sys.stderr)
    print("Please set it to your Weaviate API key.", file=sys.stderr)
    sys.exit(1)

print(f"Attempting to connect to Weaviate Cloud at: {weaviate_url}")

client = None  # Initialize client to None to ensure it's handled in finally block
try:
    # --- Connect to Weaviate Cloud ---
    # Using weaviate.connect_to_wcs for Weaviate Cloud Services (WCS)
    client = weaviate.connect_to_wcs(
        cluster_url=weaviate_url,
        api_key=weaviate_api_key
    )

    # --- Check Server Readiness ---
    # The is_ready() method checks if the Weaviate instance is operational
    if client.is_ready():
        print("Successfully connected to Weaviate and the server is ready to accept requests.")
    else:
        print("Successfully connected to Weaviate, but the server is NOT ready to accept requests.")
        print("This might indicate an issue with the Weaviate instance itself, even if the connection parameters are correct.")

except WeaviateConnectionError as e:
    print(f"Failed to connect to Weaviate Cloud. Check your URL and API key.", file=sys.stderr)
    print(f"Error details: {e}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(1)
finally:
    # --- Close the connection ---
    # It's good practice to close the client connection when done to release resources.
    if client:
        client.close()
        print("Weaviate client connection closed.")

```

**Output**:
```
Attempting to connect to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud

```

**Errors**:
```
/code/code.py:29: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
An unexpected error occurred: connect_to_wcs() got an unexpected keyword argument 'api_key'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 3.88s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Load environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url:
    raise ValueError("WCD_TEST_URL environment variable not set.")
if not weaviate_api_key:
    raise ValueError("WCD_TEST_KEY environment variable not set.")

print(f"Attempting to connect to Weaviate Cloud at: {weaviate_url}")

client = None  # Initialize client to None for finally block

try:
    # Connect to the Weaviate Cloud instance
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key)
    )

    # Check if the server is ready to accept requests
    if client.is_ready():
        print("Weaviate server is ready and connected successfully!")
    else:
        print("Weaviate server is not ready.")
        # Optionally, you might want to raise an error here or retry
        raise ConnectionError("Weaviate server reported not ready.")

except Exception as e:
    print(f"An error occurred: {e}")
    # Re-raise the exception after printing, or handle as appropriate
    raise

finally:
    # Ensure the client connection is closed
    if client:
        print("Closing Weaviate client connection.")
        client.close()
```

**Output**:
```
Attempting to connect to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Weaviate server is ready and connected successfully!
Closing Weaviate client connection.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 17.40s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes.config as wvc_config
from weaviate.exceptions import NotFoundError, WeaviateClientError

# --- Configuration ---
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_KEY = os.getenv("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"

# --- Validate Environment Variables ---
if not WCD_URL or not WCD_KEY:
    print("Error: Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")
    print("Example: export WCD_TEST_URL='https://YOUR_CLUSTER_ID.weaviate.network'")
    print("Example: export WCD_TEST_KEY='YOUR_API_KEY'")
    exit(1)

# --- Weaviate Client Connection ---
client = None
try:
    print(f"Connecting to Weaviate Cloud at {WCD_URL}...")
    client = weaviate.connect_to_wcd(
        url=WCD_URL,
        api_key=WCD_KEY
    )
    print("Successfully connected to Weaviate.")

    # --- Delete Collection if it exists ---
    print(f"Attempting to delete collection '{COLLECTION_NAME}' if it exists...")
    try:
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted successfully.")
    except NotFoundError:
        print(f"Collection '{COLLECTION_NAME}' did not exist, skipping deletion.")
    except WeaviateClientError as e:
        # Catch other potential Weaviate client errors during deletion
        print(f"An unexpected Weaviate client error occurred during deletion: {e}")
        raise # Re-raise if it's not just a NotFoundError

    # --- Define Collection Properties ---
    properties = [
        wvc_config.Property(
            name="name",
            data_type=wvc_config.DataType.TEXT,
            description="The name of the product."
        ),
        wvc_config.Property(
            name="description",
            data_type=wvc_config.DataType.TEXT,
            description="A detailed description of the product."
        ),
        wvc_config.Property(
            name="price",
            data_type=wvc_config.DataType.NUMBER,
            description="The price of the product."
        ),
        wvc_config.Property(
            name="in_stock",
            data_type=wvc_config.DataType.BOOLEAN,
            description="Whether the product is currently in stock."
        ),
    ]

    # --- Create the Collection ---
    print(f"Creating collection '{COLLECTION_NAME}' with specified properties...")
    collection = client.collections.create(
        wvc_config.CollectionConfig(
            name=COLLECTION_NAME,
            properties=properties,
            # It's good practice to explicitly configure the vectorizer.
            # Use `Configure.Vectorizer.none()` if you don't need vector search for this collection,
            # otherwise Weaviate might default to a vectorizer like 'text2vec-contextionary'.
            vectorizer_config=wvc_config.Configure.Vectorizer.none(),
            # You can also configure inverted index, sharding, etc. here if needed
            # inverted_index_config=wvc_config.Configure.InvertedIndex.defaults()
        )
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # --- Optional: Verify the collection details (after creation) ---
    print("\nVerifying collection details:")
    retrieved_collection = client.collections.get(COLLECTION_NAME)
    print(f"Collection Name: {retrieved_collection.name}")
    print("Properties:")
    for prop in retrieved_collection.config.properties:
        print(f"  - Name: {prop.name}, DataType: {prop.data_type.value}, Description: {prop.description}")
    print(f"Vectorizer: {retrieved_collection.config.vectorizer_config.vectorizer_type.value}")


except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    # --- Close the client connection ---
    if client:
        client.close()
        print("Weaviate client connection closed.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.exceptions import NotFoundError, WeaviateClientError
ImportError: cannot import name 'NotFoundError' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 6.97s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# --- Configuration ---
# Get Weaviate Cloud URL and API Key from environment variables
WEAVIATE_CLUSTER_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"

# Ensure environment variables are set
if not WEAVIATE_CLUSTER_URL:
    raise ValueError("Environment variable WCD_TEST_URL not set.")
if not WEAVIATE_API_KEY:
    raise ValueError("Environment variable WCD_TEST_KEY not set.")

print(f"Connecting to Weaviate at: {WEAVIATE_CLUSTER_URL}")

# --- Connect to the Weaviate Cloud instance ---
client = None # Initialize client to None
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_CLUSTER_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY)
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- Delete the collection if it already exists (for testing purposes) ---
    print(f"Checking if collection '{COLLECTION_NAME}' exists...")
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted successfully.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist. Proceeding with creation.")

    # --- Create the collection ---
    print(f"Creating collection '{COLLECTION_NAME}' with specified properties...")
    products_collection = client.collections.create(
        COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
        # You can add other configurations like vectorizer, RAG, etc. here if needed
        # For example, if you want a default vectorizer:
        # vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_contextionary()
    )

    print(f"\nCollection '{products_collection.name}' created successfully!")
    print("Collection schema details (a subset):")
    # You can inspect the created collection's schema
    # Note: products_collection is a Collection object, not the full schema dictionary
    # To get the full schema, you would typically fetch it via client.collections.get()
    
    # For demonstration, let's verify some properties
    retrieved_collection = client.collections.get(COLLECTION_NAME)
    print(f"- Name: {retrieved_collection.name}")
    print(f"- Properties defined: {', '.join([p.name for p in retrieved_collection.config.properties])}")

except ValueError as e:
    print(f"Configuration Error: {e}")
except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Weaviate Connection Error: Could not connect to Weaviate. Please check your URL and API Key.")
    print(f"Details: {e}")
except weaviate.exceptions.WeaviateBaseError as e:
    print(f"An error occurred with Weaviate: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- Close connection ---
    if client:
        client.close()
        print("\nWeaviate connection closed.")

```

**Output**:
```
Connecting to Weaviate at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate Cloud.
Checking if collection 'DemoProducts' exists...
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted successfully.
Creating collection 'DemoProducts' with specified properties...

Collection 'DemoProducts' created successfully!
Collection schema details (a subset):
- Name: DemoProducts
An unexpected error occurred: '_ConfigCollection' object has no attribute 'properties'

Weaviate connection closed.

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 8.30s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
import os

# Ensure environment variables are set for Weaviate Cloud connection
# For local testing, you might set them like:
# os.environ["WCD_TEST_URL"] = "YOUR_WEAVIATE_CLOUD_URL"
# os.environ["WCD_TEST_KEY"] = "YOUR_WEAVIATE_API_KEY"

# Define the collection name
COLLECTION_NAME = "DemoProducts"

# 1. Connect to Weaviate Cloud
print("Connecting to Weaviate Cloud...")
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        # Add inference API keys if you plan to use generative models or vectorizers
        # e.g., headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]}
    )
    print("Successfully connected to Weaviate Cloud.")
except KeyError as e:
    print(f"Error: Environment variable {e} not set. Please set WCD_TEST_URL and WCD_TEST_KEY.")
    exit(1)
except Exception as e:
    print(f"An error occurred during connection: {e}")
    exit(1)

try:
    # 2. Check if the collection already exists and delete it if it does
    print(f"Checking if collection '{COLLECTION_NAME}' exists...")
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted successfully.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist.")

    # 3. Define the properties for the collection
    product_properties = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),  # Floating-point number
        Property(name="in_stock", data_type=DataType.BOOL), # Boolean value
    ]

    # 4. Create the collection with the specified properties
    print(f"Creating collection '{COLLECTION_NAME}' with specified properties...")
    client.collections.create(
        name=COLLECTION_NAME,
        properties=product_properties,
        # You might want to add a vectorizer, e.g., Configure.Vectors.text2vec_weaviate()
        # For this example, we'll omit it for simplicity as it wasn't explicitly requested
        # but it's crucial for semantic search capabilities.
        # vector_config=Configure.Vectors.text2vec_weaviate(),
        # generative_config=Configure.Generative.openai(), # Example generative config
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # Optional: Verify the collection creation
    print(f"\nVerifying collection '{COLLECTION_NAME}' configuration:")
    retrieved_collection = client.collections.get(COLLECTION_NAME)
    print(f"Collection Name: {retrieved_collection.name}")
    print("Properties:")
    for prop in retrieved_collection.config.get().properties:
        print(f"  - Name: {prop.name}, DataType: {prop.data_type}")

except Exception as e:
    print(f"An error occurred during collection management: {e}")
finally:
    # 5. Close the client connection
    if client:
        print("Closing Weaviate connection.")
        client.close()
    print("Script finished.")
```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate Cloud.
Checking if collection 'DemoProducts' exists...
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted successfully.
Creating collection 'DemoProducts' with specified properties...
Collection 'DemoProducts' created successfully.

Verifying collection 'DemoProducts' configuration:
Collection Name: DemoProducts
Properties:
  - Name: name, DataType: text
  - Name: description, DataType: text
  - Name: price, DataType: number
  - Name: in_stock, DataType: boolean
Closing Weaviate connection.
Script finished.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.72s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType

# 1. Connect to Weaviate Cloud
# Get credentials from environment variables
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_API_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_URL or not WCD_API_KEY:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    print("Please set them before running the script:")
    print("  export WCD_TEST_URL=\"YOUR_WEAVIATE_CLUSTER_URL\"")
    print("  export WCD_TEST_KEY=\"YOUR_WEAVIATE_API_KEY\"")
    exit(1)

client = None # Initialize client to None for finally block
collection_name = "DemoProducts"

try:
    print(f"Connecting to Weaviate Cloud at: {WCD_URL}")
    client = weaviate.connect_to_wcs(
        cluster_url=WCD_URL,
        api_key=WCD_API_KEY,
        # You might want to add a `timeout` here for larger operations or slow connections
        # timeout_config=(5, 60) # (connect_timeout, read_timeout)
    )
    print("Successfully connected to Weaviate.")

    # 2. Define the collection schema
    # First, check if the collection already exists and delete it if it does
    # This ensures a clean slate for the example
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it...")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    print(f"Creating collection '{collection_name}'...")
    products_collection = client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        # You can add vectorizer, generatives, etc., here if needed
        # vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),
        # generatives_config=wvc.config.Configure.Generative.openai(),
    )
    print(f"Collection '{collection_name}' created successfully.")

    # 3. Batch import 50 arbitrary objects
    print("Starting batch import of 50 objects...")
    with products_collection.data.batch_uploader() as batch:
        for i in range(1, 51):
            properties_data = {
                "name": f"Product {i}",
                "description": f"This is the description for Product {i}. It's a fantastic item!",
            }
            batch.insert(
                properties=properties_data,
                # You can also add custom vectors per object here if needed:
                # vector=[0.1, 0.2, ...]
            )
    print("Batch import complete.")

    # 4. Print the number of objects in the collection
    print(f"Getting object count for '{collection_name}'...")
    # Use the aggregate method to get the total count
    response = products_collection.aggregate.over_all(total_count=True)
    
    if response:
        print(f"Number of objects in '{collection_name}': {response.total_count}")
    else:
        print("Could not retrieve object count.")

except weaviate.exceptions.WeaviateException as e:
    print(f"An Weaviate error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the client connection in the finally block to ensure it's always closed
    if client:
        client.close()
        print("Weaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud

```

**Errors**:
```
/code/code.py:22: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
Traceback (most recent call last):
  File "/code/code.py", line 22, in <module>
    client = weaviate.connect_to_wcs(
  File "/usr/local/lib/python3.9/site-packages/deprecation.py", line 260, in _inner
    return function(*args, **kwargs)
  File "/usr/local/lib/python3.9/site-packages/typing_extensions.py", line 2956, in wrapper
    return arg(*args, **kwargs)
TypeError: connect_to_wcs() got an unexpected keyword argument 'api_key'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 76, in <module>
    except weaviate.exceptions.WeaviateException as e:
AttributeError: module 'weaviate.exceptions' has no attribute 'WeaviateException'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.19s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.config import Property, DataType
from weaviate.exceptions import WeaviateBaseError, NotFoundError

# --- 1. Get Weaviate Cloud credentials from environment variables ---
# Make sure to set these environment variables before running the script:
# export WCD_TEST_URL="YOUR_WEAVIATE_CLOUD_URL"
# export WCD_TEST_KEY="YOUR_WEAVIATE_CLOUD_API_KEY"

weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

if not weaviate_url or not weaviate_api_key:
    print("Error: Weaviate Cloud URL (WCD_TEST_URL) or API Key (WCD_TEST_KEY) not found in environment variables.")
    print("Please set them before running the script.")
    exit(1)

collection_name = "DemoProducts"
num_objects_to_import = 50

# --- 2. Connect to Weaviate Cloud ---
print(f"Connecting to Weaviate Cloud at {weaviate_url}...")
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
        # You can add a `timeout_seconds` here if needed for slower connections
        # timeout_seconds=60
    )
    print("Successfully connected to Weaviate Cloud.")
except WeaviateBaseError as e:
    print(f"Failed to connect to Weaviate Cloud: {e}")
    exit(1)

try:
    # --- 3. Create or Get the collection ---
    # First, try to get the collection. If it doesn't exist, create it.
    try:
        collection = client.collections.get(collection_name)
        print(f"Collection '{collection_name}' already exists.")
        # Optionally, clear the collection before importing new data if desired for a clean run
        # print(f"Clearing existing objects from '{collection_name}'...")
        # collection.data.delete_many(where={
        #     "path": ["name"],
        #     "operator": "Exists",
        #     "valueText": True
        # })
        # print("Collection cleared.")

    except NotFoundError:
        print(f"Collection '{collection_name}' not found. Creating it...")
        collection = client.collections.create(
            name=collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ]
        )
        print(f"Collection '{collection_name}' created successfully with properties: name (text), description (text).")
    except WeaviateBaseError as e:
        print(f"An unexpected error occurred while getting/creating the collection: {e}")
        client.close()
        exit(1)

    # --- 4. Prepare arbitrary objects for batch import ---
    print(f"\nPreparing {num_objects_to_import} objects for import...")
    data_objects = []
    for i in range(num_objects_to_import):
        data_objects.append(
            {
                "name": f"Product {i+1}",
                "description": f"This is a detailed description for product number {i+1}."
            }
        )

    # --- 5. Batch import objects into the collection ---
    print(f"Starting batch import of {len(data_objects)} objects...")
    # Using dynamic batching for efficient imports
    with collection.batch.dynamic() as batch:
        for i, data_row in enumerate(data_objects):
            batch.add_object(
                properties=data_row,
            )
            # You can add a condition to stop if too many errors occur
            if batch.number_errors > 10:
                print("Batch import stopped due to excessive errors.")
                break
        
        # After the loop, the batch context manager will automatically flush any remaining objects.

    # --- 6. Check batch import results ---
    print("\nBatch import complete.")
    if batch.number_errors > 0:
        print(f"Number of objects that failed to import: {batch.number_errors}")
        if batch.failed_objects:
            print(f"First failed object details: {batch.failed_objects[0]}")
    else:
        print("All objects imported successfully (no errors reported by the batcher).")

    # --- 7. Print the total number of objects in the collection ---
    print(f"\nCounting objects in collection '{collection_name}'...")
    total_objects = collection.query.aggregate(
        total_count=True
    ).total_count
    print(f"Total number of objects in '{collection_name}': {total_objects}")

except WeaviateBaseError as e:
    print(f"An error occurred during the process: {e}")

finally:
    # --- 8. Close the client connection ---
    if client:
        print("\nClosing Weaviate client connection...")
        client.close()
        print("Connection closed.")

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.exceptions import WeaviateBaseError, NotFoundError
ImportError: cannot import name 'NotFoundError' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 25.85s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure
import os

# --- Configuration ---
# 1. Weaviate Cloud connection details from environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")

# Ensure environment variables are set
if not WEAVIATE_URL or not WEAVIATE_API_KEY:
    raise ValueError(
        "Please set the 'WCD_TEST_URL' and 'WCD_TEST_KEY' environment variables."
        "Example: export WCD_TEST_URL='YOUR_WEAVIATE_CLUSTER_URL' "
        "export WCD_TEST_KEY='YOUR_WEAVIATE_API_KEY'"
    )

COLLECTION_NAME = "DemoProducts"
NUMBER_OF_OBJECTS_TO_IMPORT = 50

# --- Weaviate Client Operations ---
print("Attempting to connect to Weaviate Cloud...")
try:
    # 1. Connect to Weaviate Cloud using Auth credentials
    # The 'with' statement ensures the client connection is properly closed after operations.
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
        # If your Weaviate Cloud instance requires an OpenAI key for default vectorization,
        # you might need to uncomment and set the header below:
        # headers={"X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY", "")}
    ) as client:
        print("Successfully connected to Weaviate.")

        # 2. Collection Management: Define and create the collection
        # Check if the collection already exists and delete it for a clean run.
        if client.collections.exists(COLLECTION_NAME):
            print(f"Deleting existing collection: '{COLLECTION_NAME}'...")
            client.collections.delete(COLLECTION_NAME)
            print(f"Collection '{COLLECTION_NAME}' deleted.")

        print(f"Creating new collection: '{COLLECTION_NAME}'...")
        # Create the collection with 'name' and 'description' text properties.
        # We explicitly set vectorizer_config to 'none' as vectors are not required for this task
        # and it avoids potential dependencies on external inference APIs.
        products_collection = client.collections.create(
            name=COLLECTION_NAME,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            vectorizer_config=Configure.Vectorizer.none()
        )
        print(f"Collection '{COLLECTION_NAME}' created successfully.")

        # 3. Data Operations: Batch import objects
        print(f"Starting batch import of {NUMBER_OF_OBJECTS_TO_IMPORT} objects...")
        # Use a fixed-size batch for efficient data ingestion.
        # The batch size can be adjusted based on your cluster's capacity and network latency.
        with products_collection.batch.fixed_size(batch_size=100) as batch:
            for i in range(NUMBER_OF_OBJECTS_TO_IMPORT):
                product_data = {
                    "name": f"Product {i+1}",  # Start product numbering from 1
                    "description": f"This is the description for Product {i+1}. It highlights its features and benefits."
                }
                batch.add_object(
                    properties=product_data
                )
        print("Batch import process completed.")

        # Check for any errors that occurred during the batch import
        if products_collection.batch.number_errors > 0:
            print(f"WARNING: {products_collection.batch.number_errors} errors occurred during batch import.")
            # Optionally print details of failed objects
            # for error in products_collection.batch.failed_objects:
            #     print(f"  Failed object: {error.data_object}, Error: {error.message}")

        # 4. Retrieve and print the number of objects in the collection
        print(f"Retrieving the total number of objects in '{COLLECTION_NAME}'...")
        # The aggregate.over_all method with total_count=True provides the count efficiently.
        aggregate_response = products_collection.aggregate.over_all(total_count=True)
        object_count = aggregate_response.total_count

        print(f"\n--- Results ---")
        print(f"Number of objects in '{COLLECTION_NAME}': {object_count}")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Could not connect to Weaviate: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Script execution finished.")
```

**Output**:
```
Attempting to connect to Weaviate Cloud...
Successfully connected to Weaviate.
Deleting existing collection: 'DemoProducts'...
Collection 'DemoProducts' deleted.
Creating new collection: 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Starting batch import of 50 objects...
Batch import process completed.
An unexpected error occurred: '_BatchCollectionWrapper' object has no attribute 'number_errors'
Script execution finished.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:196: DeprecationWarning: Dep024: You are using the `vectorizer_config` argument in `collection.config.create()`, which is deprecated.
            Use the `vector_config` argument instead.
            
  warnings.warn(

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 13.78s)

**Generated Code**:
```python
import os
from weaviate.connect import WeaviateClient
# import weaviate.collections.classes as wvc # Only needed if you use specific enums like wvc.QueryReference

# 1. Load environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if all necessary environment variables are set
if not all([WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY]):
    print("Error: Please set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    print("Example: export WCD_TEST_URL='YOUR_WEAVIATE_CLOUD_URL'")
    print("         export WCD_TEST_KEY='YOUR_WEAVIATE_CLOUD_API_KEY'")
    print("         export OPENAI_API_KEY='YOUR_OPENAI_API_KEY'")
    exit(1)

client = None # Initialize client to None for finally block
try:
    # 2. Connect to Weaviate Cloud
    # The X-OpenAI-Api-Key is passed in the headers for the text2vec-openai vectorizer
    print("Connecting to Weaviate Cloud...")
    client = WeaviateClient(
        weaviate_url=WEAVIATE_URL,
        weaviate_api_key=WEAVIATE_API_KEY,
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )
    print("Successfully connected to Weaviate.")

    collection_name = "WineReview"
    search_query = "dessert wine"
    max_results_limit = 2
    properties_to_return = ["title", "country", "price", "points"]

    print(f"\nQuerying '{collection_name}' for '{search_query}' (limit: {max_results_limit})...")

    # 3. Get the collection and perform the near_text query
    wine_reviews_collection = client.collections.get(collection_name)

    response = wine_reviews_collection.query.near_text(
        query=search_query,
        limit=max_results_limit,
        return_properties=properties_to_return
    )

    # 4. Print the results
    if response.objects:
        print("\n--- Matching Wines ---")
        for i, obj in enumerate(response.objects):
            # Access properties via obj.properties dictionary
            title = obj.properties.get("title", "N/A")
            country = obj.properties.get("country", "N/A")
            price = obj.properties.get("price", "N/A")
            points = obj.properties.get("points", "N/A")

            print(f"\nResult {i + 1}:")
            print(f"  Title: {title}")
            print(f"  Country: {country}")
            print(f"  Price: ${price if price is not None else 'N/A'}")
            print(f"  Points: {points if points is not None else 'N/A'}")
            # Optionally, you can also print the distance/certainty if available
            # if hasattr(obj, 'distance') and obj.distance is not None:
            #     print(f"  Distance: {obj.distance:.4f}")
            # if hasattr(obj, 'certainty') and obj.certainty is not None:
            #     print(f"  Certainty: {obj.certainty:.4f}")
        print("\n----------------------")
    else:
        print("No matching wines found.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
finally:
    # 5. Close the Weaviate connection
    if client:
        print("\nClosing Weaviate connection...")
        client.close()
        print("Connection closed.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 2, in <module>
    from weaviate.connect import WeaviateClient
ImportError: cannot import name 'WeaviateClient' from 'weaviate.connect' (/usr/local/lib/python3.9/site-packages/weaviate/connect/__init__.py)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.71s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# --- 1. Load environment variables ---
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if required environment variables are set
if not WCD_URL:
    raise ValueError("Environment variable WCD_TEST_URL is not set.")
if not WCD_KEY:
    raise ValueError("Environment variable WCD_TEST_KEY is not set.")
if not OPENAI_API_KEY:
    raise ValueError("Environment variable OPENAI_API_KEY is not set.")

# --- 2. Connect to Weaviate Cloud ---
print("Connecting to Weaviate Cloud...")
client = None # Initialize client to None for finally block
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        },
    )
    print("Successfully connected to Weaviate!")

    # --- 3. Get the 'WineReview' collection ---
    collection_name = "WineReview"
    print(f"Accessing collection: '{collection_name}'...")
    wine_review_collection = client.collections.get(collection_name)

    # --- 4. Define the query parameters ---
    query_text = "dessert wine"
    max_results_limit = 2
    properties_to_return = ["title", "country", "price", "points"]

    print(f"Querying for: '{query_text}' with a limit of {max_results_limit} results...")

    # --- 5. Perform the near_text query ---
    response = wine_review_collection.query.near_text(
        query=query_text,
        limit=max_results_limit,
        return_properties=properties_to_return # Specify which properties to retrieve
    )

    # --- 6. Process and print the results ---
    if response.objects:
        print("\n--- Matching Wines ---")
        for i, obj in enumerate(response.objects):
            print(f"\nResult {i+1}:")
            # Access properties directly from obj.properties dictionary
            print(f"  Title: {obj.properties.get('title', 'N/A')}")
            print(f"  Country: {obj.properties.get('country', 'N/A')}")
            print(f"  Price: {obj.properties.get('price', 'N/A')}")
            print(f"  Points: {obj.properties.get('points', 'N/A')}")
    else:
        print("\nNo matching wines found for the query.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Failed to connect to Weaviate: {e}")
except weaviate.exceptions.WeaviateGRPCError as e:
    print(f"Weaviate query error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- 7. Close the Weaviate client ---
    if client:
        print("\nClosing Weaviate client...")
        client.close()
        print("Client closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate!
Accessing collection: 'WineReview'...
Querying for: 'dessert wine' with a limit of 2 results...

--- Matching Wines ---

Result 1:
  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: 24.0
  Points: 88

Result 2:
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: 40.0
  Points: 88

Closing Weaviate client...
Client closed.

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.47s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.exceptions import WeaviateException

# Ensure environment variables are set
try:
    WCD_TEST_URL = os.environ["WCD_TEST_URL"]
    WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
except KeyError:
    print("Please set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit(1)

client = None
try:
    # 1. Connect to Weaviate Cloud
    # For more information on client instantiation, see: https://www.docs.weaviate.io/weaviate/client-libraries/python
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY  # Required for text2vec-openai
        }
    )
    print("Successfully connected to Weaviate Cloud.")

    # 2. Get the 'WineReview' collection
    # For more information on managing collections, see: https://docs.weaviate.io/weaviate/manage-data/collections
    wine_review_collection = client.collections.get("WineReview")
    print("\nQuerying the 'WineReview' collection...")

    # 3. Query the collection using near_text for semantic search
    # For more information on search operations, see: https://docs.weaviate.io/weaviate/search
    response = wine_review_collection.query.near_text(
        query="dessert wine",
        limit=2,  # Limit to a maximum of 2 results
        return_properties=["title", "country", "price", "points"]
    )

    # 4. Print the results
    if response.objects:
        print(f"Found {len(response.objects)} matching wine(s):")
        for i, wine in enumerate(response.objects):
            print(f"\n--- Wine {i+1} ---")
            print(f"Title: {wine.properties['title']}")
            print(f"Country: {wine.properties['country']}")
            print(f"Price: {wine.properties['price']:.2f}")
            print(f"Points: {wine.properties['points']}")
    else:
        print("No matching wines found for 'dessert wine'.")

except WeaviateException as e:
    print(f"Weaviate error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # 5. Close the client connection
    if client:
        print("\nClosing Weaviate connection.")
        client.close()
    else:
        print("\nClient was not initialized or connection failed.")

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.exceptions import WeaviateException
ImportError: cannot import name 'WeaviateException' from 'weaviate.exceptions' (/usr/local/lib/python3.9/site-packages/weaviate/exceptions.py)

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 18.36s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wc
import os

# 1. Load environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if environment variables are set
if not all([WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY]):
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY."
    )

# 2. Connect to Weaviate Cloud
try:
    client = weaviate.WeaviateClient(
        weaviate_url=WEAVIATE_URL,
        auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY  # Required for text2vec-openai
        }
    )
    print("Successfully connected to Weaviate Cloud.")

    # Get a handle to the 'WineReview' collection
    wines = client.collections.get("WineReview")

    # 3. Define the filtering conditions
    # Condition 1: price < 50 AND points > 90
    price_points_filter = (
        wc.Filter.by_property("price").less_than(50) &
        wc.Filter.by_property("points").greater_than(90)
    )

    # Condition 2: review_body contains at least one of the substrings
    # Note: Weaviate's LIKE operator uses '*' as a wildcard.
    review_body_filter = (
        wc.Filter.by_property("review_body").like("*spice*") |
        wc.Filter.by_property("review_body").like("*fruit*") |
        wc.Filter.by_property("review_body").like("*berry*") |
        wc.Filter.by_property("review_body").like("*cherry*") |
        wc.Filter.by_property("review_body").like("*honey*")
    )

    # Combine all filters using AND
    final_filter = price_points_filter & review_body_filter

    # 4. Perform the hybrid search query
    print(f"\nSearching for wines matching 'pair with steak'...")
    response = wines.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Hybrid search alpha value
        limit=5,    # Maximum 5 results
        return_properties=["title", "country", "price", "points", "review_body"], # Include review_body to verify filter
        where_filter=final_filter
    )

    # 5. Print the results
    if response.objects:
        print("\nMatching Wines (Title, Country, Price, Points):")
        for i, o in enumerate(response.objects):
            print(f"\n--- Result {i+1} ---")
            print(f"Title: {o.properties['title']}")
            print(f"Country: {o.properties['country']}")
            print(f"Price: ${o.properties['price']:.2f}")
            print(f"Points: {o.properties['points']}")
            # Optional: Print review body to verify the filter worked
            # print(f"Review Body (Snippet): {o.properties['review_body'][:150]}...")
            # print(f"Vector: {o.vector}") # For debugging, shows vector similarity
            # print(f"Score: {o.metadata.score}") # Semantic score
            # print(f"BM25 Score: {o.metadata.additional_properties['_additional']['_rerank']['score']}") # BM25 score
    else:
        print("\nNo wines found matching the specified criteria.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Could not connect to Weaviate: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nWeaviate client closed.")
```

**Output**:
```
An error occurred: __init__() got an unexpected keyword argument 'weaviate_url'

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 9.13s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Ensure environment variables are set
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    print("Error: Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
    exit(1)

# 1. Connect to Weaviate Cloud
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        },
    )
    print("Successfully connected to Weaviate Cloud.")
    print(f"Weaviate version: {client.get_meta()['version']}")

    # 2. Get the 'WineReview' collection
    collection_name = "WineReview"
    wine_review_collection = client.collections.get(collection_name)
    print(f"Accessed collection: {collection_name}")

    # 3. Define the query parameters
    search_query = "pair with steak"
    max_results = 5
    hybrid_alpha = 0.5

    # 4. Define the filters
    # Price less than 50 AND Points greater than 90
    # AND review_body contains any of "spice", "fruit", "berry", "cherry", "honey"
    filters = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    )

    # 5. Execute the hybrid query
    print(f"\nSearching for wines matching '{search_query}' with hybrid alpha={hybrid_alpha} and filters...")
    response = wine_review_collection.query.hybrid(
        query=search_query,
        limit=max_results,
        alpha=hybrid_alpha,
        filters=filters,
        return_metadata=MetadataQuery(score=True), # Optional: returns score for debugging/analysis
        # return_properties allows you to specify which properties to retrieve,
        # making the response lighter if you only need a subset.
        # For this problem, we'll just print specific properties from the full object.
        return_properties=["title", "country", "price", "points", "review_body"]
    )

    # 6. Print the results
    if response.objects:
        print(f"\nFound {len(response.objects)} matching wines:")
        for i, obj in enumerate(response.objects):
            print(f"\n--- Result {i+1} ---")
            print(f"Title: {obj.properties.get('title', 'N/A')}")
            print(f"Country: {obj.properties.get('country', 'N/A')}")
            print(f"Price: {obj.properties.get('price', 'N/A')}")
            print(f"Points: {obj.properties.get('points', 'N/A')}")
            # print(f"Review Body (for verification): {obj.properties.get('review_body', 'N/A')[:100]}...") # Uncomment to see review_body snippet
            if obj.metadata and obj.metadata.score is not None:
                print(f"Hybrid Score: {obj.metadata.score:.4f}")
    else:
        print("\nNo wines found matching the criteria.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 7. Close the client connection
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Successfully connected to Weaviate Cloud.
Weaviate version: 1.32.3
Accessed collection: WineReview

Searching for wines matching 'pair with steak' with hybrid alpha=0.5 and filters...

Found 5 matching wines:

--- Result 1 ---
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
Hybrid Score: 0.5000

--- Result 2 ---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
Hybrid Score: 0.3765

--- Result 3 ---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Hybrid Score: 0.0451

--- Result 4 ---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Hybrid Score: 0.0162

--- Result 5 ---
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
Hybrid Score: 0.0010

Weaviate client connection closed.

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.42s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# Ensure environment variables are set
try:
    WCD_URL = os.environ["WCD_TEST_URL"]
    WCD_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"Environment variable {e} not set. Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit(1)

client = None
try:
    # 1. Connect to Weaviate Cloud using environment variables
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=Auth.api_key(WCD_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )
    print("Successfully connected to Weaviate.")

    # 2. Get the 'WineReview' collection
    wine_reviews = client.collections.get("WineReview")
    print("Accessing 'WineReview' collection.")

    # 3. Define the query and filters
    query_text = "pair with steak"
    max_results = 5
    hybrid_alpha = 0.5

    # Define the property filters
    price_filter = Filter.by_property("price").less_than(50)
    points_filter = Filter.by_property("points").greater_than(90)

    # Define the review_body substring filters using OR
    review_body_keywords_filter = (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )

    # Combine all filters using AND
    combined_filters = price_filter & points_filter & review_body_keywords_filter

    # Define the properties to return
    return_props = ["title", "country", "price", "points"]

    # 4. Perform the hybrid search with filters
    print(f"Searching for wines matching '{query_text}' with specified criteria...")
    response = wine_reviews.query.hybrid(
        query=query_text,
        alpha=hybrid_alpha,
        limit=max_results,
        filters=combined_filters,
        return_properties=return_props
    )

    # 5. Print the results
    if response.objects:
        print(f"\nFound {len(response.objects)} wines that best match 'pair with steak' "
              "with price < 50, points > 90, and relevant keywords in review_body:")
        print("-" * 80)
        for i, wine in enumerate(response.objects):
            props = wine.properties
            print(f"Result {i+1}:")
            print(f"  Title: {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price: ${props.get('price', 'N/A'):.2f}")
            print(f"  Points: {props.get('points', 'N/A')}")
            print("-" * 80)
    else:
        print("\nNo wines found matching the specified criteria.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Could not connect to Weaviate: {e}")
except weaviate.exceptions.WeaviateClientError as e:
    print(f"Weaviate client error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # 6. Close the client connection
    if client:
        client.close()
        print("Weaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate.
Accessing 'WineReview' collection.
Searching for wines matching 'pair with steak' with specified criteria...

Found 5 wines that best match 'pair with steak' with price < 50, points > 90, and relevant keywords in review_body:
--------------------------------------------------------------------------------
Result 1:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.00
  Points: 92
--------------------------------------------------------------------------------
Result 2:
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.00
  Points: 91
--------------------------------------------------------------------------------
Result 3:
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.00
  Points: 91
--------------------------------------------------------------------------------
Result 4:
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.00
  Points: 93
--------------------------------------------------------------------------------
Result 5:
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.00
  Points: 92
--------------------------------------------------------------------------------
Weaviate client connection closed.

```

---

### gemini/gemini-2.5-flash-lite

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 1.70s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud URL and API key from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise ValueError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(weaviate_api_key),
)

# Check if the server is ready to accept requests
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 2.33s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# Retrieve Weaviate Cloud URL and API key from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise EnvironmentError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the connection (good practice, although not strictly required by the prompt to do anything else)
client.close()

print("Successfully connected to Weaviate Cloud and confirmed server readiness.")
```

**Output**:
```
Successfully connected to Weaviate Cloud and confirmed server readiness.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 6.33s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud URL and API key from environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")

# Ensure environment variables are set
if not WEAVIATE_URL:
    raise ValueError("WCD_TEST_URL environment variable not set.")
if not WEAVIATE_API_KEY:
    raise ValueError("WCD_TEST_KEY environment variable not set.")

# Define the collection name
collection_name = "DemoProducts"

# Initialize the Weaviate client
try:
    client = weaviate.Client(
        url=WEAVIATE_URL,
        auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY),
    )
except Exception as e:
    print(f"Error initializing Weaviate client: {e}")
    exit()

# Check if the collection exists and delete it if it does
try:
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it...")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist.")
except Exception as e:
    print(f"Error checking or deleting collection '{collection_name}': {e}")
    exit()

# Define the schema for the "DemoProducts" collection
collection_schema = {
    "name": collection_name,
    "properties": [
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
        {"name": "price", "dataType": ["number"]},
        {"name": "in_stock", "dataType": ["boolean"]},
    ],
}

# Create the collection
try:
    print(f"Creating collection '{collection_name}'...")
    client.collections.create(collection_schema)
    print(f"Collection '{collection_name}' created successfully.")

    # Verify the collection creation
    if client.collections.exists(collection_name):
        print(f"Verification successful: Collection '{collection_name}' exists.")
    else:
        print(f"Verification failed: Collection '{collection_name}' does not exist after creation attempt.")

except Exception as e:
    print(f"Error creating collection '{collection_name}': {e}")

finally:
    # You might want to close the client connection if it's managed manually,
    # but the Weaviate Python client typically handles this.
    pass

```

**Output**:
```
Error initializing Weaviate client: __init__() got an unexpected keyword argument 'url'

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:19: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 4.26s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Retrieve Weaviate Cloud credentials from environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

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
    print(f"Collection '{collection_name}' already exists. Deleting it first.")
    client.collections.delete(collection_name)

# Create the collection with specified properties
print(f"Creating collection '{collection_name}'...")
products_collection = client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Successfully created collection: {products_collection.name}")

# Close connection (optional, but good practice if you're done interacting)
# In many applications, you might keep the client open for the duration.
# client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists. Deleting it first.
Creating collection 'DemoProducts'...
Successfully created collection: DemoProducts

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 58640), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 3.44s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth
import os

# Replace with your actual WCD_TEST_URL and WCD_TEST_KEY
# For demonstration purposes, we're using environment variables.
# Make sure to set these variables in your environment before running the script.
# export WCD_TEST_URL="YOUR_WEAVIATE_CLOUD_URL"
# export WCD_TEST_KEY="YOUR_WEAVIATE_CLOUD_API_KEY"

weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_key = os.environ.get("WCD_TEST_KEY")

if not weaviate_url or not weaviate_key:
    raise ValueError("Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_key),
)

collection_name = "DemoProducts"

try:
    # Check if the collection already exists and delete it if it does
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # Create the collection with specified properties
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

    # You can now interact with the collection, for example, adding data:
    # print("Adding sample data...")
    # demo_products_collection = client.collections.get(collection_name)
    # demo_products_collection.data.insert({
    #     "name": "Laptop",
    #     "description": "A powerful laptop for professionals",
    #     "price": 1200.50,
    #     "in_stock": True
    # })
    # demo_products_collection.data.insert({
    #     "name": "Mouse",
    #     "description": "Ergonomic wireless mouse",
    #     "price": 25.99,
    #     "in_stock": False
    # })
    # print("Sample data added.")

except Exception as e:
    print(f"An error occurred: {e}")

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
Weaviate client connection closed.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 2.82s)

**Generated Code**:
```python
import os
import weaviate

# Connect to Weaviate Cloud using environment variables
try:
    client = weaviate.connect_to_weaviate_cloud(
        url=os.environ["WCD_TEST_URL"],
        auth_credentials=weaviate.auth.ApiKey(os.environ["WCD_TEST_KEY"]),
    )
except KeyError as e:
    print(f"Environment variable {e} not set. Please set WCD_TEST_URL and WCD_TEST_KEY.")
    exit(1)
except Exception as e:
    print(f"Failed to connect to Weaviate: {e}")
    exit(1)

collection_name = "DemoProducts"

# Check if the collection exists, create it if not
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

# Prepare objects for batch import
objects_to_import = []
for i in range(50):
    objects_to_import.append({
        "name": f"Product {i+1}",
        "description": f"This is the description for product {i+1}."
    })

# Perform batch import
try:
    with client.batch as batch:
        batch.add_objects(
            collection_name=collection_name,
            objects=objects_to_import,
        )
    print(f"Successfully imported {len(objects_to_import)} objects into '{collection_name}'.")
except Exception as e:
    print(f"Error during batch import: {e}")
    exit(1)

# Get and print the number of objects in the collection
try:
    count = client.collections.get(collection_name).count()
    print(f"Number of objects in '{collection_name}': {count}")
except Exception as e:
    print(f"Error getting object count: {e}")
```

**Output**:
```
Failed to connect to Weaviate: module 'weaviate.auth' has no attribute 'ApiKey'

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 3.26s)

**Generated Code**:
```python
import weaviate
import os

# Get Weaviate Cloud credentials from environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_KEY = os.getenv("WCD_TEST_KEY")

COLLECTION_NAME = "DemoProducts"

if not WEAVIATE_URL or not WEAVIATE_KEY:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

try:
    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=weaviate.Auth.api_key(WEAVIATE_KEY),
    )

    # Get or create the "DemoProducts" collection
    if not client.collections.exists(COLLECTION_NAME):
        client.collections.create(
            COLLECTION_NAME,
            properties=[
                weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
                weaviate.Property(name="description", data_type=weaviate.DataType.TEXT),
            ],
        )
        print(f"Collection '{COLLECTION_NAME}' created.")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")

    collection = client.collections.get(COLLECTION_NAME)

    # Prepare data for batch import
    data_rows = [
        {
            "name": f"Product {i+1}",
            "description": f"This is the description for product number {i+1}."
        } for i in range(50)
    ]

    # Perform batch import
    print("Starting batch import...")
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
        # Print the first few failed objects for debugging
        for i, failed_obj in enumerate(failed_objects[:5]):
            print(f"  Failed object {i+1}: {failed_obj}")
    else:
        print("Batch import completed successfully.")

    # Print the number of objects in the collection
    num_objects = len(collection)
    print(f"Number of objects in collection '{COLLECTION_NAME}': {num_objects}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    if 'client' in locals() and client:
        client.close()
        print("Weaviate client closed.")
```

**Output**:
```
An error occurred: module weaviate has no attribute Auth

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 4.01s)

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
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
    )
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL and WCD_TEST_KEY to connect to your Weaviate Cloud instance.")
    exit()

# Define the collection name
collection_name = "DemoProducts"

# Check if the collection already exists, if not, create it
if not client.collections.exists(collection_name):
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created.")
else:
    print(f"Collection '{collection_name}' already exists.")

# Get the collection object
collection = client.collections.get(collection_name)

# Prepare 50 arbitrary objects for batch import
objects_to_import = []
for i in range(50):
    objects_to_import.append({
        "properties": {
            "name": f"Product {i}",
            "description": f"Description for product {i}"
        }
    })

# Batch import the objects using fixed_size for efficiency
# The batch size can be adjusted based on your needs and Weaviate instance capacity.
# Here, we set it to 50, matching the number of objects we are importing.
try:
    with collection.batch.fixed_size(batch_size=50) as batch:
        for obj in objects_to_import:
            batch.add_object(
                properties=obj["properties"]
            )
    print("Batch import of 50 objects completed.")
except Exception as e:
    print(f"An error occurred during batch import: {e}")

# Print the number of objects in the collection
count_response = collection.query.aggregate.by_class(
    returning_property="name"
)
total_objects = count_response.class_aggregations[0].total_count

print(f"\nNumber of objects in the '{collection_name}' collection: {total_objects}")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists.
Batch import of 50 objects completed.

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 60, in <module>
    count_response = collection.query.aggregate.by_class(
AttributeError: '_QueryCollection' object has no attribute 'aggregate'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 58652), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 2.32s)

**Generated Code**:
```python
import os
import weaviate

# Get credentials from environment variables
weaviate_url = os.environ["WCD_TEST_URL"]
weaviate_api_key = os.environ["WCD_TEST_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the query and limit
query_text = "dessert wine"
max_results = 2

# Build the GraphQL query
query = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({"concepts": [query_text]})
    .with_limit(max_results)
)

# Execute the query
try:
    response = query.do()

    # Process and print the results
    if response and "data" in response and "Get" in response["data"]:
        wines = response["data"]["Get"]["WineReview"]
        if wines:
            print(f"Found {len(wines)} matching wines for '{query_text}':")
            for wine in wines:
                print(f"- Title: {wine.get('title', 'N/A')}")
                print(f"  Country: {wine.get('country', 'N/A')}")
                print(f"  Price: {wine.get('price', 'N/A')}")
                print(f"  Points: {wine.get('points', 'N/A')}")
        else:
            print(f"No wines found matching '{query_text}'.")
    else:
        print("An error occurred or no data was returned.")
        print(response)

except Exception as e:
    print(f"An error occurred during the query: {e}")

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 6.01s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Retrieve connection details and API keys from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Ensure all required environment variables are set
if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    raise EnvironmentError("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")

try:
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

    # Query for wines matching "dessert wine"
    query_text = "dessert wine"
    max_results = 2

    response = collection.query.near_text(
        query=query_text,
        limit=max_results,
        # Specify the properties you want to retrieve
        include_properties=["title", "country", "price", "points"]
    )

    # Print the details of matching wines
    if response.objects:
        print(f"Wines best matching '{query_text}':")
        for obj in response.objects:
            print(f"  Title: {obj.properties.get('title')}")
            print(f"  Country: {obj.properties.get('country')}")
            print(f"  Price: {obj.properties.get('price')}")
            print(f"  Points: {obj.properties.get('points')}")
            print("-" * 20)
    else:
        print(f"No wines found matching '{query_text}'.")

except weaviate.UnexpectedStatusCodeException as e:
    print(f"Weaviate API error: {e}")
except weaviate.BuiltConnectionError as e:
    print(f"Failed to connect to Weaviate: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the client connection
    if 'client' in locals() and client:
        client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing UnexpectedStatusCodeException from weaviate is deprecated. Import UnexpectedStatusCodeException from its module: weaviate.exceptions
  _Warnings.root_module_import(name, map_[name])
Traceback (most recent call last):
  File "/code/code.py", line 31, in <module>
    response = collection.query.near_text(
TypeError: near_text() got an unexpected keyword argument 'include_properties'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/code/code.py", line 52, in <module>
    except weaviate.BuiltConnectionError as e:
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 145, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute BuiltConnectionError

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 2.63s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import Filter
import os

# Connect to Weaviate Cloud
# WCD_TEST_URL and WCD_TEST_KEY should be set as environment variables
# OPENAI_API_KEY should also be set as an environment variable
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )

    # Get the WineReview collection
    wine_reviews = client.collections.get("WineReview")

    # Query for "dessert wine" with a limit of 2 results
    response = wine_reviews.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the results
    if response.objects:
        print("Found wines matching 'dessert wine':")
        for wine in response.objects:
            print(f"- Title: {wine.properties.get('title')}")
            print(f"  Country: {wine.properties.get('country')}")
            print(f"  Price: {wine.properties.get('price')}")
            print(f"  Points: {wine.properties.get('points')}")
    else:
        print("No wines found matching 'dessert wine'.")

except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the client connection
    if 'client' in locals() and client:
        client.close()
```

**Output**:
```
An error occurred: module weaviate has no attribute Auth

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 4.38s)

**Generated Code**:
```python
import os
import weaviate

# Ensure you have the necessary environment variables set
# WCD_TEST_URL: URL of your Weaviate Cloud instance
# WCD_TEST_KEY: API key for your Weaviate Cloud instance
# OPENAI_API_KEY: OpenAI API key for the vectorizer

try:
    weaviate_url = os.environ["WCD_TEST_URL"]
    weaviate_api_key = os.environ["WCD_TEST_KEY"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit()

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the query
query = "pair with steak"

# Define the hybrid search parameters
alpha = 0.5
limit = 5

# Define the filters
# Filter for price < 50 AND points > 90
price_and_points_filter = {
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
        }
    ]
}

# Filter for review_body containing "spice", "fruit", "berry", "cherry", or "honey"
review_body_filter = {
    "operator": "Or",
    "operands": [
        {
            "path": ["review_body"],
            "operator": "ContainsAny",
            "valueText": "spice"
        },
        {
            "path": ["review_body"],
            "operator": "ContainsAny",
            "valueText": "fruit"
        },
        {
            "path": ["review_body"],
            "operator": "ContainsAny",
            "valueText": "berry"
        },
        {
            "path": ["review_body"],
            "operator": "ContainsAny",
            "valueText": "cherry"
        },
        {
            "path": ["review_body"],
            "operator": "ContainsAny",
            "valueText": "honey"
        }
    ]
}

# Combine all filters using an AND operator
combined_filter = {
    "operator": "And",
    "operands": [
        price_and_points_filter,
        review_body_filter
    ]
}


# Build the GraphQL query
try:
    response = (
        client.query
        .get("WineReview", ["title", "country", "price", "points", "review_body"])
        .with_hybrid(query=query, alpha=alpha)
        .with_where(combined_filter)
        .with_limit(limit)
        .do()
    )

    # Print the results
    if "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
        wines = response["data"]["Get"]["WineReview"]
        if wines:
            print(f"Found {len(wines)} wines matching your criteria:")
            for wine in wines:
                print("-" * 30)
                print(f"Title: {wine.get('title', 'N/A')}")
                print(f"Country: {wine.get('country', 'N/A')}")
                print(f"Price: ${wine.get('price', 'N/A')}")
                print(f"Points: {wine.get('points', 'N/A')}")
                # print(f"Review Body: {wine.get('review_body', 'N/A')[:100]}...") # Optionally print a snippet of review
        else:
            print("No wines found matching your criteria.")
    else:
        print("An error occurred or no data was returned.")
        print(response)

except weaviate.errors.UnexpectedStatusCodeException as e:
    print(f"Weaviate API error: {e.status_code}")
    print(f"Response body: {e.response.text}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:19: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 19, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.08s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Get Weaviate Cloud credentials and OpenAI API key from environment variables
WCD_URL = os.environ.get("WCD_TEST_URL")
WCD_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not all([WCD_URL, WCD_KEY, OPENAI_API_KEY]):
    raise ValueError("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_URL,
    auth_credentials=Auth.api_key(WCD_KEY),
    headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Define the search query and parameters
search_query = "pair with steak"
max_results = 5
alpha_value = 0.5
required_substrings = ["spice", "fruit", "berry", "cherry", "honey"]

# Perform the hybrid search with filters
response = collection.query.hybrid(
    query=search_query,
    limit=max_results,
    alpha=alpha_value,
    filters=(
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(required_substrings)
    ),
    # Specify which properties to return
    return_properties=["title", "country", "price", "points"],
    return_metadata=MetadataQuery(score=True)
)

# Print the results
if response.objects:
    print(f"Found {len(response.objects)} wines matching your query:")
    for obj in response.objects:
        print(f"- Title: {obj.properties['title']}, Country: {obj.properties['country']}, Price: ${obj.properties['price']}, Points: {obj.properties['points']}, Score: {obj.metadata.score:.2f}")
else:
    print("No wines found matching your criteria.")

# Close the Weaviate client connection
client.close()
```

**Output**:
```
Found 5 wines matching your query:
- Title: Soléna 2009 Guadalupe Vineyard Pinot Noir, Country: US, Price: $40.0, Points: 92, Score: 0.50
- Title: Bink 2014 Pinot Noir (Anderson Valley), Country: US, Price: $49.0, Points: 91, Score: 0.38
- Title: Doña Silvina 2011 Malbec (Mendoza), Country: Argentina, Price: $27.0, Points: 91, Score: 0.05
- Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji), Country: Hungary, Price: $25.0, Points: 93, Score: 0.02
- Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico), Country: Italy, Price: $0.0, Points: 92, Score: 0.00

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.95s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.query import Filter, HybridFusion
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Add inference API keys as needed
        }
    )
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit()

# Get the WineReview collection
try:
    wine_reviews = client.collections.get("WineReview")
except Exception as e:
    print(f"Error: Could not get collection 'WineReview'. Make sure it exists.")
    print(e)
    client.close()
    exit()

# Define the search query and filters
query_text = "pair with steak"
max_results = 5
hybrid_alpha = 0.5

# Define the filters for price, points, and review body content
review_filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
)

# Perform the hybrid search
response = wine_reviews.query.hybrid(
    query=query_text,
    alpha=hybrid_alpha,
    filters=review_filters,
    limit=max_results,
    return_properties=["title", "country", "price", "points", "review_body"]
)

# Print the results
if response.objects:
    print(f"Found {len(response.objects)} wines that match your criteria:")
    for wine in response.objects:
        properties = wine.properties
        print(f"  Title: {properties.get('title')}")
        print(f"  Country: {properties.get('country')}")
        print(f"  Price: ${properties.get('price')}")
        print(f"  Points: {properties.get('points')}")
        # Optionally print the review body to verify the filter
        # print(f"  Review Body: {properties.get('review_body')[:100]}...")
        print("-" * 20)
else:
    print("No wines found matching your criteria.")

# Close the client connection
client.close()
```

**Output**:
```
Found 5 wines that match your criteria:
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

---

### openai/gpt-5-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 34.96s)

**Generated Code**:
```python
import os
import weaviate

def main():
    url = os.environ["WCD_TEST_URL"]
    api_key = os.environ["WCD_TEST_KEY"]

    client = weaviate.connect_to_wcs(
        cluster_url=url,
        auth_credentials=weaviate.auth.AuthApiKey(api_key=api_key),
    )
    try:
        print(f"Server ready: {client.is_ready()}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Server ready: True

```

**Errors**:
```
/code/code.py:8: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 16.37s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

try:
    assert client.is_ready()
finally:
    client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 27.95s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.classes.config import Property, DataType, Configure

# Read connection details from environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

# Connect and ensure the collection is (re)created
with weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=AuthApiKey(api_key=WCD_TEST_KEY),
) as client:
    collection_name = "DemoProducts"

    # If the collection exists, delete it first
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    # Create the collection with the requested properties
    client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
        # Use no vectorizer to avoid requiring any specific vectorization module
        vectorizer_config=Configure.Vectorizer.none(),
    )

    print(f"Collection '{collection_name}' created.")
```

**Output**:
```
Collection 'DemoProducts' created.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:196: DeprecationWarning: Dep024: You are using the `vectorizer_config` argument in `collection.config.create()`, which is deprecated.
            Use the `vector_config` argument instead.
            
  warnings.warn(

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 19.67s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    # Read connection details from environment variables
    cluster_url = os.getenv("WCD_TEST_URL")
    api_key = os.getenv("WCD_TEST_KEY")

    if not cluster_url or not api_key:
        raise EnvironmentError("Please set both WCD_TEST_URL and WCD_TEST_KEY environment variables.")

    # Connect to the Weaviate Cloud instance
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
            name=collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
                Property(name="price", data_type=DataType.NUMBER),
                Property(name="in_stock", data_type=DataType.BOOL),
            ],
        )

        print(f"Created collection: {products_collection.name}")

    finally:
        # Close connection
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Created collection: DemoProducts

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 21.43s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables:
# - WCD_TEST_URL: Weaviate Cloud URL
# - WCD_TEST_KEY: Weaviate Cloud API key
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

try:
    collection_name = "DemoProducts"

    # If the collection exists, delete it first
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    # Create the collection with the requested properties
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
    )

    print(f"Created collection: {collection_name}")

finally:
    client.close()
```

**Output**:
```
Created collection: DemoProducts

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 23.58s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 16.79s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 26.80s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

# Connect to Weaviate Cloud using env vars WCD_TEST_URL and WCD_TEST_KEY
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

try:
    # Create the collection if it doesn't exist
    collection_name = "DemoProducts"
    if not client.collections.exists(collection_name):
        client.collections.create(
            collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            # Uses built-in inference on Weaviate Cloud; no extra API key needed
            vector_config=Configure.Vectors.text2vec_weaviate(),
        )

    collection = client.collections.get(collection_name)

    # Batch import 50 objects
    with collection.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}",
                }
            )

    # Print the number of objects in the collection
    agg = collection.aggregate.over_all(total_count=True)
    print(agg.total_count)

finally:
    client.close()
```

**Output**:
```
50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 19.09s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Connect to Weaviate Cloud (WCS) and pass the OpenAI key for text2vec-openai
client = weaviate.connect_to_wcs(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=AuthApiKey(os.environ["WCD_TEST_KEY"]),
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
)

try:
    collection = client.collections.get("WineReview")

    res = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"],
    )

    for obj in res.objects:
        props = obj.properties or {}
        print(
            f"Title: {props.get('title')}, "
            f"Country: {props.get('country')}, "
            f"Price: {props.get('price')}, "
            f"Points: {props.get('points')}"
        )
finally:
    client.close()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)), Country: US, Price: 24.0, Points: 88
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast), Country: US, Price: 40.0, Points: 88

```

**Errors**:
```
/code/code.py:6: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.52s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={"X-OpenAI-API-Key": os.environ["OPENAI_API_KEY"]},
)

collection = client.collections.get("WineReview")

response = collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"],
)

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

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 25.31s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    # Connect to Weaviate Cloud using environment variables
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # Needed for text2vec-openai
        }
    ) as client:
        collection = client.collections.get("WineReview")

        # Semantic search for "dessert wine" with a maximum of 2 results
        response = collection.query.near_text(
            query="dessert wine",
            limit=2,
            return_properties=["title", "country", "price", "points"]
        )

        # Print desired fields
        for obj in response.objects:
            props = obj.properties or {}
            print(f"Title: {props.get('title')}")
            print(f"Country: {props.get('country')}")
            print(f"Price: {props.get('price')}")
            print(f"Points: {props.get('points')}")
            print()

if __name__ == "__main__":
    main()
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

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 37.16s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 20.32s)

**Generated Code**:
```python

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 20.40s)

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
        # Needed for text2vec-openai vectorizer
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

try:
    collection = client.collections.get("WineReview")

    # Filters:
    # - price < 50
    # - points > 90
    # - review_body contains any of: spice, fruit, berry, cherry, honey
    text_filter = (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )

    filters = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        text_filter
    )

    # Hybrid search
    response = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=filters,
        return_properties=["title", "country", "price", "points"]
    )

    # Print results
    for obj in response.objects:
        props = obj.properties or {}
        title = props.get("title")
        country = props.get("country")
        price = props.get("price")
        points = props.get("points")
        print(f"Title: {title} | Country: {country} | Price: ${price} | Points: {points}")

finally:
    client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir | Country: US | Price: $40.0 | Points: 92
Title: Bink 2014 Pinot Noir (Anderson Valley) | Country: US | Price: $49.0 | Points: 91
Title: Doña Silvina 2011 Malbec (Mendoza) | Country: Argentina | Price: $27.0 | Points: 91
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji) | Country: Hungary | Price: $25.0 | Points: 93
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico) | Country: Italy | Price: $0.0 | Points: 92

```

---

### openai/gpt-5-mini-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 15.83s)

**Generated Code**:
```python
import os
import sys
import weaviate

# Read connection info from environment
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

# Create client for Weaviate Cloud using API key auth
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(WCD_TEST_KEY),
)

# Check if the server is ready to accept requests
if client.is_ready():
    print("Weaviate server is ready.")
    sys.exit(0)
else:
    print("Weaviate server is not ready.")
    sys.exit(1)
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 12.21s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Read environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise RuntimeError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=AuthApiKey(api_key=WCD_TEST_KEY),
)

# Check that the server is ready to accept requests
assert client.is_ready()

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

**Status**: ❌ FAILURE (runtime: 16.51s)

**Generated Code**:
```python
#!/usr/bin/env python3
"""
Create a Weaviate class (collection) "DemoProducts" with properties:
- name (text)
- description (text)
- price (number)
- in_stock (boolean)

Uses environment variables:
- WCD_TEST_URL  (Weaviate Cloud URL)
- WCD_TEST_KEY  (Weaviate Cloud API key)
"""

import os
import sys
from weaviate import Client, AuthApiKey

def main():
    url = os.environ.get("WCD_TEST_URL")
    api_key = os.environ.get("WCD_TEST_KEY")

    if not url or not api_key:
        print("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.", file=sys.stderr)
        sys.exit(1)

    # Connect to Weaviate Cloud
    client = Client(url=url, auth_client_secret=AuthApiKey(api_key=api_key))

    class_name = "DemoProducts"

    # Check existing classes and delete if present
    schema = client.schema.get()
    existing_classes = [c.get("class") for c in schema.get("classes", [])]
    if class_name in existing_classes:
        print(f"Class '{class_name}' exists — deleting it first.")
        client.schema.delete_class(class_name)

    # Define the class schema
    demo_products_class = {
        "class": class_name,
        "properties": [
            {"name": "name", "dataType": ["text"]},
            {"name": "description", "dataType": ["text"]},
            {"name": "price", "dataType": ["number"]},
            {"name": "in_stock", "dataType": ["boolean"]},
        ],
    }

    # Create the class
    client.schema.create_class(demo_products_class)
    print(f"Class '{class_name}' created.")

if __name__ == "__main__":
    main()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:27: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(url=url, auth_client_secret=AuthApiKey(api_key=api_key))
Traceback (most recent call last):
  File "/code/code.py", line 54, in <module>
    main()
  File "/code/code.py", line 27, in main
    client = Client(url=url, auth_client_secret=AuthApiKey(api_key=api_key))
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 18.68s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.exceptions import UnexpectedStatusCodeException

# Read env vars
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables", file=sys.stderr)
    sys.exit(1)

# Connect to Weaviate Cloud
auth = AuthApiKey(api_key=WCD_TEST_KEY)
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=auth
)

collection_name = "DemoProducts"

# Delete the collection/class if it already exists
try:
    client.schema.delete_class(collection_name)
    print(f"Deleted existing collection/class: {collection_name}")
except UnexpectedStatusCodeException as e:
    # Usually a 404 when it doesn't exist; ignore
    print(f"No existing collection to delete: {collection_name} (continuing)")
except Exception as e:
    # Other errors should be surfaced
    client.close()
    raise

# Define the class (collection) schema
demo_products_class = {
    "class": collection_name,
    "description": "Demo products collection",
    "properties": [
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
        {"name": "price", "dataType": ["number"]},
        {"name": "in_stock", "dataType": ["boolean"]},
    ],
}

# Create the collection/class
client.schema.create_class(demo_products_class)
print(f"Created collection/class: {collection_name}")

# Close connection
client.close()
```

**Errors**:
```
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

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 12.28s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    # Read Weaviate Cloud credentials from environment
    url = os.environ.get("WCD_TEST_URL")
    api_key = os.environ.get("WCD_TEST_KEY")
    if not url or not api_key:
        raise SystemExit("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=url,
        auth_credentials=Auth.api_key(api_key),
    )

    try:
        class_name = "DemoProducts"

        # If the collection already exists, delete it first
        if client.collections.exists(class_name):
            print(f"Collection '{class_name}' exists — deleting it...")
            client.collections.delete(class_name)

        # Create the collection with the requested properties
        print(f"Creating collection '{class_name}'...")
        client.collections.create(
            class_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
                Property(name="price", data_type=DataType.NUMBER),
                Property(name="in_stock", data_type=DataType.BOOL),
            ],
        )

        print(f"Collection '{class_name}' created successfully.")
    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection 'DemoProducts' exists — deleting it...
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 18.86s)

**Generated Code**:
```python
# Requires: pip install weaviate-client
import os
import weaviate

# Read Weaviate Cloud credentials from environment
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise RuntimeError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables")

# Create client (using API key auth for Weaviate Cloud)
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.auth.AuthApiKey(WCD_TEST_KEY),
)

# Class schema for DemoProducts
class_schema = {
    "class": "DemoProducts",
    "description": "Demo products with name and description",
    "properties": [
        {"name": "name", "dataType": ["text"]},
        {"name": "description", "dataType": ["text"]},
    ],
}

# Create the class if it doesn't exist
existing = client.schema.get()
existing_classes = [c["class"] for c in existing.get("classes", [])]
if "DemoProducts" not in existing_classes:
    client.schema.create_class(class_schema)
else:
    print("Class 'DemoProducts' already exists, will append objects to it.")

# Batch import 50 objects
with client.batch as batch:
    batch.batch_size = 50  # flush after 50 objects (fits this import)
    for i in range(1, 51):
        obj = {
            "name": f"Product {i}",
            "description": f"Description {i}",
        }
        batch.add_data_object(obj, "DemoProducts")

# Query aggregate count of objects in DemoProducts
agg = client.query.aggregate("DemoProducts").with_fields("meta { count }").do()
try:
    count = agg["data"]["Aggregate"]["DemoProducts"][0]["meta"]["count"]
except Exception:
    # Fallback if response shape unexpected
    count = None

print(f"Number of objects in 'DemoProducts': {count}")
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

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 21.12s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 15.73s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

def main():
    # Read env vars
    try:
        cluster_url = os.environ["WCD_TEST_URL"]
        api_key = os.environ["WCD_TEST_KEY"]
    except KeyError as e:
        print(f"Missing environment variable: {e}. Please set WCD_TEST_URL and WCD_TEST_KEY.", file=sys.stderr)
        sys.exit(1)

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key),
    )

    collection_name = "DemoProducts"

    try:
        # Create collection if it doesn't exist
        if not client.collections.exists(collection_name):
            client.collections.create(
                collection_name,
                properties=[
                    Property(name="name", data_type=DataType.TEXT),
                    Property(name="description", data_type=DataType.TEXT),
                ]
            )
            print(f"Created collection '{collection_name}'")
        else:
            print(f"Collection '{collection_name}' already exists")

        # Get collection handle
        collection = client.collections.get(collection_name)

        # Batch import 50 objects
        with collection.batch.fixed_size(batch_size=50) as batch:
            for i in range(50):
                batch.add_object(
                    properties={
                        "name": f"Product {i}",
                        "description": f"Description {i}"
                    }
                )
            # leaving the context will flush the batch

        # Report any failed objects
        failed = collection.batch.failed_objects
        if failed:
            print(f"Batch completed with {len(failed)} failed objects")
        else:
            print("Batch completed successfully without failed objects")

        # Count objects in the collection by iterating (fine for small datasets)
        count = sum(1 for _ in collection.iterator())
        print(f"Number of objects in '{collection_name}': {count}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection 'DemoProducts' already exists
Batch completed successfully without failed objects
Number of objects in 'DemoProducts': 50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 20.67s)

**Generated Code**:
```python
import os
from weaviate import Client, auth

def main():
    # Read environment variables
    weaviate_url = os.environ.get("WCD_TEST_URL")
    weaviate_api_key = os.environ.get("WCD_TEST_KEY")
    openai_api_key = os.environ.get("OPENAI_API_KEY")  # provided per your note

    if not weaviate_url or not weaviate_api_key:
        raise SystemExit("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

    # Connect to Weaviate Cloud
    client = Client(
        url=weaviate_url,
        auth_client_secret=auth.AuthApiKey(api_key=weaviate_api_key),
        # If your remote text2vec-openai module requires the OpenAI key via header,
        # include it. Otherwise this can be omitted.
        additional_headers={"X-OpenAI-Api-Key": openai_api_key} if openai_api_key else None,
    )

    # Build and run the semantic query
    query_text = "dessert wine"
    response = (
        client.query
        .get("WineReview", ["title", "country", "price", "points"])
        .with_near_text({"concepts": [query_text]})
        .with_limit(2)
        .do()
    )

    # Parse and print results
    items = response.get("data", {}).get("Get", {}).get("WineReview", [])
    if not items:
        print("No matching wines found.")
        return

    for idx, item in enumerate(items, start=1):
        title = item.get("title")
        country = item.get("country")
        price = item.get("price")
        points = item.get("points")
        print(f"Result {idx}:")
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
/code/code.py:14: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = Client(
Traceback (most recent call last):
  File "/code/code.py", line 51, in <module>
    main()
  File "/code/code.py", line 14, in main
    client = Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 14.31s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth

# Read required environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY or not OPENAI_API_KEY:
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
    sys.exit(1)

# Connect to Weaviate Cloud, forwarding the OpenAI API key header for text2vec-openai
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Query for "dessert wine", maximum 2 results
    response = collection.query.near_text(
        query="dessert wine",
        limit=2
    )

    # Iterate results and print selected properties
    if not getattr(response, "objects", None):
        print("No results found.")
    else:
        for obj in response.objects:
            props = getattr(obj, "properties", {}) or {}
            title = props.get("title")
            country = props.get("country")
            price = props.get("price")
            points = props.get("points")

            print(f"Title: {title}")
            print(f"Country: {country}")
            print(f"Price: {price}")
            print(f"Points: {points}")
            print("-" * 40)

finally:
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

**Status**: ✅ SUCCESS (runtime: 16.66s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    # Read required environment variables
    try:
        cluster_url = os.environ["WCD_TEST_URL"]
        wcd_key = os.environ["WCD_TEST_KEY"]
        openai_key = os.environ["OPENAI_API_KEY"]
    except KeyError as e:
        raise SystemExit(f"Missing environment variable: {e}")

    # Connect to Weaviate Cloud and provide OpenAI API key for the text2vec-openai vectorizer
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(wcd_key),
        headers={"X-OpenAI-Api-Key": openai_key},
    )

    try:
        collection = client.collections.get("WineReview")
    except Exception as e:
        client.close()
        raise SystemExit(f"Could not access collection 'WineReview': {e}")

    # Semantic search for "dessert wine", limit to max 2 results
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print results
    if not response.objects:
        print("No matching wines found.")
    else:
        for idx, obj in enumerate(response.objects, start=1):
            props = obj.properties or {}
            title = props.get("title", "<no title>")
            country = props.get("country", "<unknown>")
            price = props.get("price", "<unknown>")
            points = props.get("points", "<unknown>")

            print(f"Result {idx}:")
            print(f"  Title:   {title}")
            print(f"  Country: {country}")
            print(f"  Price:   {price}")
            print(f"  Points:  {points}")
            print()

    client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
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


```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 15.76s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY or not OPENAI_API_KEY:
    raise EnvironmentError(
        "Please set WCD_TEST_URL, WCD_TEST_KEY and OPENAI_API_KEY environment variables."
    )

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
)

# Build the WHERE filter: price < 50 AND points > 90 AND (review_body LIKE any of the substrings)
where_filter = {
    "operator": "And",
    "operands": [
        {"path": ["price"], "operator": "LessThan", "valueNumber": 50},
        {"path": ["points"], "operator": "GreaterThan", "valueNumber": 90},
        {
            "operator": "Or",
            "operands": [
                {"path": ["review_body"], "operator": "Like", "valueString": "%spice%"},
                {"path": ["review_body"], "operator": "Like", "valueString": "%fruit%"},
                {"path": ["review_body"], "operator": "Like", "valueString": "%berry%"},
                {"path": ["review_body"], "operator": "Like", "valueString": "%cherry%"},
                {"path": ["review_body"], "operator": "Like", "valueString": "%honey%"},
            ],
        },
    ],
}

# Perform hybrid search with alpha=0.5 and max 5 results
response = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query="pair with steak", alpha=0.5)
    .with_where(where_filter)
    .with_limit(5)
    .do()
)

# Extract results
items = response.get("data", {}).get("Get", {}).get("WineReview", [])

if not items:
    print("No matching wines found.")
else:
    for i, item in enumerate(items, start=1):
        title = item.get("title")
        country = item.get("country")
        price = item.get("price")
        points = item.get("points")
        print(f"{i}. Title: {title} | Country: {country} | Price: {price} | Points: {points}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 14.64s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Read required environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    raise EnvironmentError(
        "Missing one of the required environment variables: WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY"
    )

# Connect to Weaviate Cloud, passing the OpenAI API key as a header for the text2vec-openai vectorizer
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Build the hybrid query with the required filters
    query_text = "pair with steak"
    max_results = 5
    alpha = 0.5

    filters = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    )

    response = collection.query.hybrid(
        query=query_text,
        limit=max_results,
        alpha=alpha,
        filters=filters,
        return_metadata=MetadataQuery(score=True)  # score included if you need it
    )

    # Iterate and print the requested fields
    for obj in response.objects:
        props = obj.properties or {}
        title = props.get("title", "<no title>")
        country = props.get("country", "<no country>")
        price = props.get("price", "<no price>")
        points = props.get("points", "<no points>")

        print(f"Title: {title}")
        print(f"Country: {country}")
        print(f"Price: {price}")
        print(f"Points: {points}")
        print("-" * 40)

finally:
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

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 17.61s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# Ensure required environment variables are present
for var in ("WCD_TEST_URL", "WCD_TEST_KEY", "OPENAI_API_KEY"):
    if var not in os.environ:
        print(f"Environment variable {var} is not set.", file=sys.stderr)
        sys.exit(1)

# Connect to Weaviate Cloud (include OpenAI API key header for the text2vec-openai vectorizer)
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
)

try:
    collection = client.collections.get("WineReview")

    # Build the substring (review_body) any-of filter
    substrings = ["spice", "fruit", "berry", "cherry", "honey"]
    substring_filters = [
        Filter.by_property("review_body").like(f"*{s}*") for s in substrings
    ]
    review_any_filter = Filter.any_of(filters=substring_filters)

    # Price < 50 and points > 90
    price_filter = Filter.by_property("price").less_than(50)
    points_filter = Filter.by_property("points").greater_than(90)

    # Combine all filters: price & points & (any of substrings)
    combined_filter = Filter.all_of(
        filters=[price_filter, points_filter, review_any_filter]
    )

    # Perform hybrid search
    response = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # balance between keyword and vector relevance
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
            print(f"Title: {title}\nCountry: {country}\nPrice: {price}\nPoints: {points}\n---")

finally:
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

---

### openai/gpt-5-nano-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 8.80s)

**Generated Code**:
```python
import os
import weaviate

def main():
    url = os.environ.get("WCD_TEST_URL")
    api_key = os.environ.get("WCD_TEST_KEY")

    if not url or not api_key:
        raise SystemExit("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set")

    client = weaviate.Client(
        url=url,
        additional_headers={"X-API-KEY": api_key}
    )

    try:
        ready = client.is_ready()
    except Exception:
        ready = False

    print("ready" if ready else "not ready")

if __name__ == "__main__":
    main()
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
  File "/code/code.py", line 24, in <module>
    main()
  File "/code/code.py", line 11, in main
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 8.02s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Retrieve credentials from environment variables
cluster_url = os.environ["WCD_TEST_URL"]
api_key = os.environ["WCD_TEST_KEY"]

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Clean up
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.26s)

**Generated Code**:
```python

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.08s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Read Weaviate Cloud connection details from environment variables
WEAVIATE_CLOUD_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_CLOUD_API_KEY = os.environ.get("WCD_TEST_KEY")

if not WEAVIATE_CLOUD_URL or not WEAVIATE_CLOUD_API_KEY:
    raise SystemExit("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_CLOUD_URL,
    auth_credentials=Auth.api_key(WEAVIATE_CLOUD_API_KEY)
)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with the required properties
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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.89s)

**Generated Code**:
```python
# demo_create_demo_products.py

import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth

def main():
    # Read Weaviate Cloud credentials from environment
    wcd_url = os.environ.get("WCD_TEST_URL")
    wcd_key = os.environ.get("WCD_TEST_KEY")

    if not wcd_url or not wcd_key:
        raise SystemExit("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_key)
    )

    try:
        # If the collection already exists, delete it first
        if client.collections.exists("DemoProducts"):
            client.collections.delete("DemoProducts")

        # Create the collection with the required properties
        client.collections.create(
            "DemoProducts",
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
                Property(name="price", data_type=DataType.NUMBER),
                Property(name="in_stock", data_type=DataType.BOOL),
            ]
        )

        print("Collection 'DemoProducts' created successfully.")
    finally:
        client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection 'DemoProducts' created successfully.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.23s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.14s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.46s)

**Generated Code**:
```python

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.89s)

**Generated Code**:
```python

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.26s)

**Generated Code**:
```python

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.23s)

**Generated Code**:
```python

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.84s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.45s)

**Generated Code**:
```python

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.74s)

**Generated Code**:
```python

```

---

