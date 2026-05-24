from runtime.authority.registry import AuthorityRegistry
from runtime.activation.fail_closed import require

class AssetIdentityValidator:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("asset_identity_contract")

    def validate(self, asset: dict):
        contract = self.contract()

        for field in contract["required_fields"]:
            require(
                bool(asset.get(field)),
                f"missing asset identity field: {field}"
            )

        require(
            asset["asset_category"] in contract["allowed_asset_categories"],
            f"unsupported asset category: {asset['asset_category']}"
        )

        require(
            asset.get("authorized_scope") is True,
            "authorized scope required"
        )

        return True
