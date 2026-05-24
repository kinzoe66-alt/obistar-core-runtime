def entrypoint_priority(route):
    status = route.get("route_status")
    url = route.get("start_url", "")

    score = 0.0

    if status == "resolved":
        score += 0.50

    if url.startswith("https://"):
        score += 0.25

    if "hilton.com" in url or "hilton.io" in url:
        score += 0.20

    if "localbiz" in url:
        score -= 0.20

    score = max(0.0, min(1.0, score))

    if score >= 0.75:
        classification = "clear_entrypoint"
    elif score >= 0.50:
        classification = "reviewable_entrypoint"
    else:
        classification = "unclear_entrypoint"

    return {
        "entrypoint_score": round(score, 4),
        "entrypoint_classification": classification,
        "manual_review_required": True,
        "autonomous_submission": False
    }
