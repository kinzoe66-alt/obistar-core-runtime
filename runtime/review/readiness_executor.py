from runtime.authority.registry import AuthorityRegistry

class ReadinessExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def contract(self):

        return self.registry.contract(
            "readiness_contract"
        )

    def evaluate(self, item: dict):

        contract = self.contract()

        req = contract["requirements"]

        if (
            item["confidence_score"]
            < req["minimum_confidence"]
        ):
            return False

        if (
            item["priority"]
            != req["required_priority"]
        ):
            return False

        prefixes = req["observation_prefix"]

        if not any(
            prefix in item["observation_id"]
            for prefix in prefixes
        ):
            return False

        return True
