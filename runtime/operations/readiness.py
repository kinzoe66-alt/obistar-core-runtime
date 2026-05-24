class OperationalReadiness:

    def evaluate(self, live_result: dict):
        imported = live_result["imported"]
        comparison = live_result["comparison"]

        return {
            "ready": (
                imported["imported_count"] > 0
                and comparison["surface_count"] > 0
                and comparison["manual_review_required"] is True
                and comparison["autonomous_submission"] is False
            ),
            "imported_count": imported["imported_count"],
            "comparison_count": comparison["surface_count"],
            "manual_review_required": True,
            "autonomous_submission": False
        }
