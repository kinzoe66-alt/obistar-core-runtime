import json

from runtime.surface_scaling.baseline_loader import load_authorized_surface_baseline
from runtime.surface_scaling.surface_batcher import batch_surfaces
from runtime.surface_scaling.scaling_readiness import scaling_readiness

def test_authorized_surface_baseline_loader(tmp_path):
    path = tmp_path / "authorized_surfaces.json"
    path.write_text(json.dumps({
        "surfaces": [
            {"surface_id": "surface-001"},
            {"surface_id": "surface-002"}
        ]
    }), encoding="utf-8")

    result = load_authorized_surface_baseline(path)

    assert result["authorized_surface_count"] == 2

def test_surface_batcher():
    batches = batch_surfaces(
        [{"id": 1}, {"id": 2}, {"id": 3}],
        batch_size=2
    )

    assert len(batches) == 2

def test_scaling_readiness():
    result = scaling_readiness(
        surface_count=12,
        replay_capacity=4
    )

    assert result["surface_scaling_ready"] is True
    assert result["recommended_mode"] == "batch_governed_api_evaluation"
