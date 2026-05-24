from runtime.assets.asset_identity import AssetIdentityValidator

def test_asset_identity_hardware():
    asset = {
        "runtime_surface_id": "hw-surface-001",
        "canonical_asset_name": "FindX7",
        "asset_category": "hardware_iot",
        "vendor": "OPPO",
        "asset_reference": "FindX7",
        "authorization_source": "HackerOne",
        "scope_status": "eligible",
        "review_alias": "OPPO FindX7 Hardware Validation Surface",
        "authorized_scope": True
    }

    assert AssetIdentityValidator().validate(asset) is True
