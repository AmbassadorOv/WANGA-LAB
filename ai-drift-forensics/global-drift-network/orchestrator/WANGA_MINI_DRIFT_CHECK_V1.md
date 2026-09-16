# WANGA Mini Drift Check

Status: PILOT
Version: 1.0.0

## Purpose

Provide a lightweight periodic research loop while the full WANGA research computer is being built.

## Cycle

`LOAD_REGISTERED_PROBES → RUN_CONTROLLED_CHECKS → COLLECT_OBSERVATIONS → COMPARE_TO_BASELINE → CLASSIFY → RECORD`

## Suggested cadence

Default: every 15 minutes when an execution environment is configured.

The cadence is an operational default, not scientific evidence. Event-driven checks may run separately under the existing event protocol.

## Classifications

- `NORMAL`
- `ANOMALY`
- `PRECURSOR_CANDIDATE`
- `TRIGGER_CANDIDATE`
- `UNAVAILABLE`
- `REVIEW`

## Trigger boundary

A mini-check does not start the 72-hour experiment by itself. A qualifying trigger must satisfy the versioned trigger protocol and be recorded as T0.

## Required records

Each cycle should retain run ID, probe version, observation IDs, baseline reference, measurement values, comparison method, classification, uncertainty, availability state and external-event context.

## No-fabrication rule

If a model endpoint, credential, source or measurement is unavailable, record the unavailable state. Do not create synthetic observations and do not interpret infrastructure failure as model drift.
