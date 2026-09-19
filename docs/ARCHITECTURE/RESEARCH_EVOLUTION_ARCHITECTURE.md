# Research Evolution Architecture

This layer records how ideas develop and how each development becomes part of the WANGA architecture.

## Purpose

Git history records changes to files. This registry records the **history of ideas**:
- where an idea first appears
- how it changes
- what evidence or discussion caused the change
- which artifacts implement or represent it
- which architectural component it belongs to
- what remains unresolved

## Core rule

Do not rewrite history to make development look linear. Preserve abandoned, competing, and superseded formulations. Link them explicitly.

## Lineage model

`source → observation → idea → formulation → revision → formalization → artifact → integration → verification → current state`

An idea may branch, merge, be superseded, or remain open.

## Required records

Each idea should have:
- `idea_id`
- `canonical_name`
- `status`: emerging | active | formalized | implemented | verified | superseded | abandoned | open
- `first_seen`
- `source_refs`
- `previous_ideas`
- `derived_ideas`
- `related_artifacts`
- `architectural_target`
- `evidence_refs`
- `decision_refs`
- `open_questions`
- `last_updated`

## Architectural integration

Every mature idea should answer:
1. What architectural layer does it belong to?
2. Is it a concept, constraint, interface, data model, algorithm, artifact, or evidence?
3. Does it modify an existing component or introduce a new component?
4. What other ideas does it depend on?
5. What depends on it?
6. What changed when it entered the architecture?

## Conversation linkage

Conversation material should be indexed as provenance, not treated as the architecture itself. A conversation can:
- introduce an idea
- revise an idea
- reject an idea
- connect previously separate ideas
- produce an artifact
- expose an unresolved question

## Minimal event schema

`event_id, idea_id, timestamp, source_ref, event_type, predecessor, successor, architectural_effect, evidence, notes`

Event types:
`introduced, clarified, expanded, constrained, formalized, implemented, tested, connected, superseded, rejected, reopened`

## Relationship vocabulary

Use explicit edges:
- `DERIVED_FROM`
- `REFINES`
- `CONTRADICTS`
- `SUPERSEDES`
- `MERGES_WITH`
- `IMPLEMENTS`
- `REPRESENTS`
- `DEPENDS_ON`
- `INTEGRATES_INTO`
- `SUPPORTED_BY`
- `TESTED_BY`
- `OPENS_QUESTION`

## Separation of concerns

- **Git history** = file/code history.
- **Research Evolution Architecture** = idea/concept history.
- **Global Architecture Registry** = current architectural structure.
- **Corpus Integration Registry** = mapping of source artifacts into the architecture.
- **Triage Protocol** = intake and classification procedure.

These layers should cross-reference each other rather than duplicate one another.

## First integration target

The first pass should not attempt to reconstruct all historical material automatically. Start with the highest-value recurring concepts and progressively attach source references and artifacts. Unknown provenance must remain marked as unknown rather than invented.
