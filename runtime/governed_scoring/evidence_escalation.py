class EvidenceEscalationEngine:

    def escalate(self, weighted):

        escalated = []

        for item in weighted.get(
            "weighted",
            []
        ):

            weight = item.get(
                "replay_weight",
                0
            )

            if weight >= 1.0:

                evidence_level = (
                    "deep_validation"
                )

            elif weight >= 0.6:

                evidence_level = (
                    "standard_validation"
                )

            else:

                evidence_level = (
                    "light_validation"
                )

            escalated.append({
                "priority": (
                    item["priority"]
                ),

                "evidence_level": (
                    evidence_level
                ),

                "manual_review_required": True,

                "autonomous_submission": False,
            })

        return {
            "evidence_escalation": (
                escalated
            ),

            "manual_review_required": True,
        }
