def reviewer_quality(package):
    score = (
        float(package.get("replay_score", 0.0)) * 0.35 +
        float(package.get("evidence_score", 0.0)) * 0.35 +
        float(package.get("explanation_score", 0.0)) * 0.30
    )

    return {
        "reviewer_quality_score": round(score, 4),
        "reviewer_quality_state": "review_ready" if score >= 0.75 else "needs_improvement"
    }
