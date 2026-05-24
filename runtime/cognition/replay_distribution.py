def replay_distribution(observation):
    attempts = int(observation.get("replay_attempts", 0))
    successes = int(observation.get("replay_successes", 0))

    if attempts <= 0:
        return {
            "replay_success_rate": 0.0,
            "replay_history_strength": "thin"
        }

    rate = successes / attempts

    if attempts < 3:
        strength = "thin"
    elif rate >= 0.8:
        strength = "stable"
    elif rate >= 0.5:
        strength = "mixed"
    else:
        strength = "unstable"

    return {
        "replay_success_rate": round(rate, 4),
        "replay_history_strength": strength
    }
