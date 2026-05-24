import json

from runtime.assets.asset_identity import AssetIdentityValidator


class HardwareScopeImporter:
    def __init__(self):
        self.validator = AssetIdentityValidator()

    def import_file(self, path):
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)

        if isinstance(data, dict):
            assets = data.get("surfaces", [])
        elif isinstance(data, list):
            assets = data
        else:
            raise ValueError(
                "authorized scope file must contain a list or surfaces object"
            )

        validated = []

        for asset in assets:
            self.validator.validate(asset)
            validated.append(asset)

        return {
            "imported_count": len(validated),
            "imported_assets": len(validated),
            "admitted_assets": validated,
            "assets": validated,
            "manual_review_required": True,
            "autonomous_submission": False
        }
