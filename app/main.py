from fastapi import FastAPI
from database import test_db
from redis_client import test_redis
from logger import logger

app = FastAPI()

# @app.get("/")
# def root():
#     return {
#         "message": "Assignment API Running"
#     }

@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": "Assignment API Running"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
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