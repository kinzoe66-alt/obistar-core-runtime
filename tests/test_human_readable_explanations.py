from runtime.explanations.human_readable import (
    HumanReadableExplanationBuilder
)

def test_human_readable_explanations():

    result = (
        HumanReadableExplanationBuilder()
        .build([
            {
                "pattern_id": "possible_idor_pattern",
                "strength": "strong_inference"
            }
        ])
    )

    assert result

    assert (
        "authorization"
        in result[0]["summary"].lower()
        or
        "object"
        in result[0]["summary"].lower()
    )

    assert (
        result[0]["confirmed_issue"]
        is False
    )
