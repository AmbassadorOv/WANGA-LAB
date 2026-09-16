# Wave Propagation Experiment V1

Status: PILOT PROTOCOL
Version: 1.0.0

## Objective

Measure the temporal structure of AI drift as an observational wave around a verified public event anchor. The experiment does not monitor or infer private behavior of individuals. Institutional and geographic references are public information domains only.

The experiment begins after the previously documented intervention window. From the observation-freeze time onward, no additional action by the research team is intended to influence the measured systems.

## Core model

`ANCHOR -> OUTBOUND WAVE -> PROPAGATION -> RETURN WAVE`

A wave is a time series of observations relative to a frozen baseline. An observed sequence is not interpreted as physical transmission or proof of causality.

## Wave phases

- `BASELINE`: observations before the event-aligned window.
- `OUTBOUND`: first detected change after the anchor.
- `PROPAGATION`: aligned changes detected on independent nodes, languages, models or information surfaces.
- `RETURN`: a later change on the originating measurement surface or defined return surface.
- `DECAY`: measured reduction toward baseline.
- `CONTROL`: comparison against unaffected or alternative control observations.

## Required measurements

For every candidate wave, calculate or retain the following components separately:

1. `amplitude` — distance from the frozen baseline.
2. `onset_time` — first observation exceeding the pre-registered detection threshold.
3. `peak_time` and `peak_amplitude` — maximum observed deviation.
4. `energy` — time-integrated absolute deviation over the declared window.
5. `persistence` — duration above threshold.
6. `rise_rate` and `decay_rate` — change per unit time around the rising and falling segments.
7. `propagation_lag` — time difference between aligned detections on two observation surfaces.
8. `attenuation_ratio` — downstream amplitude or energy relative to the reference wave.
9. `amplification_ratio` — downstream amplitude or energy relative to the reference wave.
10. `waveform_similarity` — reproducible similarity between normalized outbound and return trajectories, with time lag explicitly reported.
11. `outbound_return_ratio` — return-wave energy divided by outbound-wave energy when a valid pair exists.
12. `temporal_compression_ratio` — return duration divided by outbound duration.
13. `network_coverage` — affected eligible independent nodes divided by observed eligible nodes.
14. `cross_language_lag` — aligned detection lag between declared language surfaces.
15. `independent_node_agreement` — agreement among independently collected observations.

## Detection and pairing

A candidate wave must have:

- a declared baseline snapshot;
- a declared anchor event and timestamp;
- a fixed probe set or versioned probe set;
- observation timestamps;
- model/provider identifiers when exposed;
- input snapshot identifier or hash;
- method version;
- output hash where available;
- missing-data and unavailable-source records;
- a control comparison where feasible.

Outbound and return waves must not be paired merely because they occur after one another. Pairing requires a declared matching rule based on source surface, probe family, model/provider, time window and reproducible waveform features.

## Primary wave equations

`DA(t) = D(X_t, B) / S`

`WE = sum(|DA(t)| * delta_t)`

`PD(A,B) = T_onset(B) - T_onset(A)`

`AR(A,B) = Energy(B) / Energy(A)`

`ORR = Energy(return) / Energy(outbound)`

`TCR = Duration(return) / Duration(outbound)`

All distance functions, thresholds and normalization scales must be versioned. No composite score may replace the component measurements.

## Origin classification

The system uses three stages:

- `DRIFT_ORIGIN_CANDIDATE (DOC)`: a surface is the earliest observed location of a candidate change within the measurement coverage.
- `REPEATED_DRIFT_ORIGIN (RDO)`: the same origin pattern recurs in independent observations or events under the declared method.
- `VALIDATED_PROPAGATION_PATTERN (VPP)`: the origin/propagation pattern survives control checks and independent replication.

These labels describe measurement order, not human intent or causality.

## 72-hour schedule

The existing event windows remain active: `T-15, T-5, T0, T+1, T+5, T+10, T+20, T+30, T+60`.

After the first event window, continue regular baseline observations so that decay and return trajectories can be measured. Additional event windows may be opened only for externally verified public anchors.

## Output package

Each completed wave should produce:

- wave record;
- baseline reference;
- event anchor;
- time-series observations;
- outbound fingerprint;
- propagation links;
- return fingerprint when present;
- component metrics;
- control comparison;
- coverage and uncertainty report;
- verification status;
- reproducibility metadata.

## Interpretation constraints

The experiment may establish temporal association, similarity, propagation profile and replication status. It must not convert temporal ordering into a causal claim. Public economic, governmental, judicial or market events are contextual anchors, not proof of causality.

## Integrity rules

- Public-source measurement only.
- No personal-content collection.
- No tracking of individual officials.
- No synthetic observations.
- No API keys in Git.
- No post-hoc threshold selection without recording the change.
- Missing observations remain missing.
- Negative findings are retained.
