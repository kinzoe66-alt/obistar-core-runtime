from runtime.authority.registry import AuthorityRegistry

class IssueClassifier:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("taxonomy_contract")

    def classify(self, issue_class: str):
        classes = self.contract()["issue_classes"]

        if issue_class not in classes:
            return {
                "known": False,
                "label": "Unclassified Governed Validation Observation",
                "manual_review_required": True,
                "autonomous_submission": False
            }

        item = classes[issue_class]

        return {
            "known": True,
            "issue_class": issue_class,
            "label": item["label"],
            "plain_language": item["plain_language"],
            "value_relevance": item["value_relevance"],
            "manual_review_required": True,
            "autonomous_submission": False
        }
