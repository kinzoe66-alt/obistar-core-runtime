class AdaptiveReplayScheduler:

    def schedule(self, replay_record):

        success_rate = replay_record.get(
            "success_rate",
            0.0
        )

        if success_rate >= 0.95:
            replay_runs = 2
        elif success_rate >= 0.75:
            replay_runs = 3
        elif success_rate >= 0.50:
            replay_runs = 5
        else:
            replay_runs = 7

        return {
            "replay_runs": replay_runs,
            "success_rate": success_rate,
            "manual_review_required": True,
            "autonomous_submission": False,
        }
