from runtime.authority.registry import AuthorityRegistry
from runtime.activation.fail_closed import require

class SurfaceIntakeValidator:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "intake_contract"
        )

    def validate(self, surface: dict):

        rules = self.contract()["requirements"]

        require(
            bool(surface.get("surface_id")),
            "surface_id required"
        )

        require(
            bool(surface.get("program")),
            "program required"
        )

        require(
            bool(surface.get("authorized_scope")),
            "authorized_scope required"
        )

        require(
            bool(surface.get("validation_surface")),
            "validation_surface required"
        )

        return True
