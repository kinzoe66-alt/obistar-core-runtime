from runtime.outcome_weighting.history_loader import load_weighting_history
from runtime.outcome_weighting.workflow_weighting import workflow_weight

def build_weighting_table(path):
    histories = load_weighting_history(path)

    table = {}

    for history in histories:
        weight = workflow_weight(history)
        table[weight["workflow_family"]] = weight

    return table
