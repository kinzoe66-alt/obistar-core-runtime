def replay_retention_policy(days):
    if days < 30:
        tier = "short_term"
    elif days < 180:
        tier = "operational"
    else:
        tier = "long_term"

    return {
        "retention_days": days,
        "retention_tier": tier
    }
