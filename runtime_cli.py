import argparse
import json

from runtime.execution.planner import build_execution_plan
from runtime.authority.snapshot import write_authority_snapshot
from runtime.intake.surface_contracts import SurfaceContractExecutor
from runtime.surfaces.execution_planner import SurfaceExecutionPlanner
from runtime.comparison.comparison_runner import GovernedComparisonRunner
from runtime.imports.authorized_scope_importer import AuthorizedScopeImporter
from runtime.comparison.live_runner import LiveGovernedRunner
from runtime.outcomes.outcome_tracker import OutcomeTracker
from runtime.prioritization.review_queue import ReviewQueueBuilder
from runtime.operations.feedback import OperationalFeedbackBuilder
from runtime.assets.hardware_importer import HardwareScopeImporter
from runtime.observations.selector import ObservationSelector
from runtime.meaning.translator import OperationalMeaningTranslator

parser = argparse.ArgumentParser()

parser.add_argument(
    "command",
    choices=[
        "plan",
        "snapshot",
        "surfaces",
        "surface-plan",
        "compare",
        "import-scopes",
        "live-run",
        "track-outcome",
        "review-queue",
        "operational-feedback",
        "import-hardware",
        "select-observations",
        "meaning-report"
    ],
    nargs="?",
    default="plan"
)

parser.add_argument(
    "--file",
    default="authorized_scopes/authorized_surfaces.sample.json"
)

parser.add_argument("--surface-id", default="")
parser.add_argument("--outcome", default="")

args = parser.parse_args()

if args.command == "plan":
    plan = build_execution_plan("governed_validation")
    print(json.dumps(plan["activation_record"], indent=2))

if args.command == "snapshot":
    snapshot = write_authority_snapshot()
    print(json.dumps(snapshot, indent=2))

if args.command == "surfaces":
    surfaces = SurfaceContractExecutor().admitted_surfaces()
    print(json.dumps({
        "surface_count": len(surfaces),
        "admitted_surfaces": surfaces,
        "manual_review_required": True,
        "autonomous_submission": False
    }, indent=2))

if args.command == "surface-plan":
    print(json.dumps(SurfaceExecutionPlanner().build(), indent=2))

if args.command == "compare":
    print(json.dumps(GovernedComparisonRunner().run(args.file), indent=2))

if args.command == "import-scopes":
    print(json.dumps(
        AuthorizedScopeImporter().import_file(args.file),
        indent=2
    ))

if args.command == "live-run":
    print(json.dumps(
        LiveGovernedRunner().run(args.file),
        indent=2
    ))

if args.command == "track-outcome":
    print(json.dumps(
        OutcomeTracker().write(
            args.surface_id,
            args.outcome
        ),
        indent=2
    ))

if args.command == "review-queue":
    comparison = GovernedComparisonRunner().run(args.file)
    print(json.dumps(
        ReviewQueueBuilder().build(comparison),
        indent=2
    ))


if args.command == "operational-feedback":
    print(json.dumps(
        OperationalFeedbackBuilder().build(args.file),
        indent=2
    ))


if args.command == "import-hardware":
    print(json.dumps(
        HardwareScopeImporter().import_file(args.file),
        indent=2
    ))


if args.command == "select-observations":
    print(json.dumps(
        ObservationSelector().select(args.file),
        indent=2
    ))


if args.command == "meaning-report":
    comparison = GovernedComparisonRunner().run(args.file)
    print(json.dumps(
        OperationalMeaningTranslator().translate_results(
            comparison["results"]
        ),
        indent=2
    ))
