from functools import lru_cache
from pathlib import Path
import yaml

from runtime.substrate_paths import AUTHORITY_ROOT


def resolve_authority_path(path):
    p = Path(path)

    if p.exists():
        return p

    if str(path).startswith("authority/"):
        relative = Path(*p.parts[1:])
        candidate = AUTHORITY_ROOT / relative

        if candidate.exists():
            return candidate

    return p


def load_yaml(path):
    resolved = resolve_authority_path(path)

    with open(resolved, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@lru_cache(maxsize=8)
def load_authority_tree(root=None):
    root_path = Path(root) if root else AUTHORITY_ROOT

    if str(root_path) == "authority":
        root_path = AUTHORITY_ROOT

    docs = {}

    for path in sorted(root_path.rglob("*.yaml")):
        if "__pycache__" in path.parts:
            continue

        docs[str(path)] = load_yaml(str(path))

    return docs
