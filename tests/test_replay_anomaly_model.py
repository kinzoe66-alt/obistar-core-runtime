from runtime.governed_scoring.replay_anomaly_model import (
    HistoricalReplayAnomalyModel,
)


def test_replay_anomaly_detects_large_delta():
    result = HistoricalReplayAnomalyModel().model([
        {
            "replay_id": "r1",
            "expected_success_rate": 1.0,
            "actual_success_rate": 0.5,
        }
    ])

    assert result["anomaly_count"] == 1
    assert result["anomalies"][0]["replay_id"] == "r1"
