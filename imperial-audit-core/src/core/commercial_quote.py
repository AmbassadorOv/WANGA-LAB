"""Deterministic commercial quote calculator for the evidence service.

This module prices technical evidence work only. It does not calculate
insurance premiums, loss probabilities, coverage, or expected claims.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class QuoteInputs:
    assets: int
    jurisdictions: int
    documents: int
    verification_depth: int
    integrations: int
    annual_maintenance_rate: float = 0.0


def calculate_quote(
    inputs: QuoteInputs,
    *,
    setup_fee: float,
    asset_fee: float,
    jurisdiction_fee: float,
    document_fee: float,
    verification_fee: float,
    integration_fee: float,
) -> dict[str, float]:
    """Return a reproducible technical-service quote.

    Values are service fees, not insurance premiums or coverage prices.
    """
    if inputs.assets < 1:
        raise ValueError("assets must be >= 1")
    if inputs.jurisdictions < 1:
        raise ValueError("jurisdictions must be >= 1")
    if inputs.documents < 0 or inputs.verification_depth < 0 or inputs.integrations < 0:
        raise ValueError("scope counts cannot be negative")
    if inputs.annual_maintenance_rate < 0:
        raise ValueError("annual_maintenance_rate cannot be negative")

    setup = (
        setup_fee
        + inputs.assets * asset_fee
        + inputs.jurisdictions * jurisdiction_fee
        + inputs.documents * document_fee
        + inputs.verification_depth * verification_fee
        + inputs.integrations * integration_fee
    )
    maintenance = setup * inputs.annual_maintenance_rate
    return {
        "setup_fee": round(setup, 2),
        "annual_maintenance_fee": round(maintenance, 2),
        "first_year_service_total": round(setup + maintenance, 2),
    }
