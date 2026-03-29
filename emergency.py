def check_emergency(detected_labels):
    """
    Detect emergency vehicles based on YOLO detection labels
    """

    emergency_classes = ["ambulance", "fire truck", "police car"]

    for label in detected_labels:
        if label in emergency_classes:
            return 1   # Emergency detected

    return 0   # No emergency