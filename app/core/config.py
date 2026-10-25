# app/core/config.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "EliteAxis Global Engine"
    VERSION: str = "4.1.5-hardened"
    API_V1_STR: str = "/api/v1"
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    VAULT_ENCRYPTION_KEY: str = os.getenv("VAULT_ENCRYPTION_KEY", "")

    def validate_secrets(self):
        if not self.SECRET_KEY or len(self.SECRET_KEY) < 32:
            raise ValueError("CRITICAL: SECRET_KEY is missing or insecure (< 32 chars). Fail-closed triggered.")
        if not self.VAULT_ENCRYPTION_KEY or len(self.VAULT_ENCRYPTION_KEY) < 32:
            raise ValueError("CRITICAL: VAULT_ENCRYPTION_KEY is missing or insecure (< 32 chars). Fail-closed triggered.")
        if self.SECRET_KEY == self.VAULT_ENCRYPTION_KEY:
            raise ValueError("CRITICAL: SECRET_KEY and VAULT_ENCRYPTION_KEY must be distinct.")

settings = Settings()

try:
    settings.validate_secrets()
except Exception as e:
    print(f"[SECURITY ERROR] {e}")
