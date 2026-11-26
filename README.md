# EliteAxis Global Engine

**Python / FastAPI backend foundation for the EliteAxis digital product ecosystem**

[![Python CI](https://github.com/tanvirsparklegifts/elite-axis-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tanvirsparklegifts/elite-axis-engine/actions/workflows/ci.yml)

An in-development backend baseline for exploring modular API design, configuration boundaries, and testable service foundations. This repository is a learning and portfolio project—not a production financial platform.

## Implemented today

- FastAPI application entry point in `app/main.py`.
- Environment-backed settings using Pydantic Settings.
- Fail-closed startup validation for distinct signing and vault-encryption secrets.
- Root metadata and application-level health endpoints.
- API smoke tests for the root endpoint, health endpoint, and generated OpenAPI schema.

## Technology

- Python 3.11+
- FastAPI
- Pydantic Settings
- pytest and HTTPX for tests
- GitHub Actions for continuous integration

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest httpx
```

Set two different secrets (each at least 32 characters) before starting the app:

```bash
export SECRET_KEY='replace-with-a-long-random-signing-secret'
export VAULT_ENCRYPTION_KEY='replace-with-a-different-long-random-vault-secret'
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the OpenAPI interface.

Run tests:

```bash
pytest -q
```

Tests use test-only secrets injected by the fixture. Never reuse those values outside the test suite.

See [docs/architecture.md](docs/architecture.md) for the current component boundary, configuration flow, limitations, and engineering milestones.

## Configuration and security

- Do not commit secrets, production credentials, signing keys, or customer data.
- Use a secrets manager or protected environment variables for deployments.
- Keep `SECRET_KEY` and `VAULT_ENCRYPTION_KEY` distinct.
- The current `/health` endpoint reports application process health only; it does not check databases, queues, payment providers, or other dependencies.

## Project status and roadmap

**Status: early development.** Before production use, this project needs authentication and authorization implementation with negative-path tests, database migrations, dependency health checks, observability, rate limiting, threat modelling, deployment hardening, and independent security review.

No payment processing, custody, banking, or regulated financial capability is currently claimed.

## Engineering workflow

GitHub Actions runs the test suite on pushes and pull requests. Changes should include focused tests and documentation describing observable behavior.
