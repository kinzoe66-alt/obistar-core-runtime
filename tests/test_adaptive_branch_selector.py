from runtime.governed_scoring.branch_selector import (
    AdaptiveBranchSelector
)


def test_branch_selector_prioritizes_high_score():

    selector = AdaptiveBranchSelector()

    observations = [
        {
            "transition_value": {
                "transition_score": 0.2
            }
        },
        {
            "transition_value": {
                "transition_score": 0.8
            }
        },
    ]

    result = selector.select(
        observations
    )

    assert (
        result["selection_count"]
        == 2
    )

    assert (
        result["selected"][0]
        ["priority"]
        == "high"
    )


def test_branch_selector_rejects_zero_score():

    selector = AdaptiveBranchSelector()

    observations = [
        {
            "transition_value": {
                "transition_score": 0.0
            }
        }
    ]

    result = selector.select(
        observations
    )

    assert (
        result["selection_count"]
        == 0
    )
