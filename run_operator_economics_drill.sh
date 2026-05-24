#!/usr/bin/env bash
set -euo pipefail

echo "== queue =="
cat reports/review_queue/governed_review_queue.json

echo
echo "== review packages =="
cat operational_outputs/latest/packages/review_packages.json

echo
echo "== automatic trust drill =="
cat workflow_hardening/automatic_trust/automatic_trust_drill.md

echo
echo "== operator economics scorecard =="
cat workflow_hardening/operator_economics/operator_economics_scorecard.md
