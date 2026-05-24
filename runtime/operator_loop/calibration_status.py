def calibration_status(selected_count, held_count):
    total = selected_count + held_count
    ratio = 0.0 if total == 0 else selected_count / total

    return {
        "selected_count": selected_count,
        "held_count": held_count,
        "selection_ratio": round(ratio, 4),
        "calibration_state": "usable" if ratio >= 0.5 else "needs_tuning"
    }
