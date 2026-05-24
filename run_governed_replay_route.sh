#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import json

from runtime.governed_replay.replay_route_runner import (
    GovernedReplayRouteRunner
)

result = (
    GovernedReplayRouteRunner()
    .run()
)

print(
    json.dumps(
        result,
        indent=2
    )
)
PY
