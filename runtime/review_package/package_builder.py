def build_review_package(observation):
    return {
        "package_id": observation.get("observation_id"),
        "confirmed_issue": False,
        "manual_review_required": True,
        "summary": observation.get("summary", "Governed validation observation requires manual review."),
        "evidence": observation.get("evidence", []),
        "replay_success_rate": observation.get("replay_success_rate", 0.0),
        "reviewer_clarity_score": observation.get("reviewer_clarity_score", 0.0),
        "recommended_status": "manual_review_package"
    }
