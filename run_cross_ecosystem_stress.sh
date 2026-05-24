#!/usr/bin/env bash
set -euo pipefail

python -m pytest -q

python - <<'PY'
from runtime.surface_expansion.inventory_merge import merge_authorized_inventories
from runtime.surface_expansion.governed_expander import expand_governed_inventory

merge_authorized_inventories(
    [
        "authorized_scopes/live/hilton_authorized_surfaces.json",
        "authorized_scopes/live/second_program_authorized_surfaces.json"
    ],
    "authorized_scopes/expanded/multi_program_base.json"
)

expand_governed_inventory(
    "authorized_scopes/expanded/multi_program_base.json",
    "authorized_scopes/expanded/multi_program_96_surfaces.json",
    96
)
PY

mkdir -p calibration_runs/multi_program_96

python runtime_cli.py compare \
  --file authorized_scopes/expanded/multi_program_96_surfaces.json \
  > calibration_runs/multi_program_96/compare.json

python - <<'PY'
import json
from pathlib import Path

data = json.loads(Path("calibration_runs/multi_program_96/compare.json").read_text())

priority = {}
duplicates = {}
outcomes = {}
stable = 0
unstable = 0

for item in data["results"]:
    priority[item["review_priority"]["classification"]] = priority.get(item["review_priority"]["classification"], 0) + 1
    duplicates[item["deduplication"]["classification"]] = duplicates.get(item["deduplication"]["classification"], 0) + 1
    outcomes[item["outcome_learning"]["classification"]] = outcomes.get(item["outcome_learning"]["classification"], 0) + 1

    if item["replay_stability"]["classification"] == "stable":
        stable += 1
    else:
        unstable += 1

print("surface_count:", data["surface_count"])
print("stable:", stable)
print("unstable:", unstable)
print("priority_distribution:", priority)
print("duplicate_distribution:", duplicates)
print("outcome_distribution:", outcomes)
PY
