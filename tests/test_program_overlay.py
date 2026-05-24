from runtime.activation.program_overlay import (
    ProgramOverlay
)

def test_program_overlay():

    overlay = ProgramOverlay()

    assert overlay.validate() is True
