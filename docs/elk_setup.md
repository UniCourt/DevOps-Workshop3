# Setting up ELK stack 

Now that we know how to configure logstash, lets bring up the elk stack 

### Steps:
1. Go to elk-stack folder 
2. Run docker compose
```sh
cd elk-stack 
docker compose up -d 
```

Lets inspect the docker-compose.yaml, open `elk-stack/docker-compose.yaml`


- **Elasticsearch Service**: This service runs Elasticsearch, a distributed search and analytics engine. It is configured as follows:

  - `image`: Specifies the Docker image to use for Elasticsearch (version 8.6.0).
  - `container_name`: Sets the name of the Elasticsearch container to "elasticsearch."
  - `environment`: Configures an environment variable to specify that Elasticsearch should run in single-node mode.
  - `ports`: Maps port 9200 in the container to port 9200 on the host for accessing Elasticsearch.
  - `volumes`: Creates a Docker volume named `esdata` to persist Elasticsearch data.

- **Logstash Service**: This service runs Logstash, a data processing pipeline. It is configured as follows:

  - `image`: Specifies the Docker image to use for Logstash (version 8.6.0).
  - `container_name`: Sets the name of the Logstash container to "logstash."
  - `volumes`: Mounts the `logstash.conf` file from the host into the Logstash container for custom configuration. Additionally, it mounts Nginx log files from the application for processing.
  - `depends_on`: Specifies that this service depends on the Elasticsearch service.

- **Kibana Service**: This service runs Kibana, a web-based visualization tool for Elasticsearch. It is configured as follows:

  - `image`: Specifies the Docker image to use for Kibana (version 8.6.0).
  - `container_name`: Sets the name of the Kibana container to "kibana."
  - `environment`: Configures an environment variable `ELASTICSEARCH_HOSTS` to point to the Elasticsearch service.
  - `ports`: Maps port 5601 in the container to port 5601 on the host for accessing Kibana.
  - `depends_on`: Specifies that this service depends on the Elasticsearch service.

- **Volumes**: Defines a Docker volume named `esdata` with a local driver for persisting Elasticsearch data.






----

[Home](../README.md)