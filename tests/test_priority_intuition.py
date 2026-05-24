from runtime.queue_explanations.priority_intuition import (
    PriorityIntuitionBuilder,
)


def test_priority_intuition_review_first():
    result = PriorityIntuitionBuilder().build({
        "economic_novelty": {
            "novelty_score": 1.0,
        },
        "repeat_saturation": {
            "repeat_saturation_penalty": 0.0,
        },
        "review_priority": {
            "score": 0.74,
        },
        "priority_explanation": {
            "reviewer_summary": "high_novelty_low_saturation with stable replay",
        },
    })

    assert result["priority_band"] == "review_first"
    assert "novel signal" in result["why_this_position"]


def test_priority_intuition_priority_review():
    result = PriorityIntuitionBuilder().build({
        "economic_novelty": {
            "novelty_score": 0.55,
        },
        "repeat_saturation": {
            "repeat_saturation_penalty": 0.2,
        },
        "review_priority": {
            "score": 0.74,
        },
    })

    assert result["priority_band"] == "priority_review"
    assert "acceptable saturation" in result["why_this_position"]


def test_priority_intuition_fallback_safe():
    result = PriorityIntuitionBuilder().build({})

    assert result["priority_band"] == "standard_review"
    assert result["manual_review_required"] is True
    assert result["autonomous_submission"] is False
