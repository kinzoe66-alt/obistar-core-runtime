class RuntimeTelemetryCompressor:

    def compress(self, telemetry):

        grouped = {}

        for item in telemetry:
            key = item.get(
                "event_type",
                "unknown"
            )

            grouped.setdefault(
                key,
                {
                    "event_type": key,
                    "count": 0,
                }
            )

            grouped[key]["count"] += 1

        return {
            "compressed_events": list(
                grouped.values()
            ),
            "event_type_count": len(grouped),
            "manual_review_required": True,
            "autonomous_submission": False,
        }
