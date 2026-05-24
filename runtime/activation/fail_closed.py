def require(condition: bool, message: str):
    if not condition:
        raise PermissionError(message)
    return True
