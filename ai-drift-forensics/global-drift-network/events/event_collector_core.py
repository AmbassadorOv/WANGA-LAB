"""Shared execution core for event-driven AI drift collectors.

The core deliberately produces no synthetic observations. Without a configured
endpoint and credentials it returns NOT_CONFIGURED so missing infrastructure is
visible in the evidence chain rather than being replaced with fabricated data.
"""
from __future__ import annotations

import hashlib
import json
import os
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from typing import Any


@dataclass(frozen=True)
class EventCollectorConfig:
    event_type: str
    source_types: tuple[str, ...]
    overlay_probes: tuple[str, ...]
    window_minutes: tuple[int, ...] = (-15, -5, 0, 1, 5, 10, 20, 30, 60)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def event_hash(anchor: dict[str, Any]) -> str:
    payload = json.dumps(anchor, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def build_schedule(event_time: datetime, offsets: tuple[int, ...]) -> list[dict[str, Any]]:
    return [
        {"offset_minutes": offset, "scheduled_at": (event_time + timedelta(minutes=offset)).isoformat().replace("+00:00", "Z")}
        for offset in offsets
    ]


def build_event_anchor(config: EventCollectorConfig) -> dict[str, Any]:
    event_time_raw = os.getenv("EVENT_TIME")
    try:
        event_time = datetime.fromisoformat(event_time_raw.replace("Z", "+00:00")) if event_time_raw else datetime.now(timezone.utc)
    except ValueError:
        event_time = datetime.now(timezone.utc)
    anchor = {
        "event_id": os.getenv("EVENT_ID", f"EVT-{config.event_type}-{int(event_time.timestamp())}"),
        "event_type": config.event_type,
        "source_id": os.getenv("EVENT_SOURCE_ID", "UNSPECIFIED"),
        "detected_at": os.getenv("EVENT_DETECTED_AT", utc_now()),
        "event_time": event_time.isoformat().replace("+00:00", "Z"),
        "confidence": os.getenv("EVENT_CONFIDENCE", "UNSPECIFIED"),
        "source_locator": os.getenv("EVENT_SOURCE_LOCATOR", "UNSPECIFIED"),
        "scope": os.getenv("EVENT_SCOPE", "UNSPECIFIED"),
        "affected_providers_or_models": os.getenv("EVENT_AFFECTED_MODELS", "UNSPECIFIED"),
        "source_types": list(config.source_types),
    }
    anchor["event_hash"] = event_hash(anchor)
    return anchor


def run(config: EventCollectorConfig) -> dict[str, Any]:
    anchor = build_event_anchor(config)
    event_time = datetime.fromisoformat(anchor["event_time"].replace("Z", "+00:00"))
    endpoint = os.getenv("DRIFT_ENDPOINT", "").strip()
    token = os.getenv("DRIFT_TOKEN", "").strip()
    result: dict[str, Any] = {
        "collector_status": "READY" if endpoint and token else "NOT_CONFIGURED",
        "collector_event_type": config.event_type,
        "event_anchor": anchor,
        "measurement_schedule": build_schedule(event_time, config.window_minutes),
        "overlay_probes": list(config.overlay_probes),
        "node": os.getenv("DRIFT_NODE", "UNSPECIFIED"),
        "language": os.getenv("DRIFT_LANGUAGE", "UNSPECIFIED"),
        "model": os.getenv("DRIFT_MODEL", "UNSPECIFIED"),
        "method_version": "EVENT-COLLECTOR-CORE-1.0.0",
        "generated_at": utc_now(),
        "synthetic_observations": False,
        "observations": [],
        "warnings": [],
    }
    if not endpoint or not token:
        result["warnings"].append("Endpoint or token unavailable; no observation was fabricated.")
        return result

    payload = json.dumps({
        "event_anchor": anchor,
        "probes": config.overlay_probes,
        "schedule": result["measurement_schedule"],
        "node": result["node"],
        "language": result["language"],
        "model": result["model"],
        "method_version": result["method_version"],
    }).encode()
    request = urllib.request.Request(endpoint, data=payload, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
            result["collector_status"] = "COLLECTED"
            result["upstream_response_status"] = response.status
            result["upstream_response"] = json.loads(body) if body else None
    except Exception as exc:  # noqa: BLE001 - collector must preserve failure as evidence metadata
        result["collector_status"] = "COLLECTION_ERROR"
        result["warnings"].append(f"Upstream collection failed: {type(exc).__name__}")
    return result


def emit(config: EventCollectorConfig) -> None:
    print(json.dumps(run(config), indent=2, ensure_ascii=False))
