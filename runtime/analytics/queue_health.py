def review_queue_health(observations):
    total = len(observations)

    duplicate_heavy = [
        o for o in observations
        if o.get("duplicate_pressure") in {"moderate", "high"}
    ]

    unstable = [
        o for o in observations
        if o.get("replay_history_strength") == "unstable"
    ]

    return {
        "queue_size": total,
        "duplicate_heavy_count": len(duplicate_heavy),
        "unstable_replay_count": len(unstable),
        "queue_health": (
            "healthy"
            if len(duplicate_heavy) == 0 and len(unstable) == 0
            else "degraded"
        )
    }
