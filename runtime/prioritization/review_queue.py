class ReviewQueueBuilder:

    def build(self, comparison: dict):
        items = sorted(
            comparison["results"],
            key=lambda item: item["review_priority"]["score"],
            reverse=True
        )

        return {
            "queue": items,
            "manual_review_required": True,
            "autonomous_submission": False,
            "autonomous_rejection": False
        }
