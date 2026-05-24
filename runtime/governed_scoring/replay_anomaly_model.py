class HistoricalReplayAnomalyModel:

    def model(self, history):

        anomalies = []

        for item in history:
            expected = item.get("expected_success_rate", 1.0)
            actual = item.get("actual_success_rate", 1.0)

            delta = abs(expected - actual)

            if delta >= 0.30:
                anomalies.append({
                    "replay_id": item.get("replay_id"),
                    "delta": round(delta, 4),
                    "manual_review_required": True,
                })

        return {
            "anomalies": anomalies,
            "anomaly_count": len(anomalies),
            "manual_review_required": True,
            "autonomous_submission": False,
        }
