# Research Architecture Map

This repository is the computational workspace for a broader research architecture. A researcher contributes within a specialized domain; connections between domains are explicit and evidence-based.

## Canonical architecture registry

The repository-level system hierarchy is defined in [`GLOBAL_ARCHITECTURE_REGISTRY.md`](./GLOBAL_ARCHITECTURE_REGISTRY.md). The machine-readable registry is [`ARCHITECTURE_REGISTRY.json`](./ARCHITECTURE_REGISTRY.json). This document focuses on the research-domain layer beneath that global architecture.

## Researcher Types

| Researcher type | Architectural node | Typical contribution | Suitable funding class |
|---|---|---|---|
| Rational-logic researcher | Rational Logic | conceptual distinctions, principles, relational analysis | research foundations, interdisciplinary institutes, patient capital |
| Logic / theoretical computer scientist | Superpositional Logic / Computational Logic | formalization, operators, composition rules, proofs | deep-tech research funds, academic grants, frontier-computing investors |
| Computational linguist / NLP researcher | Computational Linguistics | language structure, semantics, syntax, symbolic representations | language-AI funds, research grants, applied AI investors |
| Structural mathematician | Structural Mathematics | invariants, transformations, combinatorics, symmetry, quantitative tests | mathematics grants, scientific foundations, deep-tech funds |
| Software / systems architect | CCLE / AI Systems | executable architecture, APIs, reproducible infrastructure | deep-tech VC, infrastructure investors, engineering R&D partners |
| AI evaluation / reliability researcher | AI Drift Forensics | benchmarks, drift detection, provenance, failure analysis | AI safety/reliability funds, enterprise AI investors, research programs |
| Experimental researcher | Research Laboratory | controlled experiments, measurements, validation | scientific grants, R&D partnerships, technology programs |
| Computational philologist | Computational Linguistics / Research Library | source-critical corpora, historical language data, textual structure | humanities-digital research grants, computational humanities funds |
| Research-methodologist / epistemology researcher | Research Core / Convergence | methodology, evidence standards, reproducibility | interdisciplinary institutes, research foundations |
| Knowledge / library systems researcher | Research Library | source organization, provenance, evidence indexing | digital scholarship grants, research infrastructure programs |
| Cross-domain convergence researcher | Research Convergence | connects specialized results into a coherent network | interdisciplinary research centers, consortium funding |
| Validation / benchmarking specialist | Complete Architectural Validation | benchmark design, reproducibility, independent testing | scientific validation programs, standards/reliability funding |

## Funding Logic

Funding classes are research-fit categories, not a claim that any particular organization will fund the program. Match capital to the work being funded rather than forcing every domain into a single investor profile.

- Fundamental research: logic, mathematics, theoretical foundations.
- Frontier/deep-tech: computational architecture, CCLE, systems engineering.
- AI reliability: evaluation, drift detection, provenance, safety and robustness.
- Language technology: computational linguistics, semantic computation, multilingual systems.
- Scientific validation: experiments, benchmarks, reproducibility and independent verification.
- Digital scholarship: computational philology, research library, structured corpora.
- Interdisciplinary infrastructure: convergence, shared tooling, research networks.

## GitHub Working Structure

Suggested repository family:

- `WANGA-LAB` — shared laboratory kernel and common research workspace.
- `rational-logic` — foundational rational-logic research.
- `superpositional-logic` — definitions, operators, relational models and experiments.
- `computational-logic` — executable logic and composition models.
- `ccle` — Computational Compositional Logic Engine.
- `computational-linguistics` — language and symbolic structure.
- `structural-mathematics` — invariants, transformations and mathematical tests.
- `ai-systems` — computational architecture and system integration.
- `ai-drift-forensics` — evaluation, drift cases and provenance.
- `research-laboratory` — reproducible experiments and validation.
- `research-library` — sources, datasets, annotations and evidence.
- `research-convergence` — cross-domain interfaces and integration records.

The actual GitHub account currently exposes `AmbassadorOv/WANGA-LAB`; additional repositories can be created later as the research separates into stable modules.

## Integration Rule

A researcher should not be required to understand every other field. The contribution should be locally rigorous, documented, reproducible, and connected through explicit interfaces. Cross-domain researchers are responsible for building and testing the links between specialized nodes.
