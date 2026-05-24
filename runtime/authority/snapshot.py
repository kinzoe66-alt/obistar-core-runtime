import json
from pathlib import Path
from runtime.authority.registry import AuthorityRegistry

def write_authority_snapshot(path="state/authority_snapshot.json"):
    registry = AuthorityRegistry()

    snapshot = {
        "authority_kinds": sorted(registry.stack.keys()),
        "contracts": []
    }

    for kind, entries in sorted(registry.stack.items()):
        for entry in entries:
            snapshot["contracts"].append({
                "kind": kind,
                "name": entry["name"],
                "version": entry["version"],
                "path": entry["path"],
            })

    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

    return snapshot
