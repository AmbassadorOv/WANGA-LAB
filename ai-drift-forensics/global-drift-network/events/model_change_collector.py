from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="MODEL_CHANGE",
    source_types=("model_release", "provider_release_feed"),
    overlay_probes=("version_behavior", "capability_regression", "instruction_consistency"),
)

if __name__ == "__main__":
    emit(CONFIG)
