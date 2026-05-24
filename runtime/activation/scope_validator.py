from runtime.authority.registry import AuthorityRegistry
from runtime.activation.fail_closed import require

class ScopeValidator:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def contract(self):

        return self.registry.contract(
            "scope_contract"
        )

    def validate(self, surface: str):

        contract = self.contract()

        allowed = contract[
            "execution_surface"
        ]["allowed"]

        require(
            surface in allowed,
            f"surface not allowed: {surface}"
        )

        require(
            contract["validator_constraints"][
                "replay_required"
            ] is True,
            "replay required"
        )

        require(
            contract["validator_constraints"][
                "evidence_required"
            ] is True,
            "evidence required"
        )

        return True
