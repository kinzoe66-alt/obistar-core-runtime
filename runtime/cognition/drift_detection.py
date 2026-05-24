def confidence_drift(current_confidence, historical_confidence):
    delta = float(current_confidence) - float(historical_confidence)

    if abs(delta) < 0.15:
        status = "stable"
    elif delta > 0:
        status = "inflating"
    else:
        status = "degrading"

    return {
        "confidence_delta": round(delta, 4),
        "confidence_drift_status": status
    }
