import json
from pathlib import Path

from src.crypto.sha256_chain import build_chain
from src.evidence.offline_court import OfflineEvidenceCourt


def make_pack(tmp_path: Path, tamper: bool = False) -> Path:
    s1 = {"exposure": "100"}
    s2 = {"correction": "0.25"}
    s3 = {"recovery": "iron"}
    timestamp = "2026-09-18T10:00:00+00:00"
    legal_bytes = b"signed-contract-test"
    legal_hash = __import__("hashlib").sha256(legal_bytes).hexdigest()
    chain = build_chain(s1, s2, s3, timestamp, legal_hash)

    if tamper:
        s3 = {"recovery": "tampered"}

    pack = tmp_path / "pack"
    pack.mkdir()
    (pack / "legal_contract.bin").write_bytes(legal_bytes)
    (pack / "audit_output.json").write_text(
        json.dumps(
            {
                "pack_id": "test-pack",
                "audit_data": {"S1": s1, "S2": s2, "S3": s3},
                "cryptographic_integrity": {
                    "hashes": chain,
                    "native_blockchain_anchors": {
                        "bitcoin": {
                            "master_hash": chain["MASTER_CHAIN_HASH"],
                            "verification_status": "UNVERIFIED",
                        },
                        "ethereum": {
                            "master_hash": chain["MASTER_CHAIN_HASH"],
                            "verification_status": "UNVERIFIED",
                        },
                    },
                },
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return pack


def test_portable_pack_verifies_local_integrity(tmp_path: Path):
    report = OfflineEvidenceCourt(make_pack(tmp_path)).verify()
    assert report.overall_status == "PARTIAL"
    assert any(item.code == "LOCAL_CHAIN" and item.status == "PASS" for item in report.findings)
    assert any(item.code == "CONTRACT_HASH" and item.status == "PASS" for item in report.findings)


def test_tampered_payload_fails(tmp_path: Path):
    report = OfflineEvidenceCourt(make_pack(tmp_path, tamper=True)).verify()
    assert report.overall_status == "FAIL"
    assert any(item.code == "LOCAL_CHAIN" and item.status == "FAIL" for item in report.findings)
