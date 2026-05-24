#!/usr/bin/env bash
set -euo pipefail

echo "== review queue =="
cat reports/review_queue/governed_review_queue.json

echo
echo "== replay package =="
cat reports/replay/replay_route_package.json

echo
echo "== review package =="
cat operational_outputs/latest/packages/review_packages.json

echo
echo "== operator signal worksheet =="
cat workflow_hardening/drill_signals/review_signal_scorecard.md
