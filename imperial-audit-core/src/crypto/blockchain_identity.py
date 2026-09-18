"""Blockchain identity metadata for Imperial Audit.

This module never generates, stores, or exposes a private key. The signing
authority remains external (hardware wallet, controlled signer, or other
approved custody system). Imperial Audit records the public identity and
verifies signatures/proofs supplied to it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BlockchainIdentity:
    network: str
    address: str
    purpose: str = "evidence-approval"

    def to_dict(self) -> dict[str, Any]:
        return {
            "network": self.network,
            "address": self.address,
            "purpose": self.purpose,
            "private_key": None,
            "custody": "external-signer",
        }


def approval_payload(master_hash: str) -> bytes:
    """Return the exact bytes that an external signer should approve."""
    if not master_hash or len(master_hash) != 64:
        raise ValueError("master_hash must be a 64-character SHA-256 hex value")
    try:
        bytes.fromhex(master_hash)
    except ValueError as exc:
        raise ValueError("master_hash must be hexadecimal") from exc
    return ("IMPERIAL-AUDIT/APPROVAL/1\nMASTER_HASH=" + master_hash + "\n").encode("utf-8")
