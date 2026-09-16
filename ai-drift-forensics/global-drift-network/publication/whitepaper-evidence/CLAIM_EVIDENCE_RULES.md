# Claim-to-Evidence Control Rules

The White Paper is generated only from traceable evidence.

## Required chain

`CLAIM → EVIDENCE IDs → SOURCE/MEASUREMENT → METHOD → VERIFICATION STATUS`

## Status semantics

- `OBSERVED`: directly measured by the project dataset.
- `SUPPORTED`: supported by a documented external source.
- `HYPOTHESIS`: proposed but not sufficiently tested.
- `REFUTED`: tested under the documented method and not supported.

## Rules

1. Every substantive empirical claim gets a stable `claim_id`.
2. Every empirical claim references one or more `evidence_id` values.
3. Evidence must retain timestamp and provenance.
4. External regulatory or institutional claims require a source record.
5. Correlation is not recorded as causation unless the study design supports causal inference.
6. Provider/model changes, prompt changes, retrieval changes, sampling variation and data changes must be considered as alternative explanations where relevant.
7. Missing or failed measurements remain missing; they are never imputed as positive findings without an explicit documented method.
8. Publication eligibility is determined by the Quality Gate, not by the Orchestrator's interpretation.
