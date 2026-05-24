from runtime.governed_scoring.reviewer_feedback import (
    ReviewerFeedbackReinforcement,
)


def test_positive_feedback_increases_score():
    result = ReviewerFeedbackReinforcement().reinforce(
        0.5,
        {"outcome": "accepted_for_review"},
    )

    assert result["adjusted_score"] == 0.6


def test_negative_feedback_decreases_score():
    result = ReviewerFeedbackReinforcement().reinforce(
        0.5,
        {"outcome": "rejected_as_low_value"},
    )

    assert result["adjusted_score"] == 0.35
