from runtime.route_resolution.route_resolver import resolve_review_route

def test_route_resolution_resolves_parent_surface():
    result = resolve_review_route(
        {
            "surface_id": "parent-001::session_workflow::1",
            "parent_authorized_surface_id": "parent-001",
            "workflow_family": "session_workflow"
        },
        {
            "surfaces": [
                {
                    "runtime_surface_id": "parent-001",
                    "asset_reference": "example.com"
                }
            ]
        }
    )

    assert result["route_status"] == "resolved"
    assert result["start_url"] == "https://example.com"
    assert result["manual_review_required"] is True

def test_route_resolution_unresolved():
    result = resolve_review_route(
        {"surface_id": "missing::workflow::1"},
        {"surfaces": []}
    )

    assert result["route_status"] == "unresolved"
