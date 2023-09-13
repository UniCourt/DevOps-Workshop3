# Kibana

Now that we've set up the ELK Stack and configured Logstash, it's time to view and explore your data using Kibana, the K in ELK. Follow the steps below to get started.

### Accessing Kibana

1. Ensure that your ELK Stack services (Elasticsearch, Logstash, and Kibana) are up and running. If not, refer to the previous steps in the workshop.

2. Open a web browser and navigate to Kibana at `http://localhost:5601`. You should see the Kibana home page.

### Viewing Data

Now that you're in Kibana, let's explore your data:

1. **Create an Index Pattern**:
   - Click on "Management" in the left sidebar.
   - Under "Kibana," click on "Index Patterns."
   - Click "Create index pattern."
   - In the "Index pattern" field, enter `nginx-access-logs-*` (or the pattern that matches your data).
   - Follow the steps in the wizard to configure your index pattern.

2. **Discover and View Data**:
   - Click on "Discover" in the left sidebar.
   - Select the newly created index pattern (e.g., `nginx-access-logs-*`) from the top menu.
   - You'll now see your log data in the Discover view.

3. **Use Date Filter**:
   - Kibana provides a date filter to narrow down your data by date and time.
   - In the top right corner, you'll find the date filter. You can specify a time range to focus on specific log entries.

4. **Use Fields**:
   - To view specific fields in your log data, check the list of available fields on the left sidebar.
   - You can click on a field to add it to your Discover view and explore data using those fields.


---
## Lets create a dashboard

Lets now create a dashboard to show the count of 5xx, 4xx, and 2xx responses our application.

### Steps to Create the Dashboard

1. **Create Visualizations**:
   - Access Kibana by navigating to `http://localhost:5601` in your web browser.

   - Click on "Visualize" in the left sidebar.

   - Choose "Create a visualization."

2. **Create a Pie Chart Visualization for HTTP Status Codes**:
   - Select the "Pie chart" visualization type.

   - In the data source section, select your index pattern (e.g., `nginx-access-logs-*`).

   - In the "Buckets" section:
     - Choose "Split slices" as the aggregation.
     - Select "Terms" as the aggregation type.
     - Choose the field that represents the HTTP status code (e.g., `http_status_code.keyword`).
     - Optionally, you can limit the number of slices shown in the chart.

   - Click the "Apply changes" button.

3. **Create Filters for Each Status Code**:
   - To create visualizations for specific HTTP status code categories (5xx, 4xx, 2xx), apply filters.

   - In the upper right corner of the visualization, click on "Add a filter."

   - Create filters for each status code category:
     - For 5xx, set a filter for `http_status_code.keyword` with a value of `5xx`.
     - For 4xx, set a filter for `http_status_code.keyword` with a value of `4xx`.
     - For 2xx, set a filter for `http_status_code.keyword` with a value of `2xx`.

4. **Save the Visualizations**:
   - Once you have created visualizations for each status code category, save them with meaningful names (e.g., "5xx Responses," "4xx Responses," "2xx Responses").

5. **Create a Dashboard**:
   - Click on "Dashboard" in the left sidebar.

   - Choose "Create a dashboard."

   - In the dashboard view, click on "Add" to add visualizations.

   - Select the visualizations you created for 5xx, 4xx, and 2xx responses and add them to the dashboard.

6. **Arrange Visualizations**:
   - You can arrange the visualizations on the dashboard as desired. Click and drag to move them and resize as needed.

7. **Save and View the Dashboard**:
   - Save the dashboard with a meaningful name (e.g., "HTTP Status Codes").

   - You can now view the dashboard with counts of 5xx, 4xx, and 2xx responses from your Nginx logs.



---
### Further Learning

Kibana offers numerous features and capabilities for data analysis and visualization. To learn more, explore the official Kibana documentation:

- [Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)


----

[Home](../README.md)