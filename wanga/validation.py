"""
WANGA Validation Pipeline
"""

import json
from typing import Dict, Any, Tuple, List
from pydantic import ValidationError

from wanga.models import WangaArchitectureSpec
from wanga.nadl import NADLValidator
from wanga.ontology import OntologyValidator
from wanga.gates import Gates231Engine


class ValidationResult:
    def __init__(self, is_valid: bool, errors: List[str], canonical_dict: Dict[str, Any] = None):
        self.is_valid = is_valid
        self.errors = errors
        self.canonical_dict = canonical_dict or {}


class WangaValidationPipeline:
    """
    Executes full validation pipeline:
    Natural Language -> Gemini (optional) -> JSON Schema -> NADL -> Ontology -> 231-Gates -> Security -> Canonicalization
    """

    def __init__(self):
        self.nadl_validator = NADLValidator()
        self.ontology_validator = OntologyValidator()
        self.gates_engine = Gates231Engine()

    def validate(self, raw_data: Dict[str, Any]) -> ValidationResult:
        errors = []

        # 1. Schema Validation via Pydantic
        try:
            spec = WangaArchitectureSpec.model_validate(raw_data)
            canonical_dict = json.loads(spec.model_dump_json())
        except ValidationError as e:
            return ValidationResult(False, [f"Schema Validation Error: {err['msg']} at {err['loc']}" for err in e.errors()])
        except Exception as e:
            return ValidationResult(False, [f"Schema Parsing Error: {str(e)}"])

        # 2. NADL Validation
        nadl_errors = self.nadl_validator.validate(canonical_dict)
        if nadl_errors:
            errors.extend(nadl_errors)

        # 3. Ontology Validation
        ontology_errors = self.ontology_validator.validate(canonical_dict)
        if ontology_errors:
            errors.extend(ontology_errors)

        # 4. 231-Gate Validation
        all_gates_pass, gate_results = self.gates_engine.evaluate_all(canonical_dict)
        if not all_gates_pass:
            for g in gate_results:
                if not g.passed:
                    errors.append(f"231-Gate Violation: [{g.name}] - {g.message}")

        if errors:
            return ValidationResult(False, errors, canonical_dict)

        return ValidationResult(True, [], canonical_dict)
