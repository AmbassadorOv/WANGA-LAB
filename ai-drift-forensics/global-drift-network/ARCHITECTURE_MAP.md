# Global Science Network — Architecture Map

Version: 0.1.0

## 1. Public front door

The network is designed as a scientific town square: one discoverable public entry point with specialized workspaces behind it.

```text
                 GLOBAL SCIENCE NETWORK
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
 Discover Research   Find Scientists   Find Funding
       │                 │                 │
 Projects · Methods · Evidence · Data · Compute
                         │
                  Research Workspace
                         │
              Evidence + Compute Fabric
                         │
             Verification / Replication
                         │
                  Quality Gate
                         │
             Knowledge / Publication
```

## 2. Existing site family

The current Wix properties are treated as specialized front ends:

- International Ai For — international coordination / network gateway.
- AI Drift Forensics — AI drift detection and forensic services/research.
- Research Core — research-computing and research-infrastructure gateway.

The exact page content of these sites is not assumed here; this map uses their known site-level roles and current architecture work.

## 3. Backend principle

The sites should eventually converge on shared identifiers and services rather than independent databases:

```text
Person ID
Institution ID
Project ID
Experiment ID
Evidence ID
Method ID
Run ID
Snapshot ID
Finding ID
Claim ID
Publication ID
```

These identifiers form the backbone for cross-site navigation and traceability.

## 4. Scientific data graph

```text
Scientist ──participates──> Project
Project ──uses──> Method
Project ──produces──> Dataset
Experiment ──produces──> Observation
Observation ──creates──> Evidence
Evidence ──verified_by──> Verification
Evidence ──replicated_by──> Replication
Evidence ──supports──> Finding
Finding ──supports──> Claim
Claim ──appears_in──> Publication
Run ──produces──> Evidence
Snapshot ──defines──> Run input state
Institution ──hosts──> Scientist / Project / Node
```

## 5. Compute path

```text
Researcher
   ↓
Experiment specification
   ↓
Job / Run definition
   ↓
Orchestrator
   ↓
Queue
   ↓
Workers / Agents
   ↓
Research Compute Node
   ↓
Result + Evidence
   ↓
Verification
```

The future GSRC and Quantic OS concepts belong here as experimental compute layers. They do not replace the evidence/provenance contracts.

## 6. Governance path

```text
Scientific contribution
        ↓
Provenance + integrity
        ↓
Verification
        ↓
Replication / dispute handling
        ↓
Quality Gate
        ↓
Publication / public release
```

Governance is a control layer over the network, not a substitute for scientific evidence.

## 7. Economic separation

```text
OPEN SCIENCE COMMONS
       │
       ├── evidence / methods / discovery
       ├── collaboration
       └── public knowledge

PROFESSIONAL SERVICES
       ├── forensic investigations
       ├── verification
       ├── analysis
       └── government evidence packages

FUNDING LAYER
       ├── donors
       ├── grants
       └── research resource matching

OPTIONAL FUTURE ECONOMIC LAYER
       └── separate digital-asset architecture
```

No economic layer is required for the scientific network to function.

## 8. Extensibility rule

Every new architecture should declare:

1. parent layer;
2. purpose;
3. public/private scope;
4. identifiers consumed and produced;
5. evidence requirements;
6. dependencies;
7. implementation status;
8. whether it is experimental or production-oriented.

This prevents the project from becoming a collection of disconnected names and sites.
