# Architecture Overview

## Runtime composition

```text
Client
  |
  v
FastAPI application (app/main.py)
  |
  +--> Pydantic Settings (app/core/config.py)
         |
         +--> SECRET_KEY
         +--> VAULT_ENCRYPTION_KEY
```

The current application is intentionally small. It exposes a root metadata route, a process-level health route, and a versioned OpenAPI schema endpoint.

## Configuration boundary

Runtime secrets are loaded from environment variables. Startup validation rejects missing or short secrets and rejects using the same value for signing and vault encryption. Tests inject disposable test-only values; those values are not suitable for deployment.

## Current limitations

- No database or cache integration is implemented in this baseline.
- No payment, custody, banking, or regulated financial workflow is implemented.
- The health endpoint does not perform dependency checks.
- Authentication/authorization behavior is not yet implemented or verified.
- This architecture has not been reviewed for production deployment.

## Next engineering milestones

1. Add authentication and authorization with positive and negative tests.
2. Introduce persistence only with explicit data models and migrations.
3. Add dependency-aware health/readiness checks when external services exist.
4. Add structured logging, request IDs, and metrics.
5. Complete threat modelling and deployment review before any production claim.
