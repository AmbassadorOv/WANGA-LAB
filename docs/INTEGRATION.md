# Integration with WANGA-LAB

The package is intentionally isolated under `src/holographic_string_nn`.

## Composition

```
22-letter identity
       |
       v
LetterGroup + SephirahLine
       |
       v
HolographicStringNode
       |
       +---- existing ARK numeric kernel
       |
       v
CollapsePolicy
       |
       +--> GROUNDED_CONCLUSION
       +--> SUPERPOSITION
       +--> SEARCH_FRONTIER
```

The existing `ark_kernel.py` remains the continuous/numeric engine.
This library is the symbolic policy layer.

## Example

```python
from holographic_string_nn import (
    CollapsePolicy,
    HolographicStringNode,
    LetterGroup,
    SephirahLine,
)

node = HolographicStringNode(
    letter="ת",
    group=LetterGroup.DOUBLES,
    sephirah_line=SephirahLine.MIDDLE,
    coherence=0.99,
)

decision = CollapsePolicy().apply(node)
print(decision.value)
# COLLAPSE
```

## Verification boundary

Passing the unit tests establishes only that the implementation obeys the coded
rules. It does not verify the underlying symbolic, historical, theological, or
physical claims.
