REQUIRED_FIELDS = ("kind", "name", "version")

def validate_contract(doc: dict, path: str = "<memory>"):
    if not isinstance(doc, dict):
        raise ValueError(f"{path} is not a mapping")

    missing = [f for f in REQUIRED_FIELDS if f not in doc]
    if missing:
        raise ValueError(f"{path} missing required fields: {missing}")

    allowed = set(doc.get("allowed_runtime_behavior", []))
    blocked = set(doc.get("blocked_runtime_behavior", []))
    overlap = allowed & blocked

    if overlap:
        raise ValueError(f"{path} has allowed/blocked overlap: {sorted(overlap)}")

    return True
