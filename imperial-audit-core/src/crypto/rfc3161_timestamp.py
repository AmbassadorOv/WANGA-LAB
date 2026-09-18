"""RFC 3161 integration boundary.

A real RFC 3161 implementation must construct a standards-compliant
TimeStampReq (ASN.1/DER) and validate the returned TimeStampResp.
This module intentionally does not treat an arbitrary HTTP response as a
valid timestamp token.
"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class TimestampResult:
    token: bytes
    tsa_url: str

def require_rfc3161_token(token: bytes) -> TimestampResult:
    if not token:
        raise ValueError("Empty timestamp token")
    raise NotImplementedError(
        "RFC 3161 ASN.1 request/response validation must be implemented "
        "with a standards-compliant TSP library before production use."
    )
