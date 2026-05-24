import json

from runtime.comparison.live_runner import LiveGovernedRunner

def test_live_runner(tmp_path):
    scope_file = tmp_path / "scopes.json"
    scope_file.write_text(json.dumps([
        {
            "surface_id": "authorized-surface-001",
            "program": "governed_program",
            "authorized_scope": True,
            "validation_surface": "api"
        }
    ]), encoding="utf-8")

    result = LiveGovernedRunner().run(str(scope_file))

    assert result["imported"]["imported_count"] == 1
    assert result["comparison"]["surface_count"] == 1
    assert result["manual_review_required"] is True
