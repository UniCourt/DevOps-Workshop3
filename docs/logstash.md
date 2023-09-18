# Logstash

Logstash is the “L” in the ELK Stack — the world’s most popular log analysis platform and is responsible for aggregating
data from different sources, processing it, and sending it down the pipeline, usually to be directly indexed in
Elasticsearch.

For more info, see <https://www.elastic.co/guide/en/logstash/current/getting-started-with-logstash.html>

### Logstash General Features

* Logstash can collect data from different sources and send to multiple destinations.

* Logstash can handle all types of logging data like Apache Logs, Windows Event Logs, Data over Network Protocols, Data
  from Standard Input and many more.

* Logstash can also handle http requests and response data.

* Logstash provides a variety of filters, which helps the user to find more meaning in the data by parsing and
  transforming it.

* Logstash can also be used for handling sensors data in internet of things.

* Logstash is open source and available under the Apache license version 2.0.
---
## Structure of logstash

```
input {
    ...
}
filter {
    ...
}
output {
    ...
}
```

### Input

This is the first stage in the Logstash pipeline, which is used to get the data in Logstash for further processing.
Logstash offers various plugins to get data from different platforms. Some of the most commonly used plugins are – File,
Syslog, Redis and Beats.

[Available Input Plugins](https://www.elastic.co/guide/en/logstash/current/input-plugins.html)

### Filter

This is the middle stage of Logstash, where the actual processing of events take place. A developer can use pre-defined
Regex Patterns by Logstash to create sequences for differentiating between the fields in the events and criteria for
accepted input events.

Logstash offers various plugins to help the developer to parse and transform the events into a desirable structure. Some
of the most commonly used filter plugins are – Grok, Mutate, Drop, Clone and Geoip.

[Available Filter Plugins](https://www.elastic.co/guide/en/logstash/current/filter-plugins.html)


### Output

This is the last stage in the Logstash pipeline, where the output events can be formatted into the structure required by
the destination systems. Lastly, it sends the output event after complete processing to the destination by using
plugins. Some of the most commonly used plugins are – Elasticsearch, File, Graphite, Statsd, etc.

[Available Output Plugins](https://www.elastic.co/guide/en/logstash/current/output-plugins.html)

------
Continued on Next Page
------

[Next](configure_logstash.md)


----

[Home](../README.md)