def calculate_green_time(congestion, emergency):

    base_time = 30

    green_time = (
        base_time +
        (congestion * 40) +
        (emergency * 60)
    )

    return int(green_time)