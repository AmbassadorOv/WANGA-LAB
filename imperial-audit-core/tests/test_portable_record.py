import json

from src.evidence.portable_record import build_ier_manifest


def test_ier_manifest_is_platform_neutral(tmp_path):
    (tmp_path / "audit_output.json").write_text(
        json.dumps(
            {
                "pack_id": "TEST-1",
                "audit_data": {"S1": "a", "S2": "b", "S3": "c"},
                "cryptographic_integrity": {
                    "hashes": {"MASTER_CHAIN_HASH": "abc123"}
                },
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "source.txt").write_text("hello", encoding="utf-8")

    manifest = build_ier_manifest(tmp_path)

    assert manifest["format"] == "IMPERIAL-EVIDENCE-RECORD"
    assert manifest["format_version"] == "1.0"
    assert manifest["platform_dependencies"] == []
    assert manifest["master_hash"] == "abc123"
    assert manifest["files"]["source.txt"]
