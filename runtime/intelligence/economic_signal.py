def economic_signal(
    reviewer_signal_ratio,
    throughput_efficiency
):
    score = (
        reviewer_signal_ratio * 0.6 +
        throughput_efficiency * 0.4
    )

    return {
        "economic_signal_score": round(score, 4),
        "economic_signal_strength": (
            "high"
            if score >= 0.75
            else "moderate"
        )
    }
