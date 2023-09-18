Now lets us create logstash configuration to parse our nginx logs 

### 1. Input Section

we want to read Nginx access logs from the file. Let's break down the input section:

```yaml
input {
  file {
    path => "/var/log/nginx/access.log"
    start_position => "beginning"
    sincedb_path => "/dev/null"
    codec => json
  }
}
```

- `file`: We are using the `file` input plugin to read data from a file.
- `path`: Specify the path to your Nginx access log file.
- `start_position => "beginning"`: Logstash starts reading the log file from the beginning.
- `sincedb_path => "/dev/null"`: Prevents Logstash from remembering file read positions between restarts.
- `codec => json`: Indicates that the input data is in JSON format.

### 2. Filter Section

The filter section defines data transformations and processing. In our case, we are parsing the `time_local` field from Nginx logs. Here's the filter section:

```yaml
filter {
  date {
    match => [ "time_local", "dd/MMM/yyyy:HH:mm:ss Z" ]
    target => "time"
    remove_field => ["time_local"]
  }
}
```

- `date`: We use the `date` filter to parse the `time_local` field.
- `match`: Specifies the source field (`time_local`) and its date format.
- `target => "time"`: Parsed timestamps are stored in the `time` field.
- `remove_field => ["time_local"]`: Removes the original `time_local` field after parsing.

### 3. Output Section

The output section determines where Logstash should send the processed data. We're sending it to Elasticsearch. Here's the output section:

```yaml
output {
  elasticsearch {
    hosts => "elasticsearch:9200"
    manage_template => false
    index => "nginx-access-logs-%{+YYYY.MM.dd}"
  }
}
```

- `elasticsearch`: We configure the `elasticsearch` output plugin to send data to Elasticsearch.
- `hosts => "elasticsearch:9200"`: Specifies the Elasticsearch instance's address and port.
- `manage_template => false`: Disables Logstash's management of index templates.
- `index => "nginx-access-logs-%{+YYYY.MM.dd}"`: Defines the index pattern for Elasticsearch. The `%{+YYYY.MM.dd}` adds a date-based suffix for time-based indexing.

----

[Home](../README.md)