# Weaviate Benchmark Results

Generated on: 2025-08-17 22:54:40

## Summary

- **anthropic/claude-3-7-sonnet-20250219**: 9/14 tasks successful
- **anthropic/claude-3-5-haiku-20241022**: 11/14 tasks successful
- **openai/gpt-4.1-mini-2025-04-14**: 9/14 tasks successful
- **cohere/command-a-03-2025**: 3/14 tasks successful
- **anthropic/claude-sonnet-4-20250514**: 13/14 tasks successful
- **anthropic/claude-opus-4-20250514**: 11/14 tasks successful
- **gemini/gemini-2.5-pro**: 12/14 tasks successful
- **gemini/gemini-2.5-flash**: 10/14 tasks successful
- **gemini/gemini-2.5-flash-lite**: 7/14 tasks successful
- **openai/gpt-5-2025-08-07**: 8/14 tasks successful
- **openai/gpt-5-mini-2025-08-07**: 5/14 tasks successful
- **openai/gpt-5-nano-2025-08-07**: 3/14 tasks successful
## Detailed Results

### anthropic/claude-3-7-sonnet-20250219

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 5.93s)

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

**Status**: ✅ SUCCESS (runtime: 5.05s)

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

**Status**: ❌ FAILURE (runtime: 9.62s)

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

# Connect to Weaviate Cloud
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
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 54992), raddr=('34.111.245.21', 443)>

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.50s)

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

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 8.02s)

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

# Close the client connection when done
client.close()
```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.60s)

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

# Prepare batch of objects
objects = [
    {
        "name": f"Product {i}",
        "description": f"Description for product {i}. This is a sample product."
    }
    for i in range(1, 51)
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for obj in objects:
        batch.add_object(
            properties=obj
        )

print(f"Added {len(objects)} objects to the collection")

# Count objects in the collection
count = collection.aggregate.over_all().count()
print(f"Total number of objects in the collection: {count}")

# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists
Added 50 objects to the collection

```

**Errors**:
```
/code/code.py:11: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)
Traceback (most recent call last):
  File "/code/code.py", line 51, in <module>
    count = collection.aggregate.over_all().count()
AttributeError: 'AggregateReturn' object has no attribute 'count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 59774), raddr=('34.111.245.21', 443)>

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 9.73s)

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

# Prepare 50 objects to import
data_objects = [
    {
        "name": f"Product {i+1}",
        "description": f"Description for product {i+1}. This is a sample product."
    } for i in range(50)
]

# Batch import the objects
with collection.batch.dynamic() as batch:
    for data_object in data_objects:
        batch.add_object(
            properties=data_object,
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

**Status**: ❌ FAILURE (runtime: 9.34s)

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
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 40306), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.12s)

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
    .with_additional(["certainty"])
    .objects
)

# Print the results
print("Matching wines for 'dessert wine':")
for wine in response:
    properties = wine.properties
    print(f"\nTitle: {properties.get('title', 'N/A')}")
    print(f"Country: {properties.get('country', 'N/A')}")
    print(f"Price: ${properties.get('price', 'N/A')}")
    print(f"Points: {properties.get('points', 'N/A')}")
    print(f"Certainty: {wine.metadata.certainty:.4f}")

# Close the client connection
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

**Status**: ✅ SUCCESS (runtime: 7.15s)

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

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.77s)

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

**Status**: ❌ FAILURE (runtime: 11.23s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter
from weaviate.classes.config import Configure

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
    .query
    .hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=Filter.and_(
            Filter.by_property("price").less_than(50),
            Filter.by_property("points").greater_than(90),
            Filter.or_(
                Filter.by_property("review_body").contains_any("spice"),
                Filter.by_property("review_body").contains_any("fruit"),
                Filter.by_property("review_body").contains_any("berry"),
                Filter.by_property("review_body").contains_any("cherry"),
                Filter.by_property("review_body").contains_any("honey")
            )
        )
    )
    .with_additional(["score"])
    .objects
)

# Print the results
print(f"Found {len(response)} matching wines:\n")
for wine in response:
    print(f"Title: {wine.properties.get('title')}")
    print(f"Country: {wine.properties.get('country')}")
    print(f"Price: ${wine.properties.get('price')}")
    print(f"Points: {wine.properties.get('points')}")
    print(f"Score: {wine.metadata.score:.4f}")
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
  File "/code/code.py", line 28, in <module>
    filters=Filter.and_(
AttributeError: type object 'Filter' has no attribute 'and_'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 58500), raddr=('34.111.245.21', 443)>

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
Score: 0.3764
--------------------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.0450
--------------------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.0159
--------------------------------------------------
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.0
Points: 92
Score: 0.0005
--------------------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 14.07s)

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
    
    for wine in response.objects:
        # Check if review_body contains any of the required substrings
        if "review_body" in wine.properties and wine.properties["review_body"]:
            if pattern.search(wine.properties["review_body"]):
                print(f"Title: {wine.properties.get('title', 'N/A')}")
                print(f"Country: {wine.properties.get('country', 'N/A')}")
                print(f"Price: ${wine.properties.get('price', 'N/A')}")
                print(f"Points: {wine.properties.get('points', 'N/A')}")
                print(f"Score: {wine.metadata.score}")
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
Score: 0.5
--------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.0
Points: 91
Score: 0.3765353560447693
--------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.0
Points: 91
Score: 0.04513849690556526
--------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.0
Points: 93
Score: 0.016171861439943314
--------------------------------

```

---

### anthropic/claude-3-5-haiku-20241022

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 4.78s)

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

**Status**: ✅ SUCCESS (runtime: 4.33s)

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

**Status**: ✅ SUCCESS (runtime: 11.70s)

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

**Status**: ✅ SUCCESS (runtime: 8.64s)

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

**Status**: ✅ SUCCESS (runtime: 8.92s)

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

**Status**: ✅ SUCCESS (runtime: 10.38s)

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
    auth_credentials=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY)
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
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:10: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 12.30s)

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
    # Define the collection schema
    client.collections.create(
        name="DemoProducts",
        properties=[
            weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
            weaviate.Property(name="description", data_type=weaviate.DataType.TEXT)
        ]
    )
except Exception as e:
    print(f"Collection might already exist: {e}")

# Get the collection
collection = client.collections.get("DemoProducts")

# Prepare batch import data
data_rows = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    } for i in range(50)
]

# Batch import objects
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(properties=data_row)
        
        # Optional: Handle potential batch import errors
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

# Close the client connection
client.close()
```

**Output**:
```
Collection might already exist: module weaviate has no attribute Property
Number of objects in the collection: 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.61s)

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

# Create the collection
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
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 51022), raddr=('34.111.245.21', 443)>

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
    # Perform vector search on WineReview collection
    wine_collection = client.collections.get("WineReview")
    
    # Perform hybrid search for "dessert wine"
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
    # Always close the client connection
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

**Status**: ✅ SUCCESS (runtime: 8.55s)

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

**Status**: ✅ SUCCESS (runtime: 10.84s)

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

**Status**: ❌ FAILURE (runtime: 11.62s)

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
        
        results = wine_reviews.query.hybrid(
            query="pair with steak",
            hybrid_search_options=HybridSearchOptions(alpha=0.5),
            filters=wine_reviews.query.filter.where(
                # Price less than 50
                path=["price"],
                operator="LessThan",
                value=50
            ).and_filter(
                # Points greater than 90
                path=["points"],
                operator="GreaterThan", 
                value=90
            ),
            limit=5
        )

        # Filter results to include specific substrings in review_body
        matching_wines = [
            result for result in results.objects 
            if any(substring in result.properties['review_body'].lower() 
                   for substring in ['spice', 'fruit', 'berry', 'cherry', 'honey'])
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

**Status**: ✅ SUCCESS (runtime: 8.90s)

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

**Status**: ✅ SUCCESS (runtime: 13.61s)

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

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

try:
    # Perform hybrid search with complex filtering
    response = wine_collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,  # Balance between semantic and keyword search
        fusion_type=HybridFusion.RELATIVE_SCORE,
        filters=(
            Filter.by_property("price").less_than(50) &
            Filter.by_property("points").greater_than(90) &
            (
                Filter.by_property("review_body").contains_any([
                    "spice", "fruit", "berry", "cherry", "honey"
                ])
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

---

### openai/gpt-4.1-mini-2025-04-14

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 2.44s)

**Generated Code**:
```python
import os
import weaviate

# Get environment variables
url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Create Weaviate client with API key authentication
client = weaviate.Client(
    url=url,
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

**Status**: ✅ SUCCESS (runtime: 2.63s)

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

**Status**: ❌ FAILURE (runtime: 3.56s)

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
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # sometimes needed if using OpenAI module, else can omit
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

**Status**: ✅ SUCCESS (runtime: 4.18s)

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

**Status**: ✅ SUCCESS (runtime: 5.03s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType

def main():
    # Connect to Weaviate Cloud using environment variables
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    )

    collection_name = "DemoProducts"

    # If the collection exists, delete it first
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    # Create the collection with specified properties
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
        # Optionally, you can specify a vectorizer here, e.g.:
        # vector_config=Configure.Vectors.text2vec_weaviate()
    )

    print(f"Collection '{collection_name}' created successfully.")

    # Close the client connection when done
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

**Status**: ❌ FAILURE (runtime: 5.94s)

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
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # sometimes needed for OpenAI modules, but optional here
    }
)

# Define the schema for the "DemoProducts" class
schema_class = {
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
if "DemoProducts" not in [c["class"] for c in client.schema.get()["classes"]]:
    client.schema.create_class(schema_class)

# Prepare batch import
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

**Status**: ✅ SUCCESS (runtime: 7.81s)

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

    # Get the collection (class) "DemoProducts"
    collection = client.collections.get("DemoProducts")

    # Prepare 50 arbitrary objects
    data_rows = [
        {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
        for i in range(1, 51)
    ]

    # Batch import objects
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

**Output**:
```
Number of objects in 'DemoProducts': 50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 8.35s)

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

    collection_name = "DemoProducts"

    # Check if collection exists, delete if it does (optional, to start fresh)
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    # Create collection with properties: name (text), description (text)
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        # Use a vectorizer suitable for text (recommended for Weaviate Cloud)
        vector_config=Configure.Vectors.text2vec_weaviate()
    )

    # Get the collection object
    collection = client.collections.get(collection_name)

    # Batch import 50 arbitrary objects
    with collection.batch.fixed_size(batch_size=50) as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )

    # Print the number of objects in the collection
    # Use the iterator to count objects
    count = sum(1 for _ in collection.iterator())
    print(f"Number of objects in collection '{collection_name}': {count}")

    # Close client connection
    client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Number of objects in collection 'DemoProducts': 50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 4.29s)

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
response = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({"concepts": [query_text]})
    .with_limit(2)
    .do()
)

# Extract and print results
for wine in response.get("data", {}).get("Get", {}).get("WineReview", []):
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

**Status**: ✅ SUCCESS (runtime: 5.60s)

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

# Query for wines best matching "dessert wine" with limit 2
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

**Status**: ✅ SUCCESS (runtime: 6.22s)

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

    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Perform a semantic search with near_text for "dessert wine"
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the results
    for obj in response.objects:
        props = obj.properties
        print(f"Title: {props.get('title', 'N/A')}")
        print(f"Country: {props.get('country', 'N/A')}")
        print(f"Price: {props.get('price', 'N/A')}")
        print(f"Points: {props.get('points', 'N/A')}")
        print("-" * 40)

    # Close the client connection
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

**Status**: ❌ FAILURE (runtime: 9.23s)

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
        }
    ]
}

# Define the filter for review_body containing at least one of the substrings
# Since Weaviate filters do not support "contains substring" natively,
# we use the "Like" operator with wildcards for each substring and combine with "Or"
review_body_substrings = ["spice", "fruit", "berry", "cherry", "honey"]
review_body_filters = [
    {
        "path": ["review_body"],
        "operator": "Like",
        "valueString": f"*{substr}*"
    }
    for substr in review_body_substrings
]

# Combine the review_body substring filters with OR
review_body_filter_obj = {
    "operator": "Or",
    "operands": review_body_filters
}

# Combine all filters: price & points AND (review_body substrings)
combined_filter = {
    "operator": "And",
    "operands": [
        filter_obj,
        review_body_filter_obj
    ]
}

# Perform the hybrid query
result = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query_text, alpha=0.5)
    .with_limit(5)
    .with_where(combined_filter)
    .do()
)

# Extract and print results
for wine in result.get("data", {}).get("Get", {}).get("WineReview", []):
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

**Status**: ✅ SUCCESS (runtime: 9.84s)

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

# Print the requested fields for each result
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

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 11.04s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter

# Connect to Weaviate Cloud with API key and OpenAI key in headers
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
# We use Filter.any_of for the substrings on review_body with .like("*substring*")

price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)
review_body_substrings_filter = Filter.any_of(
    filters=[
        Filter.by_property("review_body").like("*spice*"),
        Filter.by_property("review_body").like("*fruit*"),
        Filter.by_property("review_body").like("*berry*"),
        Filter.by_property("review_body").like("*cherry*"),
        Filter.by_property("review_body").like("*honey*"),
    ]
)

combined_filter = Filter.all_of(
    filters=[
        price_filter,
        points_filter,
        review_body_substrings_filter,
    ]
)

# Perform hybrid search with alpha=0.5, limit=5, with the filter applied
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

---

### cohere/command-a-03-2025

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 4.62s)

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
    if client.is_ready():
        print("Weaviate server is ready to accept requests.")
    else:
        print("Weaviate server is not ready.")
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

**Status**: ✅ SUCCESS (runtime: 3.91s)

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

**Status**: ❌ FAILURE (runtime: 4.88s)

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

**Status**: ❌ FAILURE (runtime: 4.85s)

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
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 36944), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.21s)

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
Traceback (most recent call last):
  File "/code/code.py", line 26, in <module>
    Property(name="in_stock", data_type=DataType.BOOLEAN),
  File "/usr/local/lib/python3.9/enum.py", line 429, in __getattr__
    raise AttributeError(name) from None
AttributeError: BOOLEAN
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 57706), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 4.61s)

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
    client.collections.delete(collection_name)
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
    obj = BatchObject(
        properties={
            "name": f"Product {i}",
            "description": f"Description {i}",
        }
    )
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

**Status**: ❌ FAILURE (runtime: 5.51s)

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
        if batch.failed_objects:
            print(f"Failed to import object: {batch.failed_objects[-1]}")
            break

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

**Status**: ❌ FAILURE (runtime: 5.62s)

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

# Get the collection
demo_products = client.collections.get("DemoProducts")

# Batch import 50 objects
with demo_products.batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
object_count = demo_products.aggregate.total()
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
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 41972), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 4.95s)

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
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")  # Pass OpenAI API key to Weaviate
    }
)

# Define the query
query = "dessert wine"

# Perform the hybrid search (combines vector and keyword search)
response = client.query.get(
    class_name="WineReview",
    properties=["title", "country", "price", "points"],
    hybrid={
        "query": query,
        "alpha": 0.5  # Balance between vector search and keyword search
    },
    limit=2  # Limit results to 2
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

**Status**: ✅ SUCCESS (runtime: 5.70s)

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

# Access the WineReview collection
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

**Status**: ✅ SUCCESS (runtime: 6.37s)

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

# Perform a semantic search with near_text
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_metadata=MetadataQuery(distance=True)
)

# Print the title, country, price, and points of each matching wine
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: {wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print(f"Distance: {wine.metadata.distance}")
    print("-" * 40)

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
----------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Distance: 0.4812379479408264
----------------------------------------

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 6.27s)

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
      hybrid: { query: "pair with steak", alpha: 0.5 }
      where: {
        operator: AND
        path: ["price", "points", "review_body"]
        value: [
          { operator: LessThan, value: 50 },
          { operator: GreaterThan, value: 90 },
          { operator: Like, value: ["spice", "fruit", "berry", "cherry", "honey"] }
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

**Status**: ❌ FAILURE (runtime: 6.32s)

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
        [
            Filter.by_property("price").less_than(50),
            Filter.by_property("points").greater_than(90),
            Filter.by_property("review_body").contains_any(
                ["spice", "fruit", "berry", "cherry", "honey"]
            ),
        ]
    ).as_condition(),
    return_metadata=True,  # Include metadata for scores
)

# Print the desired properties for each matching wine
for obj in response.objects:
    print(f"Title: {obj.properties['title']}")
    print(f"Country: {obj.properties['country']}")
    print(f"Price: {obj.properties['price']}")
    print(f"Points: {obj.properties['points']}")
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
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 42972), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.11s)

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
    filters=Filter.by_properties(
        price=Filter.by_property("price").less_than(50),
        points=Filter.by_property("points").greater_than(90),
        review_body=Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    )
)

# Print the results
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: {wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print("-" * 40)

# Close the client
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 24, in <module>
    filters=Filter.by_properties(
AttributeError: type object 'Filter' has no attribute 'by_properties'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 42992), raddr=('34.111.245.21', 443)>

```

---

### anthropic/claude-sonnet-4-20250514

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 6.16s)

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

**Status**: ✅ SUCCESS (runtime: 4.72s)

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

**Status**: ✅ SUCCESS (runtime: 8.89s)

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

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 6.61s)

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

**Status**: ✅ SUCCESS (runtime: 9.83s)

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

**Status**: ✅ SUCCESS (runtime: 10.86s)

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
    with demo_products.batch.dynamic() as batch:
        for obj in objects_to_insert:
            batch.add_object(obj)
    
    print("Successfully batch imported 50 objects!")
    
    # Print the number of objects in the collection
    response = demo_products.aggregate.over_all(total_count=True)
    object_count = response.total_count
    print(f"Number of objects in 'DemoProducts' collection: {object_count}")

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

**Status**: ✅ SUCCESS (runtime: 12.50s)

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
    # Create the collection with the specified properties
    collection_name = "DemoProducts"
    
    # Check if collection exists, if not create it
    if not client.collections.exists(collection_name):
        client.collections.create(
            name=collection_name,
            properties=[
                weaviate.classes.Property(
                    name="name",
                    data_type=weaviate.classes.DataType.TEXT
                ),
                weaviate.classes.Property(
                    name="description", 
                    data_type=weaviate.classes.DataType.TEXT
                )
            ]
        )
        print(f"Collection '{collection_name}' created successfully.")
    else:
        print(f"Collection '{collection_name}' already exists.")
    
    # Get the collection
    collection = client.collections.get(collection_name)
    
    # Create 50 arbitrary objects
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

**Status**: ❌ FAILURE (runtime: 11.86s)

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

**Status**: ✅ SUCCESS (runtime: 10.33s)

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

**Status**: ✅ SUCCESS (runtime: 7.31s)

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

# Close the connection
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

**Status**: ✅ SUCCESS (runtime: 11.18s)

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
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # For text2vec-openai vectorizer
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
        properties = wine.properties
        print(f"Title: {properties.get('title', 'N/A')}")
        print(f"Country: {properties.get('country', 'N/A')}")
        print(f"Price: {properties.get('price', 'N/A')}")
        print(f"Points: {properties.get('points', 'N/A')}")
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

**Status**: ✅ SUCCESS (runtime: 10.94s)

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
    
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title', 'N/A')}")
        print(f"Country: {wine.properties.get('country', 'N/A')}")
        print(f"Price: ${wine.properties.get('price', 'N/A')}")
        print(f"Points: {wine.properties.get('points', 'N/A')}")
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
/code/code.py:6: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 9.95s)

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

**Status**: ✅ SUCCESS (runtime: 15.68s)

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

---

### anthropic/claude-opus-4-20250514

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 26.14s)

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

**Status**: ✅ SUCCESS (runtime: 19.51s)

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

**Status**: ✅ SUCCESS (runtime: 39.38s)

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

**Status**: ✅ SUCCESS (runtime: 30.90s)

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

**Status**: ✅ SUCCESS (runtime: 42.07s)

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

**Status**: ✅ SUCCESS (runtime: 39.95s)

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

**Status**: ✅ SUCCESS (runtime: 33.11s)

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
    } 
    for i in range(50)
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

**Status**: ❌ FAILURE (runtime: 39.07s)

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
    # We can use the aggregate query to count objects
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

**Status**: ✅ SUCCESS (runtime: 22.91s)

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
Distance: 0.47662150859832764
--------------------------------------------------
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88
Distance: 0.4811869263648987
--------------------------------------------------

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 25.09s)

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

# Query for dessert wines
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the results
for obj in response.objects:
    properties = obj.properties
    print(f"Title: {properties.get('title', 'N/A')}")
    print(f"Country: {properties.get('country', 'N/A')}")
    print(f"Price: {properties.get('price', 'N/A')}")
    print(f"Points: {properties.get('points', 'N/A')}")
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

**Status**: ✅ SUCCESS (runtime: 35.21s)

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
    for wine in response.objects:
        print(f"Title: {wine.properties['title']}")
        print(f"Country: {wine.properties['country']}")
        print(f"Price: {wine.properties['price']}")
        print(f"Points: {wine.properties['points']}")
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

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 41.83s)

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

**Status**: ❌ FAILURE (runtime: 37.26s)

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
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 50594), raddr=('34.111.245.21', 443)>

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 44.37s)

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
    collection = client.collections.get("WineReview")
    
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
    response = collection.query.hybrid(
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

**Status**: ✅ SUCCESS (runtime: 24.23s)

**Generated Code**:
```python
#!/usr/bin/env python3

import os
import sys
import weaviate
from weaviate.auth import AuthApiKey

"""
Connects to a Weaviate Cloud (WCS) instance using environment variables
and checks if the server is ready to accept requests.
"""

# 1. Get connection details from environment variables
try:
    wcs_url = os.environ["WCD_TEST_URL"]
    wcs_api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("🛑 Error: Make sure WCD_TEST_URL and WCD_TEST_KEY environment variables are set.")
    sys.exit(1)

# 2. Prepare authentication credentials
auth_credentials = AuthApiKey(api_key=wcs_api_key)

# Initialize client to None so it's accessible in the `finally` block
client = None
try:
    # 3. Connect to your Weaviate Cloud instance
    # This is the modern syntax for the Weaviate Python client v4+
    client = weaviate.connect_to_wcs(
        cluster_url=wcs_url,
        auth_credentials=auth_credentials
    )
    print(f"Successfully created a client for Weaviate at {wcs_url}")

    # 4. Check if the server is ready
    # The .is_ready() method returns True if the server is ready, False otherwise.
    if client.is_ready():
        print("✅ Weaviate server is ready to accept requests.")
    else:
        print("⚠️ Weaviate server is NOT ready.")

except Exception as e:
    print(f"🛑 An error occurred while connecting or checking the server: {e}")

finally:
    # 5. Always close the connection
    if client:
        client.close()
        print("Connection to Weaviate closed.")

```

**Output**:
```
Successfully created a client for Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
✅ Weaviate server is ready to accept requests.
Connection to Weaviate closed.

```

**Errors**:
```
/code/code.py:29: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 19.57s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
import sys

# Get Weaviate Cloud credentials from environment variables
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
except KeyError:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    sys.exit(1)

try:
    # Connect to your Weaviate Cloud instance
    # The 'with' statement ensures the client is closed automatically
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key)
    ) as client:
        # Check if the server is ready to accept requests
        if client.is_ready():
            print(f"Successfully connected to Weaviate at {wcd_url}.")
            print("Weaviate is ready to accept requests.")
        else:
            print(f"Connected to Weaviate at {wcd_url}, but it is not ready.")

except Exception as e:
    print(f"An error occurred while connecting to Weaviate: {e}")

```

**Output**:
```
Successfully connected to Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud.
Weaviate is ready to accept requests.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 23.66s)

**Generated Code**:
```python
import weaviate
import os
import sys
from weaviate.classes.config import Property, DataType
from weaviate.classes.auth import AuthApiKey

# --- 1. Get Weaviate Cloud credentials from environment variables ---
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url or not wcd_api_key:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    sys.exit(1)

# Define the name for our collection
collection_name = "DemoProducts"
client = None  # Initialize client to None

try:
    # --- 2. Connect to Weaviate Cloud ---
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=AuthApiKey(wcd_api_key)
    )
    print("Connection successful.")

    # --- 3. Check if collection exists and delete it if it does ---
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # --- 4. Create the 'DemoProducts' collection ---
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

    print(f"Successfully created collection '{products_collection.name}'.")

    # --- Optional: Verify the schema ---
    schema = client.collections.get(collection_name).config.get()
    print("\nVerifying collection schema:")
    print(schema.properties)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- 5. Close the connection ---
    if client:
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 5, in <module>
    from weaviate.classes.auth import AuthApiKey
ModuleNotFoundError: No module named 'weaviate.classes.auth'

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 19.85s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# --- Get Weaviate credentials from environment variables ---
# Make sure you have these set in your environment
# e.g., export WCD_TEST_URL="https://your-weaviate-url.wcd.io"
#       export WCD_TEST_KEY="your-wcd-api-key"
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Check if the environment variables are set
if not wcd_url or not wcd_key:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

# --- Define the collection name ---
collection_name = "DemoProducts"

# Use a try...finally block to ensure the client is always closed
try:
    # --- Connect to the Weaviate Cloud instance ---
    # Using the latest Weaviate client syntax (v4)
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_key),
        # Optional: Add headers for your specific WCD instance
        # headers={
        #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY")
        # }
    )
    print("Connection successful.")

    # --- Delete the collection if it already exists ---
    # This is useful for starting with a clean slate during development
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # --- Create the collection ---
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

    print(f"Successfully created collection: '{products_collection.name}'")
    # You can print the configuration to verify
    # print("Collection config:")
    # print(products_collection.config.get())

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- Close the connection ---
    # The client.close() method is part of the v4 client
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Weaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Connection successful.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Successfully created collection: 'DemoProducts'
Weaviate client connection closed.

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 20.40s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# This script assumes you have the WCD_TEST_URL and WCD_TEST_KEY environment
# variables set, for example in a .env file.

# For more information on client instantiation, see:
# https://docs.weaviate.io/weaviate/client-libraries/python

try:
    # Connect to your Weaviate Cloud instance
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    )
    print("Successfully connected to Weaviate Cloud.")

    collection_name = "DemoProducts"

    # For more information on collection management, see:
    # https://docs.weaviate.io/weaviate/manage-data/collections

    # First, check if the collection already exists. If so, delete it.
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it.")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")

    # Create the "DemoProducts" collection with the specified properties.
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
    
    # You can verify the creation by getting the collection's configuration
    config = products.config.get()
    print("\nCollection Configuration:")
    print(config)


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the client connection when you're done
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate Cloud.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.

Collection Configuration:
_CollectionConfig(name='DemoProducts', description=None, generative_config=None, inverted_index_config=_InvertedIndexConfig(bm25=_BM25Config(b=0.75, k1=1.2), cleanup_interval_seconds=60, index_null_state=False, index_property_length=False, index_timestamps=False, stopwords=_StopwordsConfig(preset=<StopwordsPreset.EN: 'en'>, additions=None, removals=None)), multi_tenancy_config=_MultiTenancyConfig(enabled=False, auto_tenant_creation=False, auto_tenant_activation=False), properties=[_Property(name='name', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer=None, vectorizer_configs={}), _Property(name='description', description=None, data_type=<DataType.TEXT: 'text'>, index_filterable=True, index_range_filters=False, index_searchable=True, nested_properties=None, tokenization=<Tokenization.WORD: 'word'>, vectorizer_config=None, vectorizer=None, vectorizer_configs={}), _Property(name='price', description=None, data_type=<DataType.NUMBER: 'number'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer=None, vectorizer_configs={}), _Property(name='in_stock', description=None, data_type=<DataType.BOOL: 'boolean'>, index_filterable=True, index_range_filters=False, index_searchable=False, nested_properties=None, tokenization=None, vectorizer_config=None, vectorizer=None, vectorizer_configs={})], references=[], replication_config=_ReplicationConfig(factor=1, async_enabled=False, deletion_strategy=<ReplicationDeletionStrategy.NO_AUTOMATED_RESOLUTION: 'NoAutomatedResolution'>), reranker_config=None, sharding_config=_ShardingConfig(virtual_per_physical=128, desired_count=1, actual_count=1, desired_virtual_count=128, actual_virtual_count=128, key='_id', strategy='hash', function='murmur3'), vector_index_config=None, vector_index_type=None, vectorizer_config=None, vectorizer=None, vector_config={'default': _NamedVectorConfig(vectorizer=_NamedVectorizerConfig(vectorizer=<Vectorizers.NONE: 'none'>, model={}, source_properties=None), vector_index_config=_VectorIndexConfigHNSW(multi_vector=None, quantizer=None, cleanup_interval_seconds=300, distance_metric=<VectorDistances.COSINE: 'cosine'>, dynamic_ef_min=100, dynamic_ef_max=500, dynamic_ef_factor=8, ef=-1, ef_construction=128, filter_strategy=<VectorFilterStrategy.SWEEPING: 'sweeping'>, flat_search_cutoff=40000, max_connections=32, skip=False, vector_cache_max_objects=1000000000000))})

Connection to Weaviate closed.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 30.34s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.auth as wa
from weaviate.classes.config import Property, DataType

# --- 1. Configuration ---
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_API_KEY = os.getenv("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"

# Check for environment variables
if not WCD_URL or not WCD_API_KEY:
    raise ValueError(
        "WCD_TEST_URL and WCD_TEST_KEY environment variables must be set."
    )

print("Connecting to Weaviate Cloud...")

# --- 2. Connect to Weaviate Cloud ---
# Use a `try...finally` block to ensure the client is closed properly.
# The `with` statement is the recommended Pythonic way to handle this.
try:
    with weaviate.connect_to_wcs(
        cluster_url=WCD_URL,
        auth_credentials=wa.AuthApiKey(WCD_API_KEY),
    ) as client:

        print(f"Successfully connected to Weaviate: {client.is_ready()}")

        # --- 3. Recreate the Collection ---
        # To ensure the script is repeatable, we first delete the collection if it exists.
        if client.collections.exists(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it.")
            client.collections.delete(COLLECTION_NAME)

        print(f"Creating collection '{COLLECTION_NAME}'...")
        client.collections.create(
            name=COLLECTION_NAME,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            # If you are not using a generative module, you can specify the vectorizer.
            # For example, using the free `text2vec-openai` model:
            # vectorizer_config=Configure.Vectorizer.text2vec_openai()
        )
        print("Collection created successfully.")

        # --- 4. Batch Import Data ---
        # Get the collection object
        products = client.collections.get(COLLECTION_NAME)

        print(f"Generating 50 objects for batch import...")
        objects_to_add = []
        for i in range(50):
            objects_to_add.append(
                {
                    "name": f"Product {i}",
                    "description": f"This is the description for product number {i}.",
                }
            )

        print("Starting batch import...")
        # Use a context manager for batching.
        # `dynamic()` automatically handles batch size and sends requests.
        with products.batch.dynamic() as batch:
            for data_object in objects_to_add:
                batch.add_object(properties=data_object)
        
        print("Batch import complete.")

        # --- 5. Verify the number of objects ---
        # Use aggregation to get the total count of objects in the collection.
        response = products.aggregate.over_all(total_count=True)

        print("\n--- Verification ---")
        print(f"Total number of objects in '{COLLECTION_NAME}': {response.total_count}")

except Exception as e:
    print(f"An error occurred: {e}")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate: True
Collection 'DemoProducts' already exists. Deleting it.
Creating collection 'DemoProducts'...
Collection created successfully.
Generating 50 objects for batch import...
Starting batch import...
Batch import complete.

--- Verification ---
Total number of objects in 'DemoProducts': 50

```

**Errors**:
```
/code/code.py:23: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  with weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 28.91s)

**Generated Code**:
```python
import weaviate
import weaviate.classes as wvc
import os
import sys

# 1. Get Weaviate credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if the environment variables are set
if not wcd_url or not wcd_api_key:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.", file=sys.stderr)
    sys.exit(1)

# --- Main execution ---
client = None  # Initialize client to None for the finally block
try:
    # 2. Connect to Weaviate Cloud
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=weaviate.auth.AuthApiKey(wcd_api_key),
    )
    print("Connection successful.")

    collection_name = "DemoProducts"

    # 3. Recreate the collection
    # This ensures a clean start for the demo.
    if client.collections.exists(collection_name):
        print(f"Deleting existing collection: '{collection_name}'")
        client.collections.delete(collection_name)

    print(f"Creating collection: '{collection_name}'")
    products = client.collections.create(
        name=collection_name,
        properties=[
            wvc.config.Property(name="name", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="description", data_type=wvc.config.DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created successfully.")

    # 4. Prepare data for batch import
    num_objects_to_add = 50
    print(f"Preparing {num_objects_to_add} objects for import...")
    data_objects = [
        {
            "name": f"Product {i}",
            "description": f"This is the description for product number {i}.",
        }
        for i in range(1, num_objects_to_add + 1)
    ]

    # 5. Batch import objects
    print(f"Starting batch import of {len(data_objects)} objects...")
    with products.batch.dynamic() as batch:
        for obj in data_objects:
            batch.add_object(
                properties=obj
            )

    # 6. Check for and report any import errors
    if products.batch.failed_objects:
        print(f"Failed to import {len(products.batch.failed_objects)} objects.")
        # Optionally, print details of the first few failed objects
        for i, failed in enumerate(products.batch.failed_objects):
            if i >= 5: # Limit printing to the first 5 errors
                break
            print(f"  - Failed object details: {failed.message}")
    else:
        print("All objects imported successfully.")

    # 7. Print the number of objects in the collection
    # The `len()` function provides a convenient way to get the object count.
    object_count = len(products)
    print(f"\nTotal number of objects in '{collection_name}': {object_count}")

finally:
    # 8. Close the client connection
    if client:
        client.close()
        print("Client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Connection successful.
Deleting existing collection: 'DemoProducts'
Creating collection: 'DemoProducts'
Collection 'DemoProducts' created successfully.
Preparing 50 objects for import...
Starting batch import of 50 objects...
All objects imported successfully.

Total number of objects in 'DemoProducts': 50
Client connection closed.

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 24.94s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth

# This script demonstrates how to create a collection, batch import objects,
# and count the total number of objects using the Weaviate Python client v4.

# It connects to a Weaviate Cloud (WCD) instance, so you must have the
# WCD_TEST_URL and WCD_TEST_KEY environment variables set.

# 1. Get Weaviate Cloud credentials from environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not wcd_url or not wcd_api_key:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

client = None
try:
    # 2. Connect to Weaviate Cloud
    # For more information, see: https://weaviate.io/developers/weaviate/client-libraries/python#connection
    print(f"Connecting to Weaviate Cloud at {wcd_url}...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
    )
    print("Connection successful.")

    collection_name = "DemoProducts"

    # 3. Create a collection
    # For more information, see: https://weaviate.io/developers/weaviate/manage-data/collections
    
    # Clean up previous runs: delete the collection if it already exists
    if client.collections.exists(collection_name):
        print(f"Deleting existing collection: '{collection_name}'")
        client.collections.delete(collection_name)

    print(f"Creating new collection: '{collection_name}'")
    products_collection = client.collections.create(
        name=collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created.")

    # 4. Batch import objects
    # For more information, see: https://weaviate.io/developers/weaviate/manage-data/import
    print("Starting batch import of 50 objects...")

    # Use a context manager for batching. This is the recommended way to import data.
    # It automatically handles sending batches and managing errors.
    with products_collection.batch.fixed_size(batch_size=25) as batch:
        for i in range(50):
            product_object = {
                "name": f"Product {i}",
                "description": f"This is the description for product number {i}."
            }
            batch.add_object(properties=product_object)

    # Check for errors during batch import
    if len(products_collection.batch.failed_objects) > 0:
        print(f"Failed to import {len(products_collection.batch.failed_objects)} objects.")
    else:
        print("Batch import completed successfully.")


    # 5. Get and print the number of objects in the collection
    # The aggregate.total_count() method is the most efficient way to get the object count.
    total_count = products_collection.aggregate.total_count()
    print(f"\nTotal number of objects in '{collection_name}': {total_count}")

finally:
    # 6. Close the client connection
    if client:
        client.close()
        print("\nClient connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
Connection successful.
Deleting existing collection: 'DemoProducts'
Creating new collection: 'DemoProducts'
Collection 'DemoProducts' created.
Starting batch import of 50 objects...
Batch import completed successfully.

Client connection closed.

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 74, in <module>
    total_count = products_collection.aggregate.total_count()
AttributeError: '_AggregateCollection' object has no attribute 'total_count'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 22.25s)

**Generated Code**:
```python
import weaviate
import os

# --- 1. Connect to Weaviate Cloud ---
# Get connection details from environment variables
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    exit(1)

# Set up authentication credentials for Weaviate
auth_credentials = weaviate.auth.AuthApiKey(api_key=wcd_api_key)

# Connect to the Weaviate instance
# We pass the OpenAI API key in the headers for the text2vec-openai vectorizer
try:
    client = weaviate.connect_to_wcs(
        cluster_url=wcd_url,
        auth_credentials=auth_credentials,
        headers={
            "X-OpenAI-Api-Key": openai_api_key
        }
    )
    print("Successfully connected to Weaviate Cloud.")

    # --- 2. Prepare and Execute the Query ---
    # Get a handle to the 'WineReview' collection
    reviews = client.collections.get("WineReview")

    # Define the search query
    search_query = "dessert wine"

    print(f"\nSearching for wines similar to: '{search_query}'\n")

    # Execute the vector search (near_text) query
    response = reviews.query.near_text(
        query=search_query,
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # --- 3. Print the Results ---
    if not response.objects:
        print("No results found.")
    else:
        print("Found matching wines:")
        for i, wine in enumerate(response.objects):
            # The properties are stored in the .properties attribute
            props = wine.properties
            print(f"--- Result {i+1} ---")
            print(f"  Title:   {props.get('title')}")
            print(f"  Country: {props.get('country')}")
            print(f"  Price:   ${props.get('price'):.2f}" if props.get('price') is not None else "  Price:   N/A")
            print(f"  Points:  {props.get('points')}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # --- 4. Close the connection ---
    # It's good practice to close the connection when you're done
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Output**:
```
Successfully connected to Weaviate Cloud.

Searching for wines similar to: 'dessert wine'

Found matching wines:
--- Result 1 ---
  Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price:   $24.00
  Points:  88
--- Result 2 ---
  Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price:   $40.00
  Points:  88

Connection to Weaviate closed.

```

**Errors**:
```
/code/code.py:21: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 19.59s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Check for environment variables
wcd_url = os.getenv("WCD_TEST_URL")
wcd_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not all([wcd_url, wcd_api_key, openai_api_key]):
    print(
        "Error: Make sure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY "
        "environment variables are set."
    )
    exit(1)

# It's a good practice to wrap the client connection in a try...finally block
# to ensure the connection is always closed.
try:
    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            # Pass the OpenAI API key for the text2vec-openai vectorizer
            "X-OpenAI-API-Key": openai_api_key
        },
    )

    # Get a reference to the 'WineReview' collection
    reviews = client.collections.get("WineReview")

    # Perform the near_text (semantic) search
    response = reviews.query.near_text(
        query="dessert wine",
        limit=2
    )

    print("Found wines matching 'dessert wine':\n")

    # Iterate through the results and print the desired properties
    for item in response.objects:
        properties = item.properties
        print(f"  - Title: {properties.get('title')}")
        print(f"    Country: {properties.get('country')}")
        print(f"    Price: ${properties.get('price')}")
        print(f"    Points: {properties.get('points')}\n")

finally:
    # Close the connection to Weaviate
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Client connection closed.")
```

**Output**:
```
Found wines matching 'dessert wine':

  - Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
    Country: US
    Price: $24.0
    Points: 88

  - Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
    Country: US
    Price: $40.0
    Points: 88

Client connection closed.

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.84s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth

# This script requires environment variables for Weaviate Cloud and OpenAI.
# Make sure to set the following before running the script:
# WCD_TEST_URL: The URL of your Weaviate Cloud instance.
# WCD_TEST_KEY: The API key for your Weaviate Cloud instance.
# OPENAI_API_KEY: Your OpenAI API key.

try:
    # Connect to Weaviate Cloud using environment variables
    # For more information, see the Python Client library page:
    # https://docs.weaviate.io/weaviate/client-libraries/python
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]  # API key for the vectorizer
        }
    )

    # Get a handle to the 'WineReview' collection
    reviews = client.collections.get("WineReview")

    # Perform a semantic search (near_text) to find wines matching the query.
    # The 'text2vec-openai' vectorizer will convert the query "dessert wine"
    # into a vector and find the two most similar wine reviews.
    # For more information on searching, see:
    # https://docs.weaviate.io/weaviate/search
    response = reviews.query.near_text(
        query="dessert wine",
        limit=2
    )

    print("Found wines matching 'dessert wine':")
    # Iterate through the results and print the requested properties
    for item in response.objects:
        # Access the properties of each returned object
        properties = item.properties
        print(f"  Title: {properties.get('title')}")
        print(f"  Country: {properties.get('country')}")
        print(f"  Price: {properties.get('price')}")
        print(f"  Points: {properties.get('points')}")
        print("-" * 20)

except KeyError as e:
    print(f"Error: Environment variable {e} not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Always close the connection to Weaviate
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Connection to Weaviate closed.")
```

**Output**:
```
Found wines matching 'dessert wine':
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
Connection to Weaviate closed.

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 29.89s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import Filter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Get environment variables
wcs_url = os.getenv("WCD_TEST_URL")
wcs_key = os.getenv("WCD_TEST_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Check if environment variables are set
if not all([wcs_url, wcs_key, openai_key]):
    print("Error: Required environment variables (WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY) are not set.")
    exit(1)

# Define headers for API keys, as required by the text2vec-openai vectorizer
headers = {
    "X-OpenAI-Api-Key": openai_key
}

# 2. Connect to Weaviate Cloud
try:
    client = weaviate.connect_to_wcs(
        cluster_url=wcs_url,
        auth_credentials=weaviate.auth.AuthApiKey(wcs_key),
        headers=headers
    )
    print("Successfully connected to Weaviate Cloud.")

    # Get a handle to the 'WineReview' collection
    reviews = client.collections.get("WineReview")

    # 3. Define the filters
    # We need to combine three conditions with an AND logic:
    # - price is less than 50
    # - points is greater than 90
    # - review_body contains AT LEAST ONE of the specified substrings (OR logic)

    # This filter handles the OR condition for the review body
    review_body_filter = Filter.any_of([
        Filter.by_property("review_body").like("*spice*"),
        Filter.by_property("review_body").like("*fruit*"),
        Filter.by_property("review_body").like("*berry*"),
        Filter.by_property("review_body").like("*cherry*"),
        Filter.by_property("review_body").like("*honey*"),
    ])

    # Combine all filters using all_of for the final AND logic
    final_filters = Filter.all_of([
        Filter.by_property("price").less_than(50),
        Filter.by_property("points").greater_than(90),
        review_body_filter
    ])

    # 4. Execute the hybrid query
    query_text = "pair with steak"
    print(f"\nPerforming hybrid search for: '{query_text}'")
    print("With filters: price < 50, points > 90, and matching keywords in review.\n")


    response = reviews.query.hybrid(
        query=query_text,
        limit=5,
        alpha=0.5,  # 0.0 for pure keyword, 1.0 for pure vector, 0.5 for equal balance
        filters=final_filters,
        return_properties=["title", "country", "price", "points"]
    )

    # 5. Print the results
    if response.objects:
        print("Found the following matching wines:")
        print("-" * 80)
        for item in response.objects:
            wine = item.properties
            print(f"  Title:   {wine.get('title')}")
            print(f"  Country: {wine.get('country')}")
            print(f"  Price:   ${wine.get('price'):.2f}")
            print(f"  Points:  {wine.get('points')}")
            print("-" * 80)
    else:
        print("No wines found matching the specified criteria.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. Close the connection
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")
```

**Output**:
```
Successfully connected to Weaviate Cloud.

Performing hybrid search for: 'pair with steak'
With filters: price < 50, points > 90, and matching keywords in review.

Found the following matching wines:
--------------------------------------------------------------------------------
  Title:   Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price:   $40.00
  Points:  92
--------------------------------------------------------------------------------
  Title:   Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price:   $49.00
  Points:  91
--------------------------------------------------------------------------------
  Title:   Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price:   $27.00
  Points:  91
--------------------------------------------------------------------------------
  Title:   Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price:   $25.00
  Points:  93
--------------------------------------------------------------------------------
  Title:   Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price:   $0.00
  Points:  92
--------------------------------------------------------------------------------

Connection to Weaviate closed.

```

**Errors**:
```
/code/code.py:26: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 24.81s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os
import sys

# --- 1. Check for and load environment variables ---
try:
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"❌ Error: Environment variable {e} is not set.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
    sys.exit(1)

# --- 2. Connect to Weaviate Cloud ---
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={
            "X-OpenAI-API-Key": openai_api_key
        },
    )
    print("✅ Successfully connected to Weaviate Cloud.")
except Exception as e:
    print(f"❌ Error connecting to Weaviate: {e}")
    sys.exit(1)


# --- 3. Define the query and filters ---
collection_name = "WineReview"
query_text = "pair with steak"

# Define the combined filter for the query
# This uses the `&` operator to chain multiple conditions with a logical AND.
filters = (
    # Condition 1: Price must be less than 50
    Filter.by_property("price").less_than(50) &
    # Condition 2: Points must be greater than 90
    Filter.by_property("points").greater_than(90) &
    # Condition 3: The review must contain at least one of these words
    Filter.by_property("review_body").contains_any(
        ["spice", "fruit", "berry", "cherry", "honey"]
    )
)

# --- 4. Execute the hybrid search query ---
try:
    # Get the collection object
    wine_reviews = client.collections.get(collection_name)

    # Perform the hybrid search
    response = wine_reviews.query.hybrid(
        query=query_text,
        limit=5,          # Maximum of 5 results
        alpha=0.5,        # Balance between keyword and vector search
        filters=filters   # Apply the defined filters
    )

    # --- 5. Print the results ---
    print(f"\nFound {len(response.objects)} wines matching your query:\n")

    if not response.objects:
        print("No results found. Try adjusting your query or filters.")
    else:
        for i, obj in enumerate(response.objects):
            # Access the properties of each returned object
            properties = obj.properties
            
            print(f"--- Result {i+1} ---")
            print(f"  Title:   {properties.get('title')}")
            print(f"  Country: {properties.get('country')}")
            print(f"  Price:   ${properties.get('price')}")
            print(f"  Points:  {properties.get('points')}")

finally:
    # --- 6. Close the connection ---
    # It's good practice to close the connection when you're done.
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\n✅ Connection to Weaviate closed.")
```

**Output**:
```
✅ Successfully connected to Weaviate Cloud.

Found 5 wines matching your query:

--- Result 1 ---
  Title:   Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price:   $40.0
  Points:  92
--- Result 2 ---
  Title:   Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price:   $49.0
  Points:  91
--- Result 3 ---
  Title:   Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price:   $27.0
  Points:  91
--- Result 4 ---
  Title:   Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price:   $25.0
  Points:  93
--- Result 5 ---
  Title:   Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price:   $0.0
  Points:  92

✅ Connection to Weaviate closed.

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 22.10s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

# This script performs a hybrid search on a 'WineReview' collection in Weaviate.
# It finds up to 5 wines that are a good match for "pair with steak",
# cost less than 50, have a rating over 90 points, and have specific
# keywords in their review body.

# Ensure required environment variables are set
required_env_vars = ["WCD_TEST_URL", "WCD_TEST_KEY", "OPENAI_API_KEY"]
for var in required_env_vars:
    if var not in os.environ:
        raise EnvironmentError(
            f"Required environment variable '{var}' is not set. "
            "Please set it before running the script."
        )

try:
    # Connect to Weaviate Cloud using environment variables
    # For more information on connecting to Weaviate, see:
    # https://weaviate.io/developers/weaviate/client-libraries/python
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )

    # Get a reference to the 'WineReview' collection
    reviews = client.collections.get("WineReview")

    # Define the filters to apply to the search results
    # For more information on filtering, see:
    # https://weaviate.io/developers/weaviate/search/filters
    
    # 1. Filter for price less than 50
    price_filter = Filter.by_property("price").less_than(50)

    # 2. Filter for points greater than 90
    points_filter = Filter.by_property("points").greater_than(90)

    # 3. Filter for at least one keyword in the review_body
    keywords = ["spice", "fruit", "berry", "cherry", "honey"]
    keyword_filters = [
        Filter.by_property("review_body").like(f"*{keyword}*") for keyword in keywords
    ]
    # Combine the keyword filters using an 'OR' condition
    review_body_filter = Filter.any_of(keyword_filters)

    # Combine all individual filters into a single 'AND' condition
    combined_filter = Filter.all_of([
        price_filter,
        points_filter,
        review_body_filter
    ])

    # Perform the hybrid search
    # For more information on hybrid search, see:
    # https://weaviate.io/developers/weaviate/search/hybrid
    response = reviews.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        limit=5,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the results
    print("Found wines matching 'pair with steak' (price < 50, points > 90):")
    if response.objects:
        for item in response.objects:
            wine = item.properties
            print(f"\n  - Title: {wine.get('title')}")
            print(f"    Country: {wine.get('country')}")
            # Ensure price is formatted correctly if it exists
            price = wine.get('price')
            if price is not None:
                print(f"    Price: ${price:.2f}")
            else:
                print(f"    Price: N/A")
            print(f"    Points: {wine.get('points')}")
    else:
        print("No matching wines found that satisfy all criteria.")

finally:
    # Close the client connection
    if 'client' in locals() and client.is_connected():
        client.close()
        print("\nConnection to Weaviate closed.")

```

**Output**:
```
Found wines matching 'pair with steak' (price < 50, points > 90):

  - Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
    Country: US
    Price: $40.00
    Points: 92

  - Title: Bink 2014 Pinot Noir (Anderson Valley)
    Country: US
    Price: $49.00
    Points: 91

  - Title: Doña Silvina 2011 Malbec (Mendoza)
    Country: Argentina
    Price: $27.00
    Points: 91

  - Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
    Country: Hungary
    Price: $25.00
    Points: 93

  - Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
    Country: Italy
    Price: $0.00
    Points: 92

Connection to Weaviate closed.

```

---

### gemini/gemini-2.5-flash

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 10.34s)

**Generated Code**:
```python
import weaviate
import os
import sys

def connect_and_check_weaviate_cloud():
    """
    Connects to Weaviate Cloud using environment variables WCD_TEST_URL and WCD_TEST_KEY,
    and then checks if the server is ready.
    """
    # 1. Retrieve Weaviate Cloud URL and API Key from environment variables
    weaviate_url = os.getenv("WCD_TEST_URL")
    weaviate_api_key = os.getenv("WCD_TEST_KEY")

    # Check if environment variables are set
    if not weaviate_url:
        print("Error: WCD_TEST_URL environment variable not set.")
        print("Please set it to your Weaviate Cloud cluster URL.")
        sys.exit(1)
    if not weaviate_api_key:
        print("Error: WCD_TEST_KEY environment variable not set.")
        print("Please set it to your Weaviate Cloud API Key.")
        sys.exit(1)

    print(f"Attempting to connect to Weaviate Cloud at: {weaviate_url}")

    # 2. Connect to Weaviate Cloud using the latest client syntax
    # The 'with' statement ensures the client connection is properly closed
    try:
        with weaviate.connect_to_weaviate_cloud(
            cluster_url=weaviate_url,
            api_key=weaviate_api_key
        ) as client:
            print("Successfully connected to Weaviate Cloud client.")

            # 3. Check if the Weaviate server is ready to accept requests
            if client.is_ready():
                print("Weaviate server is READY to accept requests.")
            else:
                print("Weaviate server is NOT ready. It might be starting up or experiencing issues.")

    except weaviate.exceptions.WeaviateConnectionError as e:
        print(f"\nFailed to connect to Weaviate Cloud: {e}")
        print("Please verify WCD_TEST_URL, WCD_TEST_KEY, and your network connection.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    connect_and_check_weaviate_cloud()
```

**Output**:
```
Attempting to connect to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud

An unexpected error occurred: connect_to_weaviate_cloud() got an unexpected keyword argument 'api_key'

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

# Get Weaviate Cloud URL and API Key from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

# Check if environment variables are set
if not WCD_TEST_URL:
    raise ValueError(
        "WCD_TEST_URL environment variable not set. "
        "Please set it to your Weaviate Cloud URL."
    )
if not WCD_TEST_KEY:
    raise ValueError(
        "WCD_TEST_KEY environment variable not set. "
        "Please set it to your Weaviate Cloud API Key."
    )

client = None # Initialize client to None for finally block

try:
    # Connect to the Weaviate Cloud instance
    print(f"Attempting to connect to Weaviate Cloud at: {WCD_TEST_URL}")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY)
    )

    # Check that the server is ready to accept requests
    if client.is_ready():
        print("Successfully connected to Weaviate Cloud and server is ready!")
    else:
        print("Connected to Weaviate Cloud, but server is not ready.")
        # Optionally raise an error if not ready
        # raise ConnectionError("Weaviate server is not ready after connection.")

except Exception as e:
    print(f"An error occurred: {e}")
    # Handle specific exceptions if needed, e.g., ConnectionError, AuthenticationError
    if "Connection refused" in str(e):
        print("Please check if the URL is correct and accessible.")
    if "Unauthorized" in str(e):
        print("Please check if the API key is correct.")

finally:
    # Ensure the client connection is closed
    if client:
        print("Closing Weaviate client connection.")
        client.close()
```

**Output**:
```
Attempting to connect to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate Cloud and server is ready!
Closing Weaviate client connection.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.51s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType

# --- Configuration ---
# Load Weaviate Cloud credentials from environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")
COLLECTION_NAME = "DemoProducts"

# Ensure environment variables are set
if not WEAVIATE_URL or not WEAVIATE_API_KEY:
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY "
        "before running this script."
    )

# --- Connect to Weaviate ---
print(f"Connecting to Weaviate instance at: {WEAVIATE_URL}")
try:
    client = weaviate.connect(
        url=WEAVIATE_URL,
        auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
    )
    print("Successfully connected to Weaviate.")
except Exception as e:
    print(f"Failed to connect to Weaviate: {e}")
    exit(1)

# --- Define Collection Properties ---
properties_config = [
    Property(name="name", data_type=DataType.TEXT),
    Property(name="description", data_type=DataType.TEXT),
    Property(name="price", data_type=DataType.NUMBER),
    Property(name="in_stock", data_type=DataType.BOOLEAN),
]

# --- Create or Recreate Collection ---
try:
    # 1. Check if the collection already exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        # 2. Delete the collection if it exists
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted successfully.")
    else:
        print(f"Collection '{COLLECTION_NAME}' does not exist.")

    # 3. Create the new collection
    print(f"Creating collection '{COLLECTION_NAME}' with specified properties...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=properties_config,
        # Default vectorizer is text2vec-contextionary.
        # If you need a different one (e.g., for WCD with a specific model),
        # uncomment and configure below:
        # vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_openai()
        # or
        # vectorizer_config=weaviate.classes.config.Configure.Vectorizer.none() # if you handle vectorization externally
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully!")

    # Optional: Verify the schema of the created collection
    print("\n--- Verifying Collection Schema ---")
    retrieved_collection = client.collections.get(COLLECTION_NAME)
    print(f"Collection Name: {retrieved_collection.name}")
    print("Properties:")
    for prop in retrieved_collection.config.properties:
        print(f"  - Name: {prop.name}, Data Type: {prop.data_type.value}")

except Exception as e:
    print(f"An error occurred during collection creation/deletion: {e}")
finally:
    # --- Close Connection ---
    if client.is_connected():
        client.close()
        print("\nWeaviate connection closed.")
```

**Output**:
```
Connecting to Weaviate instance at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Failed to connect to Weaviate: 'module' object is not callable

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.43s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get Weaviate Cloud credentials from environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")
    print("Please set them before running the script.")
    exit(1)

# Connect to the Weaviate Cloud instance
print(f"Connecting to Weaviate Cloud at: {WCD_TEST_URL}")
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY)
    )
    print("Successfully connected to Weaviate.")
except Exception as e:
    print(f"Failed to connect to Weaviate: {e}")
    exit(1)

# Define the collection name
collection_name = "DemoProducts"

try:
    # Delete the collection if it already exists (for testing purposes)
    if client.collections.exists(collection_name):
        print(f"Collection '{collection_name}' already exists. Deleting it...")
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist. Proceeding to create.")

    # Create the collection
    print(f"Creating collection: '{collection_name}'...")
    products_collection = client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )

    print(f"Collection '{products_collection.name}' created successfully!")
    print("Properties defined:")
    for prop in products_collection.config.get().properties:
        print(f"- Name: {prop.name}, DataType: {prop.data_type}")

except Exception as e:
    print(f"An error occurred during collection creation/deletion: {e}")
finally:
    # Close connection
    if client.is_connected():
        client.close()
        print("Weaviate connection closed.")
```

**Output**:
```
Connecting to Weaviate Cloud at: yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud
Successfully connected to Weaviate.
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection: 'DemoProducts'...
Collection 'DemoProducts' created successfully!
Properties defined:
- Name: name, DataType: text
- Name: description, DataType: text
- Name: price, DataType: number
- Name: in_stock, DataType: boolean
Weaviate connection closed.

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 6.04s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure
import os

# Define environment variables for Weaviate Cloud connection
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

# Ensure environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL and WCD_TEST_KEY for Weaviate Cloud connection."
    )

COLLECTION_NAME = "DemoProducts"

# Connect to Weaviate Cloud using environment variables
# For more information on client instantiation, see: https://www.docs.weaviate.io/weaviate/client-libraries/python
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        # Add inference API keys here if you plan to use generative or vectorization modules
        # headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]}
    )

    # Check if the collection already exists and delete it if it does
    # For more information on collection management, see: https://docs.weaviate.io/weaviate/manage-data/collections
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted successfully.")

    # Define the properties for the "DemoProducts" collection
    properties = [
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]

    # Create the "DemoProducts" collection with the specified properties
    # It's good practice to configure a vectorizer for your collection.
    # Weaviate Cloud (WCD) often recommends `text2vec-weaviate` as it's built-in and doesn't require extra API keys.
    # If you have specific needs (e.g., OpenAI, Cohere), configure those instead.
    client.collections.create(
        name=COLLECTION_NAME,
        properties=properties,
        # Configure a vectorizer, e.g., text2vec-weaviate (no API key needed)
        vector_config=Configure.Vectors.text2vec_weaviate(),
        # Or, if you use OpenAI:
        # vector_config=Configure.Vectors.text2vec_openai(),
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully with specified properties.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the client connection is closed
    if 'client' in locals() and client.is_connected():
        client.close()
        print("Weaviate client connection closed.")

```

**Output**:
```
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted successfully.
Collection 'DemoProducts' created successfully with specified properties.
Weaviate client connection closed.

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 14.19s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.data import DataObject

# --- 1. Get connection details from environment variables ---
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    print("Error: Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")
    print("Please set them before running the script.")
    exit(1)

COLLECTION_NAME = "DemoProducts"

client = None  # Initialize client to None for finally block

try:
    # --- 2. Connect to Weaviate Cloud ---
    print(f"Connecting to Weaviate Cloud at: {WCD_TEST_URL}")
    client = weaviate.connect_to_wcs(
        cluster_url=WCD_TEST_URL,
        api_key=WCD_TEST_KEY
    )
    print("Successfully connected to Weaviate!")

    # --- 3. (Optional) Delete collection if it already exists for a clean run ---
    if client.collections.exists(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it for a clean run...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")

    # --- 4. Define and Create the Collection ---
    print(f"Creating collection '{COLLECTION_NAME}' with specified properties...")
    products_collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            Property(name="name", data_type=DataType.TEXT, description="Name of the product"),
            Property(name="description", data_type=DataType.TEXT, description="Description of the product"),
        ]
        # You can add vectorizer_config, inverted_index_config, etc. here if needed
        # For simplicity, default settings are used here.
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

    # --- 5. Prepare 50 arbitrary objects for batch import ---
    print("Preparing 50 objects for batch import...")
    data_objects_to_import = []
    for i in range(50):
        data_objects_to_import.append(
            DataObject(
                properties={
                    "name": f"Product {i+1}",  # Start from Product 1
                    "description": f"This is the description for Product number {i+1}. It's a fantastic item!",
                }
            )
        )
    print(f"Prepared {len(data_objects_to_import)} objects.")

    # --- 6. Batch Import Objects ---
    print("Starting batch import...")
    # The insert_many method is efficient for bulk imports
    insert_result = products_collection.data.insert_many(data_objects_to_import)
    
    # You can inspect the insert_result for any errors during import
    if insert_result.errors:
        print("Batch import completed with some errors:")
        for error in insert_result.errors:
            print(f"- {error.message}")
    else:
        print("Batch import completed successfully!")

    # --- 7. Print the number of objects in the collection ---
    print(f"\nAggregating object count for '{COLLECTION_NAME}'...")
    aggregate_result = products_collection.query.aggregate()

    # The total_count property gives the number of objects
    object_count = aggregate_result.total_count
    print(f"Number of objects in '{COLLECTION_NAME}': {object_count}")

except weaviate.WeaviateConnectionError as e:
    print(f"Connection Error: Could not connect to Weaviate. Details: {e}")
except weaviate.WeaviateAuthError as e:
    print(f"Authentication Error: API key might be incorrect or expired. Details: {e}")
except weaviate.WeaviateInvalidInputError as e:
    print(f"Invalid Input Error: Check your schema or data. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- 8. Close the connection ---
    if client:
        client.close()
        print("Weaviate connection closed.")

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
  File "/code/code.py", line 82, in <module>
    except weaviate.WeaviateConnectionError as e:
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 145, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute WeaviateConnectionError

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 22.44s)

**Generated Code**:
```python
import weaviate
import os

# 1. Connect to Weaviate Cloud using environment variables
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_URL or not WCD_KEY:
    raise ValueError(
        "Error: WCD_TEST_URL and WCD_TEST_KEY environment variables must be set."
        "\nExample: export WCD_TEST_URL='https://YOUR_CLUSTER_URL.weaviate.network'"
        "\nExample: export WCD_TEST_KEY='YOUR_API_KEY'"
    )

print(f"Connecting to Weaviate Cloud at {WCD_URL.split('//')[1].split('/')[0]}...")
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_URL,
        auth_credentials=weaviate.Auth.api_key(WCD_KEY),
    )
    print("Successfully connected to Weaviate.")
except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Failed to connect to Weaviate: {e}")
    exit()

COLLECTION_NAME = "DemoProducts"

# 2. Define the collection schema and ensure the collection exists
# If the collection exists, delete and recreate it for a clean run.
# Otherwise, create it.
try:
    if client.collections.exists(COLLECTION_NAME):
        print(f"\nCollection '{COLLECTION_NAME}' already exists. Deleting it for a clean start...")
        client.collections.delete(COLLECTION_NAME)
        print(f"Collection '{COLLECTION_NAME}' deleted.")
    
    print(f"Creating collection '{COLLECTION_NAME}' with specified properties...")
    collection = client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            weaviate.CollectionProperty(name="name", data_type=weaviate.PropertyType.TEXT),
            weaviate.CollectionProperty(name="description", data_type=weaviate.PropertyType.TEXT),
        ],
        # Explicitly configure no vectorizer as it's not needed for this example.
        # This saves resources and avoids issues if a default vectorizer isn't available.
        vectorizer_config=weaviate.config.Configure.Vectorizer.none(),
        # Configure no module inference (e.g., for vectorization or RAG)
        module_config={}, 
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully.")

except Exception as e:
    print(f"An unexpected error occurred during collection creation: {e}")
    # If creation failed, attempt to retrieve the collection if it somehow exists
    if client.collections.exists(COLLECTION_NAME):
        print(f"Attempting to get existing collection '{COLLECTION_NAME}'.")
        collection = client.collections.get(COLLECTION_NAME)
    else:
        print("Could not create or retrieve the collection. Exiting.")
        client.close()
        exit()


# 3. Batch import 50 arbitrary objects
NUM_OBJECTS_TO_IMPORT = 50
print(f"\nGenerating {NUM_OBJECTS_TO_IMPORT} arbitrary objects for batch import...")
data_rows = [
    {
        "name": f"Product {i+1:02d}", # Product name with leading zero for single digits
        "description": f"This is the detailed description for Product number {i+1}. It highlights its unique features, benefits, and specifications.",
    }
    for i in range(NUM_OBJECTS_TO_IMPORT)
]

print(f"Starting batch import of {NUM_OBJECTS_TO_IMPORT} objects into '{COLLECTION_NAME}'...")
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(
            properties=data_row,
        )
        # Optional: Check for errors during the batching process (useful for very large batches)
        # if batch.number_errors > 0:
        #     print(f"Warning: {batch.number_errors} errors encountered during batching.")

# Check for failed objects after the batch operation is complete
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Batch import completed with {len(failed_objects)} failed objects.")
    print(f"First failed object details (if any): {failed_objects[0]}")
else:
    print("Batch import completed successfully with no failed objects.")


# 4. Print the number of objects in the collection
print(f"\nVerifying object count in '{COLLECTION_NAME}'...")
try:
    object_count = len(collection)
    print(f"Total number of objects in '{COLLECTION_NAME}': {object_count}")
except Exception as e:
    print(f"Error retrieving object count: {e}")


# 5. Close the Weaviate client connection
print("\nClosing Weaviate connection...")
client.close()
print("Connection closed.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 15, in <module>
    print(f"Connecting to Weaviate Cloud at {WCD_URL.split('//')[1].split('/')[0]}...")
IndexError: list index out of range

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 11.09s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Configure, Property, DataType
import os

# Ensure environment variables are set
# For testing, you might set them like this:
# os.environ["WCD_TEST_URL"] = "YOUR_WEAVIATE_CLOUD_URL"
# os.environ["WCD_TEST_KEY"] = "YOUR_WEAVIATE_API_KEY"

# Define collection name
COLLECTION_NAME = "DemoProducts"

def main():
    client = None # Initialize client to None for finally block

    try:
        # 1. Connect to Weaviate Cloud
        print(f"Connecting to Weaviate Cloud at {os.environ.get('WCD_TEST_URL')}...")
        client = weaviate.connect_to_weaviate_cloud(
            cluster_url=os.environ["WCD_TEST_URL"],
            auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
            # Add any other required headers if your Weaviate Cloud instance needs them, e.g., for vectorization
            # headers={
            #     "X-OpenAI-Api-Key": os.environ.get("OPENAI_API_KEY")
            # }
        )
        print("Successfully connected to Weaviate Cloud.")

        # 2. Define and create the collection
        print(f"\nChecking for existing collection '{COLLECTION_NAME}'...")
        if client.collections.exists(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it...")
            client.collections.delete(COLLECTION_NAME)
            print(f"Collection '{COLLECTION_NAME}' deleted.")

        print(f"Creating collection '{COLLECTION_NAME}'...")
        products_collection = client.collections.create(
            name=COLLECTION_NAME,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            # If you want to enable vectorization, uncomment one of the following:
            # For Weaviate Cloud, text2vec-weaviate is often a good default as it doesn't require a third-party API key
            # vector_config=Configure.Vectors.text2vec_weaviate(),
            # Or if using OpenAI (requires OPENAI_API_KEY env var):
            # vector_config=Configure.Vectors.text2vec_openai(),
            # Or self-provided vectors if you plan to supply them directly
            # vector_config=Configure.Vectors.self_provided(),
        )
        print(f"Collection '{COLLECTION_NAME}' created successfully.")

        # 3. Batch import 50 arbitrary objects
        num_objects_to_import = 50
        print(f"\nBatch importing {num_objects_to_import} objects into '{COLLECTION_NAME}'...")

        # Get the collection object for data operations
        products_collection = client.collections.get(COLLECTION_NAME)

        with products_collection.batch.fixed_size(batch_size=25) as batch: # Using a batch size of 25 for this example
            for i in range(num_objects_to_import):
                product_data = {
                    "name": f"Product {i+1}",
                    "description": f"This is the description for Product {i+1}. It highlights its features and benefits."
                }
                batch.add_object(properties=product_data)
        print(f"Batch import completed. Errors: {len(products_collection.batch.failed_objects)}")

        # 4. Print the number of objects in the collection
        print(f"\nCounting objects in '{COLLECTION_NAME}'...")
        total_objects = products_collection.aggregate.total_count()
        print(f"Total number of objects in '{COLLECTION_NAME}': {total_objects}")

    except KeyError as e:
        print(f"Error: Environment variable not set. Please set {e}.")
        print("Make sure WCD_TEST_URL and WCD_TEST_KEY are set in your environment.")
    except weaviate.exceptions.WeaviateConnectionError as e:
        print(f"Weaviate connection error: {e}")
        print("Please check your Weaviate Cloud URL and API Key.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # 5. Clean up: Close the client connection
        if client:
            print("\nClosing Weaviate client connection.")
            client.close()
            print("Client connection closed.")

if __name__ == "__main__":
    # Set dummy environment variables for demonstration if not already set
    # In a real scenario, these would be properly configured
    if "WCD_TEST_URL" not in os.environ:
        os.environ["WCD_TEST_URL"] = "http://localhost:8080" # Replace with your actual Weaviate Cloud URL
        print("WARNING: WCD_TEST_URL not found, using placeholder. Please set your actual Weaviate Cloud URL.")
    if "WCD_TEST_KEY" not in os.environ:
        os.environ["WCD_TEST_KEY"] = "YOUR_API_KEY_HERE" # Replace with your actual Weaviate Cloud API Key
        print("WARNING: WCD_TEST_KEY not found, using placeholder. Please set your actual Weaviate Cloud API Key.")

    main()
```

**Output**:
```
Connecting to Weaviate Cloud at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud...
Successfully connected to Weaviate Cloud.

Checking for existing collection 'DemoProducts'...
Collection 'DemoProducts' already exists. Deleting it...
Collection 'DemoProducts' deleted.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.

Batch importing 50 objects into 'DemoProducts'...
Batch import completed. Errors: 0

Counting objects in 'DemoProducts'...
An unexpected error occurred: '_AggregateCollection' object has no attribute 'total_count'

Closing Weaviate client connection.
Client connection closed.

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.94s)

**Generated Code**:
```python
import weaviate
import os

# --- 1. Load environment variables ---
try:
    WEAVIATE_URL = os.environ["WCD_TEST_URL"]
    WEAVIATE_API_KEY = os.environ["WCD_TEST_KEY"]
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
except KeyError as e:
    print(f"Error: Missing environment variable {e}.")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY in your environment.")
    exit(1)

# --- 2. Connect to Weaviate Cloud ---
client = None
try:
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_wcs(
        cluster_url=WEAVIATE_URL,
        auth_credentials=weaviate.AuthApiKey(WEAVIATE_API_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )

    if client.is_connected():
        print(f"Successfully connected to Weaviate at {WEAVIATE_URL}")
    else:
        print("Failed to connect to Weaviate.")
        exit(1)

    # --- 3. Get the 'WineReview' collection ---
    wine_reviews_collection = client.collections.get("WineReview")

    # --- 4. Define the query parameters ---
    query_text = "dessert wine"
    max_results_limit = 2
    return_properties = ["title", "country", "price", "points"]

    print(f"\nSearching for wines best matching: '{query_text}' (Limit: {max_results_limit} results)")

    # --- 5. Perform the vector search using near_text ---
    response = wine_reviews_collection.query.near_text(
        query=query_text,
        limit=max_results_limit,
        return_properties=return_properties
    )

    # --- 6. Print the matching wine details ---
    if response.objects:
        print("\n--- Matching Wines ---")
        for i, obj in enumerate(response.objects):
            print(f"\nResult {i+1}:")
            print(f"  Title: {obj.properties.get('title', 'N/A')}")
            print(f"  Country: {obj.properties.get('country', 'N/A')}")
            # Format price if available, otherwise print N/A
            price = obj.properties.get('price')
            print(f"  Price: ${price:.2f}" if price is not None else "  Price: N/A")
            print(f"  Points: {obj.properties.get('points', 'N/A')}")
    else:
        print("No matching wines found for the query.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Weaviate connection error: {e}. Check your URL and network connection.")
except weaviate.exceptions.WeaviateAuthError as e:
    print(f"Weaviate authentication error: {e}. Check your WCD_TEST_KEY and OPENAI_API_KEY.")
except weaviate.exceptions.WeaviateGRPCError as e:
    print(f"Weaviate GRPC error: {e}. This might indicate issues with the collection schema or data.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # --- 7. Close the Weaviate client connection ---
    if client:
        client.close()
        print("\nWeaviate client connection closed.")
```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate at yqdvcmlqrpwgtemp3keqpw.c0.europe-west3.gcp.weaviate.cloud

Searching for wines best matching: 'dessert wine' (Limit: 2 results)

--- Matching Wines ---

Result 1:
  Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
  Country: US
  Price: $24.00
  Points: 88

Result 2:
  Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
  Country: US
  Price: $40.00
  Points: 88

Weaviate client connection closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:18: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 5.94s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# 1. Get API keys and cluster URL from environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if environment variables are set
if not WCD_TEST_URL:
    raise ValueError("Environment variable WCD_TEST_URL not set.")
if not WCD_TEST_KEY:
    raise ValueError("Environment variable WCD_TEST_KEY not set.")
if not OPENAI_API_KEY:
    raise ValueError("Environment variable OPENAI_API_KEY not set.")

# Initialize client outside of try-finally block to ensure it's defined
client = None
try:
    # 2. Connect to Weaviate Cloud
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        },
    )
    print("Successfully connected to Weaviate Cloud.")

    # 3. Get the 'WineReview' collection
    collection = client.collections.get("WineReview")
    print("Accessed 'WineReview' collection.")

    # 4. Perform the query
    print("Querying for 'dessert wine' (top 2 results)...")
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        # Specify which properties to retrieve to optimize performance
        return_properties=["title", "country", "price", "points"]
    )

    # 5. Print the results
    if response.objects:
        print("\nMatching wines:")
        for i, obj in enumerate(response.objects):
            print(f"--- Result {i+1} ---")
            properties = obj.properties
            print(f"Title: {properties.get('title', 'N/A')}")
            print(f"Country: {properties.get('country', 'N/A')}")
            print(f"Price: ${properties.get('price', 'N/A')}")
            print(f"Points: {properties.get('points', 'N/A')}")
    else:
        print("\nNo matching wines found for the query 'dessert wine'.")

except weaviate.exceptions.WeaviateException as e:
    print(f"Weaviate error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # 6. Close the client connection
    if client:
        print("\nClosing Weaviate client connection.")
        client.close()
    print("Script finished.")
```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate Cloud.
Accessed 'WineReview' collection.
Querying for 'dessert wine' (top 2 results)...

Matching wines:
--- Result 1 ---
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: $24.0
Points: 88
--- Result 2 ---
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: $40.0
Points: 88

Closing Weaviate client connection.
Script finished.

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 6.46s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.collections import Collection

# Load environment variables
WEAVIATE_URL = os.environ.get("WCD_TEST_URL")
WEAVIATE_API_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Ensure all necessary environment variables are set
if not all([WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY]):
    raise EnvironmentError(
        "Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY "
        "environment variables before running the script."
    )

client = None  # Initialize client to None
try:
    # 1. Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY  # Required for text2vec-openai vectorizer
        }
    )

    # Check if the client is connected
    if client.is_connected():
        print("Successfully connected to Weaviate Cloud.")
    else:
        print("Failed to connect to Weaviate Cloud.")
        exit()

    # 2. Get the 'WineReview' collection
    # Note: If the collection doesn't exist, this will raise a NotFoundError.
    # For a robust solution, you might want to add a check for existence
    # or a creation step if it's an initial setup.
    wine_collection: Collection = client.collections.get("WineReview")
    print("\nQuerying 'WineReview' collection for 'dessert wine'...")

    # 3. Query the collection using near_text
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2,  # Limit to a maximum of 2 results
        # Specify properties to return
        return_properties=["title", "country", "price", "points"]
    )

    # 4. Print the results
    if response.objects:
        print(f"\nFound {len(response.objects)} matching wines:")
        for i, obj in enumerate(response.objects):
            print(f"\n--- Result {i+1} ---")
            print(f"Title: {obj.properties.get('title', 'N/A')}")
            print(f"Country: {obj.properties.get('country', 'N/A')}")
            print(f"Price: {obj.properties.get('price', 'N/A')}")
            print(f"Points: {obj.properties.get('points', 'N/A')}")
    else:
        print("\nNo matching wines found.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Weaviate connection error: {e}")
except weaviate.exceptions.NotFoundError as e:
    print(f"Error: Collection 'WineReview' not found. Please ensure it exists in your Weaviate instance. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # 5. Close the client connection
    if client:
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Successfully connected to Weaviate Cloud.

Querying 'WineReview' collection for 'dessert wine'...

Found 2 matching wines:

--- Result 1 ---
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price: 24.0
Points: 88

--- Result 2 ---
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88

Weaviate client connection closed.

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.65s)

**Generated Code**:
```python
import os
import weaviate
import weaviate.classes.query as qc
import weaviate.classes.config as wc

# 1. Load Weaviate and OpenAI API keys from environment variables
WCD_URL = os.getenv("WCD_TEST_URL")
WCD_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not all([WCD_URL, WCD_KEY, OPENAI_API_KEY]):
    print("Error: Please set the following environment variables:")
    print("  - WCD_TEST_URL (Weaviate Cloud URL)")
    print("  - WCD_TEST_KEY (Weaviate Cloud API Key)")
    print("  - OPENAI_API_KEY (OpenAI API Key for text2vec-openai)")
    exit(1)

# 2. Connect to Weaviate Cloud
client = None # Initialize client to None for finally block
try:
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_wcs(
        cluster_url=WCD_URL,
        auth_credentials=weaviate.AuthApiKey(WCD_KEY),
        headers={
            "X-OpenAI-Api-Key": OPENAI_API_KEY
        }
    )
    print("Successfully connected to Weaviate Cloud.")

    # 3. Get the 'WineReview' collection object
    wine_reviews = client.collections.get("WineReview")

    # 4. Define the filters
    # Filter 1: Price and Points conditions (AND)
    price_points_filter = (
        qc.Filter.by_property("price").less_than(50)
        & qc.Filter.by_property("points").greater_than(90)
    )

    # Filter 2: review_body substring conditions (OR)
    # Note: Weaviate's 'like' operator uses '%' as a wildcard at the beginning/end
    # The Python client uses '*' for convenience, which gets translated to '%' internally.
    review_body_content_filter = (
        qc.Filter.by_property("review_body").like("*spice*")
        | qc.Filter.by_property("review_body").like("*fruit*")
        | qc.Filter.by_property("review_body").like("*berry*")
        | qc.Filter.by_property("review_body").like("*cherry*")
        | qc.Filter.by_property("review_body").like("*honey*")
    )

    # Combine both filters with an AND operation
    combined_filter = price_points_filter & review_body_content_filter

    # 5. Perform the hybrid search query
    print(f"\nSearching for wines that 'pair with steak' (hybrid alpha=0.5)...")
    print(f"Applying filters: Price < 50, Points > 90, and review_body contains specific keywords.")

    response = wine_reviews.query.hybrid(
        query="pair with steak",
        alpha=0.5,           # Hybrid search blend factor
        limit=5,             # Maximum 5 results
        # Specify properties for the keyword search part of hybrid query
        # (useful if you want to emphasize certain fields for keyword matching)
        query_properties=["title", "description", "review_body"],
        # Define which properties to return for each object
        return_properties=["title", "country", "price", "points"],
        filters=combined_filter # Apply the combined filters
    )

    # 6. Print the results
    if response.objects:
        print("\n--- Matching Wines Found ---")
        for i, obj in enumerate(response.objects):
            props = obj.properties
            print(f"\nResult {i+1}:")
            print(f"  Title: {props.get('title', 'N/A')}")
            print(f"  Country: {props.get('country', 'N/A')}")
            print(f"  Price: ${props.get('price', 'N/A'):.2f}")
            print(f"  Points: {props.get('points', 'N/A')}")
            # print(f"  Review Body (filtered on, not returned): (Not displayed)") # For verification if needed
        print("\n----------------------------")
    else:
        print("\nNo wines found matching the specified criteria.")

except weaviate.exceptions.WeaviateConnectionError as e:
    print(f"Weaviate Connection Error: {e}")
except weaviate.exceptions.WeaviateBaseError as e:
    print(f"Weaviate API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # 7. Close the Weaviate client connection
    if client:
        client.close()
        print("Connection to Weaviate closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate Cloud.

Searching for wines that 'pair with steak' (hybrid alpha=0.5)...
Applying filters: Price < 50, Points > 90, and review_body contains specific keywords.
Weaviate API Error: Query call with protocol GRPC search failed with message object search at index winereview: local shard object search winereview_3Pp7LBMzKD4W: Searching by property 'description' requires inverted index. Is `indexSearchable` option of property 'description' enabled? Set it to `true` or leave empty.
Connection to Weaviate closed.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:22: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 13.32s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter
import os

# 1. Retrieve Weaviate and OpenAI API keys from environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure all necessary environment variables are set
if not all([WCD_TEST_URL, WCD_TEST_KEY, OPENAI_API_KEY]):
    raise ValueError(
        "Please set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY."
        "\nExample: export WCD_TEST_URL='YOUR_WCD_URL' export WCD_TEST_KEY='YOUR_WCD_KEY' export OPENAI_API_KEY='YOUR_OPENAI_KEY'"
    )

client = None  # Initialize client to None for finally block

try:
    # 2. Connect to Weaviate Cloud
    print("Connecting to Weaviate Cloud...")
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
        headers={
            "X-OpenAI-API-Key": OPENAI_API_KEY  # Required for text2vec-openai vectorizer
        },
    )
    print("Successfully connected to Weaviate.")

    # 3. Get the 'WineReview' collection
    wine_review_collection = client.collections.get("WineReview")
    print("Accessing 'WineReview' collection...")

    # 4. Perform a hybrid search query with filters
    print("Executing hybrid query...")
    response = wine_review_collection.query.hybrid(
        query="pair with steak",
        limit=5,  # Maximum 5 results
        alpha=0.5,  # Hybrid search alpha value
        filters=(
            # Price less than 50
            Filter.by_property("price").less_than(50) &
            # Points greater than 90
            Filter.by_property("points").greater_than(90) &
            # Review body contains at least one of the specified substrings
            Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
        ),
        # Specify which properties to return for each matching object
        return_properties=["title", "country", "price", "points"]
    )

    # 5. Print the results
    print(f"\nFound {len(response.objects)} wines matching the criteria:")
    if not response.objects:
        print("No matching wines found.")
    else:
        for i, obj in enumerate(response.objects):
            print(f"\n--- Wine {i+1} ---")
            # Access properties using .get() for robustness
            print(f"Title: {obj.properties.get('title', 'N/A')}")
            print(f"Country: {obj.properties.get('country', 'N/A')}")
            # Format price to two decimal places
            print(f"Price: ${obj.properties.get('price', 0.0):.2f}")
            print(f"Points: {obj.properties.get('points', 'N/A')}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 6. Close the client connection
    if client and client.is_connected():
        client.close()
        print("\nWeaviate client connection closed.")

```

**Output**:
```
Connecting to Weaviate Cloud...
Successfully connected to Weaviate.
Accessing 'WineReview' collection...
Executing hybrid query...

Found 5 wines matching the criteria:

--- Wine 1 ---
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: $40.00
Points: 92

--- Wine 2 ---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: $49.00
Points: 91

--- Wine 3 ---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: $27.00
Points: 91

--- Wine 4 ---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: $25.00
Points: 93

--- Wine 5 ---
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: $0.00
Points: 92

Weaviate client connection closed.

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 8.08s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# Ensure environment variables are set
# For local testing, you might need to set these in your shell or .env file
# For example:
# export WCD_TEST_URL="YOUR_WEAVIATE_CLUSTER_URL"
# export WCD_TEST_KEY="YOUR_WEAVIATE_API_KEY"
# export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

# Connect to Weaviate Cloud
client = None
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
        }
    )

    # Get the 'WineReview' collection
    wine_reviews_collection = client.collections.get("WineReview")

    # Define the search query
    search_query = "pair with steak"

    # Define the filters
    # Price less than 50
    price_filter = Filter.by_property("price").less_than(50)
    # Points greater than 90
    points_filter = Filter.by_property("points").greater_than(90)
    # Review body contains any of "spice", "fruit", "berry", "cherry", or "honey"
    review_body_filter = Filter.by_property("review_body").contains_any(
        ["spice", "fruit", "berry", "cherry", "honey"]
    )

    # Combine all filters using logical AND
    combined_filters = price_filter & points_filter & review_body_filter

    print(f"Searching for wines that best match: '{search_query}'")
    print("Applying filters: Price < 50, Points > 90, Review contains 'spice', 'fruit', 'berry', 'cherry', or 'honey'")
    print("Limit: 5 results, Hybrid search alpha: 0.5\n")

    # Perform the hybrid search with specified parameters
    response = wine_reviews_collection.query.hybrid(
        query=search_query,
        alpha=0.5,
        limit=5,
        filters=combined_filters,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the results
    if response.objects:
        print("Found matching wines:")
        for i, wine in enumerate(response.objects):
            print(f"--- Result {i+1} ---")
            print(f"Title: {wine.properties.get('title', 'N/A')}")
            print(f"Country: {wine.properties.get('country', 'N/A')}")
            print(f"Price: {wine.properties.get('price', 'N/A')}")
            print(f"Points: {wine.properties.get('points', 'N/A')}")
            print("-" * 20)
    else:
        print("No wines found matching the criteria.")

except KeyError as e:
    print(f"Error: Environment variable {e} not set. Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if client:
        client.close()
        print("\nWeaviate client closed.")
```

**Output**:
```
Searching for wines that best match: 'pair with steak'
Applying filters: Price < 50, Points > 90, Review contains 'spice', 'fruit', 'berry', 'cherry', or 'honey'
Limit: 5 results, Hybrid search alpha: 0.5

Found matching wines:
--- Result 1 ---
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
--------------------
--- Result 2 ---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
--------------------
--- Result 3 ---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
--------------------
--- Result 4 ---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
--------------------
--- Result 5 ---
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
--------------------

Weaviate client closed.

```

---

### gemini/gemini-2.5-flash-lite

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 1.96s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud URL and API key from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")

if not weaviate_url or not weaviate_api_key:
    raise ValueError(
        "Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables."
    )

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
)

# Check if the server is ready
try:
    client.is_ready()
    print("Weaviate server is ready to accept requests.")
except Exception as e:
    print(f"Error connecting to Weaviate server: {e}")
    # Optionally re-raise the exception if you want to halt execution
    # raise e
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

**Status**: ✅ SUCCESS (runtime: 1.89s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Retrieve Weaviate Cloud credentials from environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")

# Ensure environment variables are set
if not wcd_url:
    raise ValueError("WCD_TEST_URL environment variable is not set.")
if not wcd_key:
    raise ValueError("WCD_TEST_KEY environment variable is not set.")

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=wcd_url,
    auth_credentials=Auth.api_key(wcd_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

# Close the client connection (optional but good practice)
client.close()

print("Successfully connected to Weaviate Cloud and server is ready.")
```

**Output**:
```
Successfully connected to Weaviate Cloud and server is ready.

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 4.52s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud connection details from environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

# Check if environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Initialize the Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(weaviate_api_key),
)

collection_name = "DemoProducts"

# Check if the collection exists and delete it if it does
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it...")
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")
else:
    print(f"Collection '{collection_name}' does not exist. Creating it...")

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
client.collections.create(
    collection_schema["name"],
    properties=collection_schema["properties"]
)

print(f"Collection '{collection_name}' created successfully with the defined properties.")

# Optional: Verify the collection creation
if client.collections.exists(collection_name):
    print(f"Verification: Collection '{collection_name}' exists.")
    retrieved_schema = client.collections.get(collection_name).properties
    print("Collection Schema:")
    for prop in retrieved_schema:
        print(f"- Name: {prop['name']}, Data Type: {prop['dataType']}")
else:
    print(f"Verification failed: Collection '{collection_name}' could not be found.")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ✅ SUCCESS (runtime: 6.85s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get Weaviate Cloud credentials from environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to the Weaviate Cloud instance
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key)
    )
    print("Successfully connected to Weaviate Cloud.")
except weaviate.UnexpectedStatusCodeException as e:
    print(f"Error connecting to Weaviate Cloud: {e}")
    exit()

# Define the collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it.")
    try:
        client.collections.delete(collection_name)
        print(f"Collection '{collection_name}' deleted successfully.")
    except weaviate.UnexpectedStatusCodeException as e:
        print(f"Error deleting collection '{collection_name}': {e}")
        # Continue to try creating the collection even if deletion failed,
        # as it might be a permission issue or transient error.

# Create the collection with specified properties
print(f"Creating collection '{collection_name}'...")
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
    print(f"Collection '{products_collection.name}' created successfully.")
except weaviate.UnexpectedStatusCodeException as e:
    print(f"Error creating collection '{collection_name}': {e}")

# Close connection
client.close()
print("Connection to Weaviate Cloud closed.")
```

**Output**:
```
Successfully connected to Weaviate Cloud.
Collection 'DemoProducts' already exists. Deleting it.
Collection 'DemoProducts' deleted successfully.
Creating collection 'DemoProducts'...
Collection 'DemoProducts' created successfully.
Connection to Weaviate Cloud closed.

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 2.48s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.config import Property, DataType
import os

# Replace with your actual environment variable names if they differ
WEAVIATE_URL_ENV_VAR = "WCD_TEST_URL"
WEAVIATE_KEY_ENV_VAR = "WCD_TEST_KEY"

# Retrieve Weaviate Cloud credentials from environment variables
weaviate_url = os.getenv(WEAVIATE_URL_ENV_VAR)
weaviate_key = os.getenv(WEAVIATE_KEY_ENV_VAR)

if not weaviate_url or not weaviate_key:
    raise ValueError(
        f"Please set the environment variables '{WEAVIATE_URL_ENV_VAR}' and '{WEAVIATE_KEY_ENV_VAR}'"
    )

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.Auth.api_key(weaviate_key),
)

collection_name = "DemoProducts"

try:
    # Check if the collection exists and delete it if it does
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
        ],
        # You can optionally configure a vectorizer here if you plan to perform semantic searches.
        # For example, using Weaviate's built-in text2vec-weaviate:
        # vector_config=weaviate.classes.config.Configure.Vectors.text2vec_weaviate(),
    )
    print(f"Collection '{collection_name}' created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    client.close()
    print("Weaviate client connection closed.")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 21, in <module>
    auth_credentials=weaviate.Auth.api_key(weaviate_key),
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 145, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute Auth

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 5.44s)

**Generated Code**:
```python
import os
import weaviate
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get Weaviate Cloud connection details from environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_key = os.getenv("WCD_TEST_KEY")

if not weaviate_url or not weaviate_key:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(weaviate_key),
)

# Define the collection schema
collection_name = "DemoProducts"
schema = {
    "classes": [
        {
            "class": collection_name,
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
            ],
        }
    ]
}

# Create the collection if it doesn't exist
if not client.schema.exists(collection_name):
    client.schema.create(schema)
    print(f"Collection '{collection_name}' created.")
else:
    print(f"Collection '{collection_name}' already exists.")

# Prepare objects for batch import
objects_to_import = []
for i in range(50):
    objects_to_import.append({
        "name": f"Product {i}",
        "description": f"Description {i}"
    })

# Batch import the objects
try:
    with client.batch as batch:
        batch.add_objects(
            collection_name=collection_name,
            objects=objects_to_import
        )
    print(f"Successfully imported {len(objects_to_import)} objects into '{collection_name}'.")
except Exception as e:
    print(f"An error occurred during batch import: {e}")

# Get and print the number of objects in the collection
try:
    count_result = client.query.aggregate(collection_name).with_total_count().do()
    if 'data' in count_result and 'Get' in count_result['data'] and collection_name in count_result['data']['Get'] and 'totalCount' in count_result['data']['Get'][collection_name]:
        num_objects = count_result['data']['Get'][collection_name]['totalCount']
        print(f"Number of objects in '{collection_name}': {num_objects}")
    else:
        print(f"Could not retrieve the total count for '{collection_name}'. Result: {count_result}")
except Exception as e:
    print(f"An error occurred while retrieving the object count: {e}")
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 4.94s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.auth import Auth

# Get Weaviate Cloud credentials from environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")

# Connect to Weaviate Cloud
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(api_key),
    )
    print("Successfully connected to Weaviate Cloud.")
except Exception as e:
    print(f"Error connecting to Weaviate Cloud: {e}")
    exit()

collection_name = "DemoProducts"

# Ensure the collection exists, create if not
if not client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' does not exist. Creating it...")
    client.collections.create(
        name=collection_name,
        properties=[
            weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
            weaviate.Property(name="description", data_type=weaviate.DataType.TEXT),
        ]
    )
    print(f"Collection '{collection_name}' created.")
else:
    print(f"Collection '{collection_name}' already exists.")

# Get the collection object
collection = client.collections.get(collection_name)

# Generate 50 arbitrary objects
data_rows = [
    {
        "name": f"Product {i+1}",
        "description": f"This is the description for product number {i+1}."
    } for i in range(50)
]

# Batch import objects
print("Starting batch import...")
try:
    with collection.batch.dynamic() as batch:
        for data_row in data_rows:
            batch.add_object(
                properties=data_row,
            )
            # Optional: add a check for errors during batching
            if batch.number_errors > 10:
                print("Batch import stopped due to excessive errors.")
                break
    print("Batch import completed.")

    # Check for failed imports
    failed_objects = collection.batch.failed_objects
    if failed_objects:
        print(f"Number of failed imports: {len(failed_objects)}")
        # print(f"First failed object: {failed_objects[0]}") # Uncomment to see details of a failed object
    else:
        print("All objects imported successfully.")

except Exception as e:
    print(f"An error occurred during batch import: {e}")

# Print the number of objects in the collection
try:
    num_objects = len(collection)
    print(f"Number of objects in the '{collection_name}' collection: {num_objects}")
except Exception as e:
    print(f"Error retrieving object count: {e}")

# Close the client connection
client.close()
print("Weaviate client connection closed.")
```

**Output**:
```
Successfully connected to Weaviate Cloud.
Collection 'DemoProducts' already exists.
Starting batch import...
Batch import completed.
All objects imported successfully.
Number of objects in the 'DemoProducts' collection: 50
Weaviate client connection closed.

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 3.12s)

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

# Define the collection schema
collection_name = "DemoProducts"
properties = [
    Property(name="name", data_type=DataType.TEXT),
    Property(name="description", data_type=DataType.TEXT),
]

# Create the collection if it doesn't exist
if not client.collections.exists(collection_name):
    client.collections.create(
        collection_name,
        properties=properties,
    )
    print(f"Collection '{collection_name}' created.")
else:
    print(f"Collection '{collection_name}' already exists.")

collection = client.collections.get(collection_name)

# Batch import 50 arbitrary objects
print("Starting batch import...")
with collection.batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i+1}",
                "description": f"This is the description for product number {i+1}.",
            }
        )
print("Batch import complete.")

# Print the number of objects in the collection
num_objects = collection.query.get().with_limit(1).with_fields("name").do()["Get"][collection_name]
print(f"Number of objects in the '{collection_name}' collection: {num_objects}")


# Close the client connection
client.close()
```

**Output**:
```
Collection 'DemoProducts' already exists.
Starting batch import...
Batch import complete.

```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 49, in <module>
    num_objects = collection.query.get().with_limit(1).with_fields("name").do()["Get"][collection_name]
AttributeError: '_QueryCollection' object has no attribute 'get'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:302: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
sys:1: ResourceWarning: unclosed <ssl.SSLSocket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.2', 48984), raddr=('34.111.245.21', 443)>

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 2.44s)

**Generated Code**:
```python
import os
import weaviate

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=os.getenv("WCD_TEST_URL"),
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WCD_TEST_KEY")),
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

# Define the query
query = "dessert wine"

# Perform the nearText search
try:
    result = (
        client.query
        .get("WineReview", ["title", "country", "price", "points"])
        .with_near_text({"concepts": query})
        .with_limit(2)
        .do()
    )

    # Print the results
    if "data" in result and "Get" in result["data"] and "WineReview" in result["data"]["Get"]:
        for wine in result["data"]["Get"]["WineReview"]:
            print(f"Title: {wine.get('title')}")
            print(f"Country: {wine.get('country')}")
            print(f"Price: {wine.get('price')}")
            print(f"Points: {wine.get('points')}")
            print("-" * 20)
    else:
        print("No results found or unexpected response format.")

except Exception as e:
    print(f"An error occurred: {e}")

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:5: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 5, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.55s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Get connection details from environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure all required environment variables are set
if not all([weaviate_url, weaviate_key, openai_api_key]):
    raise ValueError("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")

try:
    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_key),
        headers={
            "X-OpenAI-API-Key": openai_api_key
        },
    )

    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Query the collection for "dessert wine"
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        include_vector=False  # We don't need the vector for this output
    )

    # Print the title, country, price, and points of each matching wine
    if response.objects:
        print("Matching wines:")
        for obj in response.objects:
            properties = obj.properties
            print(f"  Title: {properties.get('title', 'N/A')}")
            print(f"  Country: {properties.get('country', 'N/A')}")
            print(f"  Price: {properties.get('price', 'N/A')}")
            print(f"  Points: {properties.get('points', 'N/A')}")
            print("-" * 20)
    else:
        print("No matching wines found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    if 'client' in locals() and client:
        client.close()
```

**Output**:
```
Matching wines:
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

**Status**: ✅ SUCCESS (runtime: 3.30s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
import os

# Connect to Weaviate Cloud
try:
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={
            # Add inference API keys as needed
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
    for wine in response.objects:
        print(f"Title: {wine.properties.get('title')}")
        print(f"Country: {wine.properties.get('country')}")
        print(f"Price: {wine.properties.get('price')}")
        print(f"Points: {wine.properties.get('points')}")
        print("-" * 20)

except weaviate.UnexpectedStatusCodeException as e:
    print(f"An error occurred: {e}")
    print("Please ensure that:")
    print("1. The WCD_TEST_URL and WCD_TEST_KEY environment variables are set correctly.")
    print("2. The OPENAI_API_KEY environment variable is set correctly.")
    print("3. The 'WineReview' collection exists and uses the 'text2vec-openai' vectorizer.")
except KeyError as e:
    print(f"Environment variable not set: {e}")
    print("Please ensure that WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Ensure the client connection is closed
    if 'client' in locals() and client:
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

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 3.63s)

**Generated Code**:
```python
import os
import weaviate

# Get Weaviate Cloud connection details from environment variables
wcd_url = os.environ.get("WCD_TEST_URL")
wcd_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not all([wcd_url, wcd_key, openai_api_key]):
    raise ValueError(
        "Please set the WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables."
    )

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=wcd_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=wcd_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key,
    },
)

# Define the query
query = "pair with steak"

# Define the hybrid search parameters
hybrid_params = {
    "keywords": query,
    "alpha": 0.5,
}

# Define the filter conditions
where_filter = {
    "operator": "And",
    "operands": [
        {
            "path": ["price"],
            "operator": "LessThan",
            "value_number": 50,
        },
        {
            "path": ["points"],
            "operator": "GreaterThan",
            "value_number": 90,
        },
        {
            "operator": "Or",
            "operands": [
                {
                    "path": ["review_body"],
                    "operator": "ContainsAny",
                    "value_string": "spice",
                },
                {
                    "path": ["review_body"],
                    "operator": "ContainsAny",
                    "value_string": "fruit",
                },
                {
                    "path": ["review_body"],
                    "operator": "ContainsAny",
                    "value_string": "berry",
                },
                {
                    "path": ["review_body"],
                    "operator": "ContainsAny",
                    "value_string": "cherry",
                },
                {
                    "path": ["review_body"],
                    "operator": "ContainsAny",
                    "value_string": "honey",
                },
            ],
        },
    ],
}

# Build the GraphQL query
try:
    response = (
        client.query.get(
            "WineReview",
            [
                "title",
                "country",
                "price",
                "points",
            ],
        )
        .with_hybrid(**hybrid_params)
        .with_where(where_filter)
        .with_limit(5)
        .do()
    )

    # Print the results
    if response and "data" in response and "Get" in response["data"] and "WineReview" in response["data"]["Get"]:
        wines = response["data"]["Get"]["WineReview"]
        if wines:
            print("Matching wines:")
            for wine in wines:
                print(f"- Title: {wine.get('title', 'N/A')}")
                print(f"  Country: {wine.get('country', 'N/A')}")
                print(f"  Price: {wine.get('price', 'N/A')}")
                print(f"  Points: {wine.get('points', 'N/A')}")
        else:
            print("No wines found matching the criteria.")
    else:
        print("Error retrieving data or no results found.")
        if response:
            print("Response:", response)

except Exception as e:
    print(f"An error occurred: {e}")

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

**Status**: ✅ SUCCESS (runtime: 3.22s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery
import os

# Retrieve credentials from environment variables
WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

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

    # Get the WineReview collection
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
        return_properties=["title", "country", "price", "points"],
        return_metadata=MetadataQuery(score=True)
    )

    # Print the results
    if response.objects:
        print("Matching wines:")
        for obj in response.objects:
            print(f"  Title: {obj.properties['title']}")
            print(f"  Country: {obj.properties['country']}")
            print(f"  Price: ${obj.properties['price']}")
            print(f"  Points: {obj.properties['points']}")
            print(f"  Score: {obj.metadata.score:.4f}")
            print("-" * 20)
    else:
        print("No wines found matching the criteria.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the client connection
    if 'client' in locals() and client:
        client.close()
```

**Output**:
```
Matching wines:
  Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.0
  Points: 92
  Score: 0.5000
--------------------
  Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.0
  Points: 91
  Score: 0.3765
--------------------
  Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.0
  Points: 91
  Score: 0.0451
--------------------
  Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.0
  Points: 93
  Score: 0.0162
--------------------
  Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.0
  Points: 92
  Score: 0.0010
--------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 3.95s)

**Generated Code**:
```python
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion
from weaviate.classes.config import DataType, Property
import os

# Connect to Weaviate Cloud
try:
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
    search_query = "pair with steak"
    keyword_filters = [
        Filter.by_property("review_body").contains_any(["spice", "fruit", "berry", "cherry", "honey"])
    ]
    price_filter = Filter.by_property("price").less_than(50)
    points_filter = Filter.by_property("points").greater_than(90)

    # Combine all filters
    combined_filters = Filter.all_of(
        filters=[
            Filter.any_of(filters=keyword_filters),
            price_filter,
            points_filter
        ]
    )

    # Perform the hybrid search
    response = wine_reviews.query.hybrid(
        query=search_query,
        alpha=0.5,  # Hybrid search balance
        filters=combined_filters,
        limit=5,
        return_properties=["title", "country", "price", "points", "review_body"]
    )

    # Print the results
    if response.objects:
        print(f"Found {len(response.objects)} wines that match your criteria:")
        for wine in response.objects:
            print(f"- Title: {wine.properties['title']}")
            print(f"  Country: {wine.properties['country']}")
            print(f"  Price: ${wine.properties['price']:.2f}")
            print(f"  Points: {wine.properties['points']}")
    else:
        print("No wines found matching your criteria.")

except KeyError as e:
    print(f"Environment variable not set: {e}")
    print("Please set WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY environment variables.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the client connection
    if 'client' in locals() and client:
        client.close()
```

**Output**:
```
Found 5 wines that match your criteria:
- Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
  Country: US
  Price: $40.00
  Points: 92
- Title: Bink 2014 Pinot Noir (Anderson Valley)
  Country: US
  Price: $49.00
  Points: 91
- Title: Doña Silvina 2011 Malbec (Mendoza)
  Country: Argentina
  Price: $27.00
  Points: 91
- Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
  Country: Hungary
  Price: $25.00
  Points: 93
- Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
  Country: Italy
  Price: $0.00
  Points: 92

```

---

### openai/gpt-5-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 19.66s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

url = os.environ["WCD_TEST_URL"]
api_key = os.environ["WCD_TEST_KEY"]

with weaviate.connect_to_wcs(
    cluster_url=url,
    auth_credentials=Auth.api_key(api_key),
) as client:
    if client.is_ready():
        print("Weaviate server is ready.")
    else:
        raise SystemExit("Weaviate server is not ready.")
```

**Output**:
```
Weaviate server is ready.

```

**Errors**:
```
/code/code.py:8: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  with weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 9.70s)

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

**Status**: ❌ FAILURE (runtime: 19.80s)

**Generated Code**:
```python

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 12.14s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Read connection details from environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

if not cluster_url or not api_key:
    raise ValueError("Please set the WCD_TEST_URL and WCD_TEST_KEY environment variables.")

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

**Status**: ✅ SUCCESS (runtime: 20.26s)

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
    # Delete collection if it already exists
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the collection with properties
    client.collections.create(
        "DemoProducts",
        # Recommended for Weaviate Cloud; no third-party API key required
        vector_config=Configure.Vectors.text2vec_weaviate(),
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ],
    )
finally:
    client.close()
```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 23.20s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 19.53s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 30.89s)

**Generated Code**:
```python

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 18.28s)

**Generated Code**:
```python
import os
import weaviate

# Connect to Weaviate Cloud (WCS) and pass the OpenAI API key for text2vec-openai
client = weaviate.connect_to_wcs(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.AuthApiKey(os.environ["WCD_TEST_KEY"]),
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
)

try:
    collection = client.collections.get("WineReview")

    result = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"],
    )

    for obj in result.objects:
        props = obj.properties or {}
        print(f"Title:   {props.get('title')}")
        print(f"Country: {props.get('country')}")
        print(f"Price:   {props.get('price')}")
        print(f"Points:  {props.get('points')}")
        print("-" * 40)
finally:
    client.close()
```

**Output**:
```
Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price:   24.0
Points:  88
----------------------------------------
Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price:   40.0
Points:  88
----------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:5: DeprecatedWarning: connect_to_wcs is deprecated as of 4.6.2. 
This method is deprecated and will be removed in a future release. Use :func:`connect_to_weaviate_cloud` instead.

  client = weaviate.connect_to_wcs(
/usr/local/lib/python3.9/site-packages/deprecation.py:260: DeprecationWarning: This method is deprecated and will be removed in a future release. Use `connect_to_weaviate_cloud` instead.
  return function(*args, **kwargs)

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 20.91s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    cluster_url = os.environ["WCD_TEST_URL"]
    wcd_api_key = os.environ["WCD_TEST_KEY"]
    openai_key = os.environ["OPENAI_API_KEY"]

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=cluster_url,
        auth_credentials=Auth.api_key(wcd_api_key),
        headers={"X-OpenAI-API-Key": openai_key},
    )

    try:
        collection = client.collections.get("WineReview")

        response = collection.query.near_text(
            query="dessert wine",
            limit=2
        )

        for obj in response.objects:
            props = obj.properties or {}
            print(f"Title: {props.get('title')}")
            print(f"Country: {props.get('country')}")
            print(f"Price: {props.get('price')}")
            print(f"Points: {props.get('points')}")
            print()
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

Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price: 40.0
Points: 88


```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 25.50s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

def main():
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
        headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
    ) as client:
        collection = client.collections.get("WineReview")
        response = collection.query.near_text(
            query="dessert wine",
            limit=2,
            return_properties=["title", "country", "price", "points"],
        )

        for obj in response.objects:
            props = obj.properties or {}
            print(
                f"Title: {props.get('title')}, "
                f"Country: {props.get('country')}, "
                f"Price: {props.get('price')}, "
                f"Points: {props.get('points')}"
            )

if __name__ == "__main__":
    main()
```

**Output**:
```
Title: Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)), Country: US, Price: 24.0, Points: 88
Title: Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast), Country: US, Price: 40.0, Points: 88

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 28.10s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 19.05s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Load environment variables
cluster_url = os.environ["WCD_TEST_URL"]
wcd_api_key = os.environ["WCD_TEST_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(wcd_api_key),
    headers={"X-OpenAI-Api-Key": openai_api_key},
)

try:
    collection = client.collections.get("WineReview")

    response = collection.query.hybrid(
        query="pair with steak",
        limit=5,
        alpha=0.5,
        filters=(
            Filter.by_property("price").less_than(50)
            & Filter.by_property("points").greater_than(90)
            & Filter.by_property("review_body").contains_any(
                ["spice", "fruit", "berry", "cherry", "honey"]
            )
        ),
        return_properties=["title", "country", "price", "points"],
        return_metadata=MetadataQuery(score=True),
    )

    for obj in response.objects:
        props = obj.properties or {}
        print(f"Title: {props.get('title')}")
        print(f"Country: {props.get('country')}")
        print(f"Price: {props.get('price')}")
        print(f"Points: {props.get('points')}")
        print(f"Score: {obj.metadata.score}")
        print("---")
finally:
    client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir
Country: US
Price: 40.0
Points: 92
Score: 0.5
---
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
Score: 0.3765353560447693
---
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Score: 0.04513849690556526
---
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Score: 0.016171861439943314
---
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
Score: 0.0010482011130079627
---

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 41.80s)

**Generated Code**:
```python

```

---

### openai/gpt-5-mini-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 14.46s)

**Generated Code**:
```python
import os
import sys
import weaviate

url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

if not url or not api_key:
    print("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.", file=sys.stderr)
    sys.exit(2)

client = weaviate.Client(
    url=url,
    auth_client_secret=weaviate.AuthApiKey(api_key=api_key)
)

if client.is_ready():
    print("Weaviate is ready")
    sys.exit(0)
else:
    print("Weaviate is not ready", file=sys.stderr)
    sys.exit(1)
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

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 10.20s)

**Generated Code**:
```python
import os
import weaviate

# Read credentials from environment
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
)

# Check the server is ready to accept requests
if not client.is_ready():
    raise SystemExit("Weaviate server is not ready")

client.close()
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

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 32.23s)

**Generated Code**:
```python

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 28.49s)

**Generated Code**:
```python

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 13.91s)

**Generated Code**:
```python
import os
import sys
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    WCD_TEST_URL = os.environ.get("WCD_TEST_URL")
    WCD_TEST_KEY = os.environ.get("WCD_TEST_KEY")

    if not WCD_TEST_URL or not WCD_TEST_KEY:
        print("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")
        sys.exit(1)

    collection_name = "DemoProducts"

    # Use context manager to auto-close the client
    with weaviate.connect_to_weaviate_cloud(
        cluster_url=WCD_TEST_URL,
        auth_credentials=Auth.api_key(WCD_TEST_KEY),
    ) as client:
        try:
            # If the collection exists, delete it first
            if client.collections.exists(collection_name):
                print(f"Collection '{collection_name}' exists — deleting it...")
                client.collections.delete(collection_name)

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

        except Exception as e:
            print("Error:", e)
            sys.exit(1)

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection 'DemoProducts' exists — deleting it...
Collection 'DemoProducts' created with properties: name, description, price, in_stock

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 19.76s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 24.54s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 18.95s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    # Read connection details from environment
    wc_url = os.environ["WCD_TEST_URL"]
    wc_key = os.environ["WCD_TEST_KEY"]

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wc_url,
        auth_credentials=Auth.api_key(wc_key)
    )

    try:
        collection_name = "DemoProducts"

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

        # Get the collection object
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
            # optional: check for errors while still in context
            if batch.number_errors:
                print(f"Batch reported errors: {batch.number_errors}")

        # Check for failed objects after batch completes
        failed = collection.batch.failed_objects
        if failed:
            print(f"Number of failed objects: {len(failed)}")
            # Optionally inspect failed objects
            # for f in failed: print(f)

        # Count objects in the collection by iterating (works reliably)
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
Number of objects in 'DemoProducts': 50

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 17.46s)

**Generated Code**:
```python
import os
import sys
import weaviate

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    sys.exit("Please set WCD_TEST_URL and WCD_TEST_KEY environment variables.")
if not OPENAI_API_KEY:
    sys.exit("Please set OPENAI_API_KEY environment variable.")

# Connect to Weaviate Cloud using API key auth and pass OpenAI key to the server
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
)

# Query the WineReview class for the best matches to "dessert wine", limit 2
response = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({"concepts": ["dessert wine"]})
    .with_limit(2)
    .do()
)

# Extract results
items = response.get("data", {}).get("Get", {}).get("WineReview", [])

if not items:
    print("No results found.")
else:
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
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

**Status**: ❌ FAILURE (runtime: 19.16s)

**Generated Code**:
```python
import os
import weaviate

# Load credentials from environment
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not (WCD_TEST_URL and WCD_TEST_KEY and OPENAI_API_KEY):
    raise RuntimeError("Please set WCD_TEST_URL, WCD_TEST_KEY and OPENAI_API_KEY environment variables.")

# Connect to Weaviate Cloud (latest client syntax)
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={"X-OpenAI-API-Key": OPENAI_API_KEY},
)

try:
    # Get the collection
    collection = client.collections.get("WineReview")

    # Perform a near-text query for "dessert wine" with a maximum of 2 results
    response = collection.query.near_text(
        query="dessert wine",
        limit=2
    )

    # Extract objects robustly (handle different possible return shapes)
    objs = getattr(response, "objects", None) or response.get("objects", []) or []

    for obj in objs:
        props = getattr(obj, "properties", None) or obj.get("properties", {}) or {}
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

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:143: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
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

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 15.56s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Ensure required environment variables are present
for var in ("WCD_TEST_URL", "WCD_TEST_KEY", "OPENAI_API_KEY"):
    if var not in os.environ:
        raise EnvironmentError(f"Environment variable {var} is required")

# Connect to Weaviate Cloud (and provide OpenAI API key for the text2vec-openai vectorizer)
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={"X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]},
)

try:
    collection = client.collections.get("WineReview")

    # Semantic search for "dessert wine" with a maximum of 2 results
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"],
    )

    if not response.objects:
        print("No matching wines found.")
    else:
        for obj in response.objects:
            props = obj.properties or {}
            print("Title:  ", props.get("title"))
            print("Country:", props.get("country"))
            print("Price:  ", props.get("price"))
            print("Points: ", props.get("points"))
            print("-" * 40)
finally:
    client.close()
```

**Output**:
```
Title:   Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA))
Country: US
Price:   24.0
Points:  88
----------------------------------------
Title:   Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast)
Country: US
Price:   40.0
Points:  88
----------------------------------------

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 20.78s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.34s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Load required environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Connect to Weaviate Cloud and forward the OpenAI API Key for text2vec-openai
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=Auth.api_key(WCD_TEST_KEY),
    headers={"X-OpenAI-API-Key": OPENAI_API_KEY},
)

try:
    # Get the WineReview collection
    collection = client.collections.get("WineReview")

    # Build filter:
    # - price < 50
    # - points > 90
    # - review_body contains any of the listed substrings
    review_substrings = ["spice", "fruit", "berry", "cherry", "honey"]
    filters = (
        Filter.by_property("price").less_than(50)
        & Filter.by_property("points").greater_than(90)
        & Filter.by_property("review_body").contains_any(review_substrings)
    )

    # Run hybrid query with alpha=0.5 and limit 5
    response = collection.query.hybrid(
        query="pair with steak",
        limit=5,
        alpha=0.5,
        filters=filters,
        return_metadata=MetadataQuery(score=True),
    )

    # Print requested fields for each matching wine
    for obj in response.objects:
        props = obj.properties or {}
        title = props.get("title")
        country = props.get("country")
        price = props.get("price")
        points = props.get("points")
        score = obj.metadata.score if obj.metadata is not None else None

        print(f"Title: {title}")
        print(f"Country: {country}")
        print(f"Price: {price}")
        print(f"Points: {points}")
        if score is not None:
            print(f"Score: {score:.4f}")
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
Score: 0.5000
----------------------------------------
Title: Bink 2014 Pinot Noir (Anderson Valley)
Country: US
Price: 49.0
Points: 91
Score: 0.3765
----------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Score: 0.0451
----------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Score: 0.0162
----------------------------------------
Title: Tommasi 2007 Ca' Florian  (Amarone della Valpolicella Classico)
Country: Italy
Price: 0.0
Points: 92
Score: 0.0010
----------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 17.01s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# Environment variables required:
# - WCD_TEST_URL : Weaviate Cloud URL
# - WCD_TEST_KEY : Weaviate Cloud API key
# - OPENAI_API_KEY: OpenAI API key (used by text2vec-openai vectorizer)
WCD_URL = os.environ["WCD_TEST_URL"]
WCD_KEY = os.environ["WCD_TEST_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_URL,
    auth_credentials=Auth.api_key(WCD_KEY),
    headers={"X-OpenAI-Api-Key": OPENAI_API_KEY},
)

try:
    collection = client.collections.get("WineReview")

    # Build filter: price < 50 AND points > 90 AND review_body contains at least one of the substrings
    text_subfilters = (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )

    combined_filter = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        text_subfilters
    )

    response = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        fusion_type=HybridFusion.RELATIVE_SCORE,
        limit=5,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points"],
    )

    if not response.objects:
        print("No matching wines found.")
    else:
        for obj in response.objects:
            p = obj.properties or {}
            title = p.get("title", "<no title>")
            country = p.get("country", "<no country>")
            price = p.get("price", "<no price>")
            points = p.get("points", "<no points>")
            print(f"{title} | {country} | ${price} | {points} pts")

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

---

### openai/gpt-5-nano-2025-08-07

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 10.89s)

**Generated Code**:
```python

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 10.10s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Load credentials from environment
cluster_url = os.environ.get('WCD_TEST_URL')
api_key = os.environ.get('WCD_TEST_KEY')

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Check readiness
assert client.is_ready()

# Close the client
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.29s)

**Generated Code**:
```python

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 9.93s)

**Generated Code**:
```python

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 11.53s)

**Generated Code**:
```python
# Ensure you have the latest Weaviate Python client installed:
# pip install weaviate-client

import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.init import Auth

def main():
    # Connect to Weaviate Cloud using environment variables
    # WCD_TEST_URL: Cloud instance URL
    # WCD_TEST_KEY: API key
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=os.environ["WCD_TEST_URL"],
        auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
    )

    # If the collection already exists, delete it first
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the collection with required properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )

    # Close the client when done
    client.close()

if __name__ == "__main__":
    main()
```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 10.46s)

**Generated Code**:
```python

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.10s)

**Generated Code**:
```python

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 9.93s)

**Generated Code**:
```python

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.14s)

**Generated Code**:
```python

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.17s)

**Generated Code**:
```python

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 10.93s)

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

try:
    # Get the WineReview collection
    wine_collection = client.collections.get("WineReview")

    # Semantic search: near_text for "dessert wine" with a limit of 2
    response = wine_collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the desired fields for each matching wine
    for obj in response.objects:
        props = obj.properties
        title = props.get("title")
        country = props.get("country")
        price = props.get("price")
        points = props.get("points")
        print(f"{title} | {country} | {price} | {points}")

finally:
    client.close()
```

**Output**:
```
Dynasty Cellars 2007 DC3 Meritage (Walla Walla Valley (WA)) | US | 24.0 | 88
Clos La Chance 2008 Whitestone Vineyard Cabernet Sauvignon (Central Coast) | US | 40.0 | 88

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.50s)

**Generated Code**:
```python

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 9.51s)

**Generated Code**:
```python

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 15.57s)

**Generated Code**:
```python

```

---

