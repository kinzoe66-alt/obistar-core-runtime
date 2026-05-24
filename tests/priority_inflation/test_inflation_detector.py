from runtime.priority_inflation.inflation_detector import (
    PriorityInflationDetector,
)


def test_detects_priority_inflation():
    candidates = [
        {"fatigue_adjusted_priority": 0.95},
        {"fatigue_adjusted_priority": 0.91},
        {"fatigue_adjusted_priority": 0.88},
        {"fatigue_adjusted_priority": 0.2},
    ]

    result = PriorityInflationDetector().detect(
        candidates
    )

    assert result["inflation_detected"] is True
    assert result["high_priority_count"] == 3
    assert result["candidate_count"] == 4
    assert result["confirmed_issue"] is False


def test_detects_stable_priority_distribution():
    candidates = [
        {"fatigue_adjusted_priority": 0.91},
        {"fatigue_adjusted_priority": 0.4},
        {"fatigue_adjusted_priority": 0.3},
        {"fatigue_adjusted_priority": 0.2},
    ]

    result = PriorityInflationDetector().detect(
        candidates
    )

    assert result["inflation_detected"] is False


def test_empty_candidate_list():
    result = PriorityInflationDetector().detect([])

    assert result["inflation_detected"] is False
    assert result["candidate_count"] == 0
