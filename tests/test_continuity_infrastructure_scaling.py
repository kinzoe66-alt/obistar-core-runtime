from pathlib import Path
import yaml


ROOT = Path("../obistar-nervous-system")


def load_yaml(path):
    return yaml.safe_load(
        path.read_text(encoding="utf-8")
    )


def test_primitive_compression_remains_bounded():
    data = load_yaml(
        ROOT / "compression" / "primitive_compression.yaml"
    )

    assert len(data["core_primitives"]) == 10
    assert "app_specific_logic" in data["non_goals"]
    assert data["autonomous_submission"] is False


def test_pathway_library_preserves_manual_adjudication():
    data = load_yaml(
        ROOT / "pathway_libraries" / "review_adjudication_pathway.yaml"
    )

    assert data["pathway"] == "review_adjudication"
    assert "manual_adjudication" in data["states"]
    assert data["manual_review_required"] is True


def test_overlay_library_preserves_authority_constraints():
    data = load_yaml(
        ROOT / "overlay_libraries" / "regulated_operations_overlay.yaml"
    )

    assert data["constraints"]["bounded_authority_required"] is True
    assert data["review_requirements"]["evidence_bundle_required"] is True
    assert data["autonomous_submission"] is False


def test_review_infrastructure_composition_links_layers():
    data = load_yaml(
        ROOT / "composition_libraries" / "review_infrastructure_composition.yaml"
    )

    assert data["uses"]["primitive_compression"]
    assert len(data["uses"]["pathways"]) == 3
    assert len(data["uses"]["overlays"]) == 2
    assert data["runtime_expectations"]["manual_adjudication_required"] is True
