"""
NADL (Neural Architecture Description Language) Parser & Validator
"""

from typing import Dict, Any, List


class NADLValidationError(Exception):
    pass


class NADLValidator:
    """Validates architecture definitions against NADL formal syntax and topology rules."""

    def validate(self, arch_dict: Dict[str, Any]) -> List[str]:
        errors = []

        # Check top-level required NADL constructs
        if "experiment" not in arch_dict:
            errors.append("NADL Syntax Error: Missing 'experiment' block")

        neural_components = arch_dict.get("neural_components", [])
        vnps = arch_dict.get("virtual_nano_processors", [])

        if not neural_components and not vnps:
            errors.append("NADL Topology Error: Architecture must specify at least one neural component or VNP")

        # Validate neural component dim consistency
        for idx, nc in enumerate(neural_components):
            if "input_dim" in nc and nc["input_dim"] <= 0:
                errors.append(f"NADL Error in neural_component[{idx}]: input_dim must be positive")
            if "output_dim" in nc and nc["output_dim"] <= 0:
                errors.append(f"NADL Error in neural_component[{idx}]: output_dim must be positive")

        # Validate fabric topology connections
        fabric = arch_dict.get("fabric", {})
        connections = fabric.get("connections", [])
        all_ids = set()

        for a in arch_dict.get("agents", []):
            all_ids.add(a.get("id"))
        for nc in neural_components:
            all_ids.add(nc.get("id"))
        for vnp in vnps:
            all_ids.add(vnp.get("id"))

        for conn in connections:
            src = conn.get("source")
            tgt = conn.get("target")
            if src and src not in all_ids:
                errors.append(f"NADL Fabric Error: Connection source '{src}' does not reference a valid component ID")
            if tgt and tgt not in all_ids:
                errors.append(f"NADL Fabric Error: Connection target '{tgt}' does not reference a valid component ID")

        return errors
