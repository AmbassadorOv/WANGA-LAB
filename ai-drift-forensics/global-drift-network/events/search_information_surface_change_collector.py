from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="SEARCH_INFORMATION_SURFACE_CHANGE",
    source_types=("search_change_feed", "information_surface_monitor"),
    overlay_probes=("retrieval_consistency", "freshness", "source_diversity"),
)

if __name__ == "__main__":
    emit(CONFIG)
