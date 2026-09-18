# WANGA Governance

Technical governance and continuity-planning layer for WANGA-LAB.

The governance layer connects evidence, institutions, exposure, coverage relationships, stress scenarios, monitoring, and audit history. It does not itself issue insurance, make underwriting decisions, determine legal ownership, or exercise sovereign authority.

## Components

- `WANGA_SYSTEM_GOVERNANCE_V1.md` — governance model and separation boundaries.
- `schema.json` — machine-readable governance object schema.
- `kernel.py` — deterministic connectivity and audit kernel.
- `continuity_engine.py` — deterministic exposure, coverage-gap, stress-test, and audit calculations.
- `WANGA_SEVEN_YEAR_CONTINUITY_PLAN.md` — seven-year planning framework.

## Development rule

Model -> Schema -> Kernel -> Simulation -> Verification -> Pilot -> Integration -> Audit -> Revision.

Financial, insurance, reinsurance, legal, regulatory, and monetary decisions remain subject to authorized institutions and independent validation.
