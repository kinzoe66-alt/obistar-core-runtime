def daily_throughput(workflows_run, candidates_selected, packages_ready):
    return {
        "workflows_run": workflows_run,
        "candidates_selected": candidates_selected,
        "packages_ready": packages_ready,
        "candidate_rate": 0.0 if workflows_run == 0 else round(candidates_selected / workflows_run, 4),
        "package_rate": 0.0 if workflows_run == 0 else round(packages_ready / workflows_run, 4)
    }
