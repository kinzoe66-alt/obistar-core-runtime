from runtime.resolution.composition_snapshot import (
    build_composition_snapshot
)

def test_composition_snapshot():

    snapshot = build_composition_snapshot()

    assert snapshot["composition_order"]
