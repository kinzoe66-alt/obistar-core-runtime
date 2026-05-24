#!/usr/bin/env bash
set -euo pipefail

echo "== review packages =="
cat operational_outputs/latest/packages/review_packages.json

echo
echo "== priority intuition samples =="
grep -n "priority_intuition" -A 10 operational_outputs/latest/packages/review_packages.json | head -160

echo
echo "== automatic trust drill =="
cat workflow_hardening/automatic_trust/automatic_trust_drill.md

echo
echo "== operator economics =="
cat workflow_hardening/operator_economics/operator_economics_scorecard.md

echo
echo "== team readiness scorecard =="
cat workflow_hardening/team_readiness/team_review_scorecard.md
