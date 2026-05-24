class ReviewConfidenceAdjuster:

    def adjust(self, candidate, review_memory):
        adjusted = dict(candidate)

        base_priority = candidate.get("review_priority", 0)
        replay_accuracy = review_memory.get("average_replay_accuracy", 0)
        priority_correctness = review_memory.get("average_priority_correctness", 0)

        adjustment_weight = (replay_accuracy + priority_correctness) / 2

        adjusted["review_memory_signal"] = {
            "average_replay_accuracy": replay_accuracy,
            "average_priority_correctness": priority_correctness,
            "adjustment_weight": round(adjustment_weight, 4),
        }

        adjusted["adjusted_review_priority"] = round(
            base_priority * adjustment_weight,
            4
        )

        adjusted["manual_review_required"] = True
        adjusted["confirmed_issue"] = False

        return adjusted
