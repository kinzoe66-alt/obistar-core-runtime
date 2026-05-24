#!/usr/bin/env bash
set -euo pipefail

echo "== review packages =="
cat operational_outputs/latest/packages/review_packages.json

echo
echo "== priority intuition samples =="
grep -n "priority_intuition" -A 10 operational_outputs/latest/packages/review_packages.json | head -160

echo
echo "== organizational continuity =="
cat workflow_hardening/organizational_continuity/organizational_continuity_scorecard.md

echo
echo "== enterprise trust scorecard =="
cat workflow_hardening/enterprise_trust/enterprise_trust_scorecard.md
