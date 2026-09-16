# AI Drift Forensics — Verification Protocol

## Status

Proposed technical research protocol. Not an adopted statutory, regulatory, accreditation, or international standard.

## Objective

Determine whether a reported AI-system change can be independently observed, reconstructed, reproduced, and attributed to the extent supported by available evidence.

## Verification gates

### Gate 01 — Scope integrity

The system, environment, observation period, and forensic question are explicitly bounded.

Pass condition: another investigator can identify what is and is not being tested.

### Gate 02 — Baseline integrity

The comparison state is documented sufficiently to distinguish change from ordinary variation.

Pass condition: baseline artifacts and acquisition context are preserved.

### Gate 03 — Measurement integrity

The claimed drift has a defined observable metric or structured observation method.

Pass condition: measurement procedure can be repeated from the documented protocol.

### Gate 04 — Evidence integrity

Relevant artifacts have provenance and custody records.

Pass condition: evidence identity, source, acquisition time, integrity metadata, and custody transitions are recorded where applicable.

### Gate 05 — Reconstruction integrity

The event sequence can be reconstructed from preserved evidence.

Pass condition: a reviewer can establish the documented sequence without relying solely on retrospective narrative.

### Gate 06 — Attribution integrity

The analysis distinguishes correlation, dependency, temporal precedence, reproduction, and causal inference.

Pass condition: each attribution statement has an explicit evidentiary basis and uncertainty state.

### Gate 07 — Reproduction integrity

A defined portion of the reported effect can be reproduced under documented conditions.

Pass condition: reproduction result is recorded as successful, partial, failed, or unresolved.

### Gate 08 — Independence integrity

Where independent verification is claimed, the reviewer and review conditions are documented.

Pass condition: the verification record identifies the tested artifacts and the scope of independent review.

## Result classes

- `SUPPORTED` — evidence supports the stated proposition within the defined scope.
- `PARTIALLY_SUPPORTED` — only part of the proposition is supported.
- `NOT_REPRODUCED` — the effect was not reproduced under the documented conditions.
- `REFUTED` — available evidence contradicts the proposition within scope.
- `UNRESOLVED` — evidence is insufficient for a reliable determination.

These are evidentiary result classes, not legal conclusions.

## Required verification record

Each completed verification should capture:

1. Case ID.
2. Verification ID.
3. Question tested.
4. Scope and time window.
5. Baseline reference.
6. Evidence references.
7. Procedure/version.
8. Environment information.
9. Reproduction result.
10. Attribution result and uncertainty.
11. Reviewer identity or role, subject to privacy controls.
12. Independence statement where applicable.
13. Unresolved questions.
14. Final evidence-state transition.

## Non-substitution rule

Verification cannot substitute for missing evidence. A polished report, provider statement, simulation, or analyst conclusion must not be represented as independent verification unless the corresponding verification conditions were actually satisfied.

## Security and privacy

Public demonstrations should use synthetic cases. Real institutional evidence should remain within an authorized controlled environment and should be referenced by non-sensitive identifiers in public materials.
