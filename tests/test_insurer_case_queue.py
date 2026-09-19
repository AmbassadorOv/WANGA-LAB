from tools.insurer_case_queue import CaseState, plan_activation

def test_valid_case_progression():
    case = CaseState("CASE-001", "INTAKE")
    case = case.transition("SCOPED").transition("READY_FOR_REPLAY")
    case = case.transition("REPLAY").transition("VERIFY").transition("HUMAN_GATE")
    assert case.state == "HUMAN_GATE"
    assert case.history == ("SCOPED", "READY_FOR_REPLAY", "REPLAY", "VERIFY", "HUMAN_GATE")

def test_invalid_transition_is_rejected():
    case = CaseState("CASE-001", "INTAKE")
    try:
        case.transition("VERIFY")
    except ValueError as exc:
        assert "invalid transition" in str(exc)
    else:
        raise AssertionError("invalid transition was accepted")

def test_activation_limit_queues_remaining_cases():
    cases = [CaseState(f"CASE-{i:03d}", "READY_FOR_REPLAY") for i in range(10)]
    result = plan_activation(cases, active_limit=2)
    assert [c.state for c in result[:2]] == ["REPLAY", "REPLAY"]
    assert all(c.state == "QUEUED" for c in result[2:])

def test_non_ready_cases_are_preserved():
    cases = [CaseState("BLOCKED-1", "BLOCKED"), CaseState("INTAKE-1", "INTAKE")]
    result = plan_activation(cases, active_limit=1)
    assert [c.state for c in result] == ["BLOCKED", "INTAKE"]
