from runtime.observations.quality_scorer import ObservationQualityScorer

def test_observation_quality_scorer():
    result = ObservationQualityScorer().score({
        "replay_stability": {"classification": "stable"},
        "report_quality": {"classification": "high_quality"},
        "deduplication": {"classification": "possible_duplicate"},
        "value_classification": "high_value_candidate"
    })

    assert result["classification"] == "strongest_candidate"
