import json
from pathlib import Path

from runtime.cognition.cognition_quality import assess_cognition_quality
from runtime.cognition.history_ingestion import load_replay_history

def write_cognition_quality_report(
    history_file,
    output_file,
    historical_confidence=0.5,
    evidence_quality=0.5
):
    observations = load_replay_history(history_file)

    report = {
        "report_type": "governed_cognition_quality",
        "confirmed_issue": False,
        "manual_review_required": True,
        "observations": [
            assess_cognition_quality(
                observation,
                historical_confidence=historical_confidence,
                evidence_quality=evidence_quality
            )
            for observation in observations
        ]
    }

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    Path(output_file).write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report
