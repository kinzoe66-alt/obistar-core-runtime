class ComparisonMetrics:

    def calculate(self, comparison: dict):
        results = comparison["results"]
        total = len(results)

        certified = sum(1 for item in results if item["certified"] is True)
        admissible = sum(1 for item in results if item["report_admissible"] is True)
        manual_review = sum(1 for item in results if item["manual_review_required"] is True)
        high_value = sum(1 for item in results if item.get("value_classification") == "high_value_candidate")

        return {
            "surface_count": total,
            "certification_rate": certified / total if total else 0,
            "report_admissibility_rate": admissible / total if total else 0,
            "manual_review_rate": manual_review / total if total else 0,
            "high_value_candidate_rate": high_value / total if total else 0,
            "autonomous_submission": False
        }
