from governance.continuity_engine import (
    ContinuityPlan,
    Coverage,
    Exposure,
    StressScenario,
)


def test_coverage_gap_uses_verified_exposure_only():
    plan = ContinuityPlan(
        "plan-1",
        exposures=[
            Exposure("e1", 100.0, "EUR", verified=True),
            Exposure("e2", 50.0, "EUR", verified=False),
        ],
        coverages=[Coverage("c1", 60.0, status="ACTIVE")],
    )

    assert plan.total_exposure() == 150.0
    assert plan.verified_exposure() == 100.0
    assert plan.active_capacity() == 60.0
    assert plan.coverage_gap() == 40.0


def test_stress_scenario_reports_uncovered_loss():
    plan = ContinuityPlan(
        "plan-2",
        exposures=[Exposure("e1", 100.0, "EUR", verified=True)],
        coverages=[Coverage("c1", 30.0, status="ACTIVE")],
        scenarios=[StressScenario("stress-50", 0.5)],
    )

    result = plan.stress_result("stress-50")

    assert result["stressed_loss"] == 50.0
    assert result["active_capacity"] == 30.0
    assert result["uncovered_loss"] == 20.0


def test_audit_digest_is_deterministic():
    plan = ContinuityPlan(
        "plan-3",
        exposures=[Exposure("e1", 10.0, "USD", verified=True)],
    )

    assert plan.audit_digest() == plan.audit_digest()
    assert len(plan.audit_digest()) == 64
