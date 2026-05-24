#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import json
from pathlib import Path

drill_path = Path(
    "workflow_hardening/reports/candidate_adjudication_drill.json"
)

out_path = Path(
    "workflow_hardening/reports/adjudication_repetition_report.json"
)

data = json.loads(
    drill_path.read_text(
        encoding="utf-8"
    )
)

results = []

for candidate in data["candidates"]:
    results.append({
        "sequence": candidate["sequence"],
        "candidate_id": candidate["candidate_id"],
        "surface_id": candidate["surface_id"],
        "lineage_inspected": False,
        "replay_inspected": False,
        "evidence_inspected": False,
        "manual_decision_recorded": False,
        "confusion": None,
        "hesitation": None,
        "ambiguity": None,
        "overload": None,
        "trust_gap": None,
        "review_confidence": None,
        "status": "operator_review_required",
        "manual_review_required": True,
        "autonomous_submission": False,
    })

report = {
    "workflow": "candidate_adjudication_repetition",
    "candidate_count": len(results),
    "results": results,
    "completion_rule": (
        "all candidates require manual operator review "
        "and friction recording"
    ),
    "manual_review_required": True,
    "autonomous_submission": False,
}

out_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

out_path.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8"
)

print(json.dumps(report, indent=2))
PY
