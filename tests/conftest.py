import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ENGINE_ROOT = (
    ROOT.parent / "obistar-engine"
).resolve()

if str(ENGINE_ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(ENGINE_ROOT)
    )
