def reviewer_alignment(acceptance_ratio, reviewer_clarity):
    score = (
        acceptance_ratio * 0.5 +
        reviewer_clarity * 0.5
    )

    return {
        "reviewer_alignment_score": round(score, 4),
        "reviewer_alignment_strength": (
            "high"
            if score >= 0.75
            else "developing"
        )
    }
