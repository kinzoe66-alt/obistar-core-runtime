#!/usr/bin/env bash
set -euo pipefail

echo "== queue =="
cat reports/review_queue/governed_review_queue.json

echo
echo "== replay confirmation =="
cat reports/replay/replay_route_package.json

echo
echo "== priority intuition samples =="
grep -n "priority_intuition" -A 8 operational_outputs/latest/packages/review_packages.json | head -120

echo
echo "== cognition metrics worksheet =="
cat workflow_hardening/operator_metrics/operator_cognition_metrics.md
