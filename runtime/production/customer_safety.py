def governed_customer_safety(observation_count, unstable_count):
    safe = unstable_count == 0

    return {
        "customer_safe": safe,
        "unstable_observation_count": unstable_count,
        "authorized_observation_count": observation_count,
        "recommended_mode": (
            "review_enabled"
            if safe
            else "calibration_required"
        )
    }
