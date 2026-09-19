# Global Science Network — Master Architecture Registry

Status: ARCHITECTURE BASELINE
Version: 0.2.0

## Canonical position

The repository-level canonical architecture is [`/GLOBAL_ARCHITECTURE_REGISTRY.md`](../../../GLOBAL_ARCHITECTURE_REGISTRY.md). This file is the domain-specific registry for Global Drift Network and must remain consistent with the repository-level registry.

## System hierarchy

```text
GLOBAL SCIENCE NETWORK
│
├── SCIENTIFIC COMMONS
├── RESEARCH ARCHITECTURE
├── GLOBAL DRIFT NETWORK
│   ├── Observation
│   ├── Normalization
│   ├── Drift Detection
│   ├── Cross-Surface Analysis
│   ├── Verification
│   ├── Evidence Commons
│   └── Daily Scientific Publication
├── RESEARCH EXECUTION FABRIC
├── COMPUTE FABRIC
├── KNOWLEDGE & PUBLICATION
├── FUNDING & COLLABORATION
├── INSTITUTIONAL NETWORK
├── PUBLIC SCIENTIFIC TOWN SQUARE
└── FUTURE / PRIVATE / EXPERIMENTAL EXTENSIONS
```

## Global Drift Network components

| Component | Status | Function |
|---|---|---|
| Observation Plane | BUILDING | Capture and normalize observations |
| Analysis Plane | BUILDING | Temporal, geographic, language and surface analysis |
| Scientific Control Plane | BUILDING | Verification and attribution discipline |
| Public Research Plane | BUILDING | Demand signals and publication bridge |
| Evidence Register | BUILDING | Stable evidence identity and provenance |
| Orchestrator / Queue | BUILDING | Persistent task execution |
| Worker Fabric | BUILDING | Modular observation, analysis, verification and publication responsibilities |
| Quality Gate | EXISTING | Barrier between analysis and release |
| Government Document Control | EXISTING | Controlled document metadata |
| International Drift Propagation | BUILDING | Cross-region and cross-language propagation research |

## Scientific lifecycle

```text
Observation
  ↓
Normalization
  ↓
Analysis
  ↓
Evidence
  ↓
Verification
  ↓
Replication / Dispute
  ↓
Finding
  ↓
Claim
  ↓
Quality Gate
  ↓
Publication
```

## Twelve logical agent roles

1. Scout
2. Normalizer
3. Baseline
4. Drift Detector
5. Temporal
6. Geospatial
7. Language
8. Surface Graph
9. Verification
10. Attribution
11. Demand
12. Digest & Publication

These roles are architectural responsibilities. The initial implementation may execute them through fewer worker processes.

## Evidence discipline

Raw observations, derived metrics, interpretations, and hypotheses remain distinct. Temporal association is not automatically causal attribution. Missing data, failed reproductions, rejected evidence, and unresolved questions must remain visible in the research record.

## Publication boundary

```text
GitHub research record
        ↓
Evidence / finding selection
        ↓
Quality Gate
        ↓
Wix draft
        ↓
Authorized release
        ↓
Public publication
```

The public Wix layer is a dissemination interface, not the scientific source of truth.

## Scope boundary

Global Drift Network is a specialized child architecture of the broader Global Science Network. It must not absorb institutional identity, funding, general research discovery, or future compute architectures into its own namespace. Those capabilities belong to their respective parent layers and should connect through explicit interfaces.
