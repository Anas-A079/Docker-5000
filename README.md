
# Flask + Redis Dockerized App

A simple containerized Flask application integrated with Redis, orchestrated using Docker Compose.

## Features

- Tracks page visits and last visit timestamp using Redis.
- Displays a random motivational quote on each visit.
- Configurable Redis host and port via environment variables.

## Ports

- Flask app: 3000  
- Redis: 6379 
- Nginx: 3000 

## Docker Compose Services

- `web` (Flask app) depends on `redis`.  
- `redis` stores persistent data in a Docker volume.

## Requirements

- Docker  
- Docker Compose  

## Docker & Docker Compose Commands

- Build image: `docker build -t flask-redis-app .`  
- Build with Compose: `docker compose build`  
- Start containers: `docker compose up -d`  
- Stop containers: `docker compose down`  
- Remove containers, networks, images, volumes: `docker compose down --rmi all -v`  
- View logs: `docker compose logs -f`  
- Enter container: `docker exec -it <container_name> bash`

## Access the App

Open your browser at: [http://localhost:3000](http://localhost:3000)
</pre>
