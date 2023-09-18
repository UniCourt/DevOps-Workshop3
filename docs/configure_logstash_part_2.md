# Adding more configurations for logstash

We have seen how to parse and visualize logs. Now lets try to parse the error logs along with access logs

1. **Open Your `logstash.conf` File**:
    - Locate and open your `logstash.conf` file using a text editor or code editor.

2. **Add a New Input Section for Error Logs**:
    - To differentiate between access and error logs, we'll use the `type` field. In the `input` section of
      your `logstash.conf`, add the following lines:

   ```
     file {
       path => "/var/log/nginx/error.log"
       start_position => "beginning"
       sincedb_path => "/dev/null"
       type => "error-logs"
     }
   ```

3. **Add Parsing for Error Logs in the Filter Section**:
    - In the `filter` section of your `logstash.conf`, add the following code block for error log parsing:

    ```
     if [type] == "error-logs" {
       grok {
         match => { "message" => "(?<timestamp>%{YEAR}[./]%{MONTHNUM}[./]%{MONTHDAY} %{TIME}) \[%{DATA:[nginx][error][log_level]}\] %{NUMBER:[nginx][error][pid]}#%{NUMBER:[nginx][error][tid]}: %{GREEDYDATA:[nginx][error][message]}" }
       }
     }
   ```
   
   learn more about the grok filter: https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html

4. **Update Output Configuration**:
    - In the `output` section of your `logstash.conf`, ensure that error logs are sent to a separate Elasticsearch
      index:

    ```
     if [type] == "error-logs" {
         elasticsearch {
             hosts => "elasticsearch:9200"
             manage_template => false
             index => "nginx-error-logs-%{+YYYY.MM.dd}"
         }
     }
    ```

5. **Save and Restart Logstash**:
    - Save your `logstash.conf` file and restart the Logstash to apply the changes.

To generate error logs, simply change the path of our web page to `/fail`.
- Go to http://localhost/fail

Create index pattern for nginx-error-logs-* to view the error logs in kibana 

----

[Home](../README.md)
