class ReviewerContinuityMemory:

    def build(self, review_routes):
        workflow_history = {}

        for route in review_routes:
            workflow = route.get(
                "workflow_family",
                "unknown"
            )

            workflow_history.setdefault(
                workflow,
                0
            )

            workflow_history[workflow] += 1

        continuity_score = round(
            sum(workflow_history.values()) /
            max(len(workflow_history), 1),
            4
        )

        return {
            "workflow_history": workflow_history,
            "workflow_family_count":
                len(workflow_history),
            "continuity_score":
                continuity_score,
            "manual_review_required":
                True,
            "confirmed_issue":
                False,
        }
