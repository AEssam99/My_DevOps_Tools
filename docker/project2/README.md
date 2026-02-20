# Project 2 – Flask Backend with Nginx Reverse Proxy (Docker Compose)
## Overview

This project demonstrates a multi-container Docker application using:

- Flask as a backend API service

- Nginx as a reverse proxy

- Docker Compose for orchestration

The Flask application runs on port 5000, and Nginx forwards HTTP requests from port 3002 to the Flask service.

This project demonstrates:

- Multi-container architecture

- Service-to-service communication in Docker

- Reverse proxy configuration

- Docker networking using service names

- Docker Compose orchestration

## Architecture
```java
Client (Browser)
        ↓
localhost:3002
        ↓
Nginx (Port 80)
        ↓
Flask Service (Port 5000)
```

Docker Compose creates an internal network where:

- Nginx connects to Flask using service name: flask

- No manual networking configuration required

## Project Structure
```java
project2/
│
├── docker-compose.yaml
│
├── flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── nginx/
    └── nginx.conf
```
## Flask Application
### app.py
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask backend!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

The application:

- Runs on 0.0.0.0

- Listens on port 5000

- Returns a JSON response

### Flask Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```
## Nginx Configuration
### nginx.conf
```nginx
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://flask:5000;
        }
    }
}

```

Nginx forwards all requests to:
```arduino
http://flask:5000
```

The name flask matches the Docker Compose service name.

## Docker Compose Configuration
```yaml
services:
  flask:
    build: ./flask/
    ports:
      - "5000:5000"
    container_name: flask_cont

  nginx:
    image: my_nginx
    ports:
      - "3002:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    container_name: nginx_cont
    depends_on:
      - flask
```
## Services
Service	Purpose	      Exposed Port
flask	  Backend API	  5000
nginx	  Reverse Proxy	3002
## Prerequisites

- Docker

- Docker Compose

Verify installation:
```bash
docker --version
docker compose version
```
## Build and Run the Application

From inside the project directory:
```bash
docker compose up --build
```

To run in detached mode:
```bash
docker compose up -d --build
```
## Access the Application

Open your browser:
```nginx
http://localhost:3002
```

Expected response:
```json
{
  "message": "Hello from Flask backend!"
}
```
## Useful Commands

Stop containers:
```bash
docker compose down
```

View logs:
```bash
docker compose logs
```

View running containers:
```bash
docker ps
```

Rebuild containers:
```bash
docker compose up --build
```
## Networking Explanation

- Docker Compose automatically creates a bridge network.

- Containers communicate using service names.

- proxy_pass http://flask:5000 works because flask is the service name.

No manual IP configuration required.

## Learning Outcomes

This project demonstrates:

- Building custom Docker images

- Multi-container applications

- Reverse proxy setup

- Container networking

- Docker Compose orchestration

- Backend + proxy separation pattern

## Notes

depends_on ensures Flask starts before Nginx.

For production:

- Use Gunicorn instead of Flask development server.

- Custom my_nginx was deployed from project 1.

- Add health checks.

- Implement logging strategy.

## Author

Ahmed Essam

DevOps Tools & Automation Projects
