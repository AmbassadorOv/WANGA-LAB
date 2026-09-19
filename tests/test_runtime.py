from wanga_runtime import WangaRuntime


def test_end_to_end_runtime_and_evidence():
    report = WangaRuntime().run("smoke")
    assert report["verification_status"] == "PASSED"
    assert report["state"][-1] == "COMPLETED"
    assert len(report["results"]) == 3
    assert report["evidence"][-1]["stage"] == "VERIFY"


def test_replay_is_deterministic():
    runtime = WangaRuntime()
    assert runtime.run({"x": 1}) == runtime.run({"x": 1})


def test_unknown_role_fails_closed():
    report = WangaRuntime().run("smoke", roles=("planner", "unknown"))
    assert report["verification_status"] == "FAILED"
    assert report["state"][-1] == "FAILED"
