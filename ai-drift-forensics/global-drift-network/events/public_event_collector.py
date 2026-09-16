from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="PUBLIC_EVENT",
    source_types=("public_event_feed",),
    overlay_probes=("event_reference_consistency", "uncertainty", "cross_region_consistency"),
)

if __name__ == "__main__":
    emit(CONFIG)
