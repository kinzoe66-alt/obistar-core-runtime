from runtime.governed_scoring.distributed_replay import (
    DistributedReplayOrchestrator,
)


def test_distributed_replay_assigns_items():
    result = DistributedReplayOrchestrator().plan(
        [{"id": "a"}, {"id": "b"}, {"id": "c"}],
        workers=2,
    )

    assert result["worker_count"] == 2
    assert result["assignment_count"] == 3
    assert result["assignments"][2]["worker_id"] == 0
