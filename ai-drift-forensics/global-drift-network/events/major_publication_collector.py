from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="MAJOR_PUBLICATION",
    source_types=("publication_feed", "repository_release"),
    overlay_probes=("citation_awareness", "uncertainty", "cross_language_consistency"),
)

if __name__ == "__main__":
    emit(CONFIG)
