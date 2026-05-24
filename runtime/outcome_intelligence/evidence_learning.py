def evidence_learning(packages):
    replay_supported = [
        package for package in packages
        if package.get("replay_success_rate", 0.0) >= 0.75
    ]

    return {
        "high_replay_packages": len(replay_supported),
        "evidence_learning_strength": (
            "strong"
            if len(replay_supported) >= 3
            else "developing"
        )
    }
