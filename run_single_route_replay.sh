#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
import json
from pathlib import Path

from runtime.governed_replay.single_route import (
    SingleRouteReplayExecutor,
)

queue_path = Path(
    "reports/review_queue/governed_review_queue.json"
)

queue = json.loads(
    queue_path.read_text(
        encoding="utf-8"
    )
)

candidate = queue["queue"][0]

artifact = SingleRouteReplayExecutor().run(
    candidate=candidate,
    command=["python", "--version"],
    output_path="reports/replay/single_route_replay.json",
)

print(json.dumps(artifact, indent=2))
PY
