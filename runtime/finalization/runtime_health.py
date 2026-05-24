def governed_runtime_health(test_count, operational_layers):
    stable = test_count >= 80 and operational_layers >= 10

    return {
        "runtime_stable": stable,
        "test_count": test_count,
        "operational_layers": operational_layers,
        "manual_review_required": True
    }
