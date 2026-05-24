from runtime.duplicate_clusters.cluster_monitor import (
    DuplicateClusterMonitor,
)


def test_detects_large_duplicate_cluster():
    candidates = [
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "checkout"},
    ]

    result = DuplicateClusterMonitor().monitor(
        candidates
    )

    assert result["duplicate_cluster_detected"] is True
    assert result["largest_cluster_size"] == 5
    assert result["cluster_count"] == 2
    assert result["confirmed_issue"] is False


def test_detects_stable_cluster_distribution():
    candidates = [
        {"workflow_family": "auth"},
        {"workflow_family": "checkout"},
        {"workflow_family": "profile"},
    ]

    result = DuplicateClusterMonitor().monitor(
        candidates
    )

    assert result["duplicate_cluster_detected"] is False
    assert result["cluster_count"] == 3


def test_handles_empty_candidates():
    result = DuplicateClusterMonitor().monitor([])

    assert result["cluster_count"] == 0
    assert result["largest_cluster_size"] == 0
