from pathlib import Path
import yaml


def test_high_authority_primitives_exist():
    root = Path("../obistar-nervous-system/primitives")

    required = {
        "semantic_identity.yaml",
        "authority_boundary.yaml",
        "state_transition.yaml",
        "transformation_integrity.yaml",
        "artifact_governance.yaml",
        "replay_continuity.yaml",
        "review_escalation.yaml",
        "continuity_lineage.yaml",
        "constraint_envelope.yaml",
        "operational_pathway.yaml",
    }

    found = {path.name for path in root.glob("*.yaml")}

    assert required.issubset(found)


def test_high_authority_primitives_are_review_governed():
    root = Path("../obistar-nervous-system/primitives")

    for path in root.glob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert data["primitive"]
        assert data["law"]
        assert data["requires"]
        assert data["forbids"]
        assert data["manual_review_required"] is True
