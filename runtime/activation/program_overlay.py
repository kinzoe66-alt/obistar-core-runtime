from runtime.authority.registry import AuthorityRegistry
from runtime.activation.fail_closed import require

class ProgramOverlay:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("program_contract")

    def validate(self):
        contract = self.contract()

        require(
            contract["scope_governance"]["authorized_only"] is True,
            "authorized_only required"
        )

        require(
            contract["scope_governance"]["replay_required"] is True,
            "replay required"
        )

        require(
            contract["scope_governance"]["evidence_required"] is True,
            "evidence required"
        )

        require(
            contract["workflow_constraints"]["manual_review_required"] is True,
            "manual review required"
        )

        require(
            contract["workflow_constraints"]["autonomous_submission"] is False,
            "autonomous submission blocked"
        )

        return True
