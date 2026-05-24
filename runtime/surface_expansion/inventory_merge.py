import json
from pathlib import Path

def merge_authorized_inventories(files, output_file):
    merged = {
        "program": "multi_program_governed_inventory",
        "source": "merged_authorized_inventories",
        "manual_review_required": True,
        "autonomous_submission": False,
        "surfaces": []
    }

    seen = set()

    for file in files:
        data = json.loads(Path(file).read_text(encoding="utf-8"))
        for surface in data.get("surfaces", []):
            sid = surface["runtime_surface_id"]
            if sid in seen:
                continue
            seen.add(sid)
            merged["surfaces"].append(surface)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    Path(output_file).write_text(json.dumps(merged, indent=2), encoding="utf-8")
    return merged
