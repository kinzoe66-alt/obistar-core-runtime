def throughput_optimizer(
    workflows_processed,
    reviewer_ready
):
    if workflows_processed <= 0:
        ratio = 0.0
    else:
        ratio = reviewer_ready / workflows_processed

    return {
        "reviewer_ready_ratio": round(ratio, 4),
        "throughput_quality": (
            "high"
            if ratio >= 0.5
            else "developing"
        )
    }
