REVIEWER_DECISIONS = {
    "useful",
    "duplicate",
    "low_signal",
    "needs_more_evidence",
    "not_actionable",
}


REQUIRED_FIELDS = {
    "candidate_id",
    "reviewer_decision",
    "review_notes",
    "replay_accuracy",
    "priority_correctness",
    "timestamp",
}


def validate_review_outcome(record):
    missing = REQUIRED_FIELDS - set(record.keys())

    if missing:
        return {
            "valid": False,
            "reason": "missing_required_fields",
            "missing": sorted(missing),
        }

    if record["reviewer_decision"] not in REVIEWER_DECISIONS:
        return {
            "valid": False,
            "reason": "invalid_reviewer_decision",
            "allowed": sorted(REVIEWER_DECISIONS),
        }

    for field in ["replay_accuracy", "priority_correctness"]:
        value = record[field]

        if not isinstance(value, (int, float)):
            return {
                "valid": False,
                "reason": "invalid_numeric_field",
                "field": field,
            }

        if value < 0 or value > 1:
            return {
                "valid": False,
                "reason": "numeric_field_out_of_range",
                "field": field,
            }

    return {
        "valid": True,
        "reason": "review_outcome_valid",
    }
