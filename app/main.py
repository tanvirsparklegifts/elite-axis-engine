# app/main.py
from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


@app.on_event("startup")
def validate_runtime_secrets() -> None:
    # Fail closed when the application starts; importing modules for tests remains possible.
    settings.validate_secrets()


@app.get("/")
def root():
    return {
        "engine": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "development",
    }


@app.get("/health")
def health_check():
    return {"status": "ok", "mode": "development"}
