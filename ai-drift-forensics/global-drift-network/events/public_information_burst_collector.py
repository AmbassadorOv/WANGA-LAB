from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="PUBLIC_INFORMATION_BURST",
    source_types=("public_event_feed", "news_feed"),
    overlay_probes=("freshness", "uncertainty", "cross_language_consistency"),
)

if __name__ == "__main__":
    emit(CONFIG)
