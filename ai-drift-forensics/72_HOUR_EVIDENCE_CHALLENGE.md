# 72-Hour Evidence Challenge

## Purpose

A controlled demonstration of whether an AI-operating environment can preserve enough evidence to detect, reconstruct, and investigate a defined change.

This is a forensic-readiness exercise, not a certification, regulatory audit, or determination of legal liability.

## Phase 01 — Baseline

Establish the reference state and record the relevant system, model, environment, data, configuration, dependency, and operational context.

Output: baseline evidence package.

## Phase 02 — Controlled Drift

Introduce a documented and bounded change in a test environment.

The change should be identifiable to the exercise organizers but not necessarily exposed to every observer at the moment of execution.

Output: controlled event record.

## Phase 03 — Detection

Determine whether the monitoring and forensic layer can identify that system behavior or state has changed.

Output: drift observation and measurement record.

## Phase 04 — Evidence Preservation

Capture relevant artifacts, timestamps, provenance, integrity metadata, and custody transitions.

Output: preserved evidence package.

## Phase 05 — Reconstruction

Reconstruct the event sequence from the evidence package.

Questions:

- What was the baseline state?
- What changed?
- When did the change become observable?
- Which components were affected?
- Which dependencies were involved?

Output: chronological reconstruction.

## Phase 06 — Attribution

Map observed changes across model, data, configuration, environment, and dependencies.

Separate correlation from demonstrated causation and record competing explanations.

Output: attribution graph and uncertainty record.

## Phase 07 — Verification

A reviewer repeats the defined test or inspects the evidence package under documented conditions.

Output: verification record with result class:

`SUPPORTED | PARTIALLY_SUPPORTED | NOT_REPRODUCED | REFUTED | UNRESOLVED`

## Challenge metrics

The exercise can measure:

- time to detect;
- evidence completeness;
- provenance completeness;
- reconstruction completeness;
- attribution coverage;
- reproducibility;
- unresolved evidence gaps;
- time required for independent review.

Metrics should be reported with methodology and scope. No single score should be treated as a universal measure of AI forensic readiness.

## Integrity rules

1. Do not silently modify the baseline after the challenge begins.
2. Keep simulated events distinct from real incidents.
3. Preserve raw evidence separately from analyst interpretation.
4. Record failed reproduction attempts.
5. Do not convert correlation into causal language without supporting evidence.
6. Keep confidential or personal data outside public demonstration repositories.

## Completion package

A completed challenge should produce:

`CASE → BASELINE → EVENT → EVIDENCE → RECONSTRUCTION → ATTRIBUTION → VERIFICATION`

The resulting package is intended to demonstrate what an organization can and cannot reconstruct from its available evidence.