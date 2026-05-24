class TransitionValueScorer:
    WEIGHTS = {
        "stable_state": 0.0,
        "status_transition": 0.30,
        "cors_transition": 0.20,
        "reflection_transition": 0.35,
        "proxy_transition": 0.25,
    }

    def score(self, transition):
        transitions = transition.get("transitions", [])

        score = sum(
            self.WEIGHTS.get(item, 0.10)
            for item in transitions
        )

        state_changed = transition.get(
            "state_changed",
            False
        )

        if state_changed:
            score += 0.15

        score = min(score, 1.0)

        return {
            "transition_score": round(score, 4),
            "evidence_value": self._evidence_value(score),
            "exploratory_priority": self._priority(score),
            "replay_weight": self._replay_weight(score),
            "adjudication_escalation": score >= 0.50,
            "manual_review_required": True,
            "autonomous_submission": False,
        }

    def _evidence_value(self, score):
        if score >= 0.75:
            return "high"
        if score >= 0.50:
            return "medium"
        if score > 0:
            return "low"
        return "none"

    def _priority(self, score):
        if score >= 0.75:
            return "priority_review"
        if score >= 0.50:
            return "review_candidate"
        if score > 0:
            return "low_priority_observation"
        return "no_escalation"

    def _replay_weight(self, score):
        if score >= 0.75:
            return 3
        if score >= 0.50:
            return 2
        if score > 0:
            return 1
        return 0
