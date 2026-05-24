from runtime.authority_loader import load_authority_tree
from runtime.resolution.resolver import resolve_authority_stack

from runtime.activation.handshake import (
    AuthorityHandshake
)

from runtime.activation.program_overlay import (
    ProgramOverlay
)

from runtime.activation.scope_validator import (
    ScopeValidator
)

from runtime.execution.activation_record import (
    build_activation_record
)

def build_execution_plan(
    surface: str = "governed_validation"
):

    docs = load_authority_tree("authority")

    stack = resolve_authority_stack(docs)

    ProgramOverlay().validate()

    ScopeValidator().validate(surface)

    for entries in stack.values():

        for entry in entries:

            AuthorityHandshake(
                surface
            ).admit(entry["document"])

    return {
        "surface": surface,
        "authority_stack": stack,
        "activation_record": build_activation_record(
            surface,
            stack
        ),
    }
