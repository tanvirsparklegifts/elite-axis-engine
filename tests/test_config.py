import pytest

from app.core.config import Settings


VALID_SECRET = "a-valid-secret-value-with-more-than-32-chars"
OTHER_SECRET = "a-different-vault-secret-with-more-than-32"


def test_valid_distinct_secrets_are_accepted():
    settings = Settings(SECRET_KEY=VALID_SECRET, VAULT_ENCRYPTION_KEY=OTHER_SECRET)

    settings.validate_secrets()


@pytest.mark.parametrize(
    ("secret_key", "vault_key", "message"),
    [
        ("short", OTHER_SECRET, "SECRET_KEY"),
        (VALID_SECRET, "short", "VAULT_ENCRYPTION_KEY"),
        (VALID_SECRET, VALID_SECRET, "must be distinct"),
    ],
)
def test_invalid_secrets_are_rejected(secret_key, vault_key, message):
    settings = Settings(SECRET_KEY=secret_key, VAULT_ENCRYPTION_KEY=vault_key)

    with pytest.raises(ValueError, match=message):
        settings.validate_secrets()
