# Vitruvius Orchestrator — Deep Research and Architectural Constitution

Status: DEEP RESEARCH / ARCHITECTURAL BASELINE
Version: 0.2.0
Date: 2026-09-20
Repository: Quadruple-Multilevel-projection-project/WANGA-LAB

## 1. Executive finding

Vitruvius is defined in WANGA-LAB as the highest architectural orchestration layer immediately preceding the rational-logic model layer.

Its role is not to be the rational logic, a reasoning model, or a source of truth. Its role is to preserve and interpret the whole architectural context — research objects, evidence, lineages, architecture families, integrations, descendants, compatibility records, validation history, and candidate models — and to create the documented boundary through which candidate structures are selected for the rational-logic layer.

This is a project-specific architectural synthesis. External sources support several component principles — holistic architecting, architecture meta-models/viewpoints, provenance, lineage, decision records, and Plato's whole-system knowledge motif — but they do not establish the WANGA/Vitruvius architecture as an existing external standard.

## 2. Research question

How should WANGA-LAB organize a highest-level architectural orchestrator so that:

1. historical research and current architecture remain distinguishable;
2. ideas, methods, models, architectures and evidence retain lineage;
3. integrations ("lineage marriages") become explicit knowledge-producing events;
4. the whole architecture can be reconstructed from its parts and history;
5. candidate models can be selected for downstream logical roles without silently converting analogy, prediction, or provenance into logical fact;
6. every new descendant can feed verified knowledge back into the architectural whole;
7. the structure remains extensible across the repository's research groups and future branches.

## 3. Existing WANGA architectural substrate

The repository already contains:

- a canonical global architecture registry;
- Research Evolution Architecture;
- Architecture Family Lineage;
- WANGA Lineage Tree;
- WANGA Politeia;
- Vitruvius Orchestrator specification;
- Vitruvius ASCII architecture;
- Vitruvius Link Map;
- Vitruvius machine-readable index schema;
- Vitruvius automation and branch-planning scripts;
- research-group and research-asset registries.

The current Vitruvius files therefore constitute a coherent architectural family rather than an isolated new document.

## 4. Architectural hierarchy

The canonical hierarchy is:

    RESEARCH + KNOWLEDGE
            |
            v
    ARCHITECTURE FAMILIES
            |
            v
    WANGA LINEAGE SYSTEM
            |
            v
    LINEAGE MARRIAGE / INTEGRATION
            |
            v
    WANGA POLITEIA
            |
            v
    VITRUVIUS ORCHESTRATION
            |
            v
    MODEL SELECTION BOUNDARY
            |
            v
    RATIONAL LOGIC MODEL LAYER
            |
            v
    NEURAL / ALGORITHMIC GOVERNANCE
            |
            +--------------------+
                                 |
                                 v
                     VALIDATION / OBSERVATION
                                 |
                                 v
                         NEW LINEAGE EVENT
                                 |
                                 +----> back to Vitruvius

The critical boundary is between Vitruvius and Rational Logic.

Vitruvius provides selection context; Rational Logic remains a distinct downstream layer.

## 5. What the lineage system contributes

The lineage system is not merely historical metadata.

A lineage record can express:

- origin;
- parentage;
- development;
- inherited structure;
- revisions;
- branches;
- merges;
- superseded forms;
- descendants;
- integration history;
- evidence;
- validation state;
- unresolved questions.

This is consistent with the general provenance principle that entities, activities, agents, derivations and responsibility can be represented explicitly. W3C PROV describes provenance as information about entities, activities and agents involved in producing a thing, and supports derivation relationships between entities.

WANGA extends the concept project-specifically by treating architecture genealogy as an active selection context.

## 6. Lineage marriage

A "lineage marriage" is the WANGA term for an explicit integration event between two or more lineages.

It is not a metaphor that replaces technical semantics. The underlying object is an INTEGRATION_EVENT.

Minimum conceptual contents:

- participating lineages;
- reason for integration;
- inherited elements;
- newly introduced elements;
- compatibility state;
- conflicts;
- evidence;
- validation;
- resulting descendant;
- future constraints or opportunities.

The resulting descendant becomes a new lineage node.

Thus:

    A + B
      |
      v
    INTEGRATION_EVENT
      |
      v
      X
     /     C   D

X can itself become a parent in later integrations.

## 7. WANGA Politeia

WANGA Politeia is the whole-system governance/knowledge layer immediately upstream of Vitruvius.

Its structural inspiration is Plato's Politeia/Republic, but the WANGA implementation is not a political constitution.

The useful conceptual correspondence is the emphasis on knowledge of the whole and the relationship between knowledge and governance. The Stanford Encyclopedia of Philosophy describes Plato's Republic as linking political rule to comprehensive knowledge of the good and the Forms, and notes that the knowledge relevant to ruling is not merely a partial craft but concerns the city as a whole.

WANGA transforms that motif into an architectural knowledge system:

    individual ruler / philosopher
              |
              v
    knowledge of the whole
              |
              v
    WANGA lineage graph
              |
              v
    whole-system architectural knowledge
              |
              v
    Politeia governance context

The transformation must be kept explicit: this is an architectural analogy and design lineage, not a claim that WANGA implements Plato's political philosophy.

## 8. Why Vitruvius is the correct architectural level

Vitruvius is used as the name for the meta-architectural layer because Vitruvius's De architectura presents architecture as a discipline requiring both practice and reasoning and drawing on multiple fields of knowledge. The surviving treatise also addresses architecture together with engineering, planning and related disciplines.

The WANGA interpretation is narrower and computational:

    Vitruvius
       =
    whole-architecture composition context
       +
    lineage reconstruction
       +
    model candidate space
       +
    compatibility context
       +
    selection boundary
       +
    preserved provenance

This is a project naming decision, not a claim that ancient Vitruvius described software orchestration.

## 9. External architecture-framework comparison

### NATO Architecture Framework

NAF 4.1 explicitly defines architecture methodology, viewpoints, a meta-model, glossary and related artefacts. It also states that architecting supports decision makers through coherent views and that architecture practice should support understanding, comparison and integration.

WANGA shares the need for:

- a common architectural vocabulary;
- multiple views;
- meta-level organization;
- comparison and integration;
- explicit architecture artefacts.

WANGA differs in emphasis by making developmental genealogy and recursive descendant formation first-class elements of the architecture-selection context.

### Provenance standards

W3C PROV provides a formal vocabulary for entities, activities, agents, derivations and responsibility. This supports WANGA's insistence that a new object must retain origin and transformation context.

WANGA's lineage model is not a replacement for PROV. It can be mapped to provenance concepts where appropriate.

### Architecture Decision Records

ADR practice records significant architecture decisions, context, alternatives, decisions and consequences. This supports the WANGA requirement that architectural evolution not be reduced to the final state.

WANGA adds a broader genealogical layer: the decision is one event in a lineage rather than the complete lineage itself.

## 10. Vitruvius functional boundary

Vitruvius owns the architectural context immediately before logical-model selection.

It therefore owns these conceptual responsibilities:

### Whole architecture view
Maintain the current relationship among research domains, groups, assets, lineages, architecture families, models, evidence, validation and descendants.

### Lineage reconstruction
Reconstruct origin, ancestry, branches, merges, superseded forms and descendants.

### Knowledge synthesis
Bring together documented facts, constraints, compatibility history, conflict history and validation history.

### Candidate model space
Identify models that are candidates for a downstream logical role.

### Compatibility space
Represent compatibility as scoped states:

- COMPATIBLE
- CONDITIONALLY_COMPATIBLE
- INCOMPATIBLE
- UNKNOWN

### Selection boundary
Pass a documented selection context into the rational-logic layer.

### Recursive continuity
Accept new validated observations and descendants back into the architectural knowledge system.

## 11. What Vitruvius does not own

Vitruvius is not:

- the rational logic itself;
- a universal truth engine;
- a replacement for evidence;
- a provenance standard;
- an automatic proof of correctness;
- an authority that turns prediction into fact;
- a justification for silently rewriting historical lineage;
- a substitute for human or formal validation where required.

This boundary is essential to preserve epistemic integrity.

## 12. Research-group integration

The current WANGA research groups are:

1. RG-NEURAL-CORE
2. RG-NEURAL-OS
3. RG-MODEL-RUNTIME
4. RG-NODE-NETWORK
5. RG-MEMORY-KNOWLEDGE
6. RG-ARCHITECT-INTERFACE

Vitruvius sits above them as a composition/selection layer, not as a replacement for their domain responsibilities.

The group architecture is:

    DOMAIN
      |
      v
    RESEARCH GROUP
      |
      v
    PROJECT / ASSET
      |
      v
    LINEAGE
      |
      v
    EVIDENCE / VALIDATION
      |
      v
    VITRUVIUS WHOLE-ARCHITECTURE CONTEXT
      |
      v
    CANDIDATE MODEL / ARCHITECTURE COMPOSITION

## 13. Group-specific architectural relationship

### RG-NEURAL-CORE
Supplies research on neural representation, state, transition and behavior. Vitruvius preserves its lineage and can expose candidate neural structures to the appropriate downstream selection context.

### RG-NEURAL-OS
Supplies OS/kernel/memory/scheduling architecture. Vitruvius treats these as architectural families whose historical versions and dependencies matter when selecting future compositions.

### RG-MODEL-RUNTIME
Supplies model runtime and inference-adapter knowledge. Vitruvius records runtime compatibility as contextual architecture knowledge rather than assuming that a runtime is interchangeable with a model.

### RG-NODE-NETWORK
Supplies communication, synchronization and offline operation research. Vitruvius uses its topology and integration history as composition context.

### RG-MEMORY-KNOWLEDGE
Supplies provenance, evidence, memory and knowledge representation. This group is structurally central to Vitruvius because lineage and evidence must remain attributable.

### RG-ARCHITECT-INTERFACE
Supplies the architect workspace, project graph and human-machine interface. Vitruvius uses this as the presentation/control surface for the architectural whole, while keeping the underlying records machine-readable.

## 14. Research assets already mapped to groups

The current integration registry contains 15 mapped assets. Their role is not to become 15 independent top-level architectures. They are assets within the research-group architecture and should be linked upward through lineage and integration records.

This distinction prevents repository growth from being mistaken for architectural fragmentation.

## 15. Machine-readable model

The existing Vitruvius index schema defines a graph-like structure with nodes and edges.

The intended canonical pattern is:

    NODE
      |
      +-- source
      +-- domain
      +-- status
      +-- lineage
      +-- evidence
      +-- validation

    EDGE
      |
      +-- derived_from
      +-- contains
      +-- connected_to_group
      +-- integrates_with
      +-- compatible_with
      +-- supersedes
      +-- validates
      +-- descends_to

The exact schema can evolve, but semantic identity and provenance should not be silently changed.

## 16. ASCII as constitutional architecture

The ASCII file is not decorative documentation.

It is the stable conceptual map used to preserve the hierarchy while links, machine-readable records and future branches are added.

Its role is:

- human-readable canonical topology;
- stable node naming;
- stable branch points;
- explicit upstream/downstream boundaries;
- explicit recursive return path;
- attachment surface for future links.

Changes to the conceptual hierarchy should therefore be treated as architecture changes, not casual formatting changes.

## 17. Future branch rule

Every future branch should declare at least:

- branch identity;
- parent lineage or architecture;
- purpose;
- scope;
- source/evidence;
- dependencies;
- expected outputs;
- validation state;
- integration target;
- whether it is a new descendant, revision, merge, or specialized view.

A branch without lineage identity is not yet a valid architectural descendant.

## 18. Forecasting principle

Vitruvius may use historical compatibility and integration outcomes to generate candidate compositions.

That is a forecast or architectural recommendation context.

It must remain distinguishable from:

- verified evidence;
- formal proof;
- established fact;
- logical necessity.

The repository's existing verification and quality-gate structures remain the promotion boundary.

## 19. Architectural constitution

The complete WANGA architectural chain is therefore:

    SOURCE
      |
    RESEARCH
      |
    OBSERVATION / EVIDENCE
      |
    IDEA
      |
    FORMULATION
      |
    ARTIFACT / MODEL
      |
    ARCHITECTURE FAMILY
      |
    LINEAGE
      |
    INTEGRATION / MARRIAGE
      |
    DESCENDANT
      |
    POLITEIA WHOLE-SYSTEM KNOWLEDGE
      |
    VITRUVIUS
      |
    CANDIDATE MODEL SPACE
      |
    LOGIC HANDOFF
      |
    RATIONAL LOGIC
      |
    GOVERNANCE / REASONING
      |
    VALIDATION
      |
    NEW KNOWLEDGE
      |
      +-----------------------> LINEAGE

This is the architectural constitution to which later branches can attach without losing their ancestry.

## 20. Evidence status

The following are externally supported principles:

- Vitruvius's architecture treatise treats architecture as a multidisciplinary discipline involving practice and reasoning. [VITRUVIUS-EXT-01]
- NAF 4.1 defines methodology, viewpoints, meta-model and architecture artefacts for architecture development and description. [NAF-EXT-01]
- W3C PROV provides formal provenance concepts for entities, activities, agents and derivations. [PROV-EXT-01]
- ADR practice records significant architectural decisions, their context and consequences. [ADR-EXT-01]
- Plato's Republic links governance to a comprehensive form of knowledge and distinguishes whole-system governing knowledge from partial crafts. [PLATO-EXT-01]

The following are WANGA architectural design claims:

- Vitruvius is the highest orchestration layer immediately preceding Rational Logic.
- WANGA Politeia is the whole-system lineage governance layer.
- Lineage marriage is a first-class integration event.
- The ASCII architecture is a stable constitutional topology.
- Vitruvius maintains the model-selection boundary.
- Future descendants recursively update the architectural whole.

These are design specifications and should not be presented as external standards.

## 21. Primary references

- Vitruvius, De architectura / Ten Books on Architecture; MIT-hosted translation excerpt:
  https://stuff.mit.edu/afs/athena/course/21/21h.403/www/local/vitruvius_arch.bk.1.pdf
- MIT Press, Vitruvius:
  https://mitpress.mit.edu/9780262134156/vitruvius/
- NATO Architecture Framework 4.1:
  https://www.nato.int/en/about-us/organization/nato-structure/digital-policy-committee-dpc/nato-architecture-framework-version
- W3C PROV Primer:
  https://www.w3.org/TR/prov-primer/
- W3C PROV-DM:
  https://www.w3.org/TR/prov-dm/
- Stanford Encyclopedia of Philosophy, Ancient Political Philosophy:
  https://plato.stanford.edu/entries/ancient-political/
- Stanford Encyclopedia of Philosophy, Episteme and Techne:
  https://plato.stanford.edu/entries/episteme-techne/
- Microsoft Azure Well-Architected, Architecture Decision Records:
  https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record
- Google Cloud, Architecture Decision Records:
  https://docs.cloud.google.com/architecture/architecture-decision-records

## 22. Repository integration targets

- docs/ARCHITECTURE/VITRUVIUS_ORCHESTRATOR_ARCHITECTURE.md
- docs/ARCHITECTURE/VITRUVIUS_ORCHESTRATOR_ARCHITECTURE.ASCII.txt
- docs/ARCHITECTURE/VITRUVIUS_ORCHESTRATOR_LINK_MAP.md
- docs/ARCHITECTURE/WANGA_POLITEIA.md
- docs/ARCHITECTURE/WANGA_LINEAGE_SYSTEM.md
- docs/ARCHITECTURE/WANGA_LINEAGE_TREE.md
- docs/ARCHITECTURE/ARCHITECTURE_FAMILY_LINEAGE.md
- docs/ARCHITECTURE/RESEARCH_EVOLUTION_ARCHITECTURE.md
- GLOBAL_ARCHITECTURE_REGISTRY.md
- ARCHITECTURE_REGISTRY.json
- vitruvius/VITRUVIUS_INDEX_SCHEMA_V1.json
- vitruvius/MODEL_BRIDGE.md
- vitruvius/ARCHITECTURE_BRANCH_CAPACITY.json
- scripts/vitruvius_automation_engine.py
- scripts/vitruvius_branch_architecture_orchestrator.py
- wanga-research-groups/AGENT_GROUP_REGISTRY.json
- wanga-research-groups/RESEARCH_ASSET_INTEGRATION_REGISTRY_V1.json
