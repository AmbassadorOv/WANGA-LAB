"""Deterministic offline evidence verification.

This module is deliberately an evidence verifier, not a legal decision maker.
It can establish cryptographic relationships contained in a portable evidence
pack without trusting the original application server.

A blockchain anchor is treated as independently verifiable only when the pack
contains enough chain-specific proof material and an adapter has actually
verified it. A txid, block number, or explorer URL alone is only a claim.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

from ..crypto.sha256_chain import build_chain


@dataclass(frozen=True)
class Finding:
    code: str
    status: str
    detail: str


@dataclass(frozen=True)
class VerificationReport:
    pack_id: str
    master_hash: str | None
    overall_status: str
    findings: list[Finding]

    def to_dict(self) -> dict[str, Any]:
        return {
            "pack_id": self.pack_id,
            "master_hash": self.master_hash,
            "overall_status": self.overall_status,
            "findings": [asdict(item) for item in self.findings],
        }


class OfflineEvidenceCourt:
    """Verify a portable evidence pack using local files only."""

    def __init__(self, pack_dir: str | Path):
        self.pack_dir = Path(pack_dir)

    def _read_json(self, name: str) -> dict[str, Any]:
        path = self.pack_dir / name
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
        if not isinstance(value, dict):
            raise ValueError(f"{name} must contain a JSON object")
        return value

    @staticmethod
    def _sha256_file(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def verify(self) -> VerificationReport:
        findings: list[Finding] = []
        audit = self._read_json("audit_output.json")

        pack_id = str(audit.get("pack_id", "UNSPECIFIED"))
        audit_data = audit.get("audit_data", {})
        integrity = audit.get("cryptographic_integrity", {})
        hashes = integrity.get("hashes", {})

        if not isinstance(audit_data, dict) or not isinstance(hashes, dict):
            return VerificationReport(
                pack_id=pack_id,
                master_hash=None,
                overall_status="INVALID_PACKAGE",
                findings=[
                    Finding(
                        "PACKAGE_SHAPE",
                        "FAIL",
                        "audit_data and cryptographic_integrity.hashes are required objects.",
                    )
                ],
            )

        s1 = audit_data.get("S1")
        s2 = audit_data.get("S2")
        s3 = audit_data.get("S3")
        timestamp = hashes.get("TIMESTAMP_UTC", audit.get("timestamp_utc"))
        legal_hash = hashes.get("LEGAL_CONTRACT_HASH", "")

        if not all(key in hashes for key in ("S1", "S2", "S3", "MASTER_CHAIN_HASH")):
            findings.append(
                Finding(
                    "CHAIN_FIELDS",
                    "FAIL",
                    "S1, S2, S3 and MASTER_CHAIN_HASH are required.",
                )
            )
        elif not isinstance(timestamp, str):
            findings.append(
                Finding("TIMESTAMP", "FAIL", "A committed UTC timestamp is required.")
            )
        else:
            expected = build_chain(s1, s2, s3, timestamp, legal_hash)
            if expected == {key: hashes.get(key) for key in expected}:
                findings.append(
                    Finding(
                        "LOCAL_CHAIN",
                        "PASS",
                        "S1/S2/S3, timestamp, contract hash and master hash match locally.",
                    )
                )
            else:
                findings.append(
                    Finding(
                        "LOCAL_CHAIN",
                        "FAIL",
                        "The local payload does not reproduce the recorded master chain.",
                    )
                )

        master_hash = hashes.get("MASTER_CHAIN_HASH")

        contract_path = self.pack_dir / "legal_contract.bin"
        if legal_hash:
            if contract_path.exists():
                actual = self._sha256_file(contract_path)
                findings.append(
                    Finding(
                        "CONTRACT_HASH",
                        "PASS" if actual == legal_hash else "FAIL",
                        "The local contract bytes match LEGAL_CONTRACT_HASH."
                        if actual == legal_hash
                        else "The local contract bytes do not match LEGAL_CONTRACT_HASH.",
                    )
                )
            else:
                findings.append(
                    Finding(
                        "CONTRACT_HASH",
                        "UNVERIFIED",
                        "LEGAL_CONTRACT_HASH is recorded but legal_contract.bin is absent.",
                    )
                )

        anchors = integrity.get("native_blockchain_anchors", {})
        if not isinstance(anchors, dict):
            anchors = {}

        for chain_name in ("bitcoin", "ethereum"):
            anchor = anchors.get(chain_name)
            if not isinstance(anchor, dict):
                findings.append(
                    Finding(
                        f"{chain_name.upper()}_ANCHOR",
                        "UNVERIFIED",
                        "No chain proof object is present in the portable pack.",
                    )
                )
                continue

            anchored_hash = anchor.get("master_hash")
            proof_status = anchor.get("verification_status", "UNVERIFIED")
            if anchored_hash != master_hash:
                findings.append(
                    Finding(
                        f"{chain_name.upper()}_ANCHOR",
                        "FAIL",
                        "Anchor metadata points to a different master hash.",
                    )
                )
            elif proof_status == "VERIFIED_BY_CHAIN_ADAPTER":
                findings.append(
                    Finding(
                        f"{chain_name.upper()}_ANCHOR",
                        "PASS",
                        "Chain-specific adapter reports independent verification.",
                    )
                )
            else:
                findings.append(
                    Finding(
                        f"{chain_name.upper()}_ANCHOR",
                        "UNVERIFIED",
                        "The anchor payload matches the master hash, but no independent chain proof was verified offline.",
                    )
                )

        if any(item.status == "FAIL" for item in findings):
            overall = "FAIL"
        elif any(item.status == "UNVERIFIED" for item in findings):
            overall = "PARTIAL"
        else:
            overall = "VERIFIED"

        return VerificationReport(
            pack_id=pack_id,
            master_hash=master_hash,
            overall_status=overall,
            findings=findings,
        )
