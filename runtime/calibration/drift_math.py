def metric_drift(previous, current):
    previous = float(previous)
    current = float(current)

    if previous == 0:
        delta = 0.0 if current == 0 else 1.0
    else:
        delta = (current - previous) / previous

    return {
        "drift_delta": round(delta, 4),
        "drift_state": "stable" if abs(delta) <= 0.15 else "drifting"
    }
