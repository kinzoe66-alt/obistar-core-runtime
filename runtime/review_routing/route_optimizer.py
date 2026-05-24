class ReviewRouteOptimizer:

    def optimize(self, candidates):
        prioritized = sorted(
            candidates,
            key=lambda x: x.get(
                "fatigue_adjusted_priority",
                x.get("review_priority", 0)
            ),
            reverse=True
        )

        routes = []

        for index, candidate in enumerate(prioritized):
            routes.append({
                "route_position": index + 1,
                "candidate_id": candidate.get(
                    "candidate_id",
                    "unknown"
                ),
                "workflow_family": candidate.get(
                    "workflow_family",
                    "unknown"
                ),
                "priority": candidate.get(
                    "fatigue_adjusted_priority",
                    candidate.get("review_priority", 0)
                ),
                "manual_review_required": True,
                "confirmed_issue": False,
            })

        return {
            "route_count": len(routes),
            "routes": routes,
            "manual_review_required": True,
            "confirmed_issue": False,
        }
