# Project 3 – Flask + PostgreSQL (Docker Compose)
## Overview

This project demonstrates a multi-container Docker application using:

- Flask as a backend API

- PostgreSQL as a database

- Docker Compose for orchestration

- The Flask application connects to a PostgreSQL database using environment variables and performs basic database operations.

This project demonstrates:

- Flask database integration

- PostgreSQL container setup

- Environment variable configuration

- Docker Compose networking

- Persistent database storage using volumes

## Architecture
```java
Client (Browser)
        ↓
Flask Application (Port 5000)
        ↓
PostgreSQL Database (Port 5432 - internal)
```

Docker Compose creates a shared internal network where:

- Flask connects to PostgreSQL using the service name db

- No manual IP configuration is required

## Project Structure
```java
project3/
│
├── docker-compose.yml
│
├── flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── db/   (auto-created volume directory)
```
## Flask Application
### app.py

- Connects to PostgreSQL using environment variables

- Creates a table if it does not exist

- Inserts sample data

- Returns database records as JSON

### Available Routes
Route	     Description
/	         Health check endpoint
/users	   Creates table, inserts data, and returns all users

Example response:
```nginx
http://localhost:5000/users
```

Returns:
```bash
[
  [1, "Ahmed"]
]
```
### Flask Dockerfile
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
### Requirements
```php
flask
psycopg2-binary
```
## Docker Compose Configuration
```yaml
services:
  flask:
    build: ./flask
    container_name: flask
    ports:
      - "5000:5000"
    environment:
      POSTGRES_HOST: db
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    depends_on:
      - db

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - ./db:/var/lib/postgresql/data
```
### Environment Variables

Create a .env file in the project root:
```php
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```
## Prerequisites

- Docker

- Docker Compose

## Verify installation:
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

Health check:
```nginx
http://localhost:5000/
```

Database test endpoint:
```nginx
http://localhost:5000/users
```
## Useful Commands

Stop containers:
```bash
docker compose down
```

Stop and remove volumes:
```bash
docker compose down -v
```

View logs:
```bash
docker compose logs
```

List running containers:
```bash
docker ps
```
## Persistence

PostgreSQL data is stored in:
```bash
./db
```

This ensures database data persists even if containers are removed.

## Networking Explanation

- Docker Compose automatically creates a bridge network.

- Flask connects to the database using the service name db.

- No hardcoded IP addresses are used.

- Database port 5432 is internal and not exposed to host.

## Learning Outcomes

- This project demonstrates:

- Connecting Flask to PostgreSQL

- Using environment variables securely

- Multi-container application design

- Database persistence with volumes

- Docker Compose orchestration

- Production Considerations

## For production environments:

- Use Gunicorn instead of Flask development server

- Do not expose database credentials in plain text

- Use secrets management

- Add health checks

- Use named Docker volumes instead of bind mounts

## Author

Ahmed Essam

DevOps & SysAdmin Projects
