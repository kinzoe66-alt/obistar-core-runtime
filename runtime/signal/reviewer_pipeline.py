def reviewer_pipeline(observations):
    ready = [
        observation
        for observation in observations
        if observation.get("reviewer_ready") is True
    ]

    return {
        "reviewer_pipeline_count": len(ready),
        "pipeline_status": (
            "operational"
            if len(ready) > 0
            else "needs_calibration"
        )
    }
