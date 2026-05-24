def package_gate(package):
    ready = (
        package.get("manual_review_required") is True
        and package.get("confirmed_issue") is False
        and float(package.get("replay_success_rate", 0.0)) >= 0.75
        and float(package.get("reviewer_clarity_score", 0.0)) >= 0.75
    )

    return {
        "review_package_ready": ready,
        "gate_status": (
            "ready_for_manual_review"
            if ready
            else "needs_more_evidence"
        )
    }
