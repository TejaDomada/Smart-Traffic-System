LANE_CAPACITY = 50

def calculate_congestion(vehicle_count):

    congestion = vehicle_count / LANE_CAPACITY

    return round(min(congestion,1.0),2)