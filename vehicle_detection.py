import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

VEHICLE_CLASSES = ["car","bus","truck","motorcycle"]

def detect_vehicles(frame):

    results = model(frame)

    vehicle_count = 0
    detected_labels = []

    for r in results:
        for box in r.boxes:

            class_id = int(box.cls[0])
            label = model.names[class_id]

            if label in VEHICLE_CLASSES:

                vehicle_count += 1
                detected_labels.append(label)

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

                cv2.putText(frame,label,
                            (x1,y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,(0,255,0),2)

    return vehicle_count, detected_labels, frame