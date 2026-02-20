# Project 1 – Nginx Static Website (Docker)
## Overview

This project demonstrates how to build a custom Docker image based on the official Nginx image to serve a static HTML webpage.

It showcases:

- Creating a Docker image using a Dockerfile

- Installing additional packages inside a container

- Copying static website files into the container

- Running a container with port mapping

This project is intended for learning and DevOps practice purposes.

## Project Structure
```pgsql
project1/
├── Dockerfile
└── index.html
```
## Dockerfile Used
```Dockerfile
FROM nginx
RUN apt-get update && apt-get install -y vim iputils-ping \
    && rm -rf /var/lib/apt/lists/*
COPY . /usr/share/nginx/html/
MAINTAINER Ahmed Essam
EXPOSE 3001:80
```
## How It Works

- Uses the official nginx image as the base image.

- Installs additional tools (vim and iputils-ping).

- Copies the project files into Nginx’s default web directory:

/usr/share/nginx/html/

- Nginx serves the index.html file as a static website.

## Build the Docker Image

Navigate to the project directory:
```bash
cd project1
```

Build the image:
```bash
docker build -t project1-nginx .
```
## Run the Container
```bash
docker run -d -p 3001:80 --name project1-container project1-nginx
```

Explanation:

-d → Run container in detached mode

-p 3001:80 → Map host port 3001 to container port 80

--name → Assign a custom container name

## Access the Website

Open your browser and go to:
```arduino
http://localhost:3001
```

You should see the content of index.html.

## Useful Docker Commands

List running containers:
```bash
docker ps
```

View logs:
```bash
docker logs project1-container
```

Stop container:
```bash
docker stop project1-container
```

Remove container:
```bash
docker rm project1-container
```

Remove image:
```bash
docker rmi project1-nginx
```
## Notes

This project is for demonstration and learning purposes.

Port exposure is handled during container runtime using -p.

## Author

Ahmed Essam
DevOps & System Administration Projects
