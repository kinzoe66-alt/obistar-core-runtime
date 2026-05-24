class AdjudicationPackageBuilder:

    def build(
        self,
        candidate,
        review_memory,
        continuity_memory,
    ):
        return {
            "candidate_id":
                candidate.get(
                    "candidate_id",
                    "unknown"
                ),

            "workflow_family":
                candidate.get(
                    "workflow_family",
                    "unknown"
                ),

            "priority":
                candidate.get(
                    "fatigue_adjusted_priority",
                    candidate.get(
                        "review_priority",
                        0
                    )
                ),

            "review_memory":
                review_memory,

            "continuity_memory":
                continuity_memory,

            "manual_review_required":
                True,

            "confirmed_issue":
                False,
        }
