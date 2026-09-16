# International Drift Propagation — Implementation Map

## System boundary

This project is a research layer inside the Global Drift Network. It consumes standardized observations and produces versioned relationship candidates and verification records.

## Components

```text
Global Election Registry
        |
        v
Event Normalizer
        |
        v
Observation Scheduler
        |
        v
Observation Store
        |
        +-------------------+
        |                   |
        v                   v
Drift Detector       Coverage Monitor
        |
        v
Temporal Alignment
        |
        +----------+----------+
        |          |          |
        v          v          v
Region       Language      Surface
Analysis     Analysis      Analysis
        \          |          /
         \         |         /
          v        v        v
          Propagation Graph
                 |
                 v
        Reproduction Engine
                 |
                 v
          Attribution Layer
                 |
                 v
          Verification Gate
                 |
        +--------+--------+
        |                 |
        v                 v
   Research Data     Publication Queue
```

## Repository components

- `README.md` — project definition and scope.
- `ELECTION_TRIGGER_METHOD.md` — election-trigger methodology.
- `ELECTION_REGISTRY.md` — event registry specification.
- `election-event.schema.json` — machine-readable event schema.
- `ELECTION_TRIGGER_PIPELINE.md` — end-to-end event pipeline.
- `OBSERVATION_MATRIX.md` — common measurement dimensions.
- `PROPAGATION_ANALYSIS_PROTOCOL.md` — relationship analysis and verification.
- `propagation-edge.schema.json` — machine-readable relationship edge.
- `research-demand/` — scientific demand and question prioritization inherited from the Global Drift Network.
- `daily-digest/` — daily synthesis and publication preparation.
- `orchestrator/` — routing and execution control inherited from the network.

## Operational lifecycle

```text
DISCOVER EVENT
→ REGISTER EVENT
→ FREEZE EVENT VERSION
→ CREATE BASELINE
→ SAMPLE
→ DETECT DELTA
→ PRESERVE EVIDENCE
→ ALIGN OBSERVATIONS
→ GENERATE EDGE CANDIDATES
→ TEST ALTERNATIVES
→ REPRODUCE
→ ATTRIBUTE
→ VERIFY
→ UPDATE GRAPH
→ GENERATE DIGEST
→ QUALITY GATE
→ PUBLICATION QUEUE
```

## Scaling principle

The unit of scale is the observation, not the election. An event can produce observations across multiple regions, languages, surfaces, probes, and timestamps. The graph is then constructed from those observations.

This allows the same infrastructure to support dozens or hundreds of events without changing the scientific representation.

## Research outputs

1. Event-level drift record.
2. Regional drift profile.
3. Cross-language drift profile.
4. Cross-surface interaction record.
5. Candidate propagation graph.
6. Reproduction record.
7. Attribution record.
8. Verification result.
9. Unresolved relationship register.
10. Longitudinal recurrence dataset.

## Publication rule

No automated system may publish a causal claim solely because a temporal edge exists. Public output must expose the observation, evidence, uncertainty, reproduction state, and verification state.

## Completion criterion

The project is operationally complete when a registered event can travel through the full lifecycle without manual reinterpretation of its schema, while every scientific conclusion remains traceable to observations and evidence.
