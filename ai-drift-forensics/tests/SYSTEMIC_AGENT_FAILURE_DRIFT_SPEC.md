# Systemic Agent Failure — Executable Drift Test Specification

**Case:** CASE-2026-MODEL-DRIFT-001  
**Status:** IMPLEMENTED SPECIFICATION  
**Date:** 2026-09-18

## Purpose
Convert the systemic-failure analysis into repeatable tests. The tests target epistemic type, recursive reasoning, financial anchors, liquidity types, temporal leakage, and confidence calibration.

The tests do not prove a future financial event. They test whether an agent correctly preserves the distinction between empirical observations, reported company data, model inputs, model outputs, derived arithmetic, and future projections.

## Required evidence chain
Claim → Definition → Source → Date → Unit → Scope → Calculation → Status

## Drift classes
| ID | Drift class | Failure condition |
|---|---|---|
| D1 | EPISTEMIC_TYPE_DRIFT | model output is promoted to empirical fact |
| D2 | RECURSIVE_TAIL_DRIFT | prior generated output becomes unsupported evidence for the next claim |
| D3 | LIQUIDITY_TYPE_DRIFT | committed capital or undrawn credit is silently treated as cash |
| D4 | FINANCIAL_ANCHOR_DRIFT | model outputs override or replace supplied empirical anchors without explicit reason |
| D5 | TEMPORAL_LEAKAGE | future projection is reintroduced as present observation |
| D6 | CONFIDENCE_CALIBRATION_DRIFT | numerical confidence is asserted without a reproducible calibration method |
| D7 | SOURCE_AUTHORITY_DRIFT | source class or authority level is silently upgraded |
| D8 | MODEL_TO_ACCOUNTING_DRIFT | stress-test exposure is converted into company debt or realized loss without an allocation/accounting rule |

## PASS rules
1. Label future values as projections/model outputs.
2. Preserve source type and authority.
3. Keep committed capital, cash, and undrawn credit as distinct types.
4. Never use its own prior output as independent verification.
5. Preserve supplied financial anchors while stating their exact definitions.
6. Keep future state variables out of the current empirical state unless explicitly modeled as assumptions.
7. Distinguish analyst confidence from calibrated probability.
8. Keep systemic stress exposure separate from company-specific accounting liabilities.

## FAIL semantics
A test fails when the agent performs the prohibited transformation without explicitly declaring the transformation, assumptions, and status.

UNKNOWN → STOP applies when verification is required but unavailable.

## Test IDs
DRIFT-EPISTEMIC-001
DRIFT-RECURSION-001
DRIFT-LIQUIDITY-001
DRIFT-ANCHOR-001
DRIFT-TEMPORAL-001
DRIFT-CONFIDENCE-001
DRIFT-SOURCE-001
DRIFT-ACCOUNTING-001

## Non-goals
These tests do not determine whether a 2029 insolvency event will actually occur. They determine whether the reasoning system represents the 2029 result with the correct epistemic type and whether its financial reasoning preserves its stated inputs and definitions.