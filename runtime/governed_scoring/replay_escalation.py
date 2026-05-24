class ReplayEscalationOrchestrator:

    def escalate(self, branches):

        escalated = []

        for item in branches.get(
            "selected",
            []
        ):

            priority = item.get(
                "priority"
            )

            if priority == "high":

                replay_runs = 5

            elif priority == "medium":

                replay_runs = 3

            else:

                replay_runs = 1

            escalated.append({
                "branch_action": (
                    item["branch_action"]
                ),

                "priority": priority,

                "replay_runs": replay_runs,

                "manual_review_required": True,

                "autonomous_submission": False,
            })

        return {
            "escalated": escalated,

            "escalation_count": len(
                escalated
            ),

            "manual_review_required": True,
        }
