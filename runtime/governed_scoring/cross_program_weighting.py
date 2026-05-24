class CrossProgramAdaptiveWeighting:

    def weight(self, program_records):

        weighted = []

        for record in program_records:
            base = record.get("base_score", 0.0)
            accepted = record.get("accepted_count", 0)
            rejected = record.get("rejected_count", 0)

            adjustment = (
                accepted * 0.05
            ) - (
                rejected * 0.05
            )

            score = max(
                0.0,
                min(1.0, base + adjustment),
            )

            weighted.append({
                "program_id": record.get("program_id"),
                "adjusted_score": round(score, 4),
                "manual_review_required": True,
            })

        return {
            "program_weights": weighted,
            "program_count": len(weighted),
            "manual_review_required": True,
            "autonomous_submission": False,
        }
