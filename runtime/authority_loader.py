from functools import lru_cache
from pathlib import Path
import yaml


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@lru_cache(maxsize=8)
def load_authority_tree(root):
    root_path = Path(root)
    docs = {}

    for path in sorted(root_path.rglob("*.yaml")):
        if "__pycache__" in path.parts:
            continue
        docs[str(path)] = load_yaml(str(path))

    return docs
