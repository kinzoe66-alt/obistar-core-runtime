def damp_priority(weighted_score, outcome_classification):
    score = float(weighted_score)

    if outcome_classification == "high_signal":
        capped = min(score, 0.89)
    elif outcome_classification == "medium_signal":
        capped = min(score, 0.74)
    else:
        capped = min(score, 0.49)

    if capped >= 0.85:
        classification = "highest_priority"
    elif capped >= 0.70:
        classification = "priority_review"
    else:
        classification = "hold"

    return {
        "damped_priority_score": round(capped, 4),
        "damped_priority_classification": classification,
        "manual_review_required": True,
        "autonomous_submission": False
    }
