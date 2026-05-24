from runtime.review_fatigue.fatigue_damping import (
    ReviewFatigueDamping,
)


def test_fatigue_damping_reduces_priority():
    candidate = {
        "review_priority": 1.0,
    }

    review_memory = {
        "decision_counts": {
            "duplicate": 4,
            "low_signal": 2,
        }
    }

    result = ReviewFatigueDamping().dampen(
        candidate,
        review_memory,
    )

    assert result["fatigue_pressure"] == 6
    assert result["fatigue_adjusted_priority"] < 1.0
    assert result["manual_review_required"] is True
    assert result["confirmed_issue"] is False


def test_fatigue_floor_is_preserved():
    candidate = {
        "review_priority": 1.0,
    }

    review_memory = {
        "decision_counts": {
            "duplicate": 100,
            "low_signal": 100,
        }
    }

    result = ReviewFatigueDamping().dampen(
        candidate,
        review_memory,
    )

    assert result["fatigue_damping_factor"] == 0.2
