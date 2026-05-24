def reviewer_capacity(queue_size, reviewers):
    if reviewers <= 0:
        return {
            "capacity_state": "unassigned",
            "reviewer_load": None
        }

    load = queue_size / reviewers

    if load <= 10:
        state = "healthy"
    elif load <= 25:
        state = "elevated"
    else:
        state = "saturated"

    return {
        "capacity_state": state,
        "reviewer_load": round(load, 2)
    }
