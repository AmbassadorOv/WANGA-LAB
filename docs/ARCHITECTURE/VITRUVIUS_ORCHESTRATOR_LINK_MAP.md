# Vitruvius Orchestrator — Link Map

Status: SPECIFICATION / LINK TARGET REGISTRY
Version: 0.1.0

## Purpose

This file is the stable address book for connecting verified lineage, architecture, model, evidence, artifact, and validation records to the Vitruvius meta-architecture.

The conceptual structure is fixed first. Links are added only after the target is verified.

## Root

VITRUVIUS-ORCHESTRATOR
- Architecture: [ARCHITECTURE_LINK]
- Specification: docs/ARCHITECTURE/VITRUVIUS_ORCHESTRATOR_ARCHITECTURE.md
- ASCII: docs/ARCHITECTURE/VITRUVIUS_ORCHESTRATOR_ARCHITECTURE.ASCII.txt
- Registry: ARCHITECTURE_REGISTRY.json

## Upstream links

### WANGA Politeia
- Lineage: [LINEAGE_LINK]
- Architecture: [ARCHITECTURE_LINK]
- Knowledge records: [KNOWLEDGE_LINK]

### WANGA Lineage Tree
- Tree root: [LINEAGE_ROOT_LINK]
- Active families: [FAMILY_LINK]
- Descendant index: [DESCENDANT_LINK]

### Architecture Family Lineage
- Family registry: [FAMILY_REGISTRY_LINK]
- Architecture ancestry: [ANCESTRY_LINK]
- Architecture descendants: [DESCENDANT_LINK]

### Research Evolution Architecture
- Idea registry: [IDEA_LINK]
- Development events: [EVENT_LINK]
- Research-source links: [SOURCE_LINK]

## Vitruvius internal nodes

### Whole Architecture View
VITRUVIUS-WHOLE-VIEW
- [GLOBAL_ARCHITECTURE_LINK]
- [ARCHITECTURE_GRAPH_LINK]

### Lineage Reconstruction
VITRUVIUS-LINEAGE-RECONSTRUCTION
- [LINEAGE_LINK]
- [PROVENANCE_LINK]
- [ANCESTRY_LINK]
- [DESCENDANT_LINK]

### Knowledge Synthesis
VITRUVIUS-KNOWLEDGE-SYNTHESIS
- [KNOWLEDGE_LINK]
- [EVIDENCE_LINK]
- [CONSTRAINT_LINK]
- [VALIDATION_LINK]

### Candidate Model Space
VITRUVIUS-CANDIDATE-MODEL-SPACE
- [MODEL_LINK]
- [MODEL_FAMILY_LINK]
- [MODEL_LINEAGE_LINK]
- [COMPATIBILITY_LINK]

### Compatibility / Composition
VITRUVIUS-COMPATIBILITY
- [INTEGRATION_LINK]
- [COMPATIBILITY_OBSERVATION_LINK]
- [CONFLICT_LINK]
- [HISTORICAL_RESULT_LINK]

### Model Selection
VITRUVIUS-MODEL-SELECTION
- [SELECTION_RECORD_LINK]
- [CANDIDATE_SET_LINK]
- [KNOWLEDGE_LINK]
- [VALIDATION_LINK]

### Governance Handoff
VITRUVIUS-LOGIC-SELECTION-BOUNDARY
- [LOGIC_ARCHITECTURE_LINK]
- [LOGIC_MODEL_LINK]
- [HANDOFF_RECORD_LINK]

## Downstream

### Rational Logic Model Layer

The downstream logical layer receives a documented selection context. Proprietary implementation is not exposed by this registry.
- [LOGIC_ARCHITECTURE_LINK]
- [LOGIC_MODEL_LINK]
- [VALIDATION_LINK]

### Neural / Algorithmic Governance
- [GOVERNANCE_ARCHITECTURE_LINK]
- [EXECUTION_LINK]
- [AUDIT_LINK]

## Recursive return path

RESULT → VALIDATION → NEW KNOWLEDGE → NEW LINEAGE EVENT → DESCENDANT → VITRUVIUS UPDATE
- [RESULT_LINK]
- [VALIDATION_LINK]
- [KNOWLEDGE_LINK]
- [LINEAGE_EVENT_LINK]
- [DESCENDANT_LINK]

## Link integrity rule

A placeholder must remain a placeholder until its target is verified.

Do not add a link because a file name or concept appears similar. The target must be attributable to a specific repository path, source record, artifact, evidence record, decision, or validated object.

## Planned index types

- Human-readable architecture map
- Machine-readable lineage graph
- Machine-readable model registry
- Compatibility matrix
- Integration event registry
- Logic handoff registry
- Validation registry

These may be added later without changing the Vitruvius conceptual hierarchy.