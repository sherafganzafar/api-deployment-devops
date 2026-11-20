
from fastapi import FastAPI

app = FastAPI(title="DevOps API Deployment Project")

@app.get("/")
def home():
    return {
        "message": "Welcome to my DevOps API!",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/info")
def api_info():
    return {
        "project": "API Deployment on Heroku and Linux VM",
        "framework": "FastAPI",
        "developer": "Sherafgan Zafar"
    }
