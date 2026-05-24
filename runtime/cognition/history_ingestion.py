import json
from pathlib import Path

def load_replay_history(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    observations = data.get("observations", [])
    if not isinstance(observations, list):
        raise ValueError("observations must be a list")
    return observations
