"""
WANGA Architecture Specification Helpers
"""

import json
from typing import Dict, Any, Union
from wanga.models import WangaArchitectureSpec


def load_architecture_spec(source: Union[str, Dict[str, Any]]) -> WangaArchitectureSpec:
    """Loads and validates a WANGA architecture specification from dict or JSON string/path."""
    if isinstance(source, str):
        if source.strip().startswith("{"):
            data = json.loads(source)
        else:
            with open(source, "r", encoding="utf-8") as f:
                data = json.load(f)
    elif isinstance(source, dict):
        data = source
    else:
        raise ValueError("Invalid source for architecture specification")

    return WangaArchitectureSpec.model_validate(data)


def export_architecture_schema() -> Dict[str, Any]:
    """Generates the JSON schema for WANGA Architecture Specification."""
    return WangaArchitectureSpec.model_json_schema()
