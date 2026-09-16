# Global Propagation Graph

Status: research architecture under development.

## Objective

Represent reproducible temporal relationships among drift observations across regions, languages and information surfaces.

## Graph model

Nodes represent observed entities or contexts:

- REGION
- LANGUAGE
- SURFACE
- SYSTEM
- EVENT
- OBSERVATION

Edges represent observed relationships and never imply causality by themselves.

Allowed relationship states:

- PRECEDES
- FOLLOWS
- COINCIDES

## Edge construction

An edge may be proposed only when two or more observations have:

1. valid timestamps;
2. compatible measurement definitions;
3. preserved baseline references;
4. sufficient provenance;
5. a documented temporal relationship;
6. an explicit uncertainty assessment.

## Propagation dimensions

Every candidate relationship is classified across one or more dimensions:

- cross-region;
- cross-language;
- cross-surface;
- cross-system;
- event-linked;
- persistent/transient.

## Verification lifecycle

```text
OBSERVATION
  -> CANDIDATE EDGE
  -> TEMPORAL ALIGNMENT
  -> REPRODUCTION
  -> ALTERNATIVE-EXPLANATION REVIEW
  -> ATTRIBUTION ASSESSMENT
  -> INDEPENDENT VERIFICATION
  -> VERIFIED / PARTIALLY_SUPPORTED / NOT_REPRODUCED / REFUTED / UNRESOLVED
```

## Global graph snapshots

A graph snapshot is immutable after publication. Corrections produce a new snapshot and preserve the previous snapshot for provenance.

Each snapshot must record:

- snapshot identifier;
- generation timestamp;
- source commits;
- protocol version;
- node count;
- candidate edge count;
- verified edge count;
- unresolved relationship count;
- data-quality warnings.

## Interpretation rule

A dense graph does not mean that information physically or causally propagated through the connected nodes. The graph represents measured temporal relationships. Causal interpretation requires separate evidence and verification.
