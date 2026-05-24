from runtime.authority.registry import AuthorityRegistry

class ReviewExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def contract(self):

        return self.registry.contract(
            "adjudication_contract"
        )

    def adjudicate(self, evidence: dict):

        requirements = self.contract()["requirements"]

        missing = []

        if requirements["replay_trace_required"]:
            if "replay_trace" not in evidence:
                missing.append("replay_trace")

        if requirements["evidence_bundle_required"]:
            if "evidence_bundle" not in evidence:
                missing.append("evidence_bundle")

        if missing:
            return {
                "adjudicated": False,
                "missing": missing
            }

        return {
            "adjudicated": True,
            "terminal_action": "manual_review_queue"
        }
