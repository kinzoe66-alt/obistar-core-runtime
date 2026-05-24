def replay_priority(workflow):
    replayable = float(workflow.get("replayability", 0.0))
    stability = float(workflow.get("stability", 0.0))
    noise = float(workflow.get("noise", 0.0))

    score = max(0.0, (
        replayable * 0.45 +
        stability * 0.45 -
        noise * 0.10
    ))

    return {
        "replay_priority_score": round(score, 4),
        "recommended_replay": score >= 0.7
    }
