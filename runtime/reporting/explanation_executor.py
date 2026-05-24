from runtime.authority.registry import AuthorityRegistry

class ExplanationExecutor:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def reporting_contract(self):
        return self.registry.contract("reporting_contract")

    def impact_contract(self):
        return self.registry.contract("impact_contract")

    def summarize(self, validated: dict):
        contract = self.reporting_contract()

        max_sentences = contract["explanation"]["max_summary_sentences"]

        surface = validated.get("affected_surface", "the reviewed surface")
        issue = validated.get("issue", "a governed validation issue")
        impact = validated.get("impact", "medium")

        impact_text = self.impact_contract()["impact_levels"][impact]["plain_language"]

        sentences = [
            f"A governed validation review identified {issue} on {surface}.",
            impact_text,
            "Replay evidence and manual review are required before any external reporting."
        ]

        return " ".join(sentences[:max_sentences])
