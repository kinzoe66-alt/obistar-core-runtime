def reviewer_workflow_state(observation):
    replay = observation.get("replay_history_strength")
    confidence = observation.get("confidence_drift_status")

    if replay == "stable" and confidence == "stable":
        state = "ready_for_manual_review"
    elif replay == "unstable":
        state = "needs_replay_calibration"
    else:
        state = "needs_confidence_review"

    return {
        "workflow_state": state,
        "manual_review_required": True
    }
