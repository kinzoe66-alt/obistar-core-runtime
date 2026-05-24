def evidence_history_weight(evidence_strength):
    score = float(evidence_strength)

    return {
        "evidence_history_score": round(score, 4),
        "evidence_history_classification": (
            "strong_evidence_history"
            if score >= 0.75
            else "developing_evidence_history"
        )
    }
