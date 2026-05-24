def reviewer_signal_quality(observations):
    total = len(observations)

    if total == 0:
        return {
            "reviewer_signal_quality": 0.0,
            "high_confidence_ratio": 0.0
        }

    high_confidence = [
        o for o in observations
        if o.get("replay_success_rate", 0.0) >= 0.8
    ]

    ratio = len(high_confidence) / total

    return {
        "reviewer_signal_quality": round(ratio, 4),
        "high_confidence_ratio": round(ratio, 4)
    }
