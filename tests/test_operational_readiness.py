from runtime.operations.readiness import OperationalReadiness

def test_operational_readiness():
    result = OperationalReadiness().evaluate({
        "imported": {"imported_count": 3},
        "comparison": {
            "surface_count": 3,
            "manual_review_required": True,
            "autonomous_submission": False
        }
    })

    assert result["ready"] is True
