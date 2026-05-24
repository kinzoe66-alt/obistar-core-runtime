def economic_reinforcement(
    reviewer_alignment_score,
    throughput_quality
):
    multiplier = (
        reviewer_alignment_score * 0.7 +
        throughput_quality * 0.3
    )

    return {
        "economic_reinforcement_score": round(multiplier, 4),
        "economic_reinforcement_strength": (
            "high"
            if multiplier >= 0.75
            else "developing"
        )
    }
