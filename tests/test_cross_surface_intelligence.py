from runtime.intelligence.workflow_family import workflow_family
from runtime.intelligence.replay_memory import replay_memory
from runtime.intelligence.reviewer_signal_memory import reviewer_signal_memory
from runtime.intelligence.economic_signal import economic_signal

def test_workflow_family():
    result = workflow_family(
        "GET",
        "/api/profile"
    )

    assert result["workflow_family"] == "api_workflow"

def test_replay_memory():
    result = replay_memory([
        {"replay_history_strength": "stable"},
        {"replay_history_strength": "stable"},
        {"replay_history_strength": "unstable"}
    ])

    assert result["memory_strength"] == "strong"

def test_reviewer_signal_memory():
    result = reviewer_signal_memory([
        {"reviewer_ready": True},
        {"reviewer_ready": True},
        {"reviewer_ready": False}
    ])

    assert result["reviewer_signal_strength"] == "developing"

def test_economic_signal():
    result = economic_signal(
        reviewer_signal_ratio=0.8,
        throughput_efficiency=0.8
    )

    assert result["economic_signal_strength"] == "high"
