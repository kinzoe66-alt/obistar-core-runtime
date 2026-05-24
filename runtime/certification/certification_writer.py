import json

from pathlib import Path

from runtime.certification.replay_certification import (
    ReplayCertificationBuilder
)

class CertificationWriter:

    def write(
        self,
        output=(
            "reports/"
            "replay_certification.json"
        )
    ):

        artifact = (
            ReplayCertificationBuilder()
            .build()
        )

        path = Path(output)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            json.dumps(
                artifact,
                indent=2
            ),
            encoding="utf-8"
        )

        return path
