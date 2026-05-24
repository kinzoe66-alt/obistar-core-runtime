from runtime.authority.registry import AuthorityRegistry

class OperationalMeaningTranslator:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "operational_meaning_contract"
        )

    def translate_item(self, item: dict):
        labels = self.contract()["metric_labels"]

        translated = {
            "surface_id": item.get("surface_id"),
            "surface_type": item.get("surface_type"),
            "manual_review_required": True,
            "autonomous_submission": False,
            "operational_meaning": []
        }

        for key, definition in labels.items():
            if key in item:
                translated["operational_meaning"].append({
                    "metric": key,
                    "label": definition["label"],
                    "meaning": definition["meaning"],
                    "raw_value": item[key]
                })

        return translated

    def translate_results(self, results: list):
        return {
            "translated_count": len(results),
            "items": [
                self.translate_item(item)
                for item in results
            ],
            "manual_review_required": True,
            "autonomous_submission": False
        }
