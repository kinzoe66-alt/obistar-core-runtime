from pathlib import Path
import os

RUNTIME_ROOT = Path(
    os.environ.get(
        "OBISTAR_RUNTIME_ROOT",
        "."
    )
).resolve()

ENGINE_ROOT = Path(
    os.environ.get(
        "OBISTAR_ENGINE_ROOT",
        "../obistar-engine"
    )
).resolve()

NERVOUS_SYSTEM_ROOT = Path(
    os.environ.get(
        "OBISTAR_NERVOUS_SYSTEM_ROOT",
        "../obistar-nervous-system"
    )
).resolve()

AUTHORITY_ROOT = (
    NERVOUS_SYSTEM_ROOT / "authority"
)

AUTHORIZED_SCOPES_ROOT = (
    NERVOUS_SYSTEM_ROOT / "authorized_scopes"
)

PRIMITIVES_ROOT = (
    NERVOUS_SYSTEM_ROOT / "primitives"
)

REPORTS_ROOT = (
    RUNTIME_ROOT / "reports"
)

REPLAY_HISTORY_ROOT = (
    RUNTIME_ROOT / "replay_history"
)

OUTCOME_HISTORY_ROOT = (
    RUNTIME_ROOT / "outcome_history"
)
