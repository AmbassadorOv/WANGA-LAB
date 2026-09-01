"""
Append-Only Audit Logging Component
"""

import time
import json
from typing import Dict, Any, List


class AuditLogger:
    """
    Append-only audit trail logger recording execution events, compiler steps, gate results, and artifacts.
    """

    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def record_event(
        self,
        event_type: str,
        architecture_name: str,
        version: str,
        details: Dict[str, Any]
    ) -> Dict[str, Any]:
        record = {
            "entry_index": len(self.records) + 1,
            "timestamp": time.time(),
            "event_type": event_type,
            "architecture_name": architecture_name,
            "version": version,
            "details": details
        }
        self.records.append(record)
        return record

    def get_audit_trail(self) -> List[Dict[str, Any]]:
        return list(self.records)
