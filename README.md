# WANGA-LAB

## Research Architecture

WANGA-LAB is the shared computational workspace for a larger research program spanning rational logic, Superpositional Logic, computational logic, CCLE, computational linguistics, structural mathematics, AI systems, AI evaluation and drift forensics, experimentation, research library work, and research convergence.

The laboratory separates three things that are often mixed together:

1. **Research** — questions, hypotheses, evidence and interpretation.
2. **Implementation** — code, tests, datasets, experiments and reproducible runs.
3. **Integration** — explicit interfaces connecting specialized research domains.

## Global Architecture

The repository is organized as a modular research ecosystem rather than a single application. The canonical architecture registry defines the parent/child relationship between the scientific commons, research domains, Global Drift Network, execution fabric, compute concepts, institutional network, public research interfaces, and future private or experimental extensions.

See [`GLOBAL_ARCHITECTURE_REGISTRY.md`](./GLOBAL_ARCHITECTURE_REGISTRY.md) for the canonical human-readable map, [`ARCHITECTURE_REGISTRY.json`](./ARCHITECTURE_REGISTRY.json) for the machine-readable registry, and [`ARCHITECTURE_ROADMAP.md`](./ARCHITECTURE_ROADMAP.md) for the build sequence.

## Core Computational Primitive

**Object + Relation + Composition → New Object → State → Recursive Composition**

A compact state transition is represented as:

**Cₙ₊₁ = F(Cₙ, Rₙ, Sₙ)**

This is a working computational representation, not a claim that the architecture has already been mathematically proven.

## How to Contribute

Use GitHub Issues for structured research questions, experiments, AI-drift forensic cases, and researcher profiles. Contributions should identify evidence, scope, reproducibility requirements, and expected architectural interfaces.

See [`RESEARCH_ARCHITECTURE_MAP.md`](./RESEARCH_ARCHITECTURE_MAP.md) for the researcher-role, funding-fit, domain, and repository map.

## Current Shared Workspace

The existing laboratory includes the ARK kernel and tests, research-domain specifications, Global Drift Network infrastructure, evidence/document-control components, execution queue and worker components, and publication workflow definitions.

Specialized systems can later become dedicated repositories when their interfaces and validation state justify separation. Until then, WANGA-LAB remains the common integration workspace.
