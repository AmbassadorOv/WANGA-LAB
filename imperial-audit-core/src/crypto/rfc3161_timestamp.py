"""RFC 3161 verification boundary; no fabricated success."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class TimestampVerification:
    status: str
    tsa_url: str | None
    reason: str | None = None


def verify_rfc3161_token(token: bytes | None, *, tsa_url: str | None = None) -> TimestampVerification:
    if not token:
        return TimestampVerification("UNKNOWN", tsa_url, "TIMESTAMP_TOKEN_MISSING")
    return TimestampVerification("UNKNOWN", tsa_url, "RFC3161_TOKEN_PARSER_NOT_CONFIGURED")
