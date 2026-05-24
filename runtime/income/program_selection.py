def rank_authorized_program(program):
    scope_clarity = float(program.get("scope_clarity", 0.0))
    payout_signal = float(program.get("payout_signal", 0.0))
    replay_fit = float(program.get("replay_fit", 0.0))
    report_fit = float(program.get("report_fit", 0.0))

    score = (
        scope_clarity * 0.30 +
        payout_signal * 0.25 +
        replay_fit * 0.25 +
        report_fit * 0.20
    )

    return {
        "program_id": program.get("program_id"),
        "income_priority_score": round(score, 4),
        "authorized_scope_only": True,
        "recommended_action": (
            "prioritize_governed_validation"
            if score >= 0.75
            else "defer_until_better_fit"
        )
    }
