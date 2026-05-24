from runtime.cognition.history_ingestion import load_replay_history
from runtime.cognition.cognition_quality import assess_cognition_quality

def test_replay_history_ingestion():
    observations = load_replay_history("replay_history/replay_history.sample.json")
    assert len(observations) == 1
    assert observations[0]["observation_id"] == "OBS-001"

def test_cognition_quality_assessment():
    observation = {
        "observation_id": "OBS-001",
        "replay_attempts": 5,
        "replay_successes": 4,
        "confidence": 0.82,
        "review_priority": 0.76,
        "duplicate_cluster_size": 1
    }

    result = assess_cognition_quality(
        observation,
        historical_confidence=0.74,
        evidence_quality=0.8
    )

    assert result["confirmed_issue"] is False
    assert result["manual_review_required"] is True
    assert result["replay_success_rate"] == 0.8
    assert result["replay_history_strength"] == "stable"
    assert result["confidence_drift_status"] == "stable"
    assert result["priority_inflation_detected"] is False
    assert result["duplicate_pressure"] == "none"
