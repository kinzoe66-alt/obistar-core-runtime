import json

from runtime.surface_expansion.governed_expander import expand_governed_inventory

def test_governed_inventory_expansion(tmp_path):
    source = tmp_path / "source.json"
    output = tmp_path / "expanded.json"

    source.write_text(json.dumps({
        "program": "test",
        "surfaces": [
            {
                "runtime_surface_id": "base-001",
                "canonical_asset_name": "example.com",
                "asset_category": "web",
                "vendor": "Example",
                "asset_reference": "example.com",
                "authorization_source": "HackerOne",
                "scope_status": "eligible",
                "review_alias": "Example",
                "authorized_scope": True,
                "validation_surface": "web"
            }
        ]
    }), encoding="utf-8")

    result = expand_governed_inventory(source, output, 12)

    assert result["actual_surface_count"] == 12
    assert result["surfaces"][0]["authorized_scope"] is True
    assert result["surfaces"][0]["parent_authorized_surface_id"] == "base-001"
    assert output.exists()
