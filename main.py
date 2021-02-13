

import cv2
import sys

cap = cv2.VideoCapture()
cap.open("rtsp://172.18.212.17:554/Streaming/Channels/101?transportmode=unicast&profile=Profile_1")

color_red = (70,50,255)

while(True):

    ret, frame = cap.read()

    if ret == True:
        cv2.putText(frame, "В эфире", (15, 1020), cv2.FONT_HERSHEY_COMPLEX, 1, color_red, 2)
        cv2.imshow('MARK', frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    else:
        print("NO connection to camera")

cap.release()
cv2.destroyAllWindows()
