class AdaptiveBranchSelector:

    def select(self, observations):

        prioritized = sorted(
            observations,
            key=lambda item: (
                item["transition_value"]
                ["transition_score"]
            ),
            reverse=True,
        )

        selected = []

        for item in prioritized:

            score = (
                item["transition_value"]
                ["transition_score"]
            )

            if score >= 0.50:
                selected.append({
                    "branch_action": (
                        "escalate_replay_validation"
                    ),
                    "priority": "high",
                    "observation": item,
                })

            elif score > 0:
                selected.append({
                    "branch_action": (
                        "retain_for_review"
                    ),
                    "priority": "medium",
                    "observation": item,
                })

        return {
            "selected": selected,
            "selection_count": len(
                selected
            ),
            "manual_review_required": True,
            "autonomous_submission": False,
        }
