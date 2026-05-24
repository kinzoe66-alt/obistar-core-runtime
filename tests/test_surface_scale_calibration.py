from runtime.calibration.scale_steps import scale_steps
from runtime.calibration.drift_math import metric_drift
from runtime.calibration.scale_health import scale_health
from runtime.calibration.calibration_plan import calibration_plan

def test_scale_steps():
    assert scale_steps(12, 2, 4) == [12, 24, 48, 96]

def test_metric_drift_stable():
    result = metric_drift(0.80, 0.74)
    assert result["drift_state"] == "stable"

def test_metric_drift_detected():
    result = metric_drift(0.80, 0.60)
    assert result["drift_state"] == "drifting"

def test_scale_health():
    result = scale_health([
        {"drift_state": "stable"},
        {"drift_state": "stable"}
    ])
    assert result["scale_health"] == "stable"

def test_calibration_plan():
    plan = calibration_plan([12, 24])
    assert plan[0]["surface_count"] == 12
    assert plan[0]["autonomous_submission"] is False
