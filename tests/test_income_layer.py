from runtime.income.program_selection import rank_authorized_program
from runtime.income.observation_value import governed_observation_value
from runtime.income.submission_gate import governed_submission_gate

def test_program_selection():
    result = rank_authorized_program({
        "program_id": "authorized-program-001",
        "scope_clarity": 0.9,
        "payout_signal": 0.8,
        "replay_fit": 0.85,
        "report_fit": 0.9
    })

    assert result["recommended_action"] == "prioritize_governed_validation"

def test_observation_value_and_gate():
    value = governed_observation_value({
        "observation_id": "OBS-001",
        "replay_success_rate": 0.9,
        "evidence_quality": 0.85,
        "reviewer_clarity": 0.9,
        "duplicate_penalty": 0.0
    })

    gate = governed_submission_gate(value)

    assert value["income_relevance_score"] >= 0.75
    assert gate["submission_mode"] == "manual_review_package_ready"
