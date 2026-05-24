from runtime.intake.surface_contracts import SurfaceContractExecutor

def test_surface_contracts_admit_three_surfaces():
    executor = SurfaceContractExecutor()

    surfaces = executor.admitted_surfaces()

    assert len(surfaces) >= 3
    assert all(s["manual_review_required"] is True for s in surfaces)
