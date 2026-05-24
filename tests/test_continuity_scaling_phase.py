from pathlib import Path
import yaml


ROOT = Path("../obistar-nervous-system")


def load_yaml(path):
    return yaml.safe_load(
        path.read_text(encoding="utf-8")
    )


def test_continuity_graph_protects_invariants():
    data = load_yaml(
        ROOT / "graphs" / "continuity_graph.yaml"
    )

    assert "primitive_compression" in data["nodes"]
    assert "review_adjudication" in data["nodes"]
    assert "bounded_authority" in data["protected_invariants"]
    assert data["autonomous_submission"] is False


def test_lineage_visualization_requires_traceability():
    data = load_yaml(
        ROOT / "lineage" / "lineage_visualization.yaml"
    )

    assert "source_contract" in data["required_lineage"]
    assert "hidden_transition" in data["forbids"]
    assert data["manual_review_required"] is True


def test_cross_pathway_assembly_is_bounded():
    data = load_yaml(
        ROOT / "assembly" / "cross_pathway_assembly.yaml"
    )

    assert data["composition_rules"]["shared_lineage_required"] is True
    assert data["composition_rules"]["hidden_transition_forbidden"] is True
    assert data["autonomous_submission"] is False


def test_policy_inheritance_preserves_authority_order():
    data = load_yaml(
        ROOT / "inheritance" / "policy_inheritance.yaml"
    )

    assert data["order"][0] == "primitive_invariants"
    assert data["rules"]["lower_layers_may_not_override_higher_authority"] is True


def test_review_compression_preserves_context():
    data = load_yaml(
        ROOT / "review_compression" / "review_compression.yaml"
    )

    assert "reviewer_decision" in data["preserve"]
    assert "evidence_loss" in data["forbids"]


def test_runtime_composition_automation_is_deterministic():
    data = load_yaml(
        ROOT / "automation" / "runtime_composition_automation.yaml"
    )

    assert data["constraints"]["deterministic_output_required"] is True
    assert data["constraints"]["manual_adjudication_required"] is True
