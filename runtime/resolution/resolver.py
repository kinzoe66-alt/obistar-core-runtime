from runtime.contract_validator import validate_contract
from runtime.resolution.normalizer import normalize_contract

def resolve_authority_stack(docs: dict) -> dict:
    resolved = {}

    for path, doc in sorted(docs.items()):
        validate_contract(doc, path)
        normalized = normalize_contract(doc)
        kind = normalized["kind"]
        resolved.setdefault(kind, [])
        resolved[kind].append({
            "path": path,
            "name": normalized["name"],
            "version": normalized["version"],
            "document": normalized,
        })

    return resolved
