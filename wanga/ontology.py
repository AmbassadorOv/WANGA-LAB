"""
WANGA Ontology Validator
"""

from typing import Dict, Any, List


class OntologyValidator:
    """Validates structural semantics and relationship invariants in WANGA ontology."""

    def validate(self, arch_dict: Dict[str, Any]) -> List[str]:
        errors = []

        # Ontology Invariant 1: Seed consistency
        exp = arch_dict.get("experiment", {})
        if "seed" not in exp:
            errors.append("Ontology Error: Experiment must specify an explicit seed for determinism")

        # Ontology Invariant 2: Security limits must be non-negative
        sec = arch_dict.get("security", {})
        if sec.get("max_memory_mb", 1) <= 0:
            errors.append("Ontology Error: Security max_memory_mb must be > 0")
        if sec.get("max_execution_seconds", 1) <= 0:
            errors.append("Ontology Error: Security max_execution_seconds must be > 0")

        # Ontology Invariant 3: Unique component IDs across entities
        ids = []
        for cat in ["agents", "neural_components", "virtual_nano_processors", "tools"]:
            for item in arch_dict.get(cat, []):
                item_id = item.get("id")
                if item_id:
                    if item_id in ids:
                        errors.append(f"Ontology Error: Duplicate entity ID '{item_id}' detected across architecture")
                    else:
                        ids.append(item_id)

        return errors
