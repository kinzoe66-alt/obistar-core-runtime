import json
from pathlib import Path

def load_weighting_history(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    histories = data.get("workflow_histories", [])

    if not isinstance(histories, list):
        raise ValueError("workflow_histories must be a list")

    return histories
