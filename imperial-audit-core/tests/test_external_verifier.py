from imperial_audit_core.src.core.audit_generator import generate_audit
from imperial_audit_core.src.verification.independent_verifier import verify_audit


def test_generator_is_deterministic_for_same_explicit_capture_time():
    args = ({"a": 1}, {"b": 2}, {"c": 3})
    a = generate_audit(*args, captured_at="2026-09-18T00:00:00Z")
    b = generate_audit(*args, captured_at="2026-09-18T00:00:00Z")
    assert a == b


def test_unknown_without_external_evidence():
    audit = generate_audit({"a": 1}, {"b": 2}, {"c": 3}, captured_at="2026-09-18T00:00:00Z")
    assert verify_audit(audit, external_timestamp_verified=None, external_anchor_verified=None)["status"] == "UNKNOWN"


def test_mutation_fails_integrity():
    audit = generate_audit({"a": 1}, {"b": 2}, {"c": 3}, captured_at="2026-09-18T00:00:00Z")
    audit["S3"]["c"] = 4
    assert verify_audit(audit, external_timestamp_verified=True, external_anchor_verified=True)["status"] == "FAIL"


def test_pass_requires_both_external_evidence_flags():
    audit = generate_audit({"a": 1}, {"b": 2}, {"c": 3}, captured_at="2026-09-18T00:00:00Z")
    assert verify_audit(audit, external_timestamp_verified=True, external_anchor_verified=True)["status"] == "PASS"
