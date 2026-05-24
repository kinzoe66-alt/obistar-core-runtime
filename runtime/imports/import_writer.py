import json
from pathlib import Path

from runtime.imports.authorized_scope_importer import AuthorizedScopeImporter

class ImportWriter:

    def write(
        self,
        source_path: str,
        output="reports/imports/authorized_scope_import.json"
    ):
        result = AuthorizedScopeImporter().import_file(source_path)

        out = Path(output)
        out.parent.mkdir(parents=True, exist_ok=True)

        out.write_text(
            json.dumps(result, indent=2),
            encoding="utf-8"
        )

        return out
