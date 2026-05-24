from runtime.imports.authorized_scope_importer import AuthorizedScopeImporter
from runtime.comparison.comparison_runner import GovernedComparisonRunner

class LiveGovernedRunner:

    def run(self, scope_file: str):
        imported = AuthorizedScopeImporter().import_file(scope_file)
        comparison = GovernedComparisonRunner().run(
            scope_file
        )

        return {
            "imported": imported,
            "comparison": comparison,
            "manual_review_required": True,
            "autonomous_submission": False
        }
