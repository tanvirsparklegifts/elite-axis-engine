import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    PROJECT_NAME: str = "EliteAxis Global Engine"
    VERSION: str = "4.1.5-hardened"
    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str = ""
    VAULT_ENCRYPTION_KEY: str = ""

    def validate_secrets(self) -> None:
        if len(self.SECRET_KEY) < 32:
            raise ValueError("SECRET_KEY is missing or insecure (minimum 32 characters).")
        if len(self.VAULT_ENCRYPTION_KEY) < 32:
            raise ValueError("VAULT_ENCRYPTION_KEY is missing or insecure (minimum 32 characters).")
        if self.SECRET_KEY == self.VAULT_ENCRYPTION_KEY:
            raise ValueError("SECRET_KEY and VAULT_ENCRYPTION_KEY must be distinct.")


settings = Settings()
