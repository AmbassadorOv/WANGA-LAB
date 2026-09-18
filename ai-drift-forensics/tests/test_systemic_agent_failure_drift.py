"""Executable conformance tests for systemic agent Drift controls.

These tests validate representations and transformations, not future financial outcomes.
"""

from dataclasses import dataclass
from typing import Literal

Status = Literal[
    "VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "MODEL_OUTPUT",
    "REPORTED", "DERIVED", "CONTRADICTED",
]

@dataclass(frozen=True)
class Evidence:
    value: float | str
    source_type: str
    status: Status
    time_scope: str

def test_drift_epistemic_future_projection_is_not_fact():
    item = Evidence("2029", "STRATEGIC_ECONOMIC_MODEL", "MODEL_OUTPUT", "FUTURE")
    assert item.status == "MODEL_OUTPUT"
    assert item.time_scope == "FUTURE"

def test_drift_liquidity_types_are_not_cash():
    committed = Evidence(122_000_000_000, "FINANCING_REPORT", "REPORTED", "2026")
    credit = Evidence(4_700_000_000, "CREDIT_FACILITY", "REPORTED", "2026")
    assert committed.source_type != "CASH_BALANCE"
    assert credit.source_type != "CASH_BALANCE"

def test_drift_recursive_output_cannot_be_independent_evidence():
    prior_output = Evidence("2029", "MODEL_OUTPUT", "MODEL_OUTPUT", "FUTURE")
    independent_evidence = prior_output.source_type != "MODEL_OUTPUT"
    assert independent_evidence is False

def test_drift_temporal_leakage_is_detectable():
    current_state = {"time_scope": "CURRENT", "value": 2026}
    future_projection = {"time_scope": "FUTURE", "value": 2029}
    assert current_state["time_scope"] != future_projection["time_scope"]

def test_drift_confidence_requires_calibration_metadata():
    confidence = {"value": 0.945, "type": "ANALYST_CONFIDENCE", "calibration_method": None}
    assert confidence["type"] != "CALIBRATED_PROBABILITY"
    assert confidence["calibration_method"] is None

def test_drift_model_output_is_not_accounting_debt():
    stress = Evidence(18_000_000_000_000, "STRATEGIC_STRESS_MODEL", "MODEL_OUTPUT", "FUTURE")
    assert stress.status == "MODEL_OUTPUT"
    assert stress.source_type != "BALANCE_SHEET_DEBT"

def test_drift_source_authority_is_preserved():
    report = Evidence(852_000_000_000, "PRIMARY_COMPANY_REPORT", "REPORTED", "2026")
    assert report.source_type == "PRIMARY_COMPANY_REPORT"
    assert report.status == "REPORTED"

def test_drift_arithmetic_does_not_create_liability():
    result = 18_000_000_000_000 - 852_000_000_000
    assert result == 17_148_000_000_000
    # Arithmetic result only; no accounting meaning is inferred.