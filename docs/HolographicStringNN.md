# ARK — Holographic String Neural Network

## Status

**Research implementation / architectural prototype — not a verified physical model.**

This library translates the supplied ARK specification into executable, deterministic
symbolic rules. It does **not** claim that Hebrew-letter classifications or
Sephirotic mappings constitute empirically validated neural-network physics.

## Core model

The network contains **22 HolographicStringNode** identities:

- **3 Mothers (אמות):** א, מ, ש
- **7 Doubles (כפולות):** ב, ג, ד, כ, פ, ר, ת
- **12 Simples (פשוטות):** ה, ו, ז, ח, ט, י, ל, נ, ס, ע, צ, ק

The implementation deliberately avoids a conventional numeric weight for letter
identity. A node's symbolic weight is the pair:

`(letter group, Sephirotic line)`

The runtime additionally measures a numeric **coherence** value because a collapse
threshold cannot be evaluated without a measurable runtime signal.

## Collapse policy

The operational examples imply the following deterministic gate:

1. Coherence must meet the configured stability threshold (default 0.95).
2. Mothers may collapse once stable.
3. Doubles may collapse once stable **and** placed on the middle line.
4. Simples never collapse; they remain **SEARCH_FRONTIER**.

This is an implementation decision resolving a tension in the supplied prose:
the prose says "Mother OR middle line", while the examples explicitly keep a Simple
letter open even with high coherence.

## Sephirotic lines

The current registry uses the supplied conceptual partition:

- Middle: Keter, Tiferet, Yesod, Malkhut.
- Right/left tension: Chokhmah, Binah, Chesed, Gevurah, Netzach, Hod.
- Above/below: represented as an explicit conceptual category in the specification,
  but no automatic collapse mapping is assigned because the source gives no concrete
  22-letter-to-Sephirah mapping for that category.

A complete one-to-one 22-letter mapping should therefore be treated as a separate
research artifact rather than silently inferred.

## T-Duality and holographic transform

The existing repository-level `ark_kernel.py` already contains a numeric
T-Duality/holographic iteration engine. This package does not duplicate those
continuous-state calculations. Instead, it supplies the **symbolic weighting and
collapse-policy layer** that can be composed with the existing kernel.

## Provenance

Source specification supplied in the working session:

- User-provided ARK Kernel / Holographic String Neural Network specification.
- External prototype URL supplied by the user:
  https://hds-d3dd3iumcy47-6014-ex7qf.grok-code-wild.hades-www.grok-sandbox.com/

The external prototype URL was not incorporated as verified source material in this
commit; the implementation is grounded in the specification supplied in the task.
