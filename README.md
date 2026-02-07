# Emergency Shelter Allocation System

## Getting started

```
https://github.com/Mongko1/MVC-2-2025.git
cd MVC-2-2025
```

## Prerequisite
Make sure you have:

- Docker

- Docker Compose

## Running with Docker Compose (Recommend for local development)
### 1. Build and start all services
```
docker compose up --build
```
this will start:
- Backend (FastAPI)
- Database (PostgreSQL)

### 2. Stop all services
```
docker compose down
```

## Access the API
API Docs:
```
http://localhost:8000/docs
```

## Access the Database
You can connect to the PostgreSQL database using any database client
(e.g., DBeaver, pgAdmin, etc.).

### 1. Make sure containers are running
```bash
docker compose up
```

### 2. Use the following connection settings
- Host: `localhost`
- Port: `5432`
- Database: `mvc-db`
- Username: `postgres`
- Password: `postgres`
- SSL: Disabled (default for local Docker setup)
