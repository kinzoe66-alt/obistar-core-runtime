import json

from runtime.authority.registry import AuthorityRegistry
from runtime.activation.fail_closed import require

class SurfaceContractExecutor:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contracts(self):
        return self.registry.contracts("surface_contract")

    def validate_contract(self, document: dict):
        surface = document["surface"]
        workflow = document["workflow"]
        reporting = document["reporting"]

        require(surface["authorized_scope"] is True, "authorized scope required")
        require(bool(surface["surface_id"]), "surface id required")
        require(bool(surface["program"]), "program required")
        require(bool(surface["validation_surface"]), "validation surface required")

        require(workflow["replay_required"] is True, "replay required")
        require(workflow["evidence_required"] is True, "evidence required")
        require(workflow["manual_review_required"] is True, "manual review required")

        require(reporting["replay_certification_required"] is True, "replay certification required")

        return True

    def admitted_surfaces(self, scope_file=None):
        if scope_file:
            return self._admitted_inventory_surfaces(scope_file)

        admitted = []

        for entry in self.contracts():
            doc = entry["document"]
            self.validate_contract(doc)

            admitted.append({
                "name": doc["name"],
                "surface_id": doc["surface"]["surface_id"],
                "program": doc["surface"]["program"],
                "surface_type": doc["surface"]["surface_type"],
                "validation_surface": doc["surface"]["validation_surface"],
                "manual_review_required": True
            })

        return admitted

    def _admitted_inventory_surfaces(self, scope_file):
        with open(scope_file, "r", encoding="utf-8") as handle:
            data = json.load(handle)

        if isinstance(data, dict):
            surfaces = data.get("surfaces", [])
            program = data.get("program", "governed_program")
        elif isinstance(data, list):
            surfaces = data
            program = "governed_program"
        else:
            raise ValueError("scope file must contain a list or governed surfaces object")

        admitted = []

        for surface in surfaces:
            require(surface.get("authorized_scope") is True, "authorized scope required")
            require(bool(surface.get("runtime_surface_id") or surface.get("surface_id")), "surface id required")
            require(bool(surface.get("validation_surface")), "validation surface required")

            admitted.append({
                "name": surface.get("review_alias") or surface.get("canonical_asset_name"),
                "surface_id": surface.get("runtime_surface_id") or surface.get("surface_id"),
                "program": surface.get("program") or program,
                "surface_type": surface.get("asset_category") or surface.get("surface_type"),
                "validation_surface": surface["validation_surface"],
                "workflow_family": surface.get("workflow_family", "general_workflow"),
                "manual_review_required": True
            })

        return admitted
