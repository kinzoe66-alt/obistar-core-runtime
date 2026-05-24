def throughput_metrics(
    workflows_processed,
    replay_stable,
    reviewer_ready
):
    if workflows_processed <= 0:
        efficiency = 0.0
    else:
        efficiency = (
            (replay_stable + reviewer_ready)
            / workflows_processed
        )

    return {
        "workflow_count": workflows_processed,
        "replay_stable_count": replay_stable,
        "reviewer_ready_count": reviewer_ready,
        "throughput_efficiency": round(efficiency, 4)
    }
