from runtime.review_routing.route_optimizer import (
    ReviewRouteOptimizer,
)

from runtime.reviewer_continuity.continuity_memory import (
    ReviewerContinuityMemory,
)

from runtime.adjudication_packages.package_builder import (
    AdjudicationPackageBuilder,
)

from runtime.review_exports.review_queue_exporter import (
    ReviewQueueExporter,
)


class GovernedOperationalLoop:

    def execute(
        self,
        candidates,
        review_memory,
    ):
        routing = (
            ReviewRouteOptimizer()
            .optimize(candidates)
        )

        continuity = (
            ReviewerContinuityMemory()
            .build(
                routing["routes"]
            )
        )

        packages = []

        for candidate in candidates:
            package = (
                AdjudicationPackageBuilder()
                .build(
                    candidate,
                    review_memory,
                    continuity,
                )
            )

            packages.append(package)

        export_result = (
            ReviewQueueExporter()
            .export(
                routing["routes"],
                packages,
            )
        )

        return {
            "routing": routing,
            "continuity": continuity,
            "packages": packages,
            "export_result": export_result,
            "manual_review_required": True,
            "confirmed_issue": False,
        }
