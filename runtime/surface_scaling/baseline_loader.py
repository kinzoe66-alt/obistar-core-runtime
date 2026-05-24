import json
from pathlib import Path

def load_authorized_surface_baseline(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))

    if isinstance(data, dict):
        surfaces = data.get("surfaces") or data.get("assets") or []
    elif isinstance(data, list):
        surfaces = data
    else:
        raise ValueError("authorized surface baseline must be a list or object")

    return {
        "authorized_surface_count": len(surfaces),
        "surfaces": surfaces
    }
