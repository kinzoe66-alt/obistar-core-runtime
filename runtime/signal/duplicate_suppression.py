def duplicate_suppression(observations):
    unique = []
    seen = set()

    for observation in observations:
        fingerprint = observation.get("workflow_fingerprint")

        if fingerprint in seen:
            continue

        seen.add(fingerprint)
        unique.append(observation)

    return {
        "unique_observation_count": len(unique),
        "suppressed_duplicate_count": (
            len(observations) - len(unique)
        ),
        "observations": unique
    }
