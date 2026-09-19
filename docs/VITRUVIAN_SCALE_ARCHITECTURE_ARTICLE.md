# From Architecture Graph to Vitruvian Scale Architecture

## Abstract

WANGA is evolving from a collection of related architectures into a single computational architecture whose structure can continuously discover and represent new relationships.

The central mechanism is **Vitruvian Scale Architecture**: an architectural intelligence layer in which Vitruvius observes the existing architecture family tree and relationship graph, classifies new or changed architectures, and searches for additional connections across levels.

The objective is not to freeze the architecture in a single diagram. The objective is to make the architecture capable of describing its own expansion while preserving evidence, provenance, verification boundaries and historical direction.

## 1. The architectural problem

A complex computational system is rarely one architecture. WANGA contains operating architecture, work management, model/runtime architecture, translation, agents, evidence and provenance, drift forensics, reasoning, memory and governance. These systems overlap.

A simple tree is therefore insufficient. A simple graph is also insufficient if it only records currently known edges.

The required structure combines a **family tree** for architectural lineage, a **relationship graph** for cross-family connections, a **work graph** for branches and bounded implementation tasks, and an **evidence graph** for proving what was actually built and verified.

Vitruvius is the layer that keeps these representations connected.

## 2. Vitruvian Scale Architecture

The Vitruvian Scale Architecture is the upper architecture. Its function is to continuously answer: What architecture is this? Which family does it belong to? What parent architecture contains or constrains it? Which sibling architectures can interact with it? Which interfaces does it expose? Which architectures depend on it? Which evidence and verification systems are affected? Which branches and work items are affected by a change?

The important word is **scale**. The same classification process operates at multiple levels: global architecture, subsystem, component, interface, artifact and work item.

## 3. Fractal discovery

Suppose architecture A is connected to B. Vitruvius does not stop at A → B. It examines B's family, B's interfaces, connected architectures, affected branches, evidence dependencies and verification dependencies.

A newly discovered connection can therefore expose another connection. This creates a controlled form of **architectural fractality**: not geometric self-similarity, but recursive reuse of the same relationship-discovery logic at different architectural scales.

Vitruvius does not declare every discovered edge to be true. It records discovery separately from verification.

## 4. The two architectures

### Upper: Vitruvian Scale Architecture

This is the architecture of architectural knowledge. It contains architecture families, parent/child relationships, cross-family relationships, interfaces, dependency maps, impact maps, branch mappings, evidence boundaries and verification states. Its engine is Vitruvius.

### Lower: Digital Engine Architecture

This is the architecture of computational execution. It contains Work Control, Translation, Model Fabric, Digital Model Agents, Evidence & Provenance, Drift Forensics, Rational Logic / NTM interfaces, Work Memory and Governance interfaces.

Its purpose is to turn architectural intent into bounded computational work and then preserve the resulting artifacts and evidence.

## 5. The internal engine

The internal engine can be described conceptually as the **steam-engine layer**: the part that performs the work. The term is an analogy for a work-producing core, not a statement that the system contains physical steam machinery.

The Digital Engine Architecture is the digital wrapper and execution environment around that core.

Therefore:

Vitruvian Scale Architecture = architecture of relationships

Digital Engine Architecture = architecture of execution

Internal Engine = work-producing computational core

## 6. Vitruvius as the bridge

When an architecture changes:

CHANGE → DISCOVER → CLASSIFY → TRACE FAMILY → TRACE RELATIONSHIPS → CALCULATE IMPACT → ROUTE WORK → EXECUTE → PRESERVE EVIDENCE → VERIFY → UPDATE GRAPH

This creates a closed architectural feedback loop. The graph is not merely documentation. It becomes an operational input to work routing.

## 7. Relationship states

The system uses an explicit evidence-aware lifecycle:

DISCOVERED → CANDIDATE → MAPPED → IMPLEMENTED → TESTED → VERIFIED

Vitruvius owns discovery and mapping. Independent verification owns promotion.

## 8. Branches are not architectures

A Git branch represents a workspace for change. It is therefore linked to an architecture rather than being treated as the architecture itself. One architecture may have many branches. One integration branch may touch multiple architectures. Vitruvius identifies these intersections and produces an affected-work set for the Global Work Manager.

## 9. Resulting WANGA structure

VITRUVIAN SCALE ARCHITECTURE
↓
ARCHITECTURE FAMILY TREE
↓
RELATIONSHIP GRAPH
↓
GLOBAL WORK MANAGER
↓
DIGITAL ENGINE ARCHITECTURE
↓
MODEL / AGENT EXECUTION
↓
EVIDENCE & PROVENANCE
↓
DRIFT FORENSICS / VERIFICATION
↓
UPDATED ARCHITECTURE GRAPH

The final step is essential: verification produces new knowledge about the architecture, and that knowledge becomes input to the next Vitruvius cycle.

## 10. Architectural objective

The objective is not simply to build a large collection of components. It is to build a system capable of **continuously discovering the architecture of what is being built**.

Vitruvius provides the architectural intelligence. The Vitruvian Scale Architecture provides the upper structural frame. The Digital Engine Architecture provides the lower execution frame. Evidence and verification prevent the architecture from becoming detached from what has actually been built.

Together these layers form the basis for a continuously expanding WANGA computational architecture.
