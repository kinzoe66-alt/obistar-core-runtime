class ReviewerFeedbackReinforcement:

    def reinforce(self, score, feedback):

        outcome = feedback.get("outcome")

        adjusted = score

        if outcome == "accepted_for_review":
            adjusted += 0.10
        elif outcome == "rejected_as_low_value":
            adjusted -= 0.15

        adjusted = max(
            0.0,
            min(1.0, adjusted)
        )

        return {
            "adjusted_score": round(adjusted, 4),
            "manual_review_required": True,
            "autonomous_submission": False,
        }
