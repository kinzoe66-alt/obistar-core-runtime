#!/usr/bin/env bash
set -euo pipefail

echo "== queue ordering =="
cat reports/review_queue/governed_review_queue.json

echo
echo "== replay skimmability =="
cat reports/replay/replay_route_package.json

echo
echo "== priority intuition =="
grep -n "priority_intuition" -A 10 operational_outputs/latest/packages/review_packages.json | head -160

echo
echo "== review guidance =="
grep -n "review_guidance" -A 8 operational_outputs/latest/packages/review_packages.json | head -120

echo
echo "== automatic trust drill =="
cat workflow_hardening/automatic_trust/automatic_trust_drill.md
