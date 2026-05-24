def build_review_package(candidate):

    return {

        "surface_id": (
            candidate["surface_id"]
        ),

        "workflow_family": (
            candidate.get(
                "workflow_family"
            )
        ),

        "parent_authorized_surface_id": (
            candidate.get(
                "parent_authorized_surface_id"
            )
        ),

        "review_priority": (
            candidate.get(
                "priority"
            )
        ),

        "outcome_learning": (
            candidate.get(
                "outcome_learning"
            )
        ),

        "replay_stability": (
            candidate.get(
                "replay_stability"
            )
        ),

        "report_quality": (
            candidate.get(
                "report_quality"
            )
        ),

        "deduplication": (
            candidate.get(
                "deduplication"
            )
        ),

        "economic_novelty": (
            candidate.get(
                "economic_novelty"
            )
        ),

        "repeat_saturation": (
            candidate.get(
                "repeat_saturation"
            )
        ),

        "review_guidance": {

            "manual_review_required": True,

            "replay_verification_required": True,

            "evidence_lineage_required": True,

            "autonomous_submission": False
        }
    }
