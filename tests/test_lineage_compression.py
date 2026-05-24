from runtime.governed_scoring.lineage_compression import (
    CrossSessionLineageCompressor,
)


def test_lineage_compression_merges_equivalent_transitions():
    result = CrossSessionLineageCompressor().compress([
        {
            "history": [
                {
                    "transition": {
                        "transitions": [
                            "status_transition"
                        ]
                    }
                }
            ]
        },
        {
            "history": [
                {
                    "transition": {
                        "transitions": [
                            "status_transition"
                        ]
                    }
                }
            ]
        },
    ])

    assert result["signature_count"] == 1
    assert result["lineage_signatures"][0]["count"] == 2
