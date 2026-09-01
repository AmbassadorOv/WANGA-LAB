# Sod Ha-Bechinah: Formal Configuration Project

This LaTeX research project formalizes the conceptual framework of **Sod Ha-Bechinah** (סוד הבחינה), modeling relation, value, scale, proportion, and hierarchical revelation through rigorous mathematical objects, information-theoretic abstractions, category-theoretic transformations, and TikZ visual diagrams.

## Compilation Instructions

The document is designed for modern LaTeX engines supporting Hebrew typography and Unicode math notation (such as XeLaTeX or LuaLaTeX).

```bash
cd Sod_HaBechina_Configuration
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

Or using `latexmk`:

```bash
cd Sod_HaBechina_Configuration
latexmk -xelatex main.tex
```

## Structure

- `main.tex`: Document entry point and preamble.
- `bibliography.bib`: BibTeX citations combining classical textual sources and modern mathematical literature.
- `sections/`: 13 substantive LaTeX section modules.
- `tikz/`: Standalone TikZ visual diagrams.
- `figures/`: Graphical figures and output assets.
- `README_visual_spec.md`: Canva / visual design export specifications.

## Methodological Disclaimer

This project constructs a formal computational modeling layer inspired by traditional concepts. It explicitly distinguishes mathematical definitions from historical, interpretive, or metaphysical claims.
