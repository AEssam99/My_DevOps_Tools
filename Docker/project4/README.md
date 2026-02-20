# Project 4 – Flask + PostgreSQL + Nginx (Docker Compose)

This project is a simple multi-container application built using Docker Compose.  
It includes:

- PostgreSQL database
- Flask API backend
- Nginx reverse proxy

---

## 📁 Project Structure
```java
project4/
├── db/
├── flask/
│ ├── app.py
│ ├── config.py
│ ├── Dockerfile
│ └── requirements.txt
├── nginx/
│ ├── default.config
│ └── Dockerfile
├── .env
└── docker-compose.yml
```

## ⚙️ Environment Variables

Create a `.env` file in the root directory:
```yaml
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
```

These variables are used by both the PostgreSQL and Flask containers.

---

## 🐳 Build & Run the Application

From inside the `project4` directory:

```bash
docker compose up -d --build
```
To check running containers:

```bash
docker ps
```
## Access the Application
Nginx is exposed on port 3003.

Open in your browser:

```arduino
http://localhost:3003
```
## Available Endpoints
### Home Endpoint
```sql
GET /
```
Response:

```json
{"message": "Hello from Flask API!"}
```
## Database Test Endpoint
```bash
GET /api/testdb
```
Returns PostgreSQL connection status and version.

## Users Endpoint
```bash
GET /api/users
```
- Creates a table users if it does not exist

- Inserts a user named "Ahmed"

- Returns all rows from the table

## Database
- PostgreSQL version: 15

- Persistent storage is mounted from:

```bash
./db:/var/lib/postgresql/data
```
## Stop the Application
```bash
docker compose down
```
To remove volumes as well:

```bash
docker compose down -v
```
## Technologies Used
- Python 3.10

- Flask

- psycopg2

- PostgreSQL 15

- Nginx

- Docker

- Docker Compose


