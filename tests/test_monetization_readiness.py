from runtime.analytics.reviewer_metrics import reviewer_signal_quality
from runtime.analytics.queue_health import review_queue_health
from runtime.analytics.business_readiness import monetization_readiness

def test_monetization_readiness():
    observations = [
        {
            "replay_success_rate": 0.9,
            "duplicate_pressure": "none",
            "replay_history_strength": "stable"
        },
        {
            "replay_success_rate": 0.85,
            "duplicate_pressure": "low",
            "replay_history_strength": "stable"
        }
    ]

    reviewer = reviewer_signal_quality(observations)
    queue = review_queue_health(observations)

    readiness = monetization_readiness({
        **reviewer,
        **queue
    })

    assert reviewer["reviewer_signal_quality"] == 1.0
    assert queue["queue_health"] == "healthy"
    assert readiness["monetization_ready"] is True
