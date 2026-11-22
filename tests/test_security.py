from datetime import timedelta

import pytest
from jose import jwt
from jose.exceptions import ExpiredSignatureError

from app.core import security


def test_password_hash_round_trip():
    password = "correct-horse-battery-staple"
    hashed = security.get_password_hash(password)

    assert hashed != password
    assert security.verify_password(password, hashed)
    assert not security.verify_password("wrong-password", hashed)


def test_access_token_contains_subject_and_expiry(monkeypatch):
    secret = "test-secret-key-with-at-least-32-characters"
    monkeypatch.setattr(security.settings, "SECRET_KEY", secret)

    token = security.create_access_token("architect-user")
    payload = jwt.decode(token, secret, algorithms=[security.ALGORITHM])

    assert payload["sub"] == "architect-user"
    assert "exp" in payload


def test_access_token_rejects_short_secret(monkeypatch):
    monkeypatch.setattr(security.settings, "SECRET_KEY", "too-short")

    with pytest.raises(ValueError, match="SECRET_KEY"):
        security.create_access_token("architect-user")


def test_access_token_expiry_is_enforced(monkeypatch):
    secret = "test-secret-key-with-at-least-32-characters"
    monkeypatch.setattr(security.settings, "SECRET_KEY", secret)

    token = security.create_access_token(
        "architect-user",
        expires_delta=timedelta(seconds=-1),
    )

    with pytest.raises(ExpiredSignatureError):
        jwt.decode(token, secret, algorithms=[security.ALGORITHM])
