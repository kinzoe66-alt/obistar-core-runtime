from engine.http.mutation_transport import (
    MutationTransport
)

from engine.sequencing.state_transition import (
    detect_state_transition
)

from runtime.governed_scoring.transition_value import (
    TransitionValueScorer
)

from runtime.governed_scoring.branch_selector import (
    AdaptiveBranchSelector
)

from runtime.governed_scoring.replay_escalation import (
    ReplayEscalationOrchestrator
)

from runtime.governed_scoring.replay_weighting import (
    ReplayWeightingEngine
)

from runtime.governed_scoring.evidence_escalation import (
    EvidenceEscalationEngine
)


class GovernedExplorationRuntime:

    def __init__(self):

        self.transport = (
            MutationTransport()
        )

        self.history = []

        self.scorer = (
            TransitionValueScorer()
        )

        self.selector = (
            AdaptiveBranchSelector()
        )

        self.escalator = (
            ReplayEscalationOrchestrator()
        )

        self.weighting = (
            ReplayWeightingEngine()
        )

        self.evidence = (
            EvidenceEscalationEngine()
        )

    def explore(
        self,
        url,
        mutation_name,
        headers=None,
    ):

        result = self.transport.run_mutation(
            url=url,
            mutation_name=mutation_name,
            headers=headers,
        )

        baseline = (
            result["results"][0]
            ["response"]
        )

        mutated = (
            result["results"][1]
            ["response"]
        )

        transition = (
            detect_state_transition(
                baseline,
                mutated,
            )
        )

        score = self.scorer.score(
            transition
        )

        artifact = {
            "url": url,
            "mutation_name": mutation_name,
            "transition": transition,
            "transition_value": score,
            "session": result["session"],
            "manual_review_required": True,
            "autonomous_submission": False,
        }

        self.history.append(
            artifact
        )

        return artifact

    def replay_history(self):

        branches = (
            self.selector.select(
                self.history
            )
        )

        escalation = (
            self.escalator.escalate(
                branches
            )
        )

        weighting = (
            self.weighting.weight(
                escalation
            )
        )

        evidence = (
            self.evidence.escalate(
                weighting
            )
        )

        return {
            "history": self.history,

            "history_size": len(
                self.history
            ),

            "adaptive_branches": (
                branches
            ),

            "replay_escalation": (
                escalation
            ),

            "replay_weighting": (
                weighting
            ),

            "evidence_escalation": (
                evidence
            ),

            "manual_review_required": True,
        }
