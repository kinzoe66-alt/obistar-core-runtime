import json
from pathlib import Path

def persist_calibration_snapshot(output_file, payload):
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    Path(output_file).write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8"
    )

    return {
        "snapshot_written": True,
        "output_file": output_file
    }
