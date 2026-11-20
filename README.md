# FastAPI Docker Deployment

A containerized FastAPI REST API demonstrating Docker-based application deployment and DevOps fundamentals.

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Docker
- Git and GitHub

## Features
- REST API with a health-check endpoint
- Docker containerization
- Port mapping for local access
- Git version control

## Run with Docker

```bash
docker build -t fastapi-devops:v1 .
docker run -d --name fastapi-container -p 8000:8000 fastapi-devops:v1
```

## Test the API

Health check: http://localhost:8000/health

API documentation: http://localhost:8000/docs

Expected health response:

```json
{"status":"healthy"}
```

## CI/CD
GitHub Actions workflow integration is planned.

## Author
Sherafgan Zafar