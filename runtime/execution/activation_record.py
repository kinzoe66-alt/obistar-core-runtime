from runtime.resolution.composition_snapshot import (
    build_composition_snapshot
)
from runtime.authority.registry import AuthorityRegistry

def build_activation_record(surface: str, authority_stack: dict) -> dict:
    admitted = []

    for kind, entries in sorted(authority_stack.items()):
        for entry in entries:
            admitted.append({
                "kind": kind,
                "name": entry["name"],
                "version": entry["version"],
                "path": entry["path"],
            })

    registry = AuthorityRegistry()
    scope = registry.contract("scope_contract")

    return {
        "execution_surface": surface,
        "scope": {
            "name": scope["name"],
            "allowed_surfaces": scope["execution_surface"]["allowed"],
        },
        "admitted_authority": admitted,
        "composition": build_composition_snapshot(),
        "terminal_state": "manual_review",
        "autonomous_submission": False,
    }
