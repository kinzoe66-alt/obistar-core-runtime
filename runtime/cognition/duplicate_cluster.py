def duplicate_cluster_pressure(cluster_size):
    size = int(cluster_size)

    if size <= 1:
        pressure = "none"
    elif size <= 3:
        pressure = "low"
    elif size <= 7:
        pressure = "moderate"
    else:
        pressure = "high"

    return {
        "duplicate_cluster_size": size,
        "duplicate_pressure": pressure
    }
