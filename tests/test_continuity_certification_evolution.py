from pathlib import Path
import yaml


ROOT = Path("../obistar-nervous-system")


def load_yaml(path):
    return yaml.safe_load(
        path.read_text(encoding="utf-8")
    )


def test_continuity_certification_protects_core_invariants():
    data = load_yaml(
        ROOT / "certification" / "continuity_certification.yaml"
    )

    assert "bounded_authority" in data["certifies"]
    assert "primitive_compression" in data["certifies"]
    assert "manual_adjudication_continuity" in data["certifies"]
    assert data["autonomous_submission"] is False


def test_runtime_graph_execution_is_bounded():
    data = load_yaml(
        ROOT / "graph_execution" / "runtime_graph_execution.yaml"
    )

    assert data["execution_constraints"]["deterministic_order_required"] is True
    assert data["execution_constraints"]["hidden_edge_forbidden"] is True
    assert data["execution_constraints"]["manual_adjudication_terminal"] is True


def test_policy_conflict_adjudication_blocks_silent_merge():
    data = load_yaml(
        ROOT / "conflict_adjudication" / "policy_conflict_adjudication.yaml"
    )

    assert data["resolution_policy"]["silent_merge_forbidden"] is True
    assert data["resolution_policy"]["higher_authority_preserved"] is True
    assert data["resolution_policy"]["manual_review_required"] is True


def test_lineage_graph_rendering_preserves_reviewer_context():
    data = load_yaml(
        ROOT / "graph_rendering" / "lineage_graph_rendering.yaml"
    )

    assert "primitive_to_pathway" in data["required_views"]
    assert data["rendering_constraints"]["orphan_nodes_forbidden"] is True
    assert data["rendering_constraints"]["reviewer_context_required"] is True


def test_organizational_inheritance_optimization_preserves_authority():
    data = load_yaml(
        ROOT / "inheritance_optimization" / "organizational_inheritance_optimization.yaml"
    )

    assert "primitive_compression" in data["protected"]
    assert "authority_inversion" in data["forbids"]
    assert "lineage_loss" in data["forbids"]


def test_composition_planning_requires_certification():
    data = load_yaml(
        ROOT / "composition_planning" / "composition_planning.yaml"
    )

    assert "certification_requirements" in data["outputs"]
    assert data["planning_constraints"]["deterministic_plan_required"] is True
    assert data["planning_constraints"]["policy_conflicts_must_surface"] is True


def test_review_prioritization_remains_non_final():
    data = load_yaml(
        ROOT / "review_intelligence" / "review_prioritization_intelligence.yaml"
    )

    assert "replay_consistency" in data["signals"]
    assert data["constraints"]["prioritization_only"] is True
    assert data["constraints"]["autonomous_final_decision_forbidden"] is True
