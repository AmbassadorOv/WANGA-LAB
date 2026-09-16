# GLOBAL DRIFT NETWORK

## Global Science Network architecture

This workspace is the AI-drift evidence and forensic branch of a broader Global Science Network: a modular scientific commons for research discovery, evidence, verification, computation, collaboration, publication, and future institutional research nodes.

### Architecture index

- [Repository Canonical Architecture Registry](../../../GLOBAL_ARCHITECTURE_REGISTRY.md) — top-level architecture and status map.
- [Machine-readable Architecture Registry](../../../ARCHITECTURE_REGISTRY.json) — structured architecture records.
- [Master GDN Architecture Registry](./MASTER_ARCHITECTURE_REGISTRY.md) — GDN-specific architecture and status map.
- [Architecture Map](./ARCHITECTURE_MAP.md) — system relationships and data/compute flows.
- [Site Integration Registry](./SITE_INTEGRATION_REGISTRY.md) — maps current web properties into the network.
- [Global Architecture Roadmap](../../../ARCHITECTURE_ROADMAP.md) — staged implementation plan.
- [Evidence Register Schema](./publication/GOVERNMENT_EVIDENCE_REGISTER.schema.json) — machine-readable evidence contract.
- [Quality Gate](./orchestrator/QUALITY_GATE.md) — publication barrier.
- [Queue Protocol](./orchestrator/QUEUE_PROTOCOL.md) — execution boundary.

## Scientific town-square model

```text
                    GLOBAL SCIENCE NETWORK
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
 Discover Research      Find Scientists       Find Funding
       │                     │                     │
       └──────────── Projects · Methods · Evidence ─┘
                             │
                     Research Workspace
                             │
                  Verification / Replication
                             │
                       Compute Fabric
                             │
                       Publication
                             │
                     Knowledge Graph
                             │
                    New Research / Funding
```

The public layer is the common entry point. Specialized systems remain modular children of the network.

## Existing research program

This workspace is also a research container for measuring time-varying changes across AI and information surfaces in multiple regions and languages during a high-intensity public event.

The project is observational. It does not assume that an election, publication, institution, or public figure caused any measured change.

## Core question

Can measurable changes in AI/system behavior be observed across geographic, linguistic, and informational surfaces, and can their timing and cross-surface relationships be mapped over a common timeline?

## Observation dimensions

- Time
- Geography
- Language
- AI/model surface
- Search surface
- News/public-information surface
- Event context
- Drift signature
- Cross-surface relationship

## Primary outputs

1. 30-day longitudinal dataset
2. 72-hour high-resolution event window
3. Regional drift timelines
4. Cross-language comparisons
5. Cross-surface interaction graph
6. Global drift map
7. Reproducible observation records
8. Unresolved-question register

## Evidence discipline

Raw observations, derived metrics, and interpretations must remain separate. A temporal association is not automatically a causal attribution. The dataset should preserve null results and failed reproductions.

## Initial structure

- `protocol/` — research protocol and sampling plan
- `schema/` — observation schemas
- `data/` — raw and normalized observations
- `events/` — event timeline and context records
- `analysis/` — derived drift and propagation analysis
- `reports/` — daily and final reports
- `visualization/` — timelines, matrices, and network graphs
- `orchestrator/` — deterministic execution and worker layer
- `publication/` — evidence packages and document control

## Architectural boundary

The broader Global Science Network is staged. Existing implementation, planned components, concepts, and future extensions are explicitly distinguished in the registry. The repository should not present conceptual hardware, Quantic OS, AI²³¹, or future economic layers as already deployed systems.
