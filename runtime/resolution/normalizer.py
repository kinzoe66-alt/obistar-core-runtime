def normalize_contract(doc: dict) -> dict:
    normalized = dict(doc)

    normalized.setdefault("requires", {})
    normalized.setdefault("allowed_runtime_behavior", [])
    normalized.setdefault("blocked_runtime_behavior", [])
    normalized.setdefault("replay_requirements", {})
    normalized.setdefault("manual_review", {"required": True})

    normalized["allowed_runtime_behavior"] = sorted(set(normalized["allowed_runtime_behavior"]))
    normalized["blocked_runtime_behavior"] = sorted(set(normalized["blocked_runtime_behavior"]))

    return normalized
