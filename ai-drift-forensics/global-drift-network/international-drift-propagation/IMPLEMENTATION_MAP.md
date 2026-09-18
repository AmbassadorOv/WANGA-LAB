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
        +---------------------------+
        |                           |
        v                           v
Drift Detector              Outreach Event Tracker
        |                           |
        |                           v
        |                   Butterfly Tracker
        |                           |
        +-------------+-------------+
                      |
                      v
                Temporal Alignment
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
      Region       Language      Surface
      Analysis     Analysis      Analysis
        \             |             /
         \            |            /
          v           v           v
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
          +---------+---------+
          |                   |
          v                   v
     Research Data      Publication Queue
```

## Outreach-linked observation

Every outbound institutional message can create a `T0` observation anchor.
The Outreach Butterfly Tracker then:

1. preserves the outreach event and provenance;
2. observes documented post-`T0` changes;
3. compares those changes against a declared baseline;
4. measures temporal, action, counterparty, asset/domain, and sequence overlap;
5. records propagation depth and width;
6. assigns an evidence-confidence value;
7. emits a relationship candidate for the existing propagation graph.

A temporal sequence is never treated as proof of causality.

## Repository components

- `README.md` — project definition and scope.
- `ELECTION_TRIGGER_METHOD.md` — election-trigger methodology.
- `ELECTION_REGISTRY.md` — event registry specification.
- `election-event.schema.json` — machine-readable event schema.
- `ELECTION_TRIGGER_PIPELINE.md` — end-to-end event pipeline.
- `OBSERVATION_MATRIX.md` — common measurement dimensions.
- `PROPAGATION_ANALYSIS_PROTOCOL.md` — relationship analysis and verification.
- `propagation-edge.schema.json` — machine-readable relationship edge.
- `outreach-butterfly/` — outreach-to-network propagation tracker and configuration.
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
→ REGISTER OUTREACH T0 (when applicable)
→ TRACE POST-T0 CHANGES
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

Outreach events are treated as additional temporal anchors, not as evidence of causation.

This allows the same infrastructure to support dozens or hundreds of events without changing the scientific representation.

## Research outputs

1. Event-level drift record.
2. Regional drift profile.
3. Cross-language drift profile.
4. Cross-surface interaction record.
5. Outreach-linked propagation record.
6. Candidate propagation graph.
7. Reproduction record.
8. Attribution record.
9. Verification result.
10. Unresolved relationship register.
11. Longitudinal recurrence dataset.

## Publication rule

No automated system may publish a causal claim solely because a temporal edge exists. Public output must expose the observation, evidence, uncertainty, reproduction state, and verification state.

## Completion criterion

The project is operationally complete when a registered event or outreach anchor can travel through the full lifecycle without manual reinterpretation of its schema, while every scientific conclusion remains traceable to observations and evidence.
