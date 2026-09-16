# Election Monitoring Protocol

## Scope

This protocol defines a repeatable observation program for election-linked periods inside the Global Drift Network.

It is a measurement protocol, not a political-analysis or election-forecasting framework.

## 1. Study registration

Before collection begins, register:

- `event_id`
- event description
- jurisdiction/region set
- planned observation dates
- 30-day longitudinal window
- 72-hour high-resolution window
- monitored languages
- monitored AI/model surfaces
- monitored search surfaces
- monitored public-information source sets
- protocol version
- probe registry version

The study registration becomes the reference state for later comparison.

## 2. Baseline

Collect repeated observations before the high-resolution event window. The baseline should establish normal variation for every probe that will later support a drift claim.

Record exact probe definitions and collection timestamps. Do not replace missing baseline observations with invented or silent estimates.

## 3. Repeated observation

Stable probes should be repeated at predefined intervals. A probe must preserve enough information to reproduce the measurement:

```text
probe_id
prompt/query definition
surface
model/system configuration
language
region
UTC timestamp
result reference
measurement method
```

## 4. Event-window intensification

During the configured 72-hour high-resolution window, increase observation frequency for the registered probes. Additional probes may be added only if they are explicitly marked as exploratory and are not silently merged into the baseline series.

## 5. Drift detection

Compare each observation with its registered baseline and prior observations. Classify detected changes as applicable:

- semantic
- behavioral
- distributional
- temporal
- regional
- language
- cross-surface

Detection is a signal-generation step. It does not establish cause.

## 6. Relationship analysis

When two surfaces or regions show temporally related changes, create an interaction record containing:

- source observation references
- target observation references
- timestamps
- time difference
- relationship type
- measurement strength
- reproduction status
- attribution status

The relationship must be described as observed unless separate evidence supports a stronger interpretation.

## 7. Persistence test

After the event window, continue selected probes to determine whether the observed change:

`RECOVERS → PERSISTS → OSCILLATES → UNKNOWN`

Persistence is a property of the observed trajectory, not evidence of cause.

## 8. Reproduction

A candidate drift event should be reproduced using the same or a controlled equivalent probe where feasible. Record success, partial success, failure, or unresolved status.

## 9. Attribution separation

The protocol keeps these questions separate:

1. Did the measured change occur?
2. Can the change be reproduced?
3. Which component(s) could account for the change?
4. Is there enough evidence to attribute the change to a particular component?

A positive answer to question 1 does not automatically answer questions 2–4.

## 10. Uncertainty

Every study must preserve:

- missing observations
- unavailable surfaces
- invalidated observations
- sampling limitations
- probe changes
- configuration changes
- uncertainty in measurement

Null is preferable to fabricated completeness.

## 11. Daily integration

At each daily cycle:

```text
OBSERVATIONS
    ↓
DRIFT DETECTION
    ↓
RELATIONSHIP ANALYSIS
    ↓
VERIFICATION STATUS
    ↓
DAILY DIGEST
    ↓
QUALITY GATE
    ↓
PUBLICATION QUEUE
```

Scientist-interest votes can influence which unresolved questions receive additional measurement capacity, but cannot rewrite the evidence record.

## 12. Political neutrality

The system records election events as temporal and contextual anchors. It does not rank candidates, parties, political positions, or electoral outcomes, and it does not infer voter preferences from drift observations.

## 13. Quality gate

A public result requires, at minimum:

- valid schema
- traceable source references
- explicit baseline status
- evidence class
- uncertainty where relevant
- no unsupported causal statement
- verification status recorded
- content hash

## 14. Failure handling

If a required evidence dependency is missing, the result is routed to `UNRESOLVED` or `QUALITY_REVIEW` rather than upgraded by inference.

## Status

Proposed research protocol under development.
