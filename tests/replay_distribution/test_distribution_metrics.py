from runtime.replay_distribution.distribution_metrics import (
    ReplayDistributionMetrics,
)


def test_detects_balanced_distribution():
    history = [
        {"workflow_family": "auth"},
        {"workflow_family": "checkout"},
        {"workflow_family": "profile"},
    ]

    result = ReplayDistributionMetrics().analyze(
        history
    )

    assert result["distribution_stable"] is True
    assert result["replay_count"] == 3
    assert result["confirmed_issue"] is False


def test_detects_concentrated_distribution():
    history = [
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "checkout"},
    ]

    result = ReplayDistributionMetrics().analyze(
        history
    )

    assert result["distribution_stable"] is False
    assert result["largest_bucket"] == 4


def test_handles_empty_history():
    result = ReplayDistributionMetrics().analyze([])

    assert result["replay_count"] == 0
    assert result["distribution_stable"] is False
