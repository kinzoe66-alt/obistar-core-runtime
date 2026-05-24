from runtime.route_resolution.entrypoint_priority import entrypoint_priority
from runtime.route_resolution.route_ranker import rank_routes

def test_entrypoint_priority_clear():
    result = entrypoint_priority({
        "route_status": "resolved",
        "start_url": "https://hilton.com"
    })

    assert result["entrypoint_classification"] == "clear_entrypoint"

def test_entrypoint_priority_unclear():
    result = entrypoint_priority({
        "route_status": "unresolved",
        "start_url": ""
    })

    assert result["entrypoint_classification"] == "unclear_entrypoint"

def test_rank_routes():
    routes = [
        {"route_status": "resolved", "start_url": "https://hiltonlocalbiz.com"},
        {"route_status": "resolved", "start_url": "https://hilton.com"}
    ]

    ranked = rank_routes(routes)

    assert ranked[0]["start_url"] == "https://hilton.com"
