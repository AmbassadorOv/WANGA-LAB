"""
Provenance & Artifact Cryptographic Signing Component
"""

import json
import hashlib
import time
from typing import Dict, Any, Optional, Tuple
from cryptography.hazmat.primitives.asymmetric import ed25519


class ProvenanceManager:
    """
    Manages SHA-256 state serialization, Ed25519 cryptographic signing, checkpointing, and artifact provenance generation.
    """

    def __init__(self, private_key_hex: Optional[str] = None):
        if private_key_hex:
            self.private_key = ed25519.Ed25519PrivateKey.from_private_bytes(bytes.fromhex(private_key_hex))
        else:
            self.private_key = ed25519.Ed25519PrivateKey.generate()
        self.public_key = self.private_key.public_key()

    def serialize_and_hash(self, obj: Any) -> Tuple[str, str]:
        canonical_str = json.dumps(obj, sort_keys=True)
        sha256_hash = hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()
        return canonical_str, sha256_hash

    def sign_hash(self, hash_hex: str) -> str:
        signature = self.private_key.sign(hash_hex.encode("utf-8"))
        return signature.hex()

    def verify_signature(self, hash_hex: str, signature_hex: str) -> bool:
        try:
            self.public_key.verify(bytes.fromhex(signature_hex), hash_hex.encode("utf-8"))
            return True
        except Exception:
            return False

    def create_artifact(
        self,
        architecture_id: str,
        version: str,
        experiment_id: str,
        compiler_version: str,
        source_commit: str,
        result: Dict[str, Any],
        metrics: Dict[str, Any],
        checkpoint_hash: str
    ) -> Dict[str, Any]:
        artifact_data = {
            "architecture_id": architecture_id,
            "version": version,
            "experiment_id": experiment_id,
            "compiler_version": compiler_version,
            "source_commit": source_commit,
            "result": result,
            "metrics": metrics,
            "checkpoint_hash": checkpoint_hash,
            "timestamp": time.time()
        }

        canonical_str, artifact_sha256 = self.serialize_and_hash(artifact_data)
        signature = self.sign_hash(artifact_sha256)

        artifact_data["artifact_sha256"] = artifact_sha256
        artifact_data["signature"] = signature
        return artifact_data
