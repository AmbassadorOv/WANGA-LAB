from event_collector_core import EventCollectorConfig, emit

CONFIG = EventCollectorConfig(
    event_type="POLICY_REGULATORY_EVENT",
    source_types=("official_publication", "regulatory_feed"),
    overlay_probes=("policy_freshness", "instruction_consistency", "jurisdictional_scope"),
)

if __name__ == "__main__":
    emit(CONFIG)
