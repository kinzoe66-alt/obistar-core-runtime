#!/usr/bin/env bash
set -euo pipefail

echo "== review queue =="
cat reports/review_queue/governed_review_queue.json

echo
echo "== review packages =="
cat operational_outputs/latest/packages/review_packages.json

echo
echo "== replay lineage =="
cat reports/replay/replay_route_package.json

echo
echo "== priority intuition samples =="
grep -n "priority_intuition" -A 10 operational_outputs/latest/packages/review_packages.json | head -160

echo
echo "== organizational continuity scorecard =="
cat workflow_hardening/organizational_continuity/organizational_continuity_scorecard.md
