# Architecture Family Lineage

This registry extends Research Evolution Architecture from individual ideas to complete architectural families.

## Purpose

Every architecture in WANGA should have a traceable family history: origin, parent architectures, inherited principles, mutations and revisions, branches, merges, superseded forms, descendants, and current integration point in the Global Architecture Registry.

An architecture family is not required to be linear. It may branch, merge, or contain abandoned forms.

## Family model

origin → prototype → architecture → revision → branch → merge → integration → descendant

## Family record

Each architecture family should have:
- family_id
- canonical_name
- status
- origin_refs
- parent_architectures
- child_architectures
- ancestor_ideas
- inherited_components
- introduced_components
- removed_or_superseded_components
- architectural_target
- artifact_refs
- evidence_refs
- decision_refs
- open_questions
- last_updated

## Architecture relationship vocabulary

- DESCENDS_FROM
- DERIVES_FROM
- INHERITS
- EXTENDS
- REFACTORS
- SPLITS_FROM
- MERGES_WITH
- SUPERSEDES
- RECOMBINES
- INTEGRATES_INTO
- DEPENDS_ON
- IMPLEMENTS
- VALIDATES

## Required lineage questions

For every architecture:
1. What is its parent or origin?
2. Which principles did it inherit?
3. What new problem caused it to appear?
4. What did it change?
5. What earlier architecture did it preserve or supersede?
6. Which descendants were produced from it?
7. Where does it currently live in the global architecture?
8. Which artifacts and evidence support the lineage?

## Separation

RESEARCH_EVOLUTION_ARCHITECTURE.md tracks the genealogy of ideas.

This file tracks the genealogy of architectures.

GLOBAL_ARCHITECTURE_REGISTRY.md tracks the current architecture.

The three must cross-reference each other.

## Rule

Never infer a parent merely because two architectures look similar. A lineage edge requires a source reference, explicit project decision, or documented derivation. If the origin is unknown, record UNKNOWN_ORIGIN.
