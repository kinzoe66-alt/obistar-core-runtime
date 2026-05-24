class ReplayTemplateBuilder:

    def build(self, candidate):

        surface_id = candidate.get(
            "surface_id",
            "unknown_surface"
        )

        observation_id = candidate.get(
            "observation_id",
            candidate.get(
                "package_id",
                "unknown_observation"
            )
        )

        command = [
            "python",
            "--version",
        ]

        return {
            "observation_id": (
                observation_id
            ),

            "surface_id": (
                surface_id
            ),

            "command": command,

            "deterministic": True,

            "manual_review_required": True,

            "autonomous_submission": False,
        }
