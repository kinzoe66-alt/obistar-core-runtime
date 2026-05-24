def replay_memory(observations):
    stable = [
        o for o in observations
        if o.get("replay_history_strength") == "stable"
    ]

    unstable = [
        o for o in observations
        if o.get("replay_history_strength") == "unstable"
    ]

    return {
        "stable_replay_patterns": len(stable),
        "unstable_replay_patterns": len(unstable),
        "memory_strength": (
            "strong"
            if len(stable) >= len(unstable)
            else "weak"
        )
    }
