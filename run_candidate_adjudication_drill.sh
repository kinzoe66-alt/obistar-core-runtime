#!/usr/bin/env bash
set -euo pipefail

QUEUE="reports/review_queue/governed_review_queue.json"
OUT="workflow_hardening/reports/candidate_adjudication_drill.json"

python - <<'PY'
import json
from pathlib import Path

queue_path = Path("reports/review_queue/governed_review_queue.json")
out_path = Path("workflow_hardening/reports/candidate_adjudication_drill.json")
out_path.parent.mkdir(parents=True, exist_ok=True)

queue = json.loads(queue_path.read_text(encoding="utf-8"))

items = queue.get("queue", queue if isinstance(queue, list) else [])

drill = {
    "drill": "candidate_adjudication",
    "candidate_count": len(items),
    "candidates": [],
    "manual_review_required": True,
    "autonomous_submission": False,
}

for index, item in enumerate(items[:8], start=1):
    drill["candidates"].append({
        "sequence": index,
        "candidate_id": item.get("observation_id", item.get("candidate_id", item.get("package_id", "unknown"))),
        "surface_id": item.get("surface_id", "unknown"),
        "inspection_steps": [
            "inspect_queue_position",
            "inspect_replay_artifact",
            "inspect_evidence",
            "inspect_lineage",
            "make_manual_adjudication_decision",
            "record_friction"
        ],
        "review_status": "pending_manual_adjudication",
        "friction_record_required": True,
        "manual_review_required": True,
        "autonomous_submission": False,
    })

out_path.write_text(json.dumps(drill, indent=2), encoding="utf-8")
print(json.dumps(drill, indent=2))
PY
