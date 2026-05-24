def outcome_weighted_priority(observation, workflow_weight_score, evidence_history_score):
    base_priority = float(
        observation.get("review_priority", {}).get("score", 0.0)
    )

    outcome_score = float(
        observation.get("outcome_learning", {}).get("score", 0.0)
    )

    score = (
        base_priority * 0.30 +
        workflow_weight_score * 0.35 +
        evidence_history_score * 0.20 +
        max(outcome_score, 0.0) * 0.15
    )

    return {
        "weighted_priority_score": round(score, 4),
        "weighted_priority_classification": (
            "priority_review"
            if score >= 0.70
            else "hold"
        ),
        "manual_review_required": True,
        "autonomous_submission": False
    }
