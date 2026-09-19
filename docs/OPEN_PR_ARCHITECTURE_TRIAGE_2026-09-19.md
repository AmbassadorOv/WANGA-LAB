# Open PR Architecture Triage — 2026-09-19

Purpose: classify open WANGA-LAB pull requests by architectural responsibility before integration.

## Integration groups

| Group | Responsibility | PRs | Disposition |
|---|---|---|---|
| Governance / Control Plane | operating contract, governance, continuity | #12, #26, #13 | #12/#13 merged; #26 selectively integrated as #37; original #26 superseded |
| Runtime / NTM | executable runtime and verification | #28, #19 | #28 merged; #19 superseded |
| Publication | GitHub/Wix/WordPress/publication layers | #29, #30, #31 | merged |
| Research Composition | external research synthesis and candidate discovery | #32 | merged as research-status material |
| AI Drift / Global Network | regional observations, queue, evidence publication | #9, #14 | secure clean integration prepared separately |
| Standards | governance/drift evidence candidate standard | #11 | merged; research specification only |
| Epistemic Reasoning | explicit-state reasoning frontier | #7 | merged |
| Dynamic Architecture | requirement-driven reversible architecture | #27 | retain as research specification pending conflict cleanup |
| Global Work Manager / Architecture Automation | repository-wide builder, model fabric, manager hierarchy | #15, #18 | retain for decomposition; do not merge wholesale |
| Legacy ARK / Experimental | older large ARK, SL, virtual compute and ontology branches | #3, #5, #6 | retain as historical/experimental source; not core integration |

## Evidence rule

Open PR status is not evidence of completion. Merge only after architecture ownership, security, tests, and duplication are checked.

## Immediate order

1. Maintain the current main integrity baseline.
2. Integrate secure Global Drift Network implementation.
3. Close superseded profile/control-plane/runtime duplicates.
4. Decompose #15/#18/#27 rather than merging large mixed-responsibility branches.
5. Keep legacy ARK branches as historical experimental sources until an explicit migration is justified.
