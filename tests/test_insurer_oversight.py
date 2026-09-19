from tools.insurer_oversight import build_oversight

def test_oversight_summary_is_machine_readable():
    report = build_oversight()
    assert report["total_cases"] == 10
    assert report["active_replay"] == 2
    assert report["queued"] == 5
    assert report["blocked_or_pending"] == 3
    assert report["human_gate"] == 0
    assert len(report["requires_architect_attention"]) == 3
