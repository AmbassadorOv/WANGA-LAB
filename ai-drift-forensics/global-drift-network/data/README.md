# Global Drift Network — Data Layer

This directory is the data boundary for the Global Drift Network.

## Storage layers

- `raw/` — observations preserved as collected, with no silent correction.
- `normalized/` — schema-conformant records with standardized timestamps and controlled vocabularies.
- `derived/` — calculated deltas, aggregates, timelines, and interaction edges.

## Required discipline

1. Raw records are never overwritten by normalization.
2. Every normalized record retains a reference to its raw source.
3. Missing observations are represented explicitly; they are not replaced by estimates without a documented method.
4. A baseline and its repeat observations must be distinguishable.
5. Derived metrics must identify their source observation IDs and calculation method.
6. Event references provide temporal context only. They do not establish causation.
7. Failed reproduction and null observations are retained.
8. Timestamps are stored in UTC.
9. Publicly accessible observations should avoid unnecessary personal data.
10. Synthetic examples must be clearly marked as synthetic and must not be presented as production incidents.

## Canonicalization and integrity

Before hashing a record, serialize the normalized JSON using deterministic key ordering, UTF-8 encoding, and no insignificant whitespace. Store the resulting SHA-256 digest alongside the record or in a manifest.

A hash supports integrity checking of the serialized record. It does not by itself prove that the underlying observation was true, complete, independently witnessed, or immutable.

## Observation ID convention

`GDO-YYYY-<unique-token>`

Example: `GDO-2026-IL-AI-0001`

## Derived interaction edge

An interaction edge has the form:

`source_node → target_node`

and must contain at minimum:

- source observation references
- target observation references
- temporal separation
- metric used
- direction
- confidence/uncertainty
- causal status

The default causal status is `NONE_ASSERTED` or `TEMPORAL_ASSOCIATION`.
