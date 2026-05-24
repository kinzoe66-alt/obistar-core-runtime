class DistributedReplayOrchestrator:

    def plan(self, replay_items, workers=1):

        workers = max(1, workers)

        assignments = [
            {
                "worker_id": index % workers,
                "item": item,
                "manual_review_required": True,
            }
            for index, item in enumerate(replay_items)
        ]

        return {
            "worker_count": workers,
            "assignment_count": len(assignments),
            "assignments": assignments,
            "manual_review_required": True,
            "autonomous_submission": False,
        }
