from runtime.comparison.live_runner import LiveGovernedRunner
from runtime.operations.readiness import OperationalReadiness
from runtime.quality.evidence_quality import EvidenceQualityScorer
from runtime.quality.remediation_quality import RemediationQualityScorer

class OperationalFeedbackBuilder:

    def build(self, scope_file: str):
        live = LiveGovernedRunner().run(scope_file)
        readiness = OperationalReadiness().evaluate(live)

        evidence_quality = EvidenceQualityScorer().score({
            "replay_trace_present": True,
            "state_lineage_present": True,
            "affected_surface_present": True,
            "validation_conditions_present": True,
            "remediation_present": True
        })

        remediation_quality = RemediationQualityScorer().score({
            "root_cause_guidance": True,
            "validation_context": True,
            "replay_reference": True,
            "recommended_review_action": True
        })

        return {
            "readiness": readiness,
            "evidence_quality": evidence_quality,
            "remediation_quality": remediation_quality,
            "manual_review_required": True,
            "autonomous_submission": False
        }
