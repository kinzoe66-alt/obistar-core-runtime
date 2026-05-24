def governed_submission_gate(observation):
    ready = (
        observation.get("manual_review_required") is True and
        observation.get("confirmed_issue") is False and
        float(observation.get("income_relevance_score", 0.0)) >= 0.75
    )

    return {
        "submission_ready": ready,
        "submission_mode": (
            "manual_review_package_ready"
            if ready
            else "continue_evidence_calibration"
        )
    }
