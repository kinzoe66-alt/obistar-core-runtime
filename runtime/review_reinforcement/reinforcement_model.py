class ReviewerReinforcementModel:

    def reinforce(self, review_memory):
        decision_counts = review_memory.get(
            "decision_counts",
            {}
        )

        useful = decision_counts.get("useful", 0)
        duplicate = decision_counts.get("duplicate", 0)
        low_signal = decision_counts.get("low_signal", 0)

        total = useful + duplicate + low_signal

        if total == 0:
            return {
                "reinforcement_confidence": 0,
                "signal_quality": "unknown",
            }

        useful_ratio = useful / total

        if useful_ratio >= 0.8:
            quality = "high"

        elif useful_ratio >= 0.5:
            quality = "moderate"

        else:
            quality = "weak"

        return {
            "reinforcement_confidence": round(
                useful_ratio,
                4
            ),
            "signal_quality": quality,
            "manual_review_required": True,
            "confirmed_issue": False,
        }
