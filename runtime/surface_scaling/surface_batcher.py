def batch_surfaces(surfaces, batch_size):
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than zero")

    return [
        surfaces[index:index + batch_size]
        for index in range(0, len(surfaces), batch_size)
    ]
