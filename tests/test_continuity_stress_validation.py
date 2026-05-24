from pathlib import Path
import yaml


ROOT = Path("../obistar-nervous-system")


def load_yaml(path):
    return yaml.safe_load(
        path.read_text(encoding="utf-8")
    )


def test_primitive_integrity_stress_keeps_core_bounded():
    data = load_yaml(
        ROOT / "compression" / "primitive_compression.yaml"
    )

    assert len(data["core_primitives"]) == 10
    assert "app_specific_logic" in data["non_goals"]
    assert "executable_contracts" in data["non_goals"]


def test_lineage_continuity_stress_requires_traceability():
    data = load_yaml(
        ROOT / "lineage" / "lineage_visualization.yaml"
    )

    assert "source_contract" in data["required_lineage"]
    assert "active_pathway" in data["required_lineage"]
    assert "orphan_state" in data["forbids"]


def test_policy_conflict_stress_requires_detection():
    data = load_yaml(
        ROOT / "stress_tests" / "policy_conflict_cases.yaml"
    )

    for case in data["cases"]:
        assert case["expected_result"] == "conflict_detected"
        assert case["manual_review_required"] is True

    assert data["autonomous_submission"] is False


def test_composition_explosion_stress_remains_deterministic():
    data = load_yaml(
        ROOT / "automation" / "runtime_composition_automation.yaml"
    )

    assert data["constraints"]["deterministic_output_required"] is True
    assert data["constraints"]["bounded_authority_required"] is True


def test_review_compression_stress_preserves_context():
    data = load_yaml(
        ROOT / "review_compression" / "review_compression.yaml"
    )

    assert "reviewer_decision" in data["preserve"]
    assert "lineage_signature" in data["preserve"]
    assert "evidence_loss" in data["forbids"]
    assert "reviewer_context_loss" in data["forbids"]


def test_governance_integrity_stress_rejects_invalid_cases():
    data = load_yaml(
        ROOT / "stress_tests" / "invalid_governance_cases.yaml"
    )

    for case in data["cases"]:
        assert case["expected_result"] == "rejected"

    assert data["manual_review_required"] is True
    assert data["autonomous_submission"] is False


def test_stress_suite_protects_required_invariants():
    data = load_yaml(
        ROOT / "stress_tests" / "continuity_stress_suite.yaml"
    )

    assert len(data["categories"]) == 6
    assert "bounded_authority" in data["protected_invariants"]
    assert "primitive_compression" in data["protected_invariants"]
    assert data["manual_review_required"] is True
