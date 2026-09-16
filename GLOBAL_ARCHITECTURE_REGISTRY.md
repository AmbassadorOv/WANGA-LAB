# WANGA-LAB — Canonical Global Architecture Registry

Status: ARCHITECTURE BASELINE
Version: 0.2.0

## Purpose

This is the repository-level registry for the complete research ecosystem represented by WANGA-LAB. It is the canonical index of architectures, systems, interfaces, and future extension points. It does not replace specialized specifications; it records where they belong and how they connect.

## Master hierarchy

```text
GLOBAL SCIENCE NETWORK
│
├── A. SCIENTIFIC COMMONS
│   ├── Researcher Identity
│   ├── Institutions / Laboratories
│   ├── Research Projects
│   ├── Research Questions
│   ├── Methods
│   ├── Experiments
│   ├── Data / Datasets
│   ├── Evidence
│   ├── Findings / Claims
│   ├── Publications
│   └── Knowledge Graph
│
├── B. RESEARCH ARCHITECTURE
│   ├── Rational Logic
│   ├── Superpositional Logic
│   ├── Structural Analysis
│   ├── Computational Logic
│   ├── CCLE
│   ├── Computational Linguistics
│   ├── Structural Mathematics
│   ├── AI Systems
│   ├── AI Evaluation & Drift Forensics
│   ├── Research Laboratory
│   ├── Research Library & Convergence
│   └── Complete Architectural Validation
│
├── C. GLOBAL DRIFT NETWORK
│   ├── Observation Plane
│   ├── Analysis Plane
│   ├── Scientific Control Plane
│   ├── Public Research Plane
│   ├── International Drift Propagation
│   ├── Evidence Commons
│   └── Daily Science Publication
│
├── D. RESEARCH EXECUTION FABRIC
│   ├── Run Definitions
│   ├── Immutable Snapshots
│   ├── Orchestrator
│   ├── Persistent Task Queue
│   ├── Worker / Agent Contracts
│   ├── Audit Events
│   ├── Verification
│   └── Quality Gate
│
├── E. COMPUTE FABRIC
│   ├── Research Compute Nodes
│   ├── Scientific Jobs
│   ├── GSRC (future concept)
│   ├── Quantic OS (future concept)
│   ├── AI²³¹ / EAQP research stack
│   ├── Quantic Memory (future concept)
│   └── Future hardware extensions
│
├── F. KNOWLEDGE & PUBLICATION
│   ├── Evidence-to-Claim Traceability
│   ├── Research Library
│   ├── Scientific Digest
│   ├── Government Evidence Packages
│   ├── Government Document Control
│   └── Public Publication Interfaces
│
├── G. FUNDING & COLLABORATION
│   ├── Funders / Donors
│   ├── Grants / Research Requests
│   ├── Resource Matching
│   ├── Collaborator Discovery
│   └── Investor / Research Liaison
│
├── H. INSTITUTIONAL NETWORK
│   ├── University Nodes
│   ├── Research Institute Nodes
│   ├── Government / Public Research Nodes
│   ├── Industry / Laboratory Nodes
│   └── Institutional Roles and Access
│
├── I. PUBLIC WEB / TOWN SQUARE
│   ├── International Gateway
│   ├── Research Discovery
│   ├── Scientist Directory
│   ├── Project Directory
│   ├── Evidence Browser
│   ├── Methods Browser
│   ├── Compute / Resource Discovery
│   ├── Funding Discovery
│   ├── Collaboration
│   └── Publication Portal
│
└── J. FUTURE / PRIVATE / EXPERIMENTAL EXTENSIONS
    ├── Private research spaces
    ├── Domain-specific networks
    ├── New compute architectures
    ├── Proprietary services
    └── Optional future economic / digital-asset architecture
```

## Existing repository architectures

| Architecture | Repository evidence | Status | Parent |
|---|---|---|---|
| Research Architecture | `RESEARCH_ARCHITECTURE_MAP.md`, `research-architecture/` | EXISTING | B Research Architecture |
| AI Drift Forensics | `ai-drift-forensics/` | EXISTING | C Global Drift Network |
| Global Drift Network | `ai-drift-forensics/global-drift-network/` | BUILDING | C Global Drift Network |
| International Drift Propagation | `international-drift-propagation/` | BUILDING | C Global Drift Network |
| Evidence Register | `publication/GOVERNMENT_EVIDENCE_REGISTER.schema.json` and evidence components | BUILDING | C/D |
| Execution Queue | `orchestrator/queue.py` and queue protocol | BUILDING | D |
| Worker Fabric | `orchestrator/worker_adapter.py`, `workers.py` | BUILDING | D |
| Quality Gate | `orchestrator/QUALITY_GATE.md` | EXISTING | D/F |
| Government Document Control | `publication/GOVERNMENT_DOCUMENT_CONTROL.md` | EXISTING | F |
| Daily Science Publication Pipeline | `DAILY_SCIENCE_PUBLICATION_PIPELINE.md` | EXISTING | F |
| Researcher / Experiment Issue Interfaces | `.github/ISSUE_TEMPLATE/` | EXISTING | A/B |
| ARK Kernel | `ark_kernel.py` | EXISTING EXPERIMENTAL | E / J |

## Existing research-domain architectures

The repository already defines a domain/subdomain/group model covering Rational Logic, Superpositional Logic, Structural Analysis, Computational Logic, CCLE, Computational Linguistics, Structural Mathematics, AI Systems, AI Evaluation & Drift Forensics, Research Laboratory, Research Library & Convergence, and Complete Architectural Validation.

These domains are complementary research nodes. They are not separate public platforms unless later promoted into dedicated repositories or services.

## Known web properties

The current Wix family is represented as specialized public interfaces:

| Property | Network role | Status |
|---|---|---|
| International Ai For | International coordination / gateway | EXISTING WEB PROPERTY |
| AI Drift Forensics | Drift research / forensic professional interface | EXISTING WEB PROPERTY |
| Research Core | Research-compute / research infrastructure interface | EXISTING WEB PROPERTY |

This registry does not claim that the Wix properties already implement the shared backend. The shared backend is the architecture target.

## Canonical scientific object identifiers

The future network should use stable identifiers for:

`PERSON → INSTITUTION → PROJECT → QUESTION → METHOD → EXPERIMENT → DATASET → OBSERVATION → EVIDENCE → VERIFICATION → REPLICATION → FINDING → CLAIM → RUN → SNAPSHOT → NODE → PUBLICATION`

These objects should be linkable across specialized sites, repositories, institutional nodes, and research-compute environments.

## Scientific lifecycle

```text
Researcher / Institution
        ↓
Research Question
        ↓
Project
        ↓
Method + Experiment
        ↓
Run / Snapshot
        ↓
Observation / Result
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
        ↓
Knowledge Graph
        ↓
New Research Question
```

## Separation boundaries

The following must remain distinguishable:

1. Scientific evidence vs. interpretation.
2. Open commons vs. paid professional services.
3. Public publication vs. private research workspace.
4. Experimental architecture vs. validated production infrastructure.
5. Research funding vs. scientific conclusions.
6. Optional economic mechanisms vs. the scientific evidence system.

## Architecture admission rule

Every new architecture added to WANGA-LAB must declare:

- `architecture_id`
- `name`
- `parent_architecture`
- `purpose`
- `scope` (`PUBLIC`, `INSTITUTIONAL`, `PRIVATE`, `EXPERIMENTAL`, `SERVICE`)
- `status` (`IDEA`, `PLANNED`, `BUILDING`, `EXISTING`, `VALIDATED`, `RETIRED`)
- `inputs`
- `outputs`
- `identifiers_used`
- `evidence_requirements`
- `dependencies`
- `interface_contracts`
- `validation_state`

This makes the architecture extensible without allowing new names to become disconnected systems.
