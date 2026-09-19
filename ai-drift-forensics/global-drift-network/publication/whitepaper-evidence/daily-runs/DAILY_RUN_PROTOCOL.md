# Daily Run Protocol

## Purpose

Define the reproducible daily measurement cycle for the 30-day White Paper evidence program.

## Run sequence

1. `CREATE_RUN` — create a unique `run_id` and record the scheduled execution time.
2. `BASELINE_OR_LOAD` — load the active baseline version. Day 0 establishes the baseline; later runs reference it without mutation.
3. `INPUT_SNAPSHOT` — capture the measurement configuration, target surfaces, source identifiers, prompt/control set version, and runtime metadata.
4. `CHANGE_SCAN` — record observable model, retrieval, source, configuration, or environment changes relevant to interpretation.
5. `OBSERVE` — execute the predefined measurement set.
6. `COMPARE` — calculate deltas against the declared baseline and, where applicable, the immediately preceding run.
7. `VERIFY` — check provenance, repeatability, controls, and plausible alternative explanations.
8. `EVIDENCE_RECORD` — assign Evidence IDs to observations that satisfy the evidence schema.
9. `SNAPSHOT` — persist the resulting state as a new immutable snapshot linked to its parent.
10. `QUALITY_GATE` — classify the run as PASS, REVIEW, or BLOCK for downstream publication use.

## Timing

The daily schedule is configuration-driven. The scheduler starts the run; it does not perform analysis. The Orchestrator owns the state transitions.

Recommended initial window: one run per calendar day in `Asia/Jerusalem`, with a configurable start time and maximum runtime. The exact schedule must be stored in version-controlled configuration.

## Re-runs

A failed or incomplete run must receive a new `attempt` or a new run identifier. Do not overwrite the original record. Any re-run must retain a reference to the original run and explain why it was repeated.

## Evidence discipline

A measurement is not automatically a finding. Every published claim must reference one or more Evidence IDs. Unverified observations remain explicitly marked as observations or hypotheses.
