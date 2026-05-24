from runtime.review_reinforcement.reinforcement_model import (
    ReviewerReinforcementModel,
)


def test_high_signal_quality():
    result = ReviewerReinforcementModel().reinforce({
        "decision_counts": {
            "useful": 8,
            "duplicate": 1,
            "low_signal": 1,
        }
    })

    assert result["signal_quality"] == "high"
    assert result["manual_review_required"] is True
    assert result["confirmed_issue"] is False


def test_moderate_signal_quality():
    result = ReviewerReinforcementModel().reinforce({
        "decision_counts": {
            "useful": 5,
            "duplicate": 3,
            "low_signal": 2,
        }
    })

    assert result["signal_quality"] == "moderate"


def test_weak_signal_quality():
    result = ReviewerReinforcementModel().reinforce({
        "decision_counts": {
            "useful": 1,
            "duplicate": 5,
            "low_signal": 4,
        }
    })

    assert result["signal_quality"] == "weak"
