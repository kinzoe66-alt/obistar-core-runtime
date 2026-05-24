class PriorityIntuitionBuilder:

    def build(self, item):
        explanation = item.get(
            "priority_explanation",
            {}
        )

        novelty = item.get(
            "economic_novelty",
            {}
        ).get(
            "novelty_score",
            0.5
        )

        saturation = item.get(
            "repeat_saturation",
            {}
        ).get(
            "repeat_saturation_penalty",
            0.0
        )

        priority = item.get(
            "review_priority",
            item.get("priority", {})
        ).get(
            "score",
            0.0
        )

        if novelty >= 1.0 and saturation == 0.0:
            band = "review_first"
            why_first = "novel signal with no saturation penalty"
        elif priority >= 0.74 and saturation <= 0.2:
            band = "priority_review"
            why_first = "strong review priority with acceptable saturation"
        else:
            band = "standard_review"
            why_first = "valid candidate requiring normal review"

        return {
            "priority_band": band,
            "why_this_position": why_first,
            "compressed_reason": explanation.get(
                "reviewer_summary",
                why_first
            ),
            "manual_review_required": True,
            "autonomous_submission": False,
        }
