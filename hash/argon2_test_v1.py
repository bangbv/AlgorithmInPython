# argon2_example.py
import base64
import secrets
import hmac
from typing import Tuple

from argon2.low_level import (
    hash_secret_raw,
    Type,
)


# Parameters (the ones you specified)
TIME_COST = 5
MEMORY_KIB = 7168  # Argon2 expects memory in KiB. 7168 KiB = 7 MiB
PARALLELISM = 1
HASH_LEN = 32      # output length in bytes
SALT_LEN = 32      # 32 bytes salt as requested
ARGON2_TYPE = Type.ID


def generate_salt(length: int = SALT_LEN) -> bytes:
    """Create a cryptographically secure random salt."""
    return secrets.token_bytes(length)


def derive_argon2id(
    secret: bytes,
    salt: bytes,
    time_cost: int = TIME_COST,
    memory_kib: int = MEMORY_KIB,
    parallelism: int = PARALLELISM,
    hash_len: int = HASH_LEN,
    argon2_type: Type = ARGON2_TYPE,
) -> bytes:
    """
    Derive raw hash bytes using Argon2id (low-level).
    Returns raw bytes (not encoded).
    """
    return hash_secret_raw(
        secret=secret,
        salt=salt,
        time_cost=time_cost,
        memory_cost=memory_kib,
        parallelism=parallelism,
        hash_len=hash_len,
        type=argon2_type,
    )


def encode_b64(data: bytes) -> str:
    """URL-safe base64 (no padding problems when transporting)."""
    return base64.urlsafe_b64encode(data).decode("ascii")


def decode_b64(s: str) -> bytes:
    return base64.urlsafe_b64decode(s.encode("ascii"))


def create_hash_for_secret(secret_str: str) -> Tuple[str, str]:
    """
    Given a secret (password-like string), generate salt and Argon2id hash.
    Returns (b64_salt, b64_hash).
    """
    salt = generate_salt()
    secret = secret_str.encode("utf-8")
    raw_hash = derive_argon2id(secret=secret, salt=salt)
    return encode_b64(salt), encode_b64(raw_hash)


def verify_secret_with_salt(secret_str: str, b64_salt: str, b64_expected_hash: str) -> bool:
    """
    Verify secret against stored salt and expected hash (both base64-encoded).
    Uses constant-time compare.
    """
    salt = decode_b64(b64_salt)
    expected = decode_b64(b64_expected_hash)
    candidate = derive_argon2id(secret=secret_str.encode("utf-8"), salt=salt)
    # constant-time compare
    return hmac.compare_digest(candidate, expected)


# --- Example usage ---
if __name__ == "__main__":
    pw = "S3cr3tPasswordOrMessage"
    print("Creating salt + hash for secret...")

    b64_salt, b64_hash = create_hash_for_secret(pw)
    print("salt (base64):", b64_salt)
    print("hash (base64):", b64_hash)
    print()

    print("Verifying (correct):", verify_secret_with_salt(pw, b64_salt, b64_hash))
    print("Verifying (wrong):  ", verify_secret_with_salt("wrong", b64_salt, b64_hash))
