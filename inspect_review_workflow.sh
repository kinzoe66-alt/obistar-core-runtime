#!/usr/bin/env bash
set -euo pipefail

echo "== review queue =="
cat reports/review_queue/governed_review_queue.json

echo
echo "== replay artifacts =="
find reports/replay -type f -maxdepth 2 2>/dev/null | sort || true

echo
echo "== manual review sessions =="
find runtime/manual_review reports operational_outputs -type f 2>/dev/null | grep -Ei "review|package|queue|replay" | sort || true
