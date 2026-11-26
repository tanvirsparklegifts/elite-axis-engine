"""API smoke tests for the development FastAPI baseline.

The test fixture supplies isolated test-only secrets because the app intentionally
fails closed at startup when runtime secrets are absent or weak.
"""
import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setattr(settings, "SECRET_KEY", "test-only-signing-secret-32-bytes-min")
    monkeypatch.setattr(settings, "VAULT_ENCRYPTION_KEY", "test-only-vault-secret-32-bytes-long")
    with TestClient(app) as test_client:
        yield test_client


def test_root_endpoint_reports_development_status(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "engine": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "development",
    }


def test_health_endpoint_reports_application_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "mode": "development"}


def test_openapi_schema_is_available(client):
    response = client.get(f"{settings.API_V1_STR}/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"] == settings.PROJECT_NAME
