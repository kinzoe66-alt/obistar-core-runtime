import json

from runtime.cognition.report import write_cognition_quality_report

def test_cognition_quality_report_written(tmp_path):
    output = tmp_path / "cognition_quality.json"

    report = write_cognition_quality_report(
        "replay_history/replay_history.sample.json",
        output,
        historical_confidence=0.74,
        evidence_quality=0.8
    )

    assert output.exists()
    saved = json.loads(output.read_text(encoding="utf-8"))

    assert report["report_type"] == "governed_cognition_quality"
    assert saved["confirmed_issue"] is False
    assert saved["manual_review_required"] is True
    assert saved["observations"][0]["observation_id"] == "OBS-001"
