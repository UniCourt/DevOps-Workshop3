# Creating an App

1. **Create the Application:**
    - We will start by creating a simple Flask web application "FindMyIP" that displays your IP address as well as the
      time you visited the application. This application will
      serve as the source of our log data.

2. **Host with Nginx:**
    - Next, we will host the Flask application using Nginx as a reverse proxy. This step ensures that Nginx serves our
      web application to clients.


3. **JSON Logs in Nginx:**
    - To make log processing easier, we will configure Nginx to output logs in JSON format. This format will make it
      simpler for Logstash to parse and process the logs.

### Docker Compose

To bring up the application, change directory to `application` and run the docker-compose

```shell
cd ./application

docker compose up -d 
```

The application will be available at http://localhost

Now, lets visit the webpage and then check the logs. To check the logs open the access.log file 
```sh
cd ./application/nginx/logs 
cat access.log
cat error.log 
```

---

### A Quick Note on Nginx 


Nginx is a high-performance, open-source web server and reverse proxy server. At its core, it's designed to efficiently
serve web pages and content to users, but it goes beyond that. Nginx can handle multiple tasks simultaneously, making it
a versatile tool in modern web architectures. 

It's often used as a reverse proxy, meaning it sits between clients (like
web browsers) and web servers, forwarding client requests to the appropriate server and sending the server's responses
back to clients. 

This allows for load balancing, caching, and even serving as a front-end for microservices. Nginx's
flexibility, speed, and extensive community support make it a popular choice for improving web server performance,
security, and scalability.

To learn more about how we configured the nginx for the workshop, refer:

1. Nginx minimal configurations: https://www.netnea.com/cms/nginx-tutorial-2_minimal-nginx-configuration/
2. Nginx log formatting: https://docs.nginx.com/nginx/admin-guide/monitoring/logging/
3. Complete nginx configuration reference: https://www.nginx.com/resources/wiki/start/topics/examples/full/

----

[Home](../README.md)