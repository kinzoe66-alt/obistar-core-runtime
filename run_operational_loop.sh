#!/usr/bin/env bash
set -euo pipefail

INVENTORY="${1:-authorized_scopes/expanded/multi_program_96_surfaces.json}"
RUN_ID="${2:-latest}"

OUT_DIR="operational_outputs/${RUN_ID}"

mkdir -p \
  "${OUT_DIR}/replay" \
  "${OUT_DIR}/candidates" \
  "${OUT_DIR}/packages" \
  "${OUT_DIR}/exports" \
  "${OUT_DIR}/logs"

python -m pytest -q \
  > "${OUT_DIR}/logs/tests.log" 2>&1

python runtime_cli.py compare \
  --file "${INVENTORY}" \
  > "${OUT_DIR}/replay/compare.json"

python <<'PY'
import json
from pathlib import Path

from runtime.economic_diversity.diverse_selector import (
    select_diverse_candidates
)

from runtime.economic_diversity.diversity_metrics import (
    diversity_metrics
)

from runtime.review_packages.package_builder import (
    build_review_package
)

RUN_DIR = Path(
    "operational_outputs/latest"
)

compare = json.loads(
    (
        RUN_DIR /
        "replay/compare.json"
    ).read_text(
        encoding="utf-8"
    )
)

candidates = []

for item in compare["results"]:

    if item["review_priority"]["classification"] not in [
        "highest_priority",
        "priority_review"
    ]:
        continue

    surface_id = item["surface_id"]

    parent = (
        surface_id
        .split("::")[0]
    )

    candidates.append({

        "surface_id": surface_id,

        "parent_authorized_surface_id": parent,

        "workflow_family": (
            item.get(
                "workflow_family"
            )
        ),

        "priority": (
            item["review_priority"]
        ),

        "outcome_learning": (
            item["outcome_learning"]
        ),

        "replay_stability": (
            item["replay_stability"]
        ),

        "report_quality": (
            item["report_quality"]
        ),

        "deduplication": (
            item["deduplication"]
        ),

        "manual_review_required": True,

        "autonomous_submission": False
    })

selection = select_diverse_candidates(
    candidates,
    limit=8
)

metrics = diversity_metrics(
    selection["selected_candidates"]
)

packages = [

    build_review_package(
        candidate
    )

    for candidate
    in selection["selected_candidates"]
]

summary = {

    "surface_count": (
        compare["surface_count"]
    ),

    "candidate_count": (
        len(candidates)
    ),

    "review_package_count": (
        len(packages)
    ),

    "diversity_metrics": metrics,

    "manual_review_required": True,

    "autonomous_submission": False
}

(
    RUN_DIR /
    "candidates/diversified_candidates.json"
).write_text(
    json.dumps(
        selection,
        indent=2
    ),
    encoding="utf-8"
)

(
    RUN_DIR /
    "packages/review_packages.json"
).write_text(
    json.dumps(
        packages,
        indent=2
    ),
    encoding="utf-8"
)

(
    RUN_DIR /
    "exports/operational_summary.json"
).write_text(
    json.dumps(
        summary,
        indent=2
    ),
    encoding="utf-8"
)

print(
    "operational loop complete"
)

print(
    "review_package_count:",
    len(packages)
)
PY

echo ""
echo "== operational monetization loop complete =="
