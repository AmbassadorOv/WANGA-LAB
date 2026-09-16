# GLOBAL ELECTION TRIGGER METHOD

## Purpose

Use national and subnational election events as recurring temporal anchors for the International Drift Propagation Network.

The objective is not to study election outcomes or political preferences. The objective is to measure whether AI and information-system behavior changes in time, space, language, or surface around documented events, and whether relationships between those changes can be reproduced.

## 1. Event registry

Maintain a machine-readable registry of election events with:

- event_id
- country/region
- election type
- scheduled date and time when available
- event phase
- official/source references
- timezone
- status: scheduled, active, completed, postponed, cancelled, unknown

A global election calendar is an input to the experiment, not itself evidence of Drift.

## 2. Observation windows

For each event define a common timeline:

`BASELINE → PRE_EVENT → HIGH_RESOLUTION → POST_EVENT → PERSISTENCE`

Recommended logical windows:

- Baseline: establish stable probes before event pressure increases.
- Pre-event: repeated measurements approaching the event.
- High-resolution: dense sampling during the defined event window.
- Post-event: continue identical probes after the event.
- Persistence: test whether detected changes decay, persist, or recur.

The exact duration is stored per event and must not be silently changed.

## 3. Probe matrix

Each event should use fixed probes across:

`REGION × LANGUAGE × SURFACE × TEST`

Surfaces may include:

- AI/model systems
- Search systems
- News/public-information systems
- Other explicitly documented information surfaces

Every probe records the exact wording/test definition, timestamp, surface, locale, model/system identifier when available, and baseline reference.

## 4. What is measured

Primary measurements:

- semantic delta
- behavioral delta
- distributional delta
- temporal delta
- cross-language delta
- cross-region delta
- cross-surface delta
- persistence after event

Secondary controls:

- missingness
- repeated-run variability
- sampling coverage
- instrumentation changes
- system/version/configuration changes

## 5. International comparison

Do not compare raw outputs alone. Normalize measurements against each system's own baseline and preserve the raw observation reference.

For regions A and B, evaluate:

`ΔA(t)` and `ΔB(t)`

Then calculate temporal relationships between their changes without assuming direction of causality.

Candidate edge:

`A → B`

means that a defined change in A preceded a defined change in B within a specified window.

## 6. Propagation indicators

A candidate propagation pattern becomes stronger when multiple independent observations agree on:

- timing
- direction of change
- affected probe family
- affected surface
- affected language or region
- repeated observations
- independent reproduction

A single coincident observation is not sufficient for propagation attribution.

## 7. Evidence ladder

`OBSERVED → DERIVED → CANDIDATE RELATIONSHIP → REPRODUCED → ATTRIBUTION ASSESSED → VERIFIED / UNRESOLVED`

No step may silently upgrade the previous evidence class.

## 8. Confounder control

Before interpreting a cross-region relationship, check for:

- provider/model updates
- dependency/configuration changes
- common upstream information sources
- simultaneous external events
- changes in query wording
- locale or geolocation changes
- measurement/instrumentation failures
- missing or delayed observations

If these cannot be separated, retain the relationship as unresolved or partially supported.

## 9. Global accumulation

Every election contributes to a common longitudinal dataset. After many events, compare event types and regions to identify recurring Drift signatures.

The research question becomes:

`Does the same Drift signature recur across independent events and geographic environments?`

This is more informative than treating each election as an isolated case.

## 10. Output products

Each completed event can produce:

1. Event observation package
2. Regional Drift timeline
3. Cross-language comparison
4. Cross-surface graph
5. Candidate propagation edges
6. Verification package
7. Unresolved-question record
8. Contribution to the global Drift signature dataset

## Scientific boundary

Election event timing is context. It is not a causal explanation. Political content, preferences, or outcomes must not be inferred from Drift measurements unless a separate, explicitly scoped study establishes that relationship with appropriate evidence.
