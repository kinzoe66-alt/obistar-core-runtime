from runtime.comparison.comparison_runner import GovernedComparisonRunner
from runtime.observations.quality_scorer import ObservationQualityScorer

from runtime.outcome_weighting.weighting_table import (
    build_weighting_table
)

from runtime.outcome_weighting.evidence_history import (
    evidence_history_weight
)

from runtime.outcome_weighting.outcome_weighted_priority import (
    outcome_weighted_priority
)


class ObservationSelector:

    def select(self, scope_file=None):
        comparison = GovernedComparisonRunner().run(scope_file)
        scorer = ObservationQualityScorer()

        weighting = build_weighting_table(
            "outcome_history/governed_weighting.sample.json"
        )

        enriched = []

        for item in comparison["results"]:
            quality = scorer.score(item)

            workflow_family = item.get(
                "workflow_family",
                "state_transition_workflow"
            )

            workflow_weight = weighting.get(
                workflow_family,
                {
                    "workflow_weight_score": 0.25,
                    "workflow_weight_classification": "weak_weight"
                }
            )

            evidence = evidence_history_weight(
                quality["score"]
            )

            weighted = outcome_weighted_priority(
                item,
                workflow_weight["workflow_weight_score"],
                evidence["evidence_history_score"]
            )

            updated = dict(item)

            updated["workflow_weight"] = workflow_weight
            updated["evidence_history"] = evidence
            updated["weighted_priority"] = weighted
            updated["observation_quality"] = quality

            enriched.append(updated)

        ordered = sorted(
            enriched,
            key=lambda item: (
                item["weighted_priority"]["weighted_priority_score"],
                item["observation_quality"]["score"],
                item["review_priority"]["score"]
            ),
            reverse=True
        )

        return {
            "selected_count": len(ordered),
            "ordered_observations": ordered,
            "manual_review_required": True,
            "autonomous_submission": False
        }
