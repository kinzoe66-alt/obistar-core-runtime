class AdaptiveOutcomeWeighting:

    def adjust(self, weighting_table, review_memory):
        adjusted = dict(weighting_table)

        useful = (
            review_memory
            .get("decision_counts", {})
            .get("useful", 0)
        )

        duplicate = (
            review_memory
            .get("decision_counts", {})
            .get("duplicate", 0)
        )

        low_signal = (
            review_memory
            .get("decision_counts", {})
            .get("low_signal", 0)
        )

        total = useful + duplicate + low_signal

        if total == 0:
            adjusted["adaptive_signal"] = {
                "adaptive_weight": 1.0,
                "distribution_quality": "unknown",
            }

            return adjusted

        useful_ratio = useful / total

        adaptive_weight = round(
            0.5 + useful_ratio,
            4
        )

        if useful_ratio >= 0.75:
            quality = "strong"

        elif useful_ratio >= 0.5:
            quality = "moderate"

        else:
            quality = "weak"

        adjusted["adaptive_signal"] = {
            "adaptive_weight": adaptive_weight,
            "distribution_quality": quality,
            "manual_review_required": True,
            "confirmed_issue": False,
        }

        return adjusted
