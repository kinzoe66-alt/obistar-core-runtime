def scaling_readiness(surface_count, replay_capacity):
    ready = surface_count > 0 and replay_capacity > 0

    return {
        "surface_scaling_ready": ready,
        "authorized_surface_count": surface_count,
        "replay_capacity": replay_capacity,
        "recommended_mode": (
            "batch_governed_api_evaluation"
            if ready
            else "baseline_calibration_required"
        )
    }
