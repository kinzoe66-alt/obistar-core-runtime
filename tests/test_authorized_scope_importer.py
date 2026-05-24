import json

from runtime.imports.authorized_scope_importer import AuthorizedScopeImporter

def test_authorized_scope_importer(tmp_path):
    source = tmp_path / "authorized.json"

    source.write_text(json.dumps([
        {
            "surface_id": "authorized-surface-001",
            "program": "governed_program",
            "authorized_scope": True,
            "validation_surface": "api"
        }
    ]), encoding="utf-8")

    result = AuthorizedScopeImporter().import_file(str(source))

    assert result["imported_count"] == 1
    assert result["manual_review_required"] is True
