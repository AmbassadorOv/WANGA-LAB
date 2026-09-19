# Site Integration Registry

Version: 0.1.0
Status: ARCHITECTURE BASELINE

## Purpose

Map the existing web properties into one Global Science Network without forcing them to become identical products.

## Current properties

| Site | Known role | Network position | Status |
|---|---|---|---|
| International Ai For | International coordination | Network gateway | EXISTING |
| AI Drift Forensics | AI drift / forensic research and services | Specialized scientific + professional workspace | EXISTING |
| Research Core | Research-computing / research infrastructure | Compute gateway | EXISTING |

## Target relationship

```text
                    GLOBAL SCIENCE NETWORK
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
 International Gateway   Drift Forensics    Research Core
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                    Shared identity layer
                             │
             Shared project / evidence IDs
                             │
                 Shared provenance contracts
                             │
                    Shared knowledge graph
```

## Integration requirements

The sites should not independently invent identifiers for the same scientific object. The shared model should eventually provide stable IDs for:

- researcher;
- institution;
- project;
- experiment;
- dataset;
- method;
- evidence;
- run;
- snapshot;
- finding;
- claim;
- publication;
- compute node.

## Front-end rule

A scientist should be able to enter through any specialized site and move to the relevant part of the wider network without creating a second identity or duplicating project/evidence records.

## Missing integration components

These are architecture gaps to implement later:

1. Global landing/discovery layer.
2. Scientific identity and institution registry.
3. Shared project registry.
4. Shared evidence identifier service.
5. Cross-site search.
6. Knowledge graph.
7. Researcher/project collaboration directory.
8. Funding/resource directory.
9. Public publication/evidence browser.
10. Institutional node registry.
11. API/protocol boundary between front ends and the shared core.
12. Privacy/publication controls for private research spaces.

## Scope boundary

This registry describes integration architecture only. It does not claim that the current Wix sites already implement these backend capabilities.
