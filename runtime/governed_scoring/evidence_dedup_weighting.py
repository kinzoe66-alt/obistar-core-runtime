class EvidenceDeduplicationWeighting:

    def weight(self, evidence_items):

        seen = set()
        weighted = []

        for item in evidence_items:
            signature = item.get(
                "signature"
            )

            duplicate = (
                signature in seen
            )

            if not duplicate:
                seen.add(signature)

            weighted.append({
                "signature": signature,
                "duplicate": duplicate,
                "evidence_weight": (
                    0.25 if duplicate else 1.0
                ),
                "manual_review_required": True,
            })

        return {
            "weighted_evidence": weighted,
            "unique_count": len(seen),
            "manual_review_required": True,
        }
