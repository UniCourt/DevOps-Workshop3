# Exploring Elasticsearch APIs with Kibana Dev Tools

Finally, The `E` in ELK stack, elasticsearch

In this step, we will explore some common Elasticsearch APIs and Document APIs using Kibana's Dev Tools. We'll create a new index, demonstrate various document operations, and finally delete the index.

### Accessing Kibana Dev Tools

1. Open your web browser and navigate to Kibana. By default, Kibana is hosted at `http://localhost:5601`.

2. In the Kibana interface, click on the "Dev Tools" link in the left-hand sidebar. This will open the Dev Tools panel where we can execute Elasticsearch APIs.

### Common Elasticsearch APIs

#### 1. Cluster Health API

- Checks the health of the Elasticsearch cluster, providing information about its status.
- Example API request:
  ```plaintext
  GET /_cluster/health
  ```

#### 2. Cluster State API

- Retrieves the cluster's metadata and current state.
- Example API request:
  ```plaintext
  GET /_cluster/state
  ```

#### 3. Cat APIs

Elasticsearch provides a set of Cat APIs that are designed to make it easier to view information about the cluster, nodes, indices, and more in a human-readable format. These APIs are often used for monitoring and troubleshooting purposes.
- Example APIs:
  ```plaintext
  GET _cat/indices
  ```
  
When appending ?pretty=true to any request made, the JSON returned will be pretty formatted

#### 4. Nodes Info API

- Retrieves information about the nodes in the Elasticsearch cluster.
- Example API request:
  ```plaintext
  GET /_nodes
  ```

### Creating a New Index

Let's start by creating a new index named "my-index."

```plaintext
PUT /my-index
```

### Document APIs

#### 1. Index API

- Adds or updates a document in an index.
- Example API request to add a document to the "my-index" index:
  ```plaintext
  POST /my-index/_doc/1
  {
    "field1": "value1",
    "field2": "value2"
  }
  ```

#### 2. Get API

- Retrieves a specific document by its ID.
- Example API request to get a document from the "my-index" index:
  ```plaintext
  GET /my-index/_doc/1
  ```

#### 3. Update API

- Updates an existing document.
- Example API request to update a document in the "my-index" index:
  ```plaintext
  POST /my-index/_update/1
  {
    "doc": {
      "field2": "new_value"
    }
  }
  ```

#### 4. Delete API

- Deletes a document by its ID.
- Example API request to delete a document from the "my-index" index:
  ```plaintext
  DELETE /my-index/_doc/1
  ```

#### 5. Bulk API

- Allows you to perform multiple index, update, or delete operations in a single request.
- Example API request to perform bulk operations:
  ```plaintext
  POST /my-index/_bulk
  { "index": { "_id": "1" } }
  { "field1": "value1" }
  { "delete": { "_id": "2" } }
  { "update": { "_id": "3" } }
  { "doc": { "field2": "new_value" } }
  ```

### Deleting the Index

To clean up, let's delete the "my-index" index.

```plaintext
DELETE /my-index
```


----

[Home](../README.md)