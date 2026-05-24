import json

from runtime.imports.import_writer import ImportWriter

def test_import_writer(tmp_path):
    source = tmp_path / "authorized.json"
    output = tmp_path / "import_report.json"

    source.write_text(json.dumps([
        {
            "surface_id": "authorized-surface-001",
            "program": "governed_program",
            "authorized_scope": True,
            "validation_surface": "api"
        }
    ]), encoding="utf-8")

    path = ImportWriter().write(str(source), str(output))

    assert path.exists()
