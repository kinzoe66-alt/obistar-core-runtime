def reviewer_bound(priority_distribution, max_highest_ratio=0.35):
    total = sum(priority_distribution.values())

    if total == 0:
        return {
            "reviewer_bound_state": "empty",
            "highest_priority_ratio": 0.0
        }

    highest = priority_distribution.get("highest_priority", 0)
    ratio = highest / total

    return {
        "reviewer_bound_state": (
            "bounded"
            if ratio <= max_highest_ratio
            else "overloaded"
        ),
        "highest_priority_ratio": round(ratio, 4)
    }
