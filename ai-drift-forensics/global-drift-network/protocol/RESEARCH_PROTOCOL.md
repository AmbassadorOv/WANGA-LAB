# Global Drift Network — Research Protocol

## 1. Purpose

Measure observable changes over time across multiple AI and information surfaces during a high-intensity public event, with particular attention to geographic, linguistic, temporal, and cross-surface relationships.

## 2. Study windows

### 30-day longitudinal window

The existing month of observations is treated as the primary longitudinal dataset. Each observation retains its original timestamp and source context.

### 72-hour high-resolution window

A separate 72-hour window uses denser sampling to capture short-term changes and interaction patterns.

## 3. Dimensions

Each observation should be indexed by:

- UTC timestamp
- Region/country
- Language
- Surface type
- Model/system identifier where available
- Query/test identifier
- Observation type
- Baseline reference
- Measured delta
- Event-context reference

## 4. Drift classes

- Semantic drift
- Behavioral drift
- Distributional drift
- Temporal drift
- Cross-surface drift
- Cross-region drift
- Cross-language drift

## 5. Interaction analysis

The study explicitly models directional relationships as observational edges:

`Region A → Region B`

`Surface A → Surface B`

`Language A → Language B`

An edge represents an observed temporal relationship, not proof of causal transmission.

## 6. Election/event context

Election-related events may be represented as event anchors in the timeline. Their presence must not be converted automatically into a causal explanation for any observed drift.

## 7. Sampling principle

Use repeated, stable probes wherever possible. Preserve the exact probe definition, timestamp, surface, and resulting observation. Do not silently replace missing observations with estimates.

## 8. Analysis sequence

`OBSERVE → NORMALIZE → ALIGN IN TIME → DETECT DELTA → MAP GEOGRAPHY → MAP LANGUAGE → MAP SURFACES → ANALYZE INTERACTIONS → REPRODUCE → REPORT`

## 9. Nulls and uncertainty

No-change observations, ambiguous observations, missing data, and failed reproduction attempts are first-class records.

## 10. Output

The final month report should contain a global timeline, regional matrices, cross-surface interaction graph, drift signatures, reproducibility results, and an explicit unresolved section.
