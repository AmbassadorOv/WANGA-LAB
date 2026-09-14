# WANGA-LAB

## Research Architecture

WANGA-LAB is the shared computational workspace for a larger research program spanning rational logic, Superpositional Logic, computational logic, CCLE, computational linguistics, structural mathematics, AI systems, AI evaluation and drift forensics, experimentation, research library work, and research convergence.

The laboratory separates three things that are often mixed together:

1. **Research** — questions, hypotheses, evidence and interpretation.
2. **Implementation** — code, tests, datasets, experiments and reproducible runs.
3. **Integration** — explicit interfaces connecting specialized research domains.

## Core Computational Primitive

**Object + Relation + Composition → New Object → State → Recursive Composition**

A compact state transition is represented as:

**Cₙ₊₁ = F(Cₙ, Rₙ, Sₙ)**

This is a working computational representation, not a claim that the architecture has already been mathematically proven.

## How to Contribute

Use GitHub Issues for structured research questions, experiments, AI-drift forensic cases, and researcher profiles. Contributions should identify evidence, scope, reproducibility requirements, and expected architectural interfaces.

See [`RESEARCH_ARCHITECTURE_MAP.md`](./RESEARCH_ARCHITECTURE_MAP.md) for the researcher-role, funding-fit, and repository map.

## Current Shared Workspace

The existing laboratory code includes the ARK kernel and tests. The repository can later be split into stable domain repositories as the research modules become sufficiently mature.
