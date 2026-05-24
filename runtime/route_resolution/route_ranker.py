from runtime.route_resolution.entrypoint_priority import entrypoint_priority

def rank_routes(routes):
    enriched = []

    for route in routes:
        item = dict(route)
        item["entrypoint_priority"] = entrypoint_priority(route)
        enriched.append(item)

    return sorted(
        enriched,
        key=lambda item: item["entrypoint_priority"]["entrypoint_score"],
        reverse=True
    )
