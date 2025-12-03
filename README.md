# Flask + Redis + MySQL Dockerized Apps

This project contains two containerized Flask applications: one using Redis and one using MySQL, orchestrated with Docker Compose.

---

## 1. Flask + Redis App

**Features:**
- Tracks page visits and last visit timestamp using Redis.
- Displays a random motivational quote on each visit.
- Configurable Redis host and port via environment variables.

**Ports:**
- Flask app: 3000  
- Redis: 6379 (host 6380 optional)  
- Nginx: 3000 (optional reverse proxy)

**Docker Compose Service:**
- `web` (Flask app) depends on `redis`  
- Redis stores persistent data in a Docker volume

**Access:**
- Open in browser: [http://localhost:3000](http://localhost:3000)

---
