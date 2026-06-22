from fastapi import FastAPI
from database import test_db
from redis_client import test_redis
from logger import logger
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Prometheus Metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Assignment API Running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": test_db(),
        "redis": test_redis() == "ok"
    }

@app.get("/db-test")
def db_test():
    return {
        "database_connected": test_db()
    }

@app.get("/redis-test")
def redis_test():
    return {
        "redis_status": test_redis()
    }

@app.get("/ai-health")
def ai_health():
    return {
        "llm_ready": True,
        "provider": "OpenAI Compatible",
        "status": "available"
    }