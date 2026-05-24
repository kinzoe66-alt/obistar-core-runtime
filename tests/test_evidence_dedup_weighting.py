from runtime.governed_scoring.evidence_dedup_weighting import (
    EvidenceDeduplicationWeighting,
)


def test_duplicate_evidence_receives_lower_weight():
    result = EvidenceDeduplicationWeighting().weight([
        {"signature": "a"},
        {"signature": "a"},
    ])

    assert result["unique_count"] == 1
    assert (
        result["weighted_evidence"][1]
        ["evidence_weight"]
        == 0.25
    )
