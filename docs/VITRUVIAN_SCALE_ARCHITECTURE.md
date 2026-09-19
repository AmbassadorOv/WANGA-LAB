# Vitruvian Scale Architecture

The **Vitruvian Scale Architecture (VSA)** is the upper architectural intelligence that continuously discovers additional compositional relationships among the architectures being built in WANGA.

It treats the architecture as a family tree plus a relationship graph: each architecture may contain subarchitectures, depend on other architectures, expose interfaces, share evidence, inherit constraints, or participate in a larger composition.

## Fractal relationship principle

A newly added or changed architecture is not classified in isolation. Vitruvius repeatedly evaluates:

NEW ARCHITECTURE → FAMILY → SIBLINGS → PARENT → CHILDREN → CROSS-FAMILY RELATIONS → GLOBAL GRAPH

A relationship discovered at one level may expose another relationship at the next level. This produces relationship fractals: progressively finer connection patterns represented without requiring every relationship to be known in advance.

## Two-level architecture model

- **Upper architecture — Vitruvian Scale Architecture:** discovers, classifies, composes and governs relationships among architectures.
- **Lower architecture — Digital Engine Architecture:** represents the executable computational machinery that implements the discovered architecture.
- **Internal engine:** the computational core is modeled as the system's foundational engine layer; the historical “steam engine” analogy describes its role as the source of mechanical work, not physical machinery.

The upper layer describes **what connects to what and why**. The lower layer describes **how the connected system executes**.

## Authority boundary

Vitruvius may discover and propose. It must not promote a relationship to VERIFIED merely because the graph contains it. Promotion requires independent evidence and verification.

## Relationship lifecycle

DISCOVERED → CANDIDATE → MAPPED → IMPLEMENTED → TESTED → VERIFIED

## Invariants

1. A branch is a work location, not an architecture.
2. An architecture may have many branches.
3. An architecture may belong to multiple architectural families.
4. A relationship may be direct, inherited, transitive, interface-based, evidence-based or governance-based.
5. Historical architecture is preserved rather than silently discarded.
6. Protected Rational Logic implementation remains outside the public graph.

## Atomic scale

The Vitruvian Scale is recursive down to the **family atom** level. A family atom is the smallest declared architectural concept that remains independently addressable in the relationship graph. An atom may belong to multiple root families, producing explicit cross-family bridges rather than forcing a false single-family classification.

Atomic path:

ARCHITECTURE → FAMILY → SUBFAMILY → FAMILY ATOM → SUBATOM → NEURAL ATOM ENDPOINT → GLOBAL NETWORK

Governance is attached at the atom boundary through P0-P7 mappings. This lets a descendant inherit the controls relevant to its function while retaining its own lineage and verification state.
