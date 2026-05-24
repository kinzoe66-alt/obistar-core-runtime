class PriorityInflationDetector:

    def detect(self, candidates):
        if not candidates:
            return {
                "inflation_detected": False,
                "inflation_ratio": 0,
                "high_priority_count": 0,
                "candidate_count": 0,
            }

        high_priority = [
            c for c in candidates
            if c.get("fatigue_adjusted_priority", 0) >= 0.8
        ]

        ratio = len(high_priority) / len(candidates)

        return {
            "inflation_detected": ratio >= 0.5,
            "inflation_ratio": round(ratio, 4),
            "high_priority_count": len(high_priority),
            "candidate_count": len(candidates),
            "manual_review_required": True,
            "confirmed_issue": False,
        }
