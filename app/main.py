# app/main.py
from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/")
def root():
    return {
        "engine": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "secured-and-operational"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "fail_closed_mode": "active"}
