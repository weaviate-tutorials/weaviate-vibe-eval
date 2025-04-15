# Weaviate Benchmark Results

Generated on: 2025-04-15 15:36:18

## Summary

- **openai/gpt-4o-2024-11-20**: 2/14 tasks successful
- **openai/gpt-4o-mini-2024-07-18**: 3/14 tasks successful
- **openai/gpt-4.5-preview-2025-02-27**: 12/14 tasks successful
- **openai/o3-mini-2025-01-31**: 1/14 tasks successful
- **openai/chatgpt-4o-latest**: 2/14 tasks successful
- **openai/gpt-4.1-2025-04-14**: 10/14 tasks successful
- **openai/gpt-4.1-mini-2025-04-14**: 8/14 tasks successful
## Detailed Results

### openai/gpt-4o-2024-11-20

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 4.03s)

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

# Connect to Weaviate Cloud instance
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
    print("Weaviate server is not ready. Please check your connection or credentials.")
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

**Status**: ❌ FAILURE (runtime: 5.14s)

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
assert client.is_ready(), "Weaviate server is not ready."

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

**Status**: ❌ FAILURE (runtime: 12.23s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.exceptions import WeaviateBaseError

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Ensure the environment variables are set
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    additional_headers={
        "Authorization": f"Bearer {WCD_TEST_KEY}"
    }
)

# Define the class schema for DemoProducts
demo_products_schema = {
    "class": "DemoProducts",
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
            "description": "A description of the product"
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

# Check if the class already exists, and delete it if it does
try:
    if client.schema.exists("DemoProducts"):
        print("Class 'DemoProducts' already exists. Deleting it...")
        client.schema.delete_class("DemoProducts")
        print("Class 'DemoProducts' deleted.")
except WeaviateBaseError as e:
    print(f"Error while checking or deleting existing class: {e}")
    raise

# Create the new class
try:
    print("Creating class 'DemoProducts'...")
    client.schema.create_class(demo_products_schema)
    print("Class 'DemoProducts' created successfully.")
except WeaviateBaseError as e:
    print(f"Error while creating class: {e}")
    raise
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

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 12.79s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance
auth_config = AuthApiKey(api_key=WCD_TEST_KEY)
client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)

# Define the collection (class) name
collection_name = "DemoProducts"

# Delete the collection if it already exists
if client.schema.exists(collection_name):
    client.schema.delete_class(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Define the schema for the collection
collection_schema = {
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
client.schema.create_class(collection_schema)
print(f"Created collection: {collection_name}")

# Close the client connection (optional, as the client is stateless)
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
  client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    client = weaviate.Client(url=WCD_TEST_URL, auth_client_secret=auth_config)
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 9.08s)

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

# Define the collection name
collection_name = "DemoProducts"

# Check if the collection already exists
if client.collections.exists(collection_name):
    print(f"Collection '{collection_name}' already exists. Deleting it...")
    client.collections.delete(collection_name)
    print(f"Collection '{collection_name}' deleted.")

# Create the new collection with the specified properties
print(f"Creating collection '{collection_name}'...")
client.collections.create(
    collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ],
    vectorizer_config=Configure.Vectorizer.text2vec_openai(),  # Optional: Use OpenAI vectorizer
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
Collection 'DemoProducts' created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 16.29s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.exceptions import WeaviateStartUpError

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

# Validate environment variables
if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise ValueError("Environment variables WCD_TEST_URL and WCD_TEST_KEY must be set.")

# Connect to Weaviate Cloud
try:
    client = weaviate.Client(
        url=WCD_TEST_URL,
        auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
        additional_headers={"X-OpenAI-Api-Key": WCD_TEST_KEY},  # Optional, if using OpenAI module
    )
except WeaviateStartUpError as e:
    print(f"Failed to connect to Weaviate: {e}")
    exit(1)

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
if not client.schema.contains(schema):
    client.schema.create_class(schema)

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

# Wait for the batch process to complete
batch.flush()

# Count the number of objects in the "DemoProducts" collection
result = client.query.aggregate("DemoProducts").with_meta_count().do()
count = result["data"]["Aggregate"]["DemoProducts"][0]["meta"]["count"]

# Print the number of objects in the collection
print(f"Number of objects in 'DemoProducts': {count}")
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

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.65s)

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
if not client.schema.contains(schema):
    client.schema.create_class(schema)

# Prepare 50 objects to batch import
data_rows = [
    {
        "name": f"Product {i+1}",
        "description": f"Description {i+1}",
    }
    for i in range(50)
]

# Batch import the objects
with client.batch as batch:
    batch.batch_size = 10  # Set batch size
    for data_row in data_rows:
        batch.add_data_object(
            data_object=data_row,
            class_name="DemoProducts",
        )
    if batch.errors:
        print("Batch import encountered errors.")
        for error in batch.errors:
            print(error)

# Count the number of objects in the "DemoProducts" collection
result = client.query.aggregate("DemoProducts").with_meta_count().do()
object_count = result["data"]["Aggregate"]["DemoProducts"][0]["meta"]["count"]

print(f"Number of objects in the 'DemoProducts' collection: {object_count}")

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

**Status**: ❌ FAILURE (runtime: 8.51s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.config import Configure, Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

# Create the "DemoProducts" collection if it doesn't already exist
if not client.collections.exists("DemoProducts"):
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        vectorizer_config=Configure.Vectorizer.text2vec_openai(),
    )

# Batch import 50 objects into the "DemoProducts" collection
collection = client.collections.get("DemoProducts")
with collection.batch.dynamic() as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}",
            }
        )

# Print the number of objects in the collection
num_objects = collection.query.count()
print(f"Number of objects in 'DemoProducts': {num_objects}")

# Close the client connection
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

**Status**: ❌ FAILURE (runtime: 16.56s)

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
    raise ValueError("Please ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set in the environment variables.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key  # Pass the OpenAI API key for text2vec-openai
    }
)

# Query the WineReview collection
query = "dessert wine"
response = client.query.get(
    "WineReview",  # The class name
    ["title", "country", "price", "points"]  # The properties to retrieve
).with_near_text({
    "concepts": [query]
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

**Status**: ❌ FAILURE (runtime: 11.91s)

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
    auth_client_secret=AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-API-Key": OPENAI_API_KEY
    },
)

# Query the 'WineReview' collection
response = client.query.get(
    "WineReview",  # The name of the collection
    ["title", "country", "price", "points"]  # Fields to retrieve
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

**Status**: ✅ SUCCESS (runtime: 10.33s)

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
response = client.collections.get("WineReview").query.near_text(
    query="dessert wine",
    limit=2,  # Limit to 2 results
    return_properties=["title", "country", "price", "points"]  # Properties to return
)

# Print the results
for wine in response.objects:
    print(f"Title: {wine.properties.get('title')}")
    print(f"Country: {wine.properties.get('country')}")
    print(f"Price: {wine.properties.get('price')}")
    print(f"Points: {wine.properties.get('points')}")
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

**Status**: ❌ FAILURE (runtime: 17.43s)

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
    raise ValueError("Please ensure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set in the environment variables.")

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=WCD_TEST_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=WCD_TEST_KEY),
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY  # Required for text2vec-openai
    }
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
                where: {{
                    operator: And,
                    operands: [
                        {{
                            path: ["price"],
                            operator: LessThan,
                            valueNumber: {price_limit}
                        }},
                        {{
                            path: ["points"],
                            operator: GreaterThan,
                            valueNumber: {points_min}
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
                }},
                limit: {limit}
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
        print("Matching wines:")
        for wine in results:
            print(f"Title: {wine['title']}, Country: {wine['country']}, Price: {wine['price']}, Points: {wine['points']}")
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

**Status**: ❌ FAILURE (runtime: 21.94s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.gql.query import GetBuilder

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
    }
)

# Define the query parameters
query = "pair with steak"
limit = 5
alpha = 0.5
price_limit = 50
points_threshold = 90
review_keywords = ["spice", "fruit", "berry", "cherry", "honey"]

# Build the GraphQL query
gql_query = (
    client.query
    .get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query=query, alpha=alpha)
    .with_limit(limit)
    .with_where({
        "operator": "And",
        "operands": [
            {
                "path": ["price"],
                "operator": "LessThan",
                "valueInt": price_limit
            },
            {
                "path": ["points"],
                "operator": "GreaterThan",
                "valueInt": points_threshold
            },
            {
                "operator": "Or",
                "operands": [
                    {
                        "path": ["review_body"],
                        "operator": "Like",
                        "valueString": f"*{keyword}*"
                    } for keyword in review_keywords
                ]
            }
        ]
    })
)

# Execute the query
response = gql_query.do()

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
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.gql.query import GetBuilder
ModuleNotFoundError: No module named 'weaviate.gql.query'

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 25.88s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import HybridFusion, Filter

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Define the query parameters
query = "pair with steak"
alpha = 0.5
limit = 5

# Define the filter conditions
filter_conditions = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )
)

# Perform the hybrid search
response = client.collections.get("WineReview").query.hybrid(
    query=query,
    alpha=alpha,
    fusion_type=HybridFusion.RELATIVE_SCORE,
    filters=filter_conditions,
    limit=limit,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for wine in response.objects:
    print(f"Title: {wine.properties['title']}")
    print(f"Country: {wine.properties['country']}")
    print(f"Price: {wine.properties['price']}")
    print(f"Points: {wine.properties['points']}")
    print("-" * 40)

# Close the client connection
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

### openai/gpt-4o-mini-2024-07-18

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 9.59s)

**Generated Code**:
```python
import os
import weaviate

# Get the Weaviate Cloud URL and API key from environment variables
wcd_url = os.getenv('WCD_TEST_URL')
wcd_key = os.getenv('WCD_TEST_KEY')

# Create a Weaviate client instance
client = weaviate.Client(
    url=wcd_url,
    auth_client_secret=weaviate.AuthClientSecret(wcd_key)
)

# Check if the server is ready to accept requests
try:
    client.is_ready()
    print("The Weaviate server is ready to accept requests.")
except Exception as e:
    print(f"The Weaviate server is not ready: {e}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    auth_client_secret=weaviate.AuthClientSecret(wcd_key)
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute AuthClientSecret

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 4.83s)

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

**Status**: ❌ FAILURE (runtime: 15.26s)

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
    auth_client_secret=weaviate.AuthClientSecret(weaviate_key)
)

# Define the class name and properties
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
Traceback (most recent call last):
  File "/code/code.py", line 11, in <module>
    auth_client_secret=weaviate.AuthClientSecret(weaviate_key)
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute AuthClientSecret

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 10.37s)

**Generated Code**:
```python
import os
import weaviate
from weaviate import Auth, Property, DataType

# Connect to the Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv('WCD_TEST_URL'),
    auth_credentials=Auth.api_key(os.getenv('WCD_TEST_KEY'))
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

**Status**: ✅ SUCCESS (runtime: 9.39s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud
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
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print(f"Collection '{collection_name}' created successfully.")
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

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 12.63s)

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

# Define the class for the collection if it doesn't exist
class_name = "DemoProducts"
schema = {
    "classes": [
        {
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
    ]
}

# Create the class in Weaviate if it doesn't exist
if not client.schema.contains(class_name):
    client.schema.create(schema)

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

**Status**: ❌ FAILURE (runtime: 13.30s)

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
    {"name": f"Product {i+1}", "description": f"Description {i+1}"} for i in range(50)
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
print(f"Number of objects in '{collection_name}': {len(collection)}")

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

**Status**: ❌ FAILURE (runtime: 12.90s)

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

# Create the "DemoProducts" collection with the specified properties
client.collections.create(
    "DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# Batch import 50 arbitrary objects into the collection
with client.collections.get("DemoProducts").batch.fixed_size(batch_size=50) as batch:
    for i in range(50):
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# Print the number of objects in the collection
collection = client.collections.get("DemoProducts")
object_count = collection.data.count()
print(f"Number of objects in 'DemoProducts': {object_count}")

# Close the client connection
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

**Status**: ❌ FAILURE (runtime: 9.48s)

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
    auth_client_secret=weaviate.AuthClientSecret(
        wcd_test_key
    ),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Define the query
query = "dessert wine"

# Perform the query
results = client.query.get(
    class_name='WineReview',
    properties=['title', 'country', 'price', 'points']
).with_near_text({
    "concepts": [query],
}).with_limit(2).do()

# Print the results
for wine in results['data']['Get']['WineReview']:
    print(f"Title: {wine['title']}, Country: {wine['country']}, Price: {wine['price']}, Points: {wine['points']}")
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 12, in <module>
    auth_client_secret=weaviate.AuthClientSecret(
  File "/usr/local/lib/python3.9/site-packages/weaviate/__init__.py", line 147, in __getattr__
    raise AttributeError(f"module {__name__} has no attribute {name}")
AttributeError: module weaviate has no attribute AuthClientSecret

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 14.47s)

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
    query="dessert wine",
    limit=2
).do()

# Print the title, country, price, and points of each matching wine
for obj in response['data']['Get'][collection_name]:
    title = obj.get('title')
    country = obj.get('country')
    price = obj.get('price')
    points = obj.get('points')
    
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

**Status**: ❌ FAILURE (runtime: 10.36s)

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
response = client.collections.get("WineReview").query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for obj in response.objects:
    print(f"Title: {obj.properties['title']}, Country: {obj.properties['country']}, Price: {obj.properties['price']}, Points: {obj.properties['points']}")
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

**Status**: ❌ FAILURE (runtime: 14.54s)

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
query = {
    "nearText": {
        "concepts": ["pair with steak"],
        "certainty": 0.5
    },
    "where": {
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
    },
    "limit": 5
}

# Execute the query
results = client.query.get("WineReview", ["title", "country", "price", "points"]) \
    .with_where(query["where"]) \
    .with_near_text(query["nearText"]) \
    .with_limit(query["limit"]) \
    .do()

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

**Status**: ✅ SUCCESS (runtime: 12.03s)

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

# Perform the hybrid query
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
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
    print(f"Score: {obj.metadata.score}")

# Close the client connection
client.close()
```

**Output**:
```
Title: Soléna 2009 Guadalupe Vineyard Pinot Noir, Country: US, Price: 40.0, Points: 92
Score: 0.5
Title: Bink 2014 Pinot Noir (Anderson Valley), Country: US, Price: 49.0, Points: 91
Score: 0.46207502484321594
Title: Doña Silvina 2011 Malbec (Mendoza), Country: Argentina, Price: 27.0, Points: 91
Score: 0.21977002918720245
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji), Country: Hungary, Price: 25.0, Points: 93
Score: 0.06533736735582352
Title: Château Rauzan-Ségla 2012  Margaux, Country: France, Price: 0.0, Points: 94
Score: 0.018121296539902687

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.17s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.query import Filter, HybridFusion

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

# Define the filters
filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )
)

# Perform the hybrid search
response = client.data.query.hybrid(
    query=query,
    alpha=0.5,
    filters=filters,
    limit=5,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for obj in response['data']['Get']['WineReview']:
    print(f"Title: {obj['title']}, Country: {obj['country']}, Price: {obj['price']}, Points: {obj['points']}")
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

**Status**: ❌ FAILURE (runtime: 5.42s)

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

# Check if the Weaviate server is ready
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

**Status**: ✅ SUCCESS (runtime: 4.03s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud instance using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=Auth.api_key(os.getenv("WCD_TEST_KEY"))
)

# Check if the server is ready
assert client.is_ready()

# Close the client connection
client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 13.69s)

**Generated Code**:
```python
import weaviate
import os
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_wcs(
    cluster_url=os.getenv("WCD_TEST_URL"),
    auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WCD_TEST_KEY"))
)

# Delete the collection if it already exists
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")

# Define and create the new collection
client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="price", data_type=DataType.NUMBER),
        Property(name="in_stock", data_type=DataType.BOOL),
    ]
)

print("Collection 'DemoProducts' created successfully.")

# Close the client connection
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

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 12.60s)

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

**Status**: ✅ SUCCESS (runtime: 14.78s)

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

# Create the new collection with specified properties
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

**Status**: ✅ SUCCESS (runtime: 19.54s)

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

# Define the collection schema
collection_name = "DemoProducts"

# Check if collection exists, delete if it does
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection with properties
client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT)
    ]
)

# Get the collection object
collection = client.collections.get(collection_name)

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
count = collection.aggregate.over_all(total_count=True)
print(f"Number of objects in '{collection_name}': {count.total_count}")

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

**Status**: ✅ SUCCESS (runtime: 15.15s)

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

# Check for any failed imports
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

**Status**: ✅ SUCCESS (runtime: 19.23s)

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

# Create the "DemoProducts" collection with properties "name" and "description"
if client.collections.exists("DemoProducts"):
    client.collections.delete("DemoProducts")

client.collections.create(
    name="DemoProducts",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ],
    vectorizer_config=Configure.Vectorizer.none()  # No vectorizer for simplicity
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
object_count = collection.aggregate.over_all(total_count=True).total_count
print(f"Number of objects in 'DemoProducts': {object_count}")

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

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 16.22s)

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

# Perform a similarity search for "dessert wine"
response = client.collections.get("WineReview").query.near_text(
    query="dessert wine",
    limit=2
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

**Status**: ✅ SUCCESS (runtime: 14.14s)

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

# Perform a near_text query for "dessert wine" with a limit of 2 results
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

**Status**: ✅ SUCCESS (runtime: 19.07s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

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

# Perform a semantic search using near_text
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for wine in response.objects:
    props = wine.properties
    print(f"Title: {props.get('title', 'N/A')}")
    print(f"Country: {props.get('country', 'N/A')}")
    print(f"Price: {props.get('price', 'N/A')}")
    print(f"Points: {props.get('points', 'N/A')}")
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

**Status**: ❌ FAILURE (runtime: 18.45s)

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
    properties = wine.properties
    print(f"Title: {properties.get('title')}")
    print(f"Country: {properties.get('country')}")
    print(f"Price: {properties.get('price')}")
    print(f"Points: {properties.get('points')}")
    print("-" * 40)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 20, in <module>
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

**Status**: ✅ SUCCESS (runtime: 21.30s)

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

# Perform hybrid search query with filters
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

# Print the title, country, price, and points of each matching wine
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
Score: 0.46207502484321594
----------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Score: 0.21977002918720245
----------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Score: 0.06533736735582352
----------------------------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
Score: 0.018121296539902687
----------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 21.75s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# Connect to Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

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
response = wine_collection.query.hybrid(
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
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
----------------------------------------

```

---

### openai/o3-mini-2025-01-31

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 13.34s)

**Generated Code**:
```python
#!/usr/bin/env python3
import os
import weaviate

# Create a Weaviate client using the URL and API key from the environment variables.
client = weaviate.Client(
    url=os.environ["WCD_TEST_URL"],
    auth_client_secret=weaviate.AuthApiKey(api_key=os.environ["WCD_TEST_KEY"])
)

# Check if the Weaviate server is ready to accept requests.
if client.is_ready():
    print("Weaviate Cloud instance is ready to accept requests.")
else:
    print("Weaviate Cloud instance is not ready to accept requests.")
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
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 6, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 7.87s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Read environment variables for cluster URL and API key
cluster_url = os.environ.get("WCD_TEST_URL")
api_key = os.environ.get("WCD_TEST_KEY")

# Connect to the Weaviate Cloud instance using the provided credentials
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=AuthApiKey(api_key)
)

# Check that the server is ready to accept requests
assert client.is_ready()

client.close()
```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 12.01s)

**Generated Code**:
```python
Below is an example Python script that connects to a Weaviate Cloud instance using environment variables, deletes any existing "DemoProducts" class, and then creates a new one with the specified properties:

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

def main():
    # Retrieve environment variables for URL and API key
    weaviate_url = os.environ.get("WCD_TEST_URL")
    weaviate_api_key = os.environ.get("WCD_TEST_KEY")
    
    if not weaviate_url or not weaviate_api_key:
        raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set")

    # Initialize Weaviate client connecting to Weaviate Cloud
    client = weaviate.Client(
        url=weaviate_url,
        additional_headers={"X-API-KEY": weaviate_api_key}
    )
    
    class_name = "DemoProducts"
    
    # Check if class already exists
    current_schema = client.schema.get()
    classes = current_schema.get("classes", [])
    if any(cls.get("class") == class_name for cls in classes):
        print(f"Class '{class_name}' exists. Deleting it...")
        client.schema.delete_class(class_name)
    
    # Define new class with the required properties
    class_obj = {
        "class": class_name,
        "description": "A collection to demo products data",
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
            },
            {
                "name": "price",
                "dataType": ["number"],
                "description": "Price of the product"
            },
            {
                "name": "in_stock",
                "dataType": ["boolean"],
                "description": "Stock status of the product"
            }
        ],
        # If you are not using automatic vectorization for text fields, specify "none"
        "vectorizer": "none"
    }
    
    # Create the new class
    client.schema.create_class(class_obj)
    print(f"Class '{class_name}' created successfully.")

if __name__ == "__main__":
    main()
------------------------------------------------------------

Explanation:
1. The script imports os and the latest Weaviate client.
2. It reads the connection URL and API key from the environment variables WCD_TEST_URL and WCD_TEST_KEY.
3. It connects to Weaviate Cloud using the provided URL and API key header.
4. It checks if the "DemoProducts" class exists; if so, it deletes the class.
5. Finally, it creates the "DemoProducts" class with the specified properties and sets "vectorizer" to "none" (adjust if you wish to use Weaviate’s vectorizers).

Ensure that your environment variables are properly set before running the script.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to a Weaviate Cloud instance using environment variables, deletes any existing "DemoProducts" class, and then creates a new one with the specified properties:
                ^
SyntaxError: invalid syntax

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 5.82s)

**Generated Code**:
```python
Below is the complete Python code using the latest Weaviate client syntax. This script reads the Weaviate Cloud URL and API key from the WCD_TEST_URL and WCD_TEST_KEY environment variables, connects to the Weaviate Cloud instance, deletes the "DemoProducts" collection if it already exists, and then creates the collection with the specified properties.

-------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth  # For authentication method
from weaviate.classes.config import Property, DataType

# Retrieve the Weaviate Cloud URL and API key from environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

if cluster_url is None or api_key is None:
    raise ValueError("WCD_TEST_URL and WCD_TEST_KEY environment variables must be set.")

# Connect to the Weaviate Cloud instance using the API key authentication method
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(api_key)
)

# Collection name
collection_name = "DemoProducts"

# Delete the collection if it already exists (for testing purposes)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Create the new collection with the desired properties
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

# Close connection if your client supports it
client.close()
-------------------------------------------------------

Make sure to have the Weaviate client installed (for example, using pip install weaviate-client) and that the environment variables are properly set before running the script.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is the complete Python code using the latest Weaviate client syntax. This script reads the Weaviate Cloud URL and API key from the WCD_TEST_URL and WCD_TEST_KEY environment variables, connects to the Weaviate Cloud instance, deletes the "DemoProducts" collection if it already exists, and then creates the collection with the specified properties.
                 ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 11.58s)

**Generated Code**:
```python
Below is an example Python script that connects to a Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, deletes the collection “DemoProducts” if it exists, and then creates it with properties for name (text), description (text), price (number), and in_stock (boolean).

------------------------------------------------------------
#!/usr/bin/env python3
"""
This script connects to a Weaviate Cloud instance, deletes
an existing "DemoProducts" collection (if present), and creates a
new collection with specified properties.

For more information on using the Weaviate Python client,
see: https://weaviate.io/developers/weaviate/client-libraries/python
"""

import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Connect to Weaviate Cloud using environment variables.
# WCD_TEST_URL should be the URL of your Weaviate Cloud instance.
# WCD_TEST_KEY should be your API key for that instance.
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
)

# Check if the "DemoProducts" collection already exists.
if client.collections.exists("DemoProducts"):
    # Delete the collection if it exists.
    client.collections.delete("DemoProducts")
    print('Existing "DemoProducts" collection deleted.')

# Define the collection properties.
products_properties = [
    Property(name="name", data_type=DataType.TEXT),
    Property(name="description", data_type=DataType.TEXT),
    Property(name="price", data_type=DataType.NUMBER),
    Property(name="in_stock", data_type=DataType.BOOL),
]

# Create the new collection "DemoProducts" with the defined properties.
client.collections.create("DemoProducts", properties=products_properties)
print('"DemoProducts" collection created successfully.')

# Optionally, close the client when done.
client.close()
------------------------------------------------------------

Make sure you have set the environment variables WCD_TEST_URL and WCD_TEST_KEY before running this script. For more detailed examples, refer to the Weaviate Python client documentation:
https://weaviate.io/developers/weaviate/client-libraries/python
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to a Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, deletes the collection “DemoProducts” if it exists, and then creates it with properties for name (text), description (text), price (number), and in_stock (boolean).
                ^
SyntaxError: invalid syntax

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 36.48s)

**Generated Code**:
```python
Below is an example using the latest Weaviate Python client. Before running the code, ensure you have installed the weaviate client (for example, via pip install weaviate-client) and that your environment variables WCD_TEST_URL and WCD_TEST_KEY are set.

------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

def main():
    # Get the Weaviate Cloud URL and API key from environment variables
    weaviate_url = os.environ.get("WCD_TEST_URL")
    weaviate_api_key = os.environ.get("WCD_TEST_KEY")
    if not weaviate_url or not weaviate_api_key:
        raise ValueError("Both WCD_TEST_URL and WCD_TEST_KEY must be set in your environment.")

    # Create the Weaviate client using API key authentication.
    # The latest client accepts an auth_client_secret object for API key auth.
    client = weaviate.Client(
        url=weaviate_url,
        auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key)
    )

    # Define the "DemoProducts" class (if not already present)
    class_obj = {
        "class": "DemoProducts",
        "description": "A class to store demo products.",
        "properties": [
            {
                "name": "name",
                "dataType": ["text"]
            },
            {
                "name": "description",
                "dataType": ["text"]
            }
        ],
        # since we are providing our own data, disable vectorization.
        "vectorizer": "none"
    }

    # Check if the class/schema exists already. If not, create the class.
    schema = client.schema.get()
    classes = schema.get("classes", [])
    if not any(cls["class"] == "DemoProducts" for cls in classes):
        client.schema.create_class(class_obj)
        print("Created 'DemoProducts' class in the schema.")
    else:
        print("'DemoProducts' class already exists in the schema.")

    # Configure batch mode. (You can adjust the batch size and timeout as needed.)
    client.batch.configure(batch_size=50, dynamic=False)

    # Batch import 50 objects into "DemoProducts" using the batch API.
    for i in range(50):
        obj = {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
        client.batch.add_data_object(data_object=obj, class_name="DemoProducts")
    
    # Make sure all batched objects are sent to Weaviate.
    client.batch.flush()
    print("Batch import completed.")

    # Fetch all objects in the "DemoProducts" class and print the count.
    # The get API returns a dict with an "objects" key.
    result = client.data_object.get(class_name="DemoProducts")
    objects = result.get("objects", [])
    print(f"Number of objects in 'DemoProducts': {len(objects)}")

if __name__ == '__main__':
    main()

------------------------------------------------

Explanation:

1. The script reads the Weaviate Cloud URL and API key from the environment.
2
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example using the latest Weaviate Python client. Before running the code, ensure you have installed the weaviate client (for example, via pip install weaviate-client) and that your environment variables WCD_TEST_URL and WCD_TEST_KEY are set.
                ^
SyntaxError: invalid syntax

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 18.62s)

**Generated Code**:
```python
Below is an example Python script that connects to your Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, retrieves the “DemoProducts” collection (class), and then batch imports 50 objects with “name” and “description” properties. Finally, it prints out the number of objects in the collection. (Note that this example assumes that your Weaviate schema already has a class named “DemoProducts” defined with the two properties.)

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

# Retrieve Weaviate Cloud URL and API key from environment variables
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
if not weaviate_url or not weaviate_api_key:
    raise ValueError("Both WCD_TEST_URL and WCD_TEST_KEY must be set as environment variables.")

# Connect to the Weaviate Cloud instance using the latest client methodology
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.AuthApiKey(weaviate_api_key)
)

# Get the "DemoProducts" collection (class) from Weaviate.
# (It is assumed that this class exists in your schema.)
collection = client.collections.get("DemoProducts")

# Create 50 objects with arbitrary data.
data_rows = [
    {"name": f"Product {i}", "description": f"Description {i}"}
    for i in range(1, 51)  # Products 1 to 50
]

# Batch import the objects using the dynamic batch API.
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(properties=data_row)
        # Optionally, check if errors have reached a threshold.
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

# Report if there were any objects that failed to import.
failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection.
# (Under the hood, this uses the collection’s __len__() method to query the count)
print("Number of objects in 'DemoProducts':", len(collection))

# Close the client connection
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to your Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, retrieves the “DemoProducts” collection (class), and then batch imports 50 objects with “name” and “description” properties. Finally, it prints out the number of objects in the collection. (Note that this example assumes that your Weaviate schema already has a class named “DemoProducts” defined with the two properties.)
                ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 10.18s)

**Generated Code**:
```python
Below is an example Python script using the latest Weaviate client syntax that connects to Weaviate Cloud (using the environment variables WCD_TEST_URL and WCD_TEST_KEY), creates a collection called "DemoProducts" with text properties “name” and “description” (if it does not already exist), batch imports 50 objects, and finally prints the number of objects in the collection.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# ------------------------------------------------------------------------------
# 1. CONNECT TO WEAVIATE CLOUD
# ------------------------------------------------------------------------------
# Ensure that the following environment variables are set:
#   WCD_TEST_URL  - The URL of your Weaviate Cloud instance.
#   WCD_TEST_KEY  - The API key for your Weaviate Cloud instance.
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

# ------------------------------------------------------------------------------
# 2. CREATE/GET COLLECTION "DemoProducts"
# ------------------------------------------------------------------------------
# Check if the collection already exists; if not, create it.
collection_name = "DemoProducts"
if not client.collections.exists(collection_name):
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT)
        ]
    )

# Get the collection handle for further operations.
demo_products = client.collections.get(collection_name)

# ------------------------------------------------------------------------------
# 3. BATCH IMPORT 50 OBJECTS INTO THE COLLECTION
# ------------------------------------------------------------------------------
# We use the dynamic batch mode for efficient import.
with demo_products.batch.dynamic() as batch:
    for i in range(50):
        # Each object has a "name" and "description" property.
        batch.add_object(
            properties={
                "name": f"Product {i}",
                "description": f"Description {i}"
            }
        )

# ------------------------------------------------------------------------------
# 4. PRINT THE NUMBER OF OBJECTS IN THE COLLECTION
# ------------------------------------------------------------------------------
# We can use an aggregate GraphQL query to count the objects.
# The aggregate query requests meta information (including count) for the collection.
aggregate_response = client.query.aggregate(collection_name)\
    .with_fields("meta { count }")\
    .do()

# Extract the count from the returned JSON structure.
# The response structure looks like:
# { "data": { "Aggregate": { "DemoProducts": [ { "meta": { "count": <number> } } ] } } }
count = aggregate_response["data"]["Aggregate"][collection_name][0]["meta"]["count"]
print(f"Number of objects in '{collection_name}': {count}")

# ------------------------------------------------------------------------------
# 5. CLEANUP: CLOSE THE CLIENT
# ------------------------------------------------------------------------------
client.close()

------------------------------------------------------------

Additional information and detailed examples for operations like collection management and batch imports can be found in the Weaviate documentation:
• Python Client Library: https://weaviate.io/developers/weaviate/client-libraries/python
• Batch Import: https://weaviate.io/developers/weaviate/manage-data/import

This script demonstrates a minimal end-to-end example; you may adapt or extend it to better suit your use case.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script using the latest Weaviate client syntax that connects to Weaviate Cloud (using the environment variables WCD_TEST_URL and WCD_TEST_KEY), creates a collection called "DemoProducts" with text properties “name” and “description” (if it does not already exist), batch imports 50 objects, and finally prints the number of objects in the collection.
                ^
SyntaxError: invalid syntax

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 8.73s)

**Generated Code**:
```python
#!/usr/bin/env python3
"""
This script connects to a Weaviate Cloud instance and queries the "WineReview"
class to find wines that best match the text query "dessert wine". It returns at
most 2 results and prints out the title, country, price, and points for each
matching wine.

Make sure the following environment variables are set:
  - WCD_TEST_URL: URL for your Weaviate Cloud instance.
  - WCD_TEST_KEY: API key for the Weaviate Cloud instance.
  - OPENAI_API_KEY: API key needed for the text2vec-openai vectorizer.
"""

import os
import weaviate

# Retrieve the environment variables.
weaviate_url = os.environ.get("WCD_TEST_URL")
weaviate_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not weaviate_url or not weaviate_api_key or not openai_api_key:
    raise ValueError("One or more of the required environment variables are missing.")

# Initialize the Weaviate client for Weaviate Cloud.
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_api_key)
)

# Pass the OpenAI API key via additional headers (required by text2vec-openai).
client.set_additional_headers({
    "X-Openai-Api-Key": openai_api_key
})

# Build the query:
# - Query the "WineReview" collection.
# - Use nearText to find wines matching the concept "dessert wine".
# - Limit the number of results to 2.
query_result = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({"concepts": ["dessert wine"]})
    .with_limit(2)
    .do()
)

# Extract the results from the query response.
results = query_result.get("data", {}).get("Get", {}).get("WineReview", [])

# Print the desired fields for each matching wine.
for wine in results:
    title = wine.get("title", "N/A")
    country = wine.get("country", "N/A")
    price = wine.get("price", "N/A")
    points = wine.get("points", "N/A")
    print(f"Title: {title}")
    print(f"Country: {country}")
    print(f"Price: {price}")
    print(f"Points: {points}")
    print("-" * 30)
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])
/code/code.py:26: DeprecationWarning: 
Python client v3 `weaviate.Client(...)` has been removed.

Upgrade your code to use Python client v4 `weaviate.WeaviateClient` connections and methods.
    - For Python Client v4 usage, see: https://weaviate.io/developers/weaviate/client-libraries/python
    - For code migration, see: https://weaviate.io/developers/weaviate/client-libraries/python/v3_v4_migration

If you have to use v3 code, install the v3 client and pin the v3 dependency in your requirements file: `weaviate-client>=3.26.7;<4.0.0`
  client = weaviate.Client(
Traceback (most recent call last):
  File "/code/code.py", line 26, in <module>
    client = weaviate.Client(
TypeError: __init__() got an unexpected keyword argument 'url'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 10.85s)

**Generated Code**:
```python
Below is an example of how you can achieve this using the latest Weaviate client syntax:

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth

# Read environment variable values
cluster_url = os.environ.get("WCD_TEST_URL")
wcd_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not (cluster_url and wcd_api_key and openai_api_key):
    raise EnvironmentError("One or more required environment variables are missing.")

# Connect to your Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(wcd_api_key),
    headers={"X-OpenAI-API-Key": openai_api_key}
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Query the collection using near_text with the query "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Loop over each matching object and print the selected properties.
# It is assumed that each object has properties: title, country, price, and points.
for obj in response.objects:
    props = obj.properties
    title = props.get("title", "N/A")
    country = props.get("country", "N/A")
    price = props.get("price", "N/A")
    points = props.get("points", "N/A")
    print(f"Title: {title}")
    print(f"Country: {country}")
    print(f"Price: {price}")
    print(f"Points: {points}")
    print("-" * 40)

# Close the connection
client.close()
------------------------------------------------------------

Explanation:

1. We import os and weaviate along with the Auth class that lets us pass the API key.
2. The code reads the Weaviate Cloud URL (WCD_TEST_URL), the Cloud API key (WCD_TEST_KEY), and the OpenAI API key (OPENAI_API_KEY) from the environment.
3. The client is connected to Weaviate Cloud using the provided credentials. The OpenAI API key is sent along via the headers.
4. We get the "WineReview" collection and run a near_text query for "dessert wine" with a limit of 2.
5. Finally, for each result returned, we print the wine’s title, country, price, and points, then close the client connection.

Make sure that you have the necessary environment variables set and the latest Weaviate Python client installed before running this script.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example of how you can achieve this using the latest Weaviate client syntax:
                ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 16.93s)

**Generated Code**:
```python
Below is an example Python script using the latest Weaviate client syntax. This script connects to a Weaviate Cloud instance (using the environment variables WCD_TEST_URL and WCD_TEST_KEY) and authenticates with the OpenAI API key (stored in OPENAI_API_KEY). It then queries the "WineReview" collection using a near_text search for the query "dessert wine" and prints the title, country, price, and points for each of up to 2 matching wines.

--------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud using env vars:
#   WCD_TEST_URL is the cluster URL
#   WCD_TEST_KEY is the API key for the Cloud instance
# Also include the OpenAI API Key header for the text2vec_openai vectorizer.
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the 'WineReview' collection
wine_collection = client.collections.get("WineReview")

# Query the collection using a near_text search for "dessert wine", with a maximum of 2 results.
response = wine_collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the title, country, price, and points for each matching wine.
for wine in response.objects:
    props = wine.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
    print("-" * 40)

# Optionally, close the client when done:
client.close()

--------------------------------------------------

Notes:
• For more details on the Weaviate Python client (v4.x) and available query options, see:
  https://weaviate.io/developers/weaviate/client-libraries/python
• Ensure that the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are properly set before running the script.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script using the latest Weaviate client syntax. This script connects to a Weaviate Cloud instance (using the environment variables WCD_TEST_URL and WCD_TEST_KEY) and authenticates with the OpenAI API key (stored in OPENAI_API_KEY). It then queries the "WineReview" collection using a near_text search for the query "dessert wine" and prints the title, country, price, and points for each of up to 2 matching wines.
                ^
SyntaxError: invalid syntax

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 17.12s)

**Generated Code**:
```python
Below is an example Python script that connects to Weaviate Cloud with the provided environment variables, and performs a hybrid search on the WineReview collection using text2vec-openai. It applies a filter that returns wines with a price less than 50, points greater than 90, and whose review_body contains at least one of the substrings "spice", "fruit", "berry", "cherry", or "honey". The hybrid search is done with a query “pair with steak” using alpha=0.5 and returns up to 5 results. Make sure you have installed the latest Weaviate Python client (e.g. via pip install weaviate-client).

----------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

def main():
    # Retrieve environment variables
    wc_url = os.getenv("WCD_TEST_URL")
    wc_key = os.getenv("WCD_TEST_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not (wc_url and wc_key and openai_api_key):
        raise ValueError("Please make sure WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set in your environment.")

    # Create a client connection to Weaviate Cloud
    client = weaviate.Client(
        url=wc_url,
        auth_client_secret=weaviate.AuthApiKey(api_key=wc_key),
        additional_headers={"X-Openai-Api-Key": openai_api_key}
    )

    # Build a where filter:
    #   - price < 50
    #   - points > 90
    #   - review_body contains at least one of the substrings ("spice", "fruit", "berry", "cherry", "honey")
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

    # Execute the query using a hybrid search
    try:
        result = (
            client.query
            .get("WineReview", ["title", "country", "price", "points"])
            .with_hybrid(query="pair with steak", alpha=0.5)
            .with_where(where_filter)
            .with_limit(5)
            .do()
        )
    except Exception as e:
        print("Error running the query:", e)
        return

    # Process and print the results
    reviews = result.get("data", {}).get("Get", {}).get("WineReview", [])
    if not reviews:
        print("No matching wines found.")
        return

    for wine in reviews:
        title   = wine.get("title", "N/A")
        country = wine.get("country", "N/A")
        price   = wine.get("price", "N/A")
        points  = wine.get("points", "N/A")
        print(f"Title: {title}\nCountry: {country}\nPrice: {price}\nPoints: {points}\n{'-'*40}")

if __name__ == "__main__":
    main()

----------------------------------------------------------------

Ensure that your environment has the variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY set before running this script. This code uses the latest client syntax to perform a hybrid search and apply the necessary filtering conditions.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that connects to Weaviate Cloud with the provided environment variables, and performs a hybrid search on the WineReview collection using text2vec-openai. It applies a filter that returns wines with a price less than 50, points greater than 90, and whose review_body contains at least one of the substrings "spice", "fruit", "berry", "cherry", or "honey". The hybrid search is done with a query “pair with steak” using alpha=0.5 and returns up to 5 results. Make sure you have installed the latest Weaviate Python client (e.g. via pip install weaviate-client).
                ^
SyntaxError: invalid syntax

```

---

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 21.92s)

**Generated Code**:
```python
Below is an example using the latest Weaviate client syntax. Make sure you have set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY before running the code.

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate
from weaviate.classes.init import Auth  # For API key authentication
from weaviate.classes.query import Filter, MetadataQuery

# Retrieve the required environment variables
cluster_url = os.environ.get("WCD_TEST_URL")
wcd_api_key = os.environ.get("WCD_TEST_KEY")
openai_api_key = os.environ.get("OPENAI_API_KEY")

if not cluster_url or not wcd_api_key or not openai_api_key:
    raise ValueError("Environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY must be set.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=cluster_url,
    auth_credentials=Auth.api_key(wcd_api_key),
    headers={"X-OpenAI-API-Key": openai_api_key},
)

# Get the WineReview collection
collection = client.collections.get("WineReview")

# Define the query parameters
search_query = "pair with steak"
max_results = 5
alpha = 0.5

# Build the filters:
# - price must be less than 50
# - points must be greater than 90
# - review_body must contain at least one of the keywords.
filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(
        ["spice", "fruit", "berry", "cherry", "honey"]
    )
)

# Run the hybrid search query using the text2vec-openai vectorizer in WineReview collection
response = collection.query.hybrid(
    query=search_query,
    limit=max_results,
    alpha=alpha,
    filters=filters,
    return_metadata=MetadataQuery(score=True)
)

# Print the relevant properties for each matching wine: title, country, price, and points.
print("Matching Wines:")
for obj in response.objects:
    props = obj.properties
    title = props.get("title")
    country = props.get("country")
    price = props.get("price")
    points = props.get("points")
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
    print(f"Score: {obj.metadata.score}\n")

# Close the client connection
client.close()
------------------------------------------------------------

Explanation:
1. We import the required modules and pull the necessary API keys and cluster URL from the environment.
2. The client is connected to Weaviate Cloud using the API key provided for both the Weaviate Cloud and OpenAI.
3. We retrieve the WineReview collection.
4. The query is executed as a hybrid search with the query "pair with steak", a result limit of 5, and alpha set to 0.5.
5. We combine three filters using logical AND (&):
   • Price is less than 50.
   • Points are greater than 90.
   • review_body contains at least one keyword from ["spice", "fruit", "berry", "cherry", "honey"].
6. Finally, for each matching wine, the code prints the title, country, price, and points together with the result’s score.

This example should serve as a complete solution using the latest Weaviate client syntax.
```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example using the latest Weaviate client syntax. Make sure you have set the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY before running the code.
                ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 17.74s)

**Generated Code**:
```python
Below is an example Python script that uses the latest Weaviate client syntax to connect to a Weaviate Cloud instance, query the WineReview collection using a hybrid search (with α = 0.5), and only return wines that satisfy the following conditions:

• The wine best matches the query "pair with steak"  
• The result list is limited to 5 objects  
• Each wine has price < 50  
• Each wine has points > 90  
• The review_body contains at least one of the substrings "spice", "fruit", "berry", "cherry", or "honey"

Make sure you have the environment variables set:
 • OPENAI_API_KEY  
 • WCD_TEST_URL  (Weaviate Cloud instance URL)  
 • WCD_TEST_KEY  (Weaviate Cloud API key)

You can learn more about using filters and hybrid search on the Weaviate documentation pages:
https://weaviate.io/developers/weaviate/search

Below is the complete code:

------------------------------------------------------------
#!/usr/bin/env python3
import os
import weaviate

# Read API keys and URLs from environment variables
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

# Connect to Weaviate Cloud with API-key authentication
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=weaviate.AuthApiKey(WCD_TEST_KEY),
    headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY
    }
)

# Retrieve the WineReview collection (class)
wine_review = client.collections.get("WineReview")

# Define the where filter object to enforce:
# - price less than 50
# - points greater than 90
# - review_body LIKE one of required substrings
filter_conditions = {
    "operator": "And",
    "operands": [
        {
            "path": ["price"],
            "operator": "LessThan",
            "valueNumber": 50

```

**Errors**:
```
  File "/code/code.py", line 1
    Below is an example Python script that uses the latest Weaviate client syntax to connect to a Weaviate Cloud instance, query the WineReview collection using a hybrid search (with α = 0.5), and only return wines that satisfy the following conditions:
                ^
SyntaxError: invalid syntax

```

---

### openai/chatgpt-4o-latest

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 3.47s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

# Ensure the environment variables are set
if not weaviate_url or not weaviate_api_key:
    raise EnvironmentError("WCD_TEST_URL and WCD_TEST_KEY must be set in the environment.")

# Create authentication object
auth_config = AuthApiKey(api_key=weaviate_api_key)

# Connect to Weaviate Cloud
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config,
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is not ready.")
```

**Errors**:
```
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

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 1.59s)

**Generated Code**:
```python
Sure! Here's the Python code using the latest Weaviate client syntax to connect to a Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, and then check if the server is ready:

import os
import weaviate
from weaviate.classes.init import Auth

# Load environment variables
cluster_url = os.environ["WCD_TEST_URL"]
api_key = os.environ["WCD_TEST_KEY"]

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

**Errors**:
```
  File "/code/code.py", line 1
    Sure! Here's the Python code using the latest Weaviate client syntax to connect to a Weaviate Cloud instance using the environment variables WCD_TEST_URL and WCD_TEST_KEY, and then check if the server is ready:
        ^
SyntaxError: invalid syntax

```

---

#### zero_shot_create_collection

*Zero shot: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 16.15s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.collections.classes.config import Property, DataType

# Load environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")

if not weaviate_url or not weaviate_api_key:
    raise EnvironmentError("WCD_TEST_URL and WCD_TEST_KEY must be set in environment variables.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
)

# Collection name
collection_name = "DemoProducts"

# Delete collection if it exists
if collection_name in client.collections.list_all():
    client.collections.delete(collection_name)
    print(f"Deleted existing collection: {collection_name}")

# Define collection schema
properties = [
    Property(name="name", data_type=DataType.TEXT),
    Property(name="description", data_type=DataType.TEXT),
    Property(name="price", data_type=DataType.NUMBER),
    Property(name="in_stock", data_type=DataType.BOOL),
]

# Create the collection
client.collections.create(
    name=collection_name,
    properties=properties,
)

print(f"Collection '{collection_name}' created successfully.")

# Close the client connection
client.close()
```

**Output**:
```
Deleted existing collection: DemoProducts
Collection 'DemoProducts' created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 8.24s)

**Generated Code**:
```python
Sure! Here's the complete Python code using the latest Weaviate client syntax to create a collection named "DemoProducts" with the specified properties, connecting to Weaviate Cloud using environment variables WCD_TEST_URL and WCD_TEST_KEY:

import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Load environment variables
cluster_url = os.getenv("WCD_TEST_URL")
api_key = os.getenv("WCD_TEST_KEY")

# Ensure environment variables are set
if not cluster_url or not api_key:
    raise EnvironmentError("WCD_TEST_URL and WCD_TEST_KEY must be set in environment variables.")

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
    print(f"Deleted existing collection: {collection_name}")

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

print(f"Created collection: {products_collection.name}")

# Close the client connection
client.close()

Make sure you have the weaviate-client installed (version 4.x or later) and that your environment variables WCD_TEST_URL and WCD_TEST_KEY are correctly set before running this script.

You can set the environment variables in your terminal like this:

export WCD_TEST_URL="https://your-instance.weaviate.network"
export WCD_TEST_KEY="your-api-key"

Let me know if you want to add vectorization or other settings to the collection!
```

**Errors**:
```
  File "/code/code.py", line 1
    Sure! Here's the complete Python code using the latest Weaviate client syntax to create a collection named "DemoProducts" with the specified properties, connecting to Weaviate Cloud using environment variables WCD_TEST_URL and WCD_TEST_KEY:
        ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ❌ FAILURE (runtime: 4.35s)

**Generated Code**:
```python
Here's Python code using the latest Weaviate Python client (v4.x) to:

- Connect to a Weaviate Cloud instance using environment variables WCD_TEST_URL and WCD_TEST_KEY
- Delete the "DemoProducts" collection if it already exists
- Create a new "DemoProducts" collection with the specified properties

from weaviate import connect_to_weaviate_cloud
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType
import os

# Connect to Weaviate Cloud using environment variables
client = connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Delete the collection if it already exists
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the "DemoProducts" collection
    client.collections.create(
        name="DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )

    print("Collection 'DemoProducts' created successfully.")

finally:
    # Always close the client when done
    client.close()

This code uses the latest v4.x syntax and follows best practices for connection handling and collection management.

For more information, see:
- Python Client Library: https://weaviate.io/developers/weaviate/client-libraries/python
- Collection Management: https://weaviate.io/developers/weaviate/manage-data/collections
```

**Errors**:
```
  File "/code/code.py", line 1
    Here's Python code using the latest Weaviate Python client (v4.x) to:
                                                                         ^
SyntaxError: EOL while scanning string literal

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 6.43s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.collections.classes.config import Property, DataType
from weaviate.classes.init import AdditionalConfig

# Load environment variables
WEAVIATE_URL = os.getenv("WCD_TEST_URL")
WEAVIATE_API_KEY = os.getenv("WCD_TEST_KEY")

if not WEAVIATE_URL or not WEAVIATE_API_KEY:
    raise EnvironmentError("WCD_TEST_URL and WCD_TEST_KEY must be set in environment variables.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
    additional_config=AdditionalConfig(timeout=(10, 60))  # Optional: increase timeout for batch ops
)

# Define the collection schema
collection_name = "DemoProducts"

# Delete the collection if it already exists (optional, for clean runs)
if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

# Create the collection
client.collections.create(
    name=collection_name,
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
    ]
)

# Get the collection object
collection = client.collections.get(collection_name)

# Prepare 50 objects
objects = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    }
    for i in range(50)
]

# Batch import the objects
collection.data.insert_many(objects)

# Count and print the number of objects in the collection
count = collection.aggregate.over_all(total_count=True).total_count
print(f"Number of objects in '{collection_name}': {count}")

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

**Status**: ❌ FAILURE (runtime: 5.97s)

**Generated Code**:
```python
Sure! Here's a complete Python script using the latest Weaviate client syntax to:

- Connect to a Weaviate Cloud instance using environment variables WCD_TEST_URL and WCD_TEST_KEY.
- Create (or get) a collection named DemoProducts with text properties name and description.
- Batch import 50 objects with arbitrary values.
- Print the number of objects in the collection.

Make sure you have the latest weaviate-client installed (v4+):

pip install weaviate-client --upgrade

Here's the code:

import os
import weaviate
from weaviate.auth import AuthApiKey
from weaviate.classes.config import Property, DataType, CollectionConfig

# Load environment variables
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

if not WCD_TEST_URL or not WCD_TEST_KEY:
    raise EnvironmentError("WCD_TEST_URL and WCD_TEST_KEY must be set as environment variables.")

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WCD_TEST_URL,
    auth_credentials=AuthApiKey(WCD_TEST_KEY),
)

# Define collection name
collection_name = "DemoProducts"

# Check if collection exists, if not, create it
if collection_name not in client.collections.list_all():
    client.collections.create(
        config=CollectionConfig(
            name=collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ]
        )
    )

# Get the collection
collection = client.collections.get(collection_name)

# Prepare 50 objects
data_rows = [
    {"name": f"Product {i+1}", "description": f"Description {i+1}"} for i in range(50)
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
print(f"Number of objects in '{collection_name}': {len(collection)}")

# Close the client connection
client.close()

This script will:

- Automatically create the DemoProducts collection if it doesn't exist.
- Import 50 simple product objects.
- Print the number of objects in the collection after import.

Let me know if you want to add vectorization or other features!
```

**Errors**:
```
  File "/code/code.py", line 1
    Sure! Here's a complete Python script using the latest Weaviate client syntax to:
        ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 5.33s)

**Generated Code**:
```python
Here's a complete Python script using the latest Weaviate Python client (v4.x) that:

- Connects to a Weaviate Cloud instance using environment variables WCD_TEST_URL and WCD_TEST_KEY.
- Creates a collection named DemoProducts with name and description properties.
- Batch imports 50 objects into the collection.
- Prints the number of objects in the collection.

Make sure you have the weaviate-client package installed (v4.x). You can install it with:

pip install weaviate-client>=4.0.0

Now, here's the code:

import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure

# Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # Create the collection if it doesn't exist
    collection_name = "DemoProducts"
    if not client.collections.exists(collection_name):
        client.collections.create(
            name=collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            vectorizer_config=Configure.Vectorizer.text2vec_openai()  # Optional: use OpenAI vectorizer
        )

    # Get the collection
    collection = client.collections.get(collection_name)

    # Batch import 50 objects
    with collection.batch.dynamic() as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )

    # Count the number of objects in the collection
    count = collection.aggregate.count()
    print(f"Number of objects in '{collection_name}': {count}")

finally:
    client.close()

This script ensures:

- Safe connection handling with try/finally.
- Dynamic batching for efficient import.
- Automatic collection creation if it doesn't exist.

Let me know if you want to use a different vectorizer or add more properties!
```

**Errors**:
```
  File "/code/code.py", line 1
    Here's a complete Python script using the latest Weaviate Python client (v4.x) that:
                                                                                        ^
SyntaxError: EOL while scanning string literal

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 7.40s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Authenticate with Weaviate Cloud
auth_config = AuthApiKey(api_key=weaviate_api_key)

# Create Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config,
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key  # For text2vec-openai
    }
)

# Perform a semantic search using nearText
response = client.collections.get("WineReview").query.near_text(
    query="dessert wine",
    limit=2,
    return_properties=["title", "country", "price", "points"]
)

# Print the results
for i, wine in enumerate(response.objects, start=1):
    props = wine.properties
    print(f"Result {i}:")
    print(f"  Title:   {props.get('title')}")
    print(f"  Country: {props.get('country')}")
    print(f"  Price:   {props.get('price')}")
    print(f"  Points:  {props.get('points')}")
    print()
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

**Status**: ❌ FAILURE (runtime: 3.43s)

**Generated Code**:
```python
Sure! Here's the complete Python code using the latest Weaviate client syntax to query the WineReview collection for wines that best match the query "dessert wine", with a limit of 2 results. It prints the title, country, price, and points of each matching wine.

Make sure the environment variables OPENAI_API_KEY, WCD_TEST_URL, and WCD_TEST_KEY are set before running the script.

Python Code:

import os
import weaviate
from weaviate.classes.init import Auth

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WCD_TEST_URL = os.getenv("WCD_TEST_URL")
WCD_TEST_KEY = os.getenv("WCD_TEST_KEY")

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

# Perform a near_text query
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print selected properties of each matching wine
for obj in response.objects:
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
    print("-" * 40)

# Close the client connection
client.close()

This script will output the top 2 wines that semantically match the query "dessert wine", showing their title, country, price, and points.
```

**Errors**:
```
  File "/code/code.py", line 1
    Sure! Here's the complete Python code using the latest Weaviate client syntax to query the WineReview collection for wines that best match the query "dessert wine", with a limit of 2 results. It prints the title, country, price, and points of each matching wine.
        ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.10s)

**Generated Code**:
```python
Here's the Python code using the latest Weaviate Python client (v4.x) to connect to a Weaviate Cloud instance and perform a semantic search on the WineReview collection using the query "dessert wine". It retrieves up to 2 results and prints the title, country, price, and points for each result:

import os
import weaviate
from weaviate.classes.init import Auth

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
    collection = client.collections.get("WineReview")

    # Perform semantic search using near_text
    response = collection.query.near_text(
        query="dessert wine",
        limit=2,
        return_properties=["title", "country", "price", "points"]
    )

    # Print the results
    for obj in response.objects:
        props = obj.properties
        print("Title:", props.get("title"))
        print("Country:", props.get("country"))
        print("Price:", props.get("price"))
        print("Points:", props.get("points"))
        print("-" * 40)

finally:
    # Close the client connection
    client.close()

Make sure the environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set before running this script.

This code uses the near_text semantic search powered by the text2vec-openai vectorizer and retrieves the specified fields from the WineReview collection.
```

**Errors**:
```
  File "/code/code.py", line 1
    Here's the Python code using the latest Weaviate Python client (v4.x) to connect to a Weaviate Cloud instance and perform a semantic search on the WineReview collection using the query "dessert wine". It retrieves up to 2 results and prints the title, country, price, and points for each result:
                                                                                                                                                                                                                                                                                                           ^
SyntaxError: EOL while scanning string literal

```

---

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 16.21s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import AuthApiKey

# Load environment variables
weaviate_url = os.getenv("WCD_TEST_URL")
weaviate_api_key = os.getenv("WCD_TEST_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Authenticate with Weaviate Cloud
auth_config = AuthApiKey(api_key=weaviate_api_key)

# Initialize Weaviate client
client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config,
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key  # For text2vec-openai
    }
)

# Define the substrings to match in review_body
keywords = ["spice", "fruit", "berry", "cherry", "honey"]
# Construct the filter for review_body using OR conditions
review_body_filter = {
    "operator": "Or",
    "operands": [
        {
            "path": ["review_body"],
            "operator": "Like",
            "valueText": f"*{kw}*"
        } for kw in keywords
    ]
}

# Combine all filters
filters = {
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

# Perform hybrid search
response = client.collections.get("WineReview").query.hybrid(
    query="pair with steak",
    alpha=0.5,
    limit=5,
    filters=filters,
    return_metadata=["score"],
    return_properties=["title", "country", "price", "points"]
)

# Print results
for obj in response.objects:
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
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

#### simple_example_complex_hybrid_query

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 5.47s)

**Generated Code**:
```python
Sure! Here's the complete Python code using the latest Weaviate client syntax to query the WineReview collection as per your requirements:

- Hybrid search with alpha=0.5
- Limit 5 results
- Filters:
  - price < 50
  - points > 90
  - review_body contains any of: "spice", "fruit", "berry", "cherry", "honey"
- Print title, country, price, and points

Make sure you have the latest weaviate-client installed (pip install weaviate-client).

Python Code:

import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, MetadataQuery

# Load environment variables
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

# Define the hybrid query
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

Make sure your environment variables WCD_TEST_URL, WCD_TEST_KEY, and OPENAI_API_KEY are set before running the script.

Let me know if you need help setting those or modifying the query further!
```

**Errors**:
```
  File "/code/code.py", line 1
    Sure! Here's the complete Python code using the latest Weaviate client syntax to query the WineReview collection as per your requirements:
        ^
SyntaxError: invalid syntax

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 12.94s)

**Generated Code**:
```python
Here's a complete Python script using the latest Weaviate Python client (v4.x) to perform a hybrid search on the WineReview collection, with the specified filters and connection settings:

Python Code:

import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

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

    # Define the filter:
    # price < 50 AND points > 90 AND review_body contains one of the keywords
    keyword_filter = (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )

    combined_filter = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        keyword_filter
    )

    # Perform hybrid search
    response = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        fusion_type=HybridFusion.RELATIVE_SCORE,
        filters=combined_filter,
        return_properties=["title", "country", "price", "points"],
        limit=5
    )

    # Print results
    for obj in response.objects:
        props = obj.properties
        print(f"Title: {props.get('title')}")
        print(f"Country: {props.get('country')}")
        print(f"Price: {props.get('price')}")
        print(f"Points: {props.get('points')}")
        print("-" * 40)

finally:
    client.close()

What this code does:

- Connects to your Weaviate Cloud instance using credentials from environment variables.
- Queries the WineReview collection using a hybrid search with alpha=0.5 for the query "pair with steak".
- Applies filters:
  - price < 50
  - points > 90
  - review_body contains at least one of the keywords: spice, fruit, berry, cherry, honey
- Limits results to 5.
- Prints the title, country, price, and points of each result.

Make sure the WineReview collection exists and has the appropriate schema and data.
```

**Errors**:
```
  File "/code/code.py", line 1
    Here's a complete Python script using the latest Weaviate Python client (v4.x) to perform a hybrid search on the WineReview collection, with the specified filters and connection settings:
                                                                                                                                                                                               ^
SyntaxError: EOL while scanning string literal

```

---

### openai/gpt-4.1-2025-04-14

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 5.95s)

**Generated Code**:
```python
import os
import weaviate

# Get credentials from environment variables
url = os.environ["WCD_TEST_URL"]
api_key = os.environ["WCD_TEST_KEY"]

# Create a Weaviate client for Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=url,
    auth_credentials=weaviate.auth.AuthApiKey(api_key),
)

# Check if the server is ready
if client.is_ready():
    print("Weaviate server is ready to accept requests.")
else:
    print("Weaviate server is NOT ready.")

# Close the client connection
client.close()
```

**Output**:
```
Weaviate server is ready to accept requests.

```

---

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 6.10s)

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

**Status**: ✅ SUCCESS (runtime: 14.11s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.collections.classes.config import Property, DataType

# Get environment variables
WEAVIATE_URL = os.environ["WCD_TEST_URL"]
WEAVIATE_API_KEY = os.environ["WCD_TEST_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=WEAVIATE_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_API_KEY),
)

collection_name = "DemoProducts"

# Delete collection if it exists
if collection_name in client.collections.list_all():
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
    name=collection_name,
    properties=properties,
)

print(f"Collection '{collection_name}' created successfully.")

# Optional: Close the client connection
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

#### simple_example_create_collection

*Simple example: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 10.13s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

# Get credentials from environment variables
CLUSTER_URL = os.environ["WCD_TEST_URL"]
API_KEY = os.environ["WCD_TEST_KEY"]

# Connect to the Weaviate Cloud instance
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=CLUSTER_URL,
    auth_credentials=Auth.api_key(API_KEY)
)

# Collection name
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

**Status**: ✅ SUCCESS (runtime: 11.83s)

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

try:
    # Delete the collection if it exists
    if client.collections.exists("DemoProducts"):
        client.collections.delete("DemoProducts")

    # Create the collection with the specified properties
    client.collections.create(
        "DemoProducts",
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="price", data_type=DataType.NUMBER),
            Property(name="in_stock", data_type=DataType.BOOL),
        ]
    )
finally:
    client.close()
```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 11.77s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.collections.classes.config import Property, DataType

# Get credentials from environment variables
WCD_TEST_URL = os.environ["WCD_TEST_URL"]
WCD_TEST_KEY = os.environ["WCD_TEST_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=WCD_TEST_URL,
    auth_credentials=weaviate.auth.AuthApiKey(WCD_TEST_KEY),
)

# Define collection schema
collection_name = "DemoProducts"
properties = [
    Property(name="name", data_type=DataType.TEXT),
    Property(name="description", data_type=DataType.TEXT),
]

# Create collection if it doesn't exist
if collection_name not in client.collections.list_all():
    client.collections.create(
        name=collection_name,
        properties=properties,
        vectorizer_config=weaviate.collections.classes.config.Configure.Vectorizer.text2vec_openai(),  # or your preferred vectorizer
    )

# Get collection handle
collection = client.collections.get(collection_name)

# Prepare 50 objects
objects = [
    {
        "name": f"Product {i}",
        "description": f"Description {i}"
    }
    for i in range(1, 51)
]

# Batch import
collection.data.insert_many(objects)

# Count objects in the collection
count = collection.aggregate.count()
print(f"Number of objects in '{collection_name}': {count}")

# Close connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 46, in <module>
    count = collection.aggregate.count()
AttributeError: '_AggregateCollection' object has no attribute 'count'
/usr/local/lib/python3.9/site-packages/weaviate/warnings.py:314: ResourceWarning: Con004: The connection to Weaviate was not closed properly. This can lead to memory leaks.
            Please make sure to close the connection using `client.close()`.
  warnings.warn(
/usr/local/lib/python3.9/asyncio/selector_events.py:702: ResourceWarning: unclosed transport <_SelectorSocketTransport fd=6 read=idle write=<idle, bufsize=0>>

```

---

#### simple_example_batch_import

*Simple example: Batch import data into a collection*

**Status**: ✅ SUCCESS (runtime: 16.66s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.auth import Auth

# Get credentials from environment variables
CLUSTER_URL = os.environ["WCD_TEST_URL"]
API_KEY = os.environ["WCD_TEST_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=CLUSTER_URL,
    auth_credentials=Auth.api_key(API_KEY),
)

# Ensure the collection exists with the correct schema
COLLECTION_NAME = "DemoProducts"
if COLLECTION_NAME not in client.collections.list_all():
    client.collections.create(
        name=COLLECTION_NAME,
        properties=[
            weaviate.Property(name="name", data_type=weaviate.DataType.TEXT),
            weaviate.Property(name="description", data_type=weaviate.DataType.TEXT),
        ],
    )

collection = client.collections.get(COLLECTION_NAME)

# Prepare 50 objects
data_rows = [
    {"name": f"Product {i+1}", "description": f"Description {i+1}"}
    for i in range(50)
]

# Batch import
with collection.batch.dynamic() as batch:
    for data_row in data_rows:
        batch.add_object(properties=data_row)
        if batch.number_errors > 10:
            print("Batch import stopped due to excessive errors.")
            break

failed_objects = collection.batch.failed_objects
if failed_objects:
    print(f"Number of failed imports: {len(failed_objects)}")
    print(f"First failed object: {failed_objects[0]}")

# Print the number of objects in the collection
print(len(collection))

client.close()
```

**Output**:
```
50

```

---

#### extensive_examples_batch_import

*Extensive examples: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 13.79s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure

# 1. Connect to Weaviate Cloud using environment variables
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=Auth.api_key(os.environ["WCD_TEST_KEY"])
)

try:
    # 2. Ensure the "DemoProducts" collection exists with the correct schema
    collection_name = "DemoProducts"
    if not client.collections.exists(collection_name):
        client.collections.create(
            collection_name,
            properties=[
                Property(name="name", data_type=DataType.TEXT),
                Property(name="description", data_type=DataType.TEXT),
            ],
            vectorizer_config=Configure.Vectorizer.text2vec_openai()  # or .none() if you don't want vectorization
        )

    # 3. Get the collection object
    collection = client.collections.get(collection_name)

    # 4. Batch import 50 objects
    with collection.batch.dynamic() as batch:
        for i in range(50):
            batch.add_object(
                properties={
                    "name": f"Product {i}",
                    "description": f"Description {i}"
                }
            )

    # 5. Print the number of objects in the collection
    count = collection.aggregate.count()
    print(f"Number of objects in '{collection_name}': {count}")

finally:
    client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 39, in <module>
    count = collection.aggregate.count()
AttributeError: '_AggregateCollection' object has no attribute 'count'

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 11.78s)

**Generated Code**:
```python
import os
import weaviate

# Get credentials from environment
weaviate_url = os.environ["WCD_TEST_URL"]
weaviate_api_key = os.environ["WCD_TEST_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    cluster_url=weaviate_url,
    auth_credentials=weaviate.auth.AuthApiKey(weaviate_api_key),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Query the WineReview collection
response = client.collections.get("WineReview").query.near_text(
    query="dessert wine"
).limit(2).fetch(
    properties=["title", "country", "price", "points"]
)

# Print results
for obj in response.objects:
    print("Title:", obj.properties.get("title"))
    print("Country:", obj.properties.get("country"))
    print("Price:", obj.properties.get("price"))
    print("Points:", obj.properties.get("points"))
    print("-" * 40)

# Close the client connection
client.close()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 10, in <module>
    client = weaviate.connect_to_wcs(
TypeError: connect_to_wcs() got an unexpected keyword argument 'additional_headers'

```

---

#### simple_example_basic_semantic_search

*Simple example: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.20s)

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

# Query for wines matching "dessert wine"
response = collection.query.near_text(
    query="dessert wine",
    limit=2
)

# Print the desired properties for each result
for obj in response.objects:
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
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

**Status**: ✅ SUCCESS (runtime: 14.85s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth

# Connect to Weaviate Cloud with OpenAI vectorizer key
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

    # Perform a semantic search for "dessert wine"
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

#### zero_shot_complex_hybrid_query

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 13.42s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.connect import ConnectionParams
from weaviate.collections.query import Filter, FilterOperator

# Load environment variables
weaviate_url = os.environ["WCD_TEST_URL"]
weaviate_api_key = os.environ["WCD_TEST_KEY"]
openai_api_key = os.environ["OPENAI_API_KEY"]

# Connect to Weaviate Cloud
client = weaviate.connect_to_wcs(
    ConnectionParams.from_url(
        url=weaviate_url,
        api_key=weaviate_api_key,
    ),
    additional_headers={
        "X-OpenAI-Api-Key": openai_api_key
    }
)

# Build the filter for price, points, and review_body substrings
price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)
review_body_filter = (
    Filter.by_property("review_body").contains("spice") |
    Filter.by_property("review_body").contains("fruit") |
    Filter.by_property("review_body").contains("berry") |
    Filter.by_property("review_body").contains("cherry") |
    Filter.by_property("review_body").contains("honey")
)
combined_filter = price_filter & points_filter & review_body_filter

# Query the WineReview collection
results = client.collections.get("WineReview").query.hybrid(
    query="pair with steak",
    alpha=0.5,
    limit=5,
    filters=combined_filter,
    return_properties=["title", "country", "price", "points"]
)

# Print results
for obj in results.objects:
    props = obj.properties
    print(f"Title: {props['title']}")
    print(f"Country: {props['country']}")
    print(f"Price: {props['price']}")
    print(f"Points: {props['points']}")
    print("-" * 40)
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 4, in <module>
    from weaviate.collections.query import Filter, FilterOperator
ImportError: cannot import name 'Filter' from 'weaviate.collections.query' (/usr/local/lib/python3.9/site-packages/weaviate/collections/query.py)

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

# Build the filter
review_keywords = ["spice", "fruit", "berry", "cherry", "honey"]
filters = (
    Filter.by_property("price").less_than(50) &
    Filter.by_property("points").greater_than(90) &
    Filter.by_property("review_body").contains_any(review_keywords)
)

# Perform the hybrid search
response = collection.query.hybrid(
    query="pair with steak",
    limit=5,
    alpha=0.5,
    filters=filters,
    return_metadata=MetadataQuery(score=True),
    return_properties=["title", "country", "price", "points"]
)

# Print results
for obj in response.objects:
    props = obj.properties
    print(f"Title: {props.get('title')}")
    print(f"Country: {props.get('country')}")
    print(f"Price: {props.get('price')}")
    print(f"Points: {props.get('points')}")
    print(f"Score: {obj.metadata.score}")
    print("-" * 40)

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
Score: 0.46158072352409363
----------------------------------------
Title: Doña Silvina 2011 Malbec (Mendoza)
Country: Argentina
Price: 27.0
Points: 91
Score: 0.21982641518115997
----------------------------------------
Title: Dobogó 2011 Szent Tamás Betsek Vineyards  (Tokaji)
Country: Hungary
Price: 25.0
Points: 93
Score: 0.06552334129810333
----------------------------------------
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
Score: 0.01862688735127449
----------------------------------------

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 12.36s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter, HybridFusion

# Connect to Weaviate Cloud with OpenAI key for vectorization
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

    # Build the filter:
    # price < 50 AND points > 90 AND
    # (review_body LIKE "*spice*" OR "*fruit*" OR "*berry*" OR "*cherry*" OR "*honey*")
    review_body_filter = (
        Filter.by_property("review_body").like("*spice*") |
        Filter.by_property("review_body").like("*fruit*") |
        Filter.by_property("review_body").like("*berry*") |
        Filter.by_property("review_body").like("*cherry*") |
        Filter.by_property("review_body").like("*honey*")
    )
    filters = (
        Filter.by_property("price").less_than(50) &
        Filter.by_property("points").greater_than(90) &
        review_body_filter
    )

    # Perform hybrid search
    response = collection.query.hybrid(
        query="pair with steak",
        alpha=0.5,
        fusion_type=HybridFusion.RELATIVE_SCORE,
        filters=filters,
        limit=5,
        return_properties=["title", "country", "price", "points"]
    )

    # Print results
    for obj in response.objects:
        props = obj.properties
        print(f"Title: {props.get('title')}")
        print(f"Country: {props.get('country')}")
        print(f"Price: {props.get('price')}")
        print(f"Points: {props.get('points')}")
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
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
----------------------------------------

```

---

### openai/gpt-4.1-mini-2025-04-14

#### zero_shot_connect

*Zero shot: Basic Weaviate connection*

**Status**: ❌ FAILURE (runtime: 2.93s)

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
    additional_headers={
        "X-OpenAI-Api-Key": api_key  # sometimes needed, but usually not for WCD
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

#### simple_example_connect

*Simple example: Basic Weaviate connection*

**Status**: ✅ SUCCESS (runtime: 2.45s)

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

**Status**: ❌ FAILURE (runtime: 5.13s)

**Generated Code**:
```python
import os
import weaviate

# Load environment variables
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
        },
        {
            "name": "price",
            "dataType": ["number"],
            "description": "Price of the product"
        },
        {
            "name": "in_stock",
            "dataType": ["boolean"],
            "description": "Whether the product is in stock"
        }
    ]
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

**Status**: ✅ SUCCESS (runtime: 4.97s)

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
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### extensive_examples_create_collection

*Extensive examples: Create a Weaviate collection with properties*

**Status**: ✅ SUCCESS (runtime: 5.38s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType

def main():
    # Read environment variables
    wcd_url = os.environ["WCD_TEST_URL"]
    wcd_key = os.environ["WCD_TEST_KEY"]

    # Connect to Weaviate Cloud
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_key)
    )

    collection_name = "DemoProducts"

    # If collection exists, delete it first
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    # Create collection with specified properties
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

    # Close client connection when done
    client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Collection "DemoProducts" created successfully.

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:

```

---

#### zero_shot_batch_import

*Zero shot: Batch import data into a collection*

**Status**: ❌ FAILURE (runtime: 7.29s)

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
        "X-OpenAI-Api-Key": WCD_TEST_KEY  # sometimes needed for OpenAI integration, but optional here
    }
)

# Define the schema for the "DemoProducts" class
schema = {
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
    client.schema.create_class(schema)

# Prepare batch import of 50 objects
with client.batch as batch:
    batch.batch_size = 20  # optional, default is 100
    for i in range(1, 51):
        obj = {
            "name": f"Product {i}",
            "description": f"Description {i}"
        }
        batch.add_data_object(obj, "DemoProducts")

# Query to count the number of objects in DemoProducts
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

**Status**: ❌ FAILURE (runtime: 7.16s)

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

    # Get the collection (class) reference
    collection = client.collections.get(class_name)

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

    # Print the number of objects in the collection
    print(f"Number of objects in '{class_name}': {len(collection)}")

    client.close()

if __name__ == "__main__":
    main()
```

**Errors**:
```
Traceback (most recent call last):
  File "/code/code.py", line 75, in <module>
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

**Status**: ✅ SUCCESS (runtime: 10.47s)

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

    # Check if collection exists, delete if it does (optional, to start fresh)
    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    # Create collection with properties: name and description (both TEXT)
    client.collections.create(
        collection_name,
        properties=[
            Property(name="name", data_type=DataType.TEXT),
            Property(name="description", data_type=DataType.TEXT),
        ],
        # Use a vectorizer, e.g. text2vec-openai for text properties (optional but recommended)
        vectorizer_config=Configure.Vectorizer.text2vec_openai()
    )

    # Get the collection object
    collection = client.collections.get(collection_name)

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
    # We can query all objects and count them
    response = collection.query.fetch_objects(
        limit=1000,  # large enough to get all 50 objects
        return_properties=["name"]
    )
    print(f"Number of objects in '{collection_name}': {len(response.objects)}")

    # Close client connection
    client.close()

if __name__ == "__main__":
    main()
```

**Output**:
```
Number of objects in 'DemoProducts': 0

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/collections/classes/config.py:2041: PydanticDeprecatedSince211: Accessing this attribute on the instance is deprecated, and will be removed in Pydantic V3. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.
  for cls_field in self.model_fields:
{'message': 'Failed to send all objects in a batch of 48', 'error': "WeaviateInsertManyAllFailedError('Every object failed during insertion. Here is the set of all errors: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY')"}
{'message': 'Failed to send 48 objects in a batch of 48. Please inspect client.batch.failed_objects or collection.batch.failed_objects for the failed objects.'}
{'message': 'Failed to send all objects in a batch of 2', 'error': "WeaviateInsertManyAllFailedError('Every object failed during insertion. Here is the set of all errors: API Key: no api key found neither in request header: X-Openai-Api-Key nor in environment variable under OPENAI_APIKEY')"}
{'message': 'Failed to send 2 objects in a batch of 2. Please inspect client.batch.failed_objects or collection.batch.failed_objects for the failed objects.'}

```

---

#### zero_shot_basic_semantic_search

*Zero shot: Query a collection to find objects that match a natural language query*

**Status**: ❌ FAILURE (runtime: 3.71s)

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

# Perform the vector search using the text2vec-openai vectorizer
result = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_near_text({"concepts": [query_text]})
    .with_limit(2)
    .do()
)

# Extract and print results
wines = result.get("data", {}).get("Get", {}).get("WineReview", [])
for wine in wines:
    title = wine.get("title")
    country = wine.get("country")
    price = wine.get("price")
    points = wine.get("points")
    print(f"Title: {title}, Country: {country}, Price: {price}, Points: {points}")
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

**Status**: ✅ SUCCESS (runtime: 9.82s)

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

---

#### extensive_examples_basic_semantic_search

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.13s)

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

    # Perform a semantic search using near_text with the query "dessert wine"
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

**Status**: ❌ FAILURE (runtime: 8.74s)

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
    additional_headers={
        "X-OpenAI-Api-Key": OPENAI_API_KEY,
        "Authorization": f"Bearer {WCD_TEST_KEY}"
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
# We use a "Or" operator with "Like" operators for each substring
review_body_filter = {
    "operator": "Or",
    "operands": [
        {"path": ["review_body"], "operator": "Like", "valueString": "*spice*"},
        {"path": ["review_body"], "operator": "Like", "valueString": "*fruit*"},
        {"path": ["review_body"], "operator": "Like", "valueString": "*berry*"},
        {"path": ["review_body"], "operator": "Like", "valueString": "*cherry*"},
        {"path": ["review_body"], "operator": "Like", "valueString": "*honey*"},
    ]
}

# Combine the two filters with an "And"
combined_filter = {
    "operator": "And",
    "operands": [
        filter_obj,
        review_body_filter
    ]
}

# Perform the hybrid query
result = (
    client.query.get("WineReview", ["title", "country", "price", "points"])
    .with_hybrid(query_text, alpha=0.5)
    .with_limit(5)
    .with_where(combined_filter)
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

**Status**: ✅ SUCCESS (runtime: 5.90s)

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
Title: Château Rauzan-Ségla 2012  Margaux, Country: France, Price: 0.0, Points: 94

```

---

#### extensive_examples_complex_hybrid_query

*Extensive examples: Query a collection to find objects that match a natural language query*

**Status**: ✅ SUCCESS (runtime: 7.11s)

**Generated Code**:
```python
import os
import weaviate
from weaviate.classes.query import Filter, HybridFusion

# Connect to Weaviate Cloud with API key and OpenAI API key in headers
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.environ["WCD_TEST_URL"],
    auth_credentials=weaviate.AuthApiKey(api_key=os.environ["WCD_TEST_KEY"]),
    headers={
        "X-OpenAI-Api-Key": os.environ["OPENAI_API_KEY"]
    }
)

# Get the WineReview collection
wine_collection = client.collections.get("WineReview")

# Build the filter:
# price < 50 AND points > 90 AND (review_body LIKE "*spice*" OR "*fruit*" OR "*berry*" OR "*cherry*" OR "*honey*")
price_filter = Filter.by_property("price").less_than(50)
points_filter = Filter.by_property("points").greater_than(90)

# Substring filters on review_body (case-insensitive LIKE)
# Weaviate's like filter supports wildcards * for substring matching
review_substrings = ["spice", "fruit", "berry", "cherry", "honey"]
review_filters = None
for substr in review_substrings:
    f = Filter.by_property("review_body").like(f"*{substr}*")
    review_filters = f if review_filters is None else (review_filters | f)

# Combine all filters with AND
combined_filter = price_filter & points_filter & review_filters

# Perform hybrid search with alpha=0.5, limit=5
response = wine_collection.query.hybrid(
    query="pair with steak",
    alpha=0.5,
    fusion_type=HybridFusion.RELATIVE_SCORE,
    filters=combined_filter,
    limit=5,
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

# Close client connection when done
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
Title: Château Rauzan-Ségla 2012  Margaux
Country: France
Price: 0.0
Points: 94
----------------------------------------

```

**Errors**:
```
/usr/local/lib/python3.9/site-packages/weaviate/__init__.py:145: DeprecationWarning: Dep010: Importing AuthApiKey from weaviate is deprecated. Import AuthApiKey from its module: weaviate.auth
  _Warnings.root_module_import(name, map_[name])

```

---

