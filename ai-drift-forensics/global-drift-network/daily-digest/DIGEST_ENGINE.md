# Daily Digest Engine

## Purpose

Turn the latest research state into one traceable daily scientific brief.

## Input layers

1. New observations and normalized observations.
2. Drift analysis outputs.
3. Verification records.
4. Unresolved questions.
5. Research-demand snapshot.
6. Git history and source commit references.

## Pipeline

`CHANGE_SCAN → EVIDENCE_CLASSIFY → DELTA_SUMMARY → VERIFICATION_FILTER → DEMAND_MERGE → DRAFT → QUALITY_GATE → QUEUE`

## Evidence precedence

`VERIFIED > OBSERVED > DERIVED > REPORTED > HYPOTHESIS`

The precedence controls wording and publication eligibility; it does not imply that one fact class is intrinsically more important.

## Daily brief contract

Every generated brief contains:

- report ID and UTC generation time
- source commits
- observation window
- observed changes
- derived measurements
- reproduced/verified findings
- unresolved questions
- research-demand signals
- next measurement actions
- quality-gate result
- content hash

## Publication gate

Automatic Wix publication is allowed only when:

- schema validation passes;
- every finding has a source reference;
- unsupported causal language is absent;
- unresolved items are explicitly marked;
- source commits are recorded;
- content hash is generated;
- the publication queue accepts the report.

Otherwise the report remains `QUALITY_REVIEW` or `DRAFT`.

## Idempotency

A report is uniquely identified by `(report_date, source_state_hash, protocol_version)`. Re-running the engine over the same state must not create duplicate publication items.
