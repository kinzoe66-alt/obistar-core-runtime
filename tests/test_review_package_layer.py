from runtime.review_package.package_builder import build_review_package
from runtime.review_package.package_gate import package_gate

def test_review_package_ready():
    package = build_review_package({
        "observation_id": "OBS-001",
        "summary": "Authorized governed validation observation.",
        "evidence": ["replay-1", "replay-2"],
        "replay_success_rate": 0.9,
        "reviewer_clarity_score": 0.85
    })

    gate = package_gate(package)

    assert package["confirmed_issue"] is False
    assert package["manual_review_required"] is True
    assert gate["review_package_ready"] is True
