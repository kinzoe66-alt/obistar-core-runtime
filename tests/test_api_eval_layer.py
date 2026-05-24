from runtime.api_eval.workflow_fingerprint import workflow_fingerprint
from runtime.api_eval.replay_priority import replay_priority
from runtime.api_eval.reviewer_clarity import reviewer_clarity_score
from runtime.api_eval.throughput_metrics import throughput_metrics

def test_workflow_fingerprint():
    result = workflow_fingerprint(
        "GET",
        "/api/profile",
        {"id": 1}
    )

    assert len(result["workflow_fingerprint"]) == 16

def test_replay_priority():
    result = replay_priority({
        "replayability": 0.9,
        "stability": 0.85,
        "noise": 0.1
    })

    assert result["recommended_replay"] is True

def test_reviewer_clarity():
    result = reviewer_clarity_score({
        "evidence_quality": 0.9,
        "replay_success_rate": 0.9,
        "operational_meaning": 0.8
    })

    assert result["reviewer_ready"] is True

def test_throughput_metrics():
    result = throughput_metrics(
        workflows_processed=100,
        replay_stable=70,
        reviewer_ready=60
    )

    assert result["throughput_efficiency"] == 1.3
