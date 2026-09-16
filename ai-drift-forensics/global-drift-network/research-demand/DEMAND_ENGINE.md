# Research Demand Engine

## Purpose

Aggregate scientist interest into a transparent research-priority signal without allowing demand signals to modify evidence or findings.

## Input

- validated `Research Interest Vote` records
- topic registry
- current research capacity
- data availability
- measurement feasibility
- urgency indicators
- unresolved questions already present in the research system

## Topic score

For each topic:

`priority = demand × importance × measurability × data_availability × urgency`

Each factor is normalized to `[0,1]`. The engine preserves the individual factors so the aggregate score is auditable.

`demand` is derived from aggregated votes, not from individual identity.

## Processing

`INGEST → VALIDATE → DEDUPLICATE → AGGREGATE → NORMALIZE → SCORE → EXPLAIN → QUEUE`

## Constraints

1. Votes cannot alter raw observations.
2. Votes cannot upgrade a hypothesis to a finding.
3. No unnecessary personal information is required.
4. Free-text requests are retained only when needed for research interpretation.
5. Low-data topics remain visible rather than being silently discarded.
6. Every generated priority record references its input period and topic registry version.

## Output

A `ResearchDemandSnapshot` containing:

- snapshot timestamp
- aggregation period
- topic demand counts
- normalized demand
- factor values
- priority signal
- recommended research queue
- unresolved data limitations

The queue is a recommendation to the research orchestration layer, not an automatic publication decision.
