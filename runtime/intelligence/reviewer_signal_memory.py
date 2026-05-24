def reviewer_signal_memory(observations):
    reviewer_ready = [
        o for o in observations
        if o.get("reviewer_ready") is True
    ]

    total = len(observations)

    if total == 0:
        ratio = 0.0
    else:
        ratio = len(reviewer_ready) / total

    return {
        "reviewer_signal_ratio": round(ratio, 4),
        "reviewer_signal_strength": (
            "high"
            if ratio >= 0.7
            else "developing"
        )
    }
