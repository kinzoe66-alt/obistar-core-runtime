import json

from runtime.assets.hardware_importer import HardwareScopeImporter

def test_hardware_importer(tmp_path):
    path = tmp_path / "hardware.json"

    path.write_text(json.dumps([
        {
            "runtime_surface_id": "hw-surface-001",
            "canonical_asset_name": "FindX7",
            "asset_category": "hardware_iot",
            "vendor": "OPPO",
            "asset_reference": "FindX7",
            "authorization_source": "HackerOne",
            "scope_status": "eligible",
            "review_alias": "OPPO FindX7 Hardware Validation Surface",
            "program": "governed_program",
            "surface_type": "hardware_iot",
            "authorized_scope": True,
            "validation_surface": "hardware_iot"
        }
    ]), encoding="utf-8")

    result = HardwareScopeImporter().import_file(str(path))

    assert result["imported_count"] == 1
    assert result["admitted_assets"][0]["canonical_asset_name"] == "FindX7"
