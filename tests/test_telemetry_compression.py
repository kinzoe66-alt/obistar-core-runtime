from runtime.governed_scoring.telemetry_compression import (
    RuntimeTelemetryCompressor,
)


def test_telemetry_compression_groups_events():
    result = RuntimeTelemetryCompressor().compress([
        {"event_type": "replay"},
        {"event_type": "replay"},
        {"event_type": "transition"},
    ])

    assert result["event_type_count"] == 2
    assert result["compressed_events"][0]["count"] == 2
