"""Bitcoin/OpenTimestamps anchoring boundary.

Anchoring a digest proves that an anchoring record exists; it does not
prove the truth of the underlying financial claims.
"""

from __future__ import annotations

def create_ots_submission(digest_hex: str) -> dict[str, str]:
    if len(digest_hex) != 64:
        raise ValueError("Expected SHA-256 digest")
    int(digest_hex, 16)
    return {"digest": digest_hex, "status": "PENDING_EXTERNAL_ANCHOR"}
