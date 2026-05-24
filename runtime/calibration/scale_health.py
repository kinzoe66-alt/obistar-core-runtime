def scale_health(metrics):
    bad = [
        metric for metric in metrics
        if metric.get("drift_state") == "drifting"
    ]

    return {
        "drifting_metric_count": len(bad),
        "scale_health": "stable" if len(bad) == 0 else "needs_calibration"
    }
