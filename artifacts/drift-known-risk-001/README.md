# drift-known-risk-001

## Evidence Status

**Current state:** PLANNED

This directory is the canonical template for the first empirical AI-drift forensic case.

A planned artifact is not evidence of a completed client investigation.

## Objective

Demonstrate a reproducible path from supplied evidence to drift observation, replay, analysis, and verification.

## Case identity

- Case reference: `CASE_REF_2026_DRIFT_KNOWN_RISK_001`
- Subject: controlled AI-drift forensic evaluation
- Client: not assigned
- Confidentiality: to be defined per case
- Status: PLANNED

## Required package

- `case.yaml` — case metadata and scope
- `evidence-manifest.json` — supplied evidence inventory and hashes
- `replay/` — deterministic replay inputs and instructions
- `outputs/` — replay outputs and normalized observations
- `verification/` — verification results and integrity checks

## Verification rule

The case may be marked **VERIFIED** only after the defined replay and evidence-integrity checks succeed.

External timestamping or anchoring must remain UNKNOWN/PENDING until actual external proof is received and independently checked.

## Non-claims

This artifact does not by itself establish:
- regulatory certification
- insurance underwriting authority
- legal admissibility in a particular proceeding
- commercial performance
- a completed client engagement

Those claims require separate evidence and, where applicable, legal or contractual review.
