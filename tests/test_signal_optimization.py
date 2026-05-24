from runtime.signal.noise_filter import noise_filter
from runtime.signal.duplicate_suppression import duplicate_suppression
from runtime.signal.reviewer_pipeline import reviewer_pipeline
from runtime.signal.throughput_optimizer import throughput_optimizer

def test_noise_filter():
    result = noise_filter([
        {
            "replay_history_strength": "stable",
            "reviewer_ready": True
        },
        {
            "replay_history_strength": "unstable",
            "reviewer_ready": False
        }
    ])

    assert result["filtered_observation_count"] == 1

def test_duplicate_suppression():
    result = duplicate_suppression([
        {"workflow_fingerprint": "abc"},
        {"workflow_fingerprint": "abc"},
        {"workflow_fingerprint": "xyz"}
    ])

    assert result["unique_observation_count"] == 2

def test_reviewer_pipeline():
    result = reviewer_pipeline([
        {"reviewer_ready": True},
        {"reviewer_ready": False}
    ])

    assert result["pipeline_status"] == "operational"

def test_throughput_optimizer():
    result = throughput_optimizer(
        workflows_processed=100,
        reviewer_ready=60
    )

    assert result["throughput_quality"] == "high"
