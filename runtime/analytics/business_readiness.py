def monetization_readiness(metrics):
    signal_quality = metrics.get("reviewer_signal_quality", 0.0)
    queue_health = metrics.get("queue_health", "degraded")

    ready = signal_quality >= 0.7 and queue_health == "healthy"

    return {
        "monetization_ready": ready,
        "recommended_operating_mode": (
            "small_scale_paid_validation"
            if ready
            else "continue_calibration"
        )
    }
