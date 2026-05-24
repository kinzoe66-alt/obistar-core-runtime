class ProgramSpecificScoringOverlay:

    def apply(self, score, overlay):

        multiplier = overlay.get(
            "priority_multiplier",
            1.0
        )

        adjusted = max(
            0.0,
            min(
                1.0,
                score * multiplier
            )
        )

        return {
            "adjusted_score": round(adjusted, 4),
            "overlay_applied": True,
            "manual_review_required": True,
            "autonomous_submission": False,
        }
