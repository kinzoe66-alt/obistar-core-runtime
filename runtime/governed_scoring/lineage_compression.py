class CrossSessionLineageCompressor:

    def compress(self, sessions):

        signatures = {}

        for session in sessions:
            for item in session.get("history", []):
                transition = item.get(
                    "transition",
                    {}
                )

                key = tuple(
                    transition.get(
                        "transitions",
                        []
                    )
                )

                signatures.setdefault(
                    key,
                    {
                        "signature": list(key),
                        "count": 0,
                    }
                )

                signatures[key]["count"] += 1

        return {
            "lineage_signatures": list(
                signatures.values()
            ),
            "signature_count": len(
                signatures
            ),
            "manual_review_required": True,
        }
