def workflow_weight(history):
    replay = float(history.get("replay_success_rate", 0.0))
    reviewer = float(history.get("reviewer_acceptance_rate", 0.0))
    evidence = float(history.get("evidence_strength", 0.0))

    score = (
        replay * 0.30 +
        reviewer * 0.45 +
        evidence * 0.25
    )

    return {
        "workflow_family": history.get("workflow_family"),
        "workflow_weight_score": round(score, 4),
        "workflow_weight_classification": (
            "strong_weight"
            if score >= 0.75
            else "weak_weight"
        )
    }
