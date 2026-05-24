#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import json
from pathlib import Path

drill = Path(
    "workflow_hardening/reports/adjudication_repetition_report.json"
)

scorecard = Path(
    "workflow_hardening/operator_trust/operator_trust_scorecard.json"
)

out = Path(
    "workflow_hardening/operator_trust/operator_trust_summary.json"
)

drill_data = json.loads(
    drill.read_text(encoding="utf-8")
)

scorecard_data = json.loads(
    scorecard.read_text(encoding="utf-8")
)

summary = {
    "summary": "operator_trust_formation",
    "candidate_count": drill_data.get("candidate_count", 0),
    "tracked_signals": list(scorecard_data["signals"].keys()),
    "trust_objective": {
        "review_throughput_refinement": True,
        "adjudication_confidence_acceleration": True,
        "evidence_readability_optimization": True,
        "lineage_clarity_compression": True,
        "operator_hesitation_reduction": True,
        "review_queue_prioritization_tuning": True
    },
    "completion_state": "operator_scoring_required",
    "manual_review_required": True,
    "autonomous_submission": False
}

out.write_text(
    json.dumps(summary, indent=2),
    encoding="utf-8"
)

print(json.dumps(summary, indent=2))
PY
