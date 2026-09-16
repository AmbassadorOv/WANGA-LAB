from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="PLATFORM_CHANGE",
    source_types=("provider_change_log", "platform_status"),
    overlay_probes=("routing_behavior", "interface_independence", "response_consistency"),
)

if __name__ == "__main__":
    emit(CONFIG)
