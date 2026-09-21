"""TNRL Kernel: neuro-symbolic execution core for the Talmudic reasoning language."""
from .ir import Term, Predicate, Proposition, ReasoningNode, TruthStatus
from .operators import Operator, apply_operator
