from runtime.cognition_damping.priority_damping import damp_priority
from runtime.cognition_damping.reviewer_bound import reviewer_bound

def test_high_signal_damping_remains_elevated():
    result = damp_priority(1.0, "high_signal")
    assert result["damped_priority_classification"] == "highest_priority"

def test_medium_signal_damping_does_not_overinflate():
    result = damp_priority(1.0, "medium_signal")
    assert result["damped_priority_classification"] == "priority_review"

def test_weak_signal_damping_suppresses():
    result = damp_priority(1.0, "weak_signal")
    assert result["damped_priority_classification"] == "hold"

def test_reviewer_bound_detects_overload():
    result = reviewer_bound({
        "highest_priority": 96
    })
    assert result["reviewer_bound_state"] == "overloaded"
