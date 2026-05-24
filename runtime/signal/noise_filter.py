def noise_filter(observations):
    filtered = [
        observation
        for observation in observations
        if (
            observation.get("replay_history_strength") == "stable"
            and observation.get("reviewer_ready") is True
        )
    ]

    return {
        "filtered_observation_count": len(filtered),
        "filtered_observations": filtered
    }
