from pathlib import Path
import yaml


ROOT = Path("../obistar-nervous-system")


def load_yaml(path):
    return yaml.safe_load(
        path.read_text(encoding="utf-8")
    )


def test_primitive_standard_declares_core_primitives():
    data = load_yaml(
        ROOT / "standards" / "continuity_primitives.yaml"
    )

    assert "semantic_identity" in data["primitives"]
    assert "operational_pathway" in data["primitives"]
    assert data["manual_review_required"] is True


def test_governed_validation_pathway_is_bounded():
    data = load_yaml(
        ROOT / "pathways" / "governed_validation_pathway.yaml"
    )

    assert data["pathway"] == "governed_validation"
    assert "manual_adjudication" in data["states"]
    assert data["autonomous_submission"] is False


def test_governance_overlay_forbids_exploratory_expansion():
    data = load_yaml(
        ROOT / "overlays" / "governed_validation_overlay.yaml"
    )

    assert data["constraints"]["authorized_scope_only"] is True
    assert data["constraints"]["exploratory_expansion_forbidden"] is True
    assert data["manual_review_required"] is True


def test_runtime_composition_links_layers():
    data = load_yaml(
        ROOT / "composition" / "governed_validation_composition.yaml"
    )

    assert data["uses"]["primitive_standard"]
    assert data["uses"]["pathway"]
    assert data["uses"]["governance_overlay"]
    assert data["runtime_expectations"]["review_adjudication_loop_required"] is True
