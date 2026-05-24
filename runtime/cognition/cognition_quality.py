from runtime.cognition.replay_distribution import replay_distribution
from runtime.cognition.drift_detection import confidence_drift
from runtime.cognition.priority_inflation import priority_inflation
from runtime.cognition.duplicate_cluster import duplicate_cluster_pressure

def assess_cognition_quality(observation, historical_confidence=0.5, evidence_quality=0.5):
    replay = replay_distribution(observation)
    drift = confidence_drift(observation.get("confidence", 0.0), historical_confidence)
    inflation = priority_inflation(
        observation.get("review_priority", 0.0),
        replay["replay_success_rate"],
        evidence_quality
    )
    duplicate = duplicate_cluster_pressure(observation.get("duplicate_cluster_size", 1))

    return {
        "observation_id": observation.get("observation_id"),
        "confirmed_issue": False,
        "manual_review_required": True,
        **replay,
        **drift,
        **inflation,
        **duplicate
    }
