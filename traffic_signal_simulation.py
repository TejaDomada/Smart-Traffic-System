import numpy as np
import cv2

def show_signal(green_time):

    signal = np.zeros((300,120,3),dtype=np.uint8)

    # RED
    signal[:] = 0
    cv2.circle(signal,(60,50),30,(0,0,255),-1)
    cv2.imshow("Traffic Signal",signal)
    cv2.waitKey(1000)

    # YELLOW
    signal[:] = 0
    cv2.circle(signal,(60,150),30,(0,255,255),-1)
    cv2.imshow("Traffic Signal",signal)
    cv2.waitKey(1000)

    # GREEN
    signal[:] = 0
    cv2.circle(signal,(60,250),30,(0,255,0),-1)

    cv2.putText(signal,f"{green_time}s",
                (10,290),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,(255,255,255),2)

    cv2.imshow("Traffic Signal",signal)
    cv2.waitKey(green_time * 1000)