class DuplicateClusterMonitor:

    def monitor(self, candidates):
        clusters = {}

        for candidate in candidates:
            workflow = candidate.get(
                "workflow_family",
                "unknown"
            )

            clusters.setdefault(workflow, 0)
            clusters[workflow] += 1

        largest_cluster = max(
            clusters.values(),
            default=0
        )

        return {
            "cluster_count": len(clusters),
            "largest_cluster_size": largest_cluster,
            "duplicate_cluster_detected":
                largest_cluster >= 5,
            "clusters": clusters,
            "manual_review_required": True,
            "confirmed_issue": False,
        }
