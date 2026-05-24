def governed_observation_value(observation):
    replay = float(observation.get("replay_success_rate", 0.0))
    evidence = float(observation.get("evidence_quality", 0.0))
    duplicate_penalty = float(observation.get("duplicate_penalty", 0.0))
    reviewer_clarity = float(observation.get("reviewer_clarity", 0.0))

    score = max(0.0, (
        replay * 0.35 +
        evidence * 0.30 +
        reviewer_clarity * 0.25 -
        duplicate_penalty * 0.10
    ))

    return {
        "observation_id": observation.get("observation_id"),
        "income_relevance_score": round(score, 4),
        "confirmed_issue": False,
        "manual_review_required": True
    }
