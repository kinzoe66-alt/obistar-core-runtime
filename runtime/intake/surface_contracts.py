import json
from pathlib import Path

from runtime.substrate_paths import (
    AUTHORIZED_SCOPES_ROOT,
)


class SurfaceContractExecutor:

    def admitted_surfaces(
        self,
        scope_file=(
            "authorized_scopes/"
            "expanded/"
            "multi_program_96_surfaces.json"
        ),
    ):

        return self._admitted_inventory_surfaces(
            scope_file
        )

    def _resolve_scope_path(
        self,
        scope_file,
    ):

        if scope_file is None:

            scope_file = (
                "authorized_scopes/"
                "expanded/"
                "multi_program_96_surfaces.json"
            )

        p = Path(scope_file)

        if p.exists():
            return p

        if str(scope_file).startswith(
            "authorized_scopes/"
        ):

            relative = Path(
                *p.parts[1:]
            )

            candidate = (
                AUTHORIZED_SCOPES_ROOT
                / relative
            )

            if candidate.exists():
                return candidate

        return p

    def _normalize_surface(
        self,
        surface,
    ):

        return {
            "surface_id": (
                surface.get(
                    "surface_id",
                    surface.get(
                        "runtime_surface_id",
                        "unknown_surface",
                    ),
                )
            ),

            "surface_type": (
                surface.get(
                    "surface_type",
                    surface.get(
                        "workflow_family",
                        "general_surface",
                    ),
                )
            ),

            "validation_surface": (
                surface.get(
                    "validation_surface",
                    "general",
                )
            ),

            "workflow_family": (
                surface.get(
                    "workflow_family",
                    "general_workflow",
                )
            ),

            **surface,
        }

    def _admitted_inventory_surfaces(
        self,
        scope_file,
    ):

        resolved = self._resolve_scope_path(
            scope_file
        )

        with open(
            resolved,
            "r",
            encoding="utf-8",
        ) as handle:

            inventory = json.load(
                handle
            )

        if isinstance(
            inventory,
            list,
        ):

            surfaces = inventory

        else:

            surfaces = inventory.get(
                "surfaces",
                [],
            )

        return [
            self._normalize_surface(
                surface
            )
            for surface in surfaces
        ]


class SurfaceContracts(
    SurfaceContractExecutor
):
    pass
