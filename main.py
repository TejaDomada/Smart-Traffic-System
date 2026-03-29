import cv2

from vehicle_detection import detect_vehicles
from calculate_congestion import calculate_congestion
from emergency import check_emergency
from signal_controller import calculate_green_time
from traffic_signal_simulation import show_signal


video = cv2.VideoCapture("new_video.mp4")

while video.isOpened():

    ret, frame = video.read()

    if not ret:
        break


    # 1 Vehicle Detection
    vehicle_count, detected_labels, annotated_frame = detect_vehicles(frame)


    # 2 Congestion Calculation
    congestion = calculate_congestion(vehicle_count)


    # 3 Emergency Detection
    emergency = check_emergency(detected_labels)


    # 4 Signal Timing
    green_time = calculate_green_time(congestion, emergency)


    # Display info
    cv2.putText(annotated_frame,
                f"Vehicles: {vehicle_count}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(255,0,0),2)

    cv2.putText(annotated_frame,
                f"Congestion: {congestion}",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(0,0,255),2)

    cv2.putText(annotated_frame,
                f"Emergency: {'YES' if emergency else 'NO'}",
                (20,120),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(0,165,255),2)

    cv2.putText(annotated_frame,
                f"Green Time: {green_time} sec",
                (20,160),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(0,255,0),2)


    cv2.imshow("Smart Traffic Management System", annotated_frame)


    # press Q to simulate signal
    if cv2.waitKey(1) & 0xFF == ord('s'):
        show_signal(green_time)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()