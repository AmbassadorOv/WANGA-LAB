from wanga_research_groups.neural_thinking_machine.ntm_core import NTMOrchestrator

def test_ntm_end_to_end():
    result=NTMOrchestrator().run("POC smoke test")
    assert result["verification_status"]=="PASSED"
    assert result["reasoning_status"]=="VERIFIED_FINDING"
    assert result["pipeline"][-1]=="SYNTHESIZE"
    assert len(result["results"])==2

def test_ntm_deterministic_task_id():
    a=NTMOrchestrator().run("same input")
    b=NTMOrchestrator().run("same input")
    assert a==b
