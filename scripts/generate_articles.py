#!/usr/bin/env python3
from pathlib import Path
import re
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")
titles=[x[2:].strip() for x in Path("data/articles.yml").read_text(encoding="utf-8").splitlines() if x.startswith("- ")]
out=Path("_posts"); out.mkdir(exist_ok=True)
for i,title in enumerate(titles,1):
 p=out/f"2026-09-{min(28,((i-1)//4)+1):02d}-{i:03d}-{slug(title)}.md"
 p.write_text(f'''---
layout: default
title: "{title}"
categories: [copernicus]
---
# {title}

This WANGA Copernicus research article examines a problem by first identifying the frame in which the problem was defined. It separates observation from interpretation, tests whether the boundary remains adequate, and preserves evidence for reconstruction.

## Research question

What changes when a problem is examined outside the conceptual boundary that originally produced it?

## Method

1. Identify the existing box or boundary.
2. Record its assumptions and criteria.
3. Separate observation, interpretation, inference, and prediction.
4. Test the boundary against the problem.
5. Preserve evidence and reconstruct the problem when the boundary is exhausted.

## WANGA connection

This node connects to Rational Logic, the Neural Thinking Machine, evidence and provenance, drift forensics, research groups, and the Copernicus publication layer. It is a research artifact; external factual claims require primary-source verification.
''',encoding="utf-8")
print("generated",len(titles),"article pages")