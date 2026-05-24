from runtime.operator_loop.candidate_selector import select_operational_candidates
from runtime.operator_loop.calibration_status import calibration_status
from runtime.operator_loop.reviewer_quality import reviewer_quality
from runtime.operator_loop.daily_throughput import daily_throughput

def test_candidate_selector():
    selected = select_operational_candidates([
        {
            "manual_review_required": True,
            "autonomous_submission": False,
            "review_priority": {"classification": "priority_review"},
            "replay_stability": {"classification": "stable"},
            "report_quality": {"classification": "high_quality"}
        },
        {
            "manual_review_required": True,
            "autonomous_submission": False,
            "review_priority": {"classification": "hold"},
            "replay_stability": {"classification": "stable"},
            "report_quality": {"classification": "high_quality"}
        }
    ])

    assert len(selected) == 1

def test_calibration_status():
    result = calibration_status(2, 1)
    assert result["calibration_state"] == "usable"

def test_reviewer_quality():
    result = reviewer_quality({
        "replay_score": 1.0,
        "evidence_score": 1.0,
        "explanation_score": 0.8
    })
    assert result["reviewer_quality_state"] == "review_ready"

def test_daily_throughput():
    result = daily_throughput(100, 12, 4)
    assert result["candidate_rate"] == 0.12
    assert result["package_rate"] == 0.04
