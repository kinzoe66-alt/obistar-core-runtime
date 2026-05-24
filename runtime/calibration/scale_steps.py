def scale_steps(start, multiplier, steps):
    values = []
    current = start

    for _ in range(steps):
        values.append(current)
        current *= multiplier

    return values
