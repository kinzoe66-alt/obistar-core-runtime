def onboarding_readiness(metrics):
    replay_quality = metrics.get("replay_quality", 0.0)
    reviewer_signal = metrics.get("reviewer_signal_quality", 0.0)

    ready = replay_quality >= 0.7 and reviewer_signal >= 0.7

    return {
        "onboarding_ready": ready,
        "recommended_customer_stage": (
            "limited_governed_validation_beta"
            if ready
            else "internal_calibration_only"
        )
    }
