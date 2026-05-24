#!/usr/bin/env bash
set -euo pipefail

SCALE="${1:-12}"

mkdir -p calibration_runs/${SCALE}_surfaces/logs

python runtime_cli.py compare \
  > calibration_runs/${SCALE}_surfaces/logs/compare.log 2>&1

python runtime_cli.py select-observations \
  > calibration_runs/${SCALE}_surfaces/logs/select_observations.log 2>&1

python runtime_cli.py meaning-report \
  > calibration_runs/${SCALE}_surfaces/logs/meaning_report.log 2>&1

python runtime_cli.py review-queue \
  > calibration_runs/${SCALE}_surfaces/logs/review_queue.log 2>&1

cp reports/observations/observation_selection.json \
   calibration_runs/${SCALE}_surfaces/observation_selection.json

cp reports/review_queue/governed_review_queue.json \
   calibration_runs/${SCALE}_surfaces/review_queue.json

cp reports/meaning/operational_meaning.json \
   calibration_runs/${SCALE}_surfaces/operational_meaning.json

echo "saved calibration snapshot for ${SCALE} surfaces"
