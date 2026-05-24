from runtime.prioritization.review_priority import ReviewPriorityScorer

def test_review_priority_hold_for_duplicate_weak_signal():
    result = ReviewPriorityScorer().score({
        "value_classification": "high_value_candidate",
        "replay_stability": {"classification": "stable"},
        "report_quality": {"classification": "high_quality"},
        "deduplication": {"classification": "duplicate"},
        "outcome_learning": {"classification": "weak_signal"}
    })

    assert result["classification"] == "hold"

def test_review_priority_high_for_strong_unique_signal():
    result = ReviewPriorityScorer().score({
        "value_classification": "high_value_candidate",
        "replay_stability": {"classification": "stable"},
        "report_quality": {"classification": "high_quality"},
        "deduplication": {"classification": "unique"},
        "outcome_learning": {"classification": "high_signal"}
    })

    assert result["classification"] == "highest_priority"
