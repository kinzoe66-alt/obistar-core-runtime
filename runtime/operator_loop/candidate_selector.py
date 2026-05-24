def select_operational_candidates(observations):
    return [
        item for item in observations
        if (
            item.get("manual_review_required") is True
            and item.get("autonomous_submission") is False
            and item.get("review_priority", {}).get("classification") == "priority_review"
            and item.get("replay_stability", {}).get("classification") == "stable"
            and item.get("report_quality", {}).get("classification") == "high_quality"
        )
    ]
