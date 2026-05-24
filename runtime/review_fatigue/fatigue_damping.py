class ReviewFatigueDamping:

    def dampen(self, candidate, review_memory):
        adjusted = dict(candidate)

        duplicate_count = (
            review_memory
            .get("decision_counts", {})
            .get("duplicate", 0)
        )

        low_signal_count = (
            review_memory
            .get("decision_counts", {})
            .get("low_signal", 0)
        )

        pressure = duplicate_count + low_signal_count

        damping_factor = max(
            0.2,
            1 - (pressure * 0.05)
        )

        base_priority = candidate.get(
            "adjusted_review_priority",
            candidate.get("review_priority", 0)
        )

        adjusted["fatigue_pressure"] = pressure

        adjusted["fatigue_damping_factor"] = round(
            damping_factor,
            4
        )

        adjusted["fatigue_adjusted_priority"] = round(
            base_priority * damping_factor,
            4
        )

        adjusted["manual_review_required"] = True
        adjusted["confirmed_issue"] = False

        return adjusted
