import hashlib
import json

def workflow_fingerprint(method, path, params=None):
    payload = {
        "method": method,
        "path": path,
        "params": params or {}
    }

    normalized = json.dumps(payload, sort_keys=True)
    digest = hashlib.sha256(normalized.encode()).hexdigest()

    return {
        "workflow_fingerprint": digest[:16],
        "normalized_workflow": payload
    }
