from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="SERVICE_INCIDENT",
    source_types=("provider_status", "service_incident_feed"),
    overlay_probes=("availability", "latency", "error_behavior", "recovery_behavior"),
)

if __name__ == "__main__":
    emit(CONFIG)
