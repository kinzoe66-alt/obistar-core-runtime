class ConfidenceDriftDetector:

    def detect(self, confidence_history):
        if len(confidence_history) < 2:
            return {
                "drift_detected": False,
                "drift_delta": 0,
                "history_size": len(confidence_history),
            }

        minimum = min(confidence_history)
        maximum = max(confidence_history)

        delta = round(maximum - minimum, 4)

        return {
            "drift_detected": delta >= 0.25,
            "drift_delta": delta,
            "history_size": len(confidence_history),
            "minimum_confidence": minimum,
            "maximum_confidence": maximum,
            "manual_review_required": True,
            "confirmed_issue": False,
        }
