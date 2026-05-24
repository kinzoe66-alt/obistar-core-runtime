class OutcomeScorer:

    def score(self, outcomes, workflow_weight=None, evidence_history=None):

        normalized = []

        for outcome in outcomes:

            if isinstance(outcome, str):
                normalized.append({
                    "outcome": outcome
                })

            elif isinstance(outcome, dict):
                normalized.append(outcome)

        accepted = sum(
            1 for outcome in normalized
            if outcome.get("outcome") in [
                "accepted",
                "rewarded"
            ]
        )

        rejected = sum(
            1 for outcome in normalized
            if outcome.get("outcome") in [
                "rejected",
                "duplicate",
                "informational"
            ]
        )

        base_score = accepted - (rejected * 0.4)

        workflow_score = 0.0
        evidence_score = 0.0

        if workflow_weight:
            workflow_score = float(
                workflow_weight.get(
                    "workflow_weight_score",
                    0.0
                )
            )

        if evidence_history:
            evidence_score = float(
                evidence_history.get(
                    "evidence_history_score",
                    0.0
                )
            )

        adaptive_score = (
            base_score +
            workflow_score * 0.75 +
            evidence_score * 0.50
        )

        if adaptive_score >= 1.0:
            classification = "high_signal"

        elif adaptive_score >= 0.5:
            classification = "medium_signal"

        else:
            classification = "weak_signal"

        return {
            "classification": classification,
            "score": round(adaptive_score, 4),
            "manual_review_required": True,
            "autonomous_submission": False
        }
