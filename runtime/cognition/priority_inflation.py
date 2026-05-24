def priority_inflation(review_priority, replay_success_rate, evidence_quality):
    priority = float(review_priority)
    replay = float(replay_success_rate)
    evidence = float(evidence_quality)

    inflated = priority >= 0.75 and (replay < 0.5 or evidence < 0.5)

    return {
        "priority_inflation_detected": inflated,
        "priority_inflation_reason": (
            "priority exceeds replay/evidence support"
            if inflated
            else "priority supported by replay/evidence signal"
        )
    }
