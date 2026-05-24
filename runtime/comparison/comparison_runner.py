from runtime.surfaces.execution_planner import (
    SurfaceExecutionPlanner
)

from runtime.certification.replay_certification import (
    ReplayCertificationBuilder
)

from runtime.reporting.governed_report import (
    GovernedReportBuilder
)

from runtime.comparison.metrics import (
    ComparisonMetrics
)

from runtime.value.value_scorer import (
    ValueScorer
)

from runtime.stability.replay_stability import (
    ReplayStabilityScorer
)

from runtime.quality.report_quality import (
    ReportQualityScorer
)

from runtime.deduplication.deduplication_scorer import (
    DeduplicationScorer
)

from runtime.deduplication.history import (
    DeduplicationHistory
)

from runtime.prioritization.review_priority import (
    ReviewPriorityScorer
)

from runtime.patterns.pattern_inferencer import (
    PatternInferencer
)

from runtime.explanations.human_readable import (
    HumanReadableExplanationBuilder
)

from runtime.outcome_weighting.weighting_table import (
    build_weighting_table
)

from runtime.outcome_weighting.evidence_history import (
    evidence_history_weight
)

class GovernedComparisonRunner:

    def run(self, scope_file=None):

        surface_plan = (
            SurfaceExecutionPlanner()
            .build(scope_file)
        )

        certification = (
            ReplayCertificationBuilder()
            .build()
        )

        report_builder = (
            GovernedReportBuilder()
        )

        value_scorer = (
            ValueScorer()
        )

        stability_scorer = (
            ReplayStabilityScorer()
        )

        quality_scorer = (
            ReportQualityScorer()
        )

        deduplication_scorer = (
            DeduplicationScorer()
        )

        deduplication_history = (
            DeduplicationHistory()
        )

        priority_scorer = (
            ReviewPriorityScorer()
        )

        pattern_inferencer = (
            PatternInferencer()
        )

        explanation_builder = (
            HumanReadableExplanationBuilder()
        )

        weighting = build_weighting_table(
            "outcome_history/governed_weighting.sample.json"
        )

        results = []

        for item in surface_plan[
            "surface_execution_plan"
        ]:

            observation = {
                "replay_stable": (
                    certification["certified"]
                ),

                "evidence_complete": True,

                "state_lineage_present": True,

                "authorization_boundary_relevant":
                    item["surface_type"] in [
                        "api",
                        "session_workflow",
                        "state_transition"
                    ],

                "business_workflow_relevant":
                    item["surface_type"] in [
                        "session_workflow",
                        "state_transition"
                    ],

                "manual_review": True,

                "evidence": {
                    "replay_trace":
                        certification.get(
                            "execution_trace"
                        ),

                    "evidence_bundle": True,

                    "state_lineage":
                        certification.get(
                            "execution_trace"
                        ),

                    "boundary_context":
                        item["surface_type"],

                    "workflow_context":
                        item["workflow"]
                }
            }

            pattern_observation = {
                "object_reference_present": item["surface_type"] in [
                    "api",
                    "session_workflow"
                ],
                "authorization_context_present": item["surface_type"] in [
                    "api",
                    "session_workflow",
                    "state_transition"
                ],
                "protected_workflow_present": item["surface_type"] in [
                    "session_workflow",
                    "state_transition"
                ],
                "session_context_present": item["surface_type"] == "session_workflow",
                "workflow_context_present": item["surface_type"] in [
                    "session_workflow",
                    "state_transition"
                ],
                "state_lineage_present": True,
                "replay_stable": certification["certified"],
                "evidence_complete": True
            }

            inferred_patterns = (
                pattern_inferencer
                .infer(pattern_observation)
            )

            explanations = (
                explanation_builder
                .build(inferred_patterns)
            )

            value = value_scorer.score(
                observation
            )

            current_signature = {
                "surface_type": item["surface_type"],
                "validation_surface": item["validation_surface"],
                "issue_class": "governed_validation_observation",
                "workflow": item["workflow"],
                "cognition_focus": (
                    item["cognition"][0]["validator_focus"]
                    if item["cognition"]
                    else []
                )
            }

            deduplication = (
                deduplication_history
                .compare_against_history(
                    current_signature,
                    deduplication_scorer
                )
            )

            stability = (
                stability_scorer.score({
                    "replay_consistent": True,
                    "evidence_consistent": True,
                    "lineage_consistent": True,
                    "cognition_consistent": True
                })
            )

            evidence_bundle = {
                "affected_surface":
                    item["surface_id"],

                "issue":
                    "a governed validation observation",

                "impact": "medium",

                "evidence": {
                    "surface_type":
                        item["surface_type"],

                    "workflow":
                        item["workflow"],

                    "cognition":
                        item["cognition"],

                    "value": value,

                    "stability": stability
                },

                "remediation":
                    "Review the governed validation evidence and replay trace."
            }

            report = report_builder.build({
                "replay": True,
                "confidence": 0.91,
                "manual_review": True,
                "evidence_bundle": evidence_bundle
            })

            quality = (
                quality_scorer.score({
                    "simplified_explanation": True,
                    "remediation_present": True,
                    "replay_reference_present": True,
                    "evidence_complete": True,
                    "impact_clarity": True
                })
            )

            from runtime.outcomes.outcome_scorer import (
                OutcomeScorer
            )

            from runtime.outcomes.outcome_history import (
                OutcomeHistory
            )

            workflow_family = item.get(
                "workflow_family",
                "general_workflow"
            )

            workflow_weight = weighting.get(
                workflow_family,
                {
                    "workflow_weight_score": 0.25,
                    "workflow_weight_classification": "weak_weight"
                }
            )

            evidence_history = evidence_history_weight(
                quality["score"]
            )

            outcomes = (
                OutcomeScorer()
                .score(
                    OutcomeHistory()
                    .outcomes_for(
                        item["surface_id"]
                    ),
                    workflow_weight=workflow_weight,
                    evidence_history=evidence_history
                )
            )

            base_result = {

                "surface_id":
                    item["surface_id"],

                "surface_type":
                    item["surface_type"],

                "workflow_family":
                    item.get("workflow_family", "general_workflow"),

                "certified":
                    certification["certified"],

                "report_admissible":
                    report["admissible"],

                "value_classification":
                    value["classification"],

                "value_score":
                    value["score"],

                "replay_stability":
                    stability,

                "report_quality":
                    quality,

                "inferred_patterns":
                    inferred_patterns,

                "human_readable_explanations":
                    explanations,

                "deduplication":
                    deduplication,

                "outcome_learning":
                    outcomes,

                "manual_review_required": True,

                "autonomous_submission": False
            }

            base_result["workflow_family"] = workflow_family
            base_result["workflow_weight"] = workflow_weight
            base_result["evidence_history"] = evidence_history

            base_result["review_priority"] = (
                priority_scorer.score(base_result)
            )

            results.append(base_result)

        comparison = {
            "surface_count": len(results),
            "results": results,
            "manual_review_required": True,
            "autonomous_submission": False
        }

        comparison["metrics"] = (
            ComparisonMetrics()
            .calculate(comparison)
        )

        return comparison

if __name__ == "__main__":
    result = GovernedComparisonRunner().run()
    print(result)
