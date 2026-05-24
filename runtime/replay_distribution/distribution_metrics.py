class ReplayDistributionMetrics:

    def analyze(self, replay_history):
        if not replay_history:
            return {
                "distribution_stable": False,
                "replay_count": 0,
                "workflow_distribution": {},
            }

        distribution = {}

        for replay in replay_history:
            workflow = replay.get(
                "workflow_family",
                "unknown"
            )

            distribution.setdefault(workflow, 0)
            distribution[workflow] += 1

        replay_count = sum(
            distribution.values()
        )

        largest_bucket = max(
            distribution.values(),
            default=0
        )

        concentration_ratio = round(
            largest_bucket / replay_count,
            4
        )

        return {
            "distribution_stable":
                concentration_ratio < 0.7,

            "replay_count":
                replay_count,

            "workflow_distribution":
                distribution,

            "largest_bucket":
                largest_bucket,

            "concentration_ratio":
                concentration_ratio,

            "manual_review_required":
                True,

            "confirmed_issue":
                False,
        }
