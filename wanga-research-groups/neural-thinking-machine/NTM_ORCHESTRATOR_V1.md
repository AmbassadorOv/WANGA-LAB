# NTM Orchestrator V1

Status: INITIAL / EXPERIMENTAL

## Purpose

Coordinate high-level reasoning requests and route version, semantic, structural, and drift analysis through the Neural Thinking Machine without turning the NTM into an unrestricted autonomous authority.

## Pipeline

`INGEST_STATE -> LOAD_RELEVANT_HISTORY -> NORMALIZE -> VERSION_DIFF -> STRUCTURAL_DIFF -> SEMANTIC_DIFF -> DRIFT_CLASSIFICATION -> HIGH_LOGIC_ANALYSIS -> REPAIR_CANDIDATE -> VERIFICATION_GATE -> RETURN`

## Drift classes

1. `LETTER_DRIFT` — tracked symbolic unit changed.
2. `POSITION_DRIFT` — unit remains but changes position.
3. `SEQUENCE_DRIFT` — ordering changes.
4. `WORD_DRIFT` — word-level composition changes.
5. `SEMANTIC_DRIFT` — role or meaning representation changes.
6. `STRUCTURAL_DRIFT` — relation, hierarchy, matrix, or architecture changes.
7. `VERSION_DIRECTION_DRIFT` — current development departs from an earlier documented direction.
8. `INTENT_RECOVERY_CANDIDATE` — current state cannot be interpreted reliably without historical recovery.
9. `UNAVAILABLE` — required evidence is missing.
10. `REVIEW` — evidence or interpretation is insufficient for automatic classification.

## 620 symbolic tracking

The initial design supports a 620-slot/token tracking layer. The tracker must record exact source/version/position information and must not silently manufacture missing entries. The numerical definition, matrix arrangement, and relationship to the user's historical 620-letter work must be recovered from the repository/history before being treated as a validated invariant.

## High-logic behavior

The NTM may:

- compare competing architectural representations;
- identify contradictions;
- trace a concept through versions;
- recover candidate original intent;
- construct explicit reasoning chains;
- request specialist research;
- propose a repair or reconciliation;
- send the result back for verification.

The NTM must not:

- rewrite historical evidence;
- treat an inference as an observation;
- silently delete a legacy design;
- convert temporal succession into causality;
- declare an unverified symbolic mapping to be scientific fact.

## Anchor behavior

If a subsystem reports a logical failure or unresolved contradiction, the NTM receives the bounded state and relevant evidence rather than the entire network state by default. This prevents the cognitive CPU from becoming a single-point dependency for every operation.

## Return envelope

Every completed reasoning cycle should identify:

- source state/version;
- compared versions;
- detected drift class(es);
- evidence references;
- reasoning status;
- repair candidate, if any;
- verification status;
- unresolved questions;
- whether historical intent recovery was used.

## Status semantics

`OBSERVATION -> DIFFERENCE -> CANDIDATE -> VERIFIED_FINDING -> ARCHITECTURAL_CHANGE`

Promotion requires the appropriate verification step. This document is an initial architecture, not a claim that the complete Thinking Machine is already implemented.
