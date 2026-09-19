# Event Response Protocol v1

Status: CONFIGURED PILOT
Version: 1.0.0

## Purpose

This protocol measures AI behavioral change around externally observable events while preserving the distinction between temporal association and causation.

An event is an anchor. It is not itself a drift observation.

## Event record

Each event anchor should contain:

- `event_id`
- `event_type`
- `source_id`
- `detected_at`
- `event_time`
- `confidence`
- `source_locator`
- `event_hash`
- `scope`
- `affected_providers_or_models` when known

The event source must be retained as provenance. Missing or inaccessible sources must be recorded as unavailable rather than replaced with synthetic observations.

## Measurement modes

NORMAL: scheduled baseline/control observations every 15 minutes.

FAST: 5-minute observations during an elevated monitoring window.

EVENT: event-aligned burst around the anchor:

`T-15 -> T-5 -> T0 -> T+1 -> T+5 -> T+10 -> T+20 -> T+30 -> T+60`

The same fixed probe set used by the normal monitoring program should be retained across the event window. Event-specific probes may be added as an overlay, but they must be versioned separately.

## Two primary event metrics

### Event Impact Index (EII)

EII measures the normalized change in the observed behavior vector relative to the pre-event control baseline.

Conceptually:

`EII(t) = D(X_t, B) / S`

where `X_t` is the event-window observation vector, `B` is the pre-event baseline vector, `D` is a declared reproducible distance or task-specific delta function, and `S` is the declared normalization scale.

The implementation must retain the underlying component deltas. A composite score must never replace the evidence record.

### Propagation / Network Impact Index (PNI)

PNI describes how broadly and persistently an event-aligned change appears across independent observation nodes.

Components:

- affected-node coverage
- cross-language coverage
- cross-region coverage
- time-to-change
- persistence
- independent-node agreement

Coverage and uncertainty must be reported separately from impact magnitude.

## Control design

Where feasible, include an unaffected control node, model, language, or probe family. Controls reduce false attribution caused by common infrastructure changes, probe instability, or ordinary variance.

A change observed only after an event is classified initially as a `TEMPORALLY_ASSOCIATED_CHANGE`. Stronger causal language requires additional controlled evidence.

## Evidence lifecycle

`EVENT_ANCHOR -> OBSERVATION -> CANDIDATE_DELTA -> CONTROL_CHECK -> VERIFICATION -> REPLICATION -> FINDING`

Rejected or unresolved observations remain traceable and are not silently removed.

## Event-specific measurement

Every event family must define:

1. event anchor fields;
2. source type;
3. fixed probe set;
4. event-specific probe overlay;
5. observation windows;
6. control strategy;
7. expected evidence fields;
8. verification requirements;
9. limitations.

## Initial event families

- `MODEL_CHANGE`
- `PLATFORM_CHANGE`
- `SERVICE_INCIDENT`
- `PUBLIC_INFORMATION_BURST`
- `PUBLIC_EVENT`
- `POLICY_REGULATORY_EVENT`
- `MAJOR_PUBLICATION`
- `SEARCH_INFORMATION_SURFACE_CHANGE`

No family is assumed to produce drift. The protocol measures whether a reproducible behavioral delta is observed.

## Data integrity rules

- No synthetic observations.
- No API keys in Git.
- Every observation references an input snapshot and method version.
- Output hashes and provenance should be retained when available.
- Public event sources are anchors, not proof of model causality.
- Missing credentials or endpoints produce `NOT_CONFIGURED` or `UNAVAILABLE`, never fabricated measurements.
