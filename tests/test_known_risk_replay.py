from tools.replay_known_risk import build_replay, load_inputs

def test_known_risk_is_criterion_drift():
    result = build_replay(load_inputs())
    assert result["case_ref"] == "CASE_REF_2026_DRIFT_KNOWN_RISK_001"
    assert result["fixture"] == "synthetic"
    assert result["deviation_detected"] is True
    assert result["drift_type"] == "CRITERION_DRIFT"
    assert result["model_output_changed"] is False
    assert result["criterion_changed"] is True
    assert result["baseline_evaluation"]["decision"] == "REJECT"
    assert result["observed_evaluation"]["decision"] == "ACCEPT"
    assert result["baseline_evaluation"]["score"] == result["observed_evaluation"]["score"]
