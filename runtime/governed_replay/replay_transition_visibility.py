class ReplayTransitionVisibility:

    def augment(
        self,
        replay_sequence,
        candidate_id="unknown_observation",
        surface_id="unknown_surface",
    ):

        transitions = [
            (
                "candidate_ingest",
                "validated",
            ),

            (
                "evidence_normalization",
                "stable",
            ),

            (
                "review_package_generation",
                "reviewer_ready",
            ),
        ]

        augmented = []

        for index, execution in enumerate(
            replay_sequence
        ):

            transition_index = min(
                index,
                len(transitions) - 1,
            )

            transition, result = (
                transitions[
                    transition_index
                ]
            )

            augmented.append({

                "step": (
                    index + 1
                ),

                "transition": (
                    transition
                ),

                "result": (
                    result
                ),

                "candidate_id": (
                    candidate_id
                ),

                "surface_id": (
                    surface_id
                ),

                "execution": (
                    execution
                ),
            })

        if not augmented:

            augmented.append({

                "step": 1,

                "transition": (
                    "candidate_ingest"
                ),

                "result": (
                    "validated"
                ),

                "candidate_id": (
                    candidate_id
                ),

                "surface_id": (
                    surface_id
                ),

                "execution": None,
            })

        return augmented
