def reviewer_clarity_score(observation):
    evidence = float(observation.get("evidence_quality", 0.0))
    replay = float(observation.get("replay_success_rate", 0.0))
    meaning = float(observation.get("operational_meaning", 0.0))

    score = (
        evidence * 0.4 +
        replay * 0.4 +
        meaning * 0.2
    )

    return {
        "reviewer_clarity_score": round(score, 4),
        "reviewer_ready": score >= 0.75
    }
