class ReplayWeightingEngine:

    def weight(self, escalation):

        weighted = []

        for item in escalation.get(
            "escalated",
            []
        ):

            replay_runs = item.get(
                "replay_runs",
                1
            )

            weight = round(
                replay_runs / 5,
                2
            )

            weighted.append({
                "priority": (
                    item["priority"]
                ),

                "replay_runs": (
                    replay_runs
                ),

                "replay_weight": (
                    weight
                ),

                "manual_review_required": True,

                "autonomous_submission": False,
            })

        return {
            "weighted": weighted,
            "weight_count": len(
                weighted
            ),
            "manual_review_required": True,
        }
