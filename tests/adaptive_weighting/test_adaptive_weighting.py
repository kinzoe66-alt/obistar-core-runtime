from runtime.adaptive_weighting.adaptive_weighting import (
    AdaptiveOutcomeWeighting,
)


def test_strong_adaptive_weighting():
    result = AdaptiveOutcomeWeighting().adjust(
        {"base_weight": 1.0},
        {
            "decision_counts": {
                "useful": 8,
                "duplicate": 1,
                "low_signal": 1,
            }
        }
    )

    assert (
        result["adaptive_signal"]["distribution_quality"]
        == "strong"
    )

    assert (
        result["adaptive_signal"]["adaptive_weight"]
        > 1.0
    )

    assert (
        result["adaptive_signal"]["confirmed_issue"]
        is False
    )


def test_weak_adaptive_weighting():
    result = AdaptiveOutcomeWeighting().adjust(
        {"base_weight": 1.0},
        {
            "decision_counts": {
                "useful": 1,
                "duplicate": 5,
                "low_signal": 4,
            }
        }
    )

    assert (
        result["adaptive_signal"]["distribution_quality"]
        == "weak"
    )


def test_empty_review_memory():
    result = AdaptiveOutcomeWeighting().adjust(
        {"base_weight": 1.0},
        {
            "decision_counts": {}
        }
    )

    assert (
        result["adaptive_signal"]["adaptive_weight"]
        == 1.0
    )
