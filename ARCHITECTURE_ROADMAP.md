# WANGA-LAB — Global Architecture Roadmap

Version: 0.2.1
Status: planning baseline

## Phase 0 — Foundation already present

The repository currently contains the research-domain architecture, AI Drift Forensics, Global Drift Network structures, research issue templates, an experimental ARK kernel, evidence/document-control specifications, and an execution queue/worker/quality-gate layer.

The Global Drift Network already defines a 12-role logical agent model, a 4-worker initial execution boundary, evidence/publication separation, and a GitHub-to-Wix publication bridge.

## Phase 1 — Make the registry authoritative

1. Keep `GLOBAL_ARCHITECTURE_REGISTRY.md` as the human-readable canonical map.
2. Keep `ARCHITECTURE_REGISTRY.json` as the machine-readable registry.
3. Require every new architecture to declare parent, scope, status, identifiers, dependencies, interfaces, and validation state.
4. Link every specialized specification back to the canonical registry.

## Phase 1A — Lineage knowledge and governance

Treat lineage management as a first-class architecture, not as administrative metadata.

Build and maintain:

1. Research Evolution Architecture
2. Architecture Family Lineage
3. WANGA Lineage Tree
4. WANGA Politeia

The Politeia layer converts lineage history, integration events, validation results, and descendant outcomes into reusable knowledge for future architecture composition.

The architecture prediction loop is:

`composition request → lineage inspection → compatibility knowledge → prediction → validation → integration → descendant → new lineage knowledge`

Every governance revision is itself a lineage event.

## Phase 2 — Build the shared scientific object model

Create stable identifiers and schemas for:

`PERSON, INSTITUTION, PROJECT, QUESTION, METHOD, EXPERIMENT, DATASET, OBSERVATION, EVIDENCE, VERIFICATION, REPLICATION, FINDING, CLAIM, RUN, SNAPSHOT, NODE, PUBLICATION`

The objective is not to create one giant database immediately. The objective is to define interoperable records so separate systems can reference the same scientific objects.

## Phase 3 — Scientific town square

Build the public discovery layer around the existing specialized web properties:

- Discover Research
- Find Scientists
- Find Projects
- Find Methods
- Find Evidence
- Find Data
- Find Compute
- Find Funding
- Find Collaborators
- Publish
- Verify
- Replicate

Any front end may become an entry point, but the shared identity/project/evidence model remains common.

## Phase 4 — Institutional network

Add institutional node concepts for universities, laboratories, research institutes, public research organizations, and industry laboratories. Each node receives explicit roles, access boundaries, research affiliations, and compute/evidence capabilities.

Private institutional workspaces remain isolated from the public commons except for deliberately published records.

## Phase 5 — Research execution fabric

Complete the executable research lifecycle:

`Research Request → Run Definition → Snapshot → Queue → Worker/Agent → Result → Evidence → Verification → Quality Gate → Publication`

Prioritize lease recovery, retry behavior, snapshot reduction, evidence linking, end-to-end tests, and controlled external data connectors before scaling autonomous agents.

## Phase 6 — Global scientific compute

Evolve the compute layer from local research jobs to connected research nodes. The future GSRC and Quantic OS concepts remain experimental until independently specified and validated.

The compute architecture must preserve reproducibility, provenance, isolation, and auditable execution regardless of hardware or runtime.

## Phase 7 — Knowledge graph and research marketplace

Connect people, institutions, projects, methods, evidence, findings, publications, funding opportunities, and compute resources into a navigable research graph.

Funding and resource matching should support discovery and coordination without becoming part of scientific verification.

## Phase 8 — Specialized and private extensions

Allow additional scientific networks, commercial services, institutional systems, domain-specific architectures, and experimental compute systems to attach as children of the global network.

No child architecture should redefine the common evidence or identity primitives without an explicit versioned interface change.

## Phase 9 — Optional future economic layer

A future digital-asset or network-economic architecture may be designed independently. It is not required for the scientific network, evidence commons, verification system, or public research portal to function.

Any future economic mechanism must therefore have its own specification, governance, accounting model, and legal review rather than being embedded invisibly into scientific records.

## Immediate build order

```text
1. Canonical architecture registry
2. Shared object identifiers + schemas
3. Cross-site identity/project/evidence model
4. Research discovery portal
5. Evidence / verification browser
6. Institutional node registry
7. Complete execution pipeline
8. Knowledge graph
9. Distributed research compute nodes
10. Future specialized/private/economic extensions
```
