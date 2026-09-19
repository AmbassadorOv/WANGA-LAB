from tools.insurer_intake import load_records, triage

def base_record(case_ref="CASE-001"):
    return {"case_ref":case_ref,"business_domain":"banking-exposure","system_model":"synthetic-model",
            "claimed_or_observed_drift":"behavior changed","requested_deliverable":"forensic triage",
            "evidence":{"baseline":"b","outputs":"o","provenance":"p"}}

def test_ready_for_replay():
    assert triage(base_record()).status == "READY_FOR_REPLAY"

def test_missing_evidence_is_blocked():
    r = base_record(); r["evidence"] = {"baseline":"b"}
    result = triage(r)
    assert result.status == "NEEDS_EVIDENCE"
    assert set(result.missing) == {"outputs","provenance"}

def test_client_access_gate():
    r = base_record(); r["client_access_required"] = True
    assert triage(r).status == "PENDING_CLIENT_ACCESS"

def test_out_of_scope_gate():
    r = base_record(); r["out_of_scope"] = True
    assert triage(r).status == "OUT_OF_SCOPE"

def test_concurrency_is_controlled():
    records = [base_record(f"CASE-{i:03d}") for i in range(10)]
    results = load_records(records, active_limit=2)
    assert [r["status"] for r in results[:2]] == ["READY_FOR_REPLAY"] * 2
    assert all(r["status"] == "QUEUED_FOR_REPLAY" for r in results[2:])
