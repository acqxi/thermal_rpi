#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# camera_preview.py
# Preview from camera
#
# Author : sosorry
# Date   : 04/18/2015
# Usage  : python3 camera_preview.py

import cv2
import imutils

#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, 320)
    cv2.putText(frame, "press 'q' to quit ", (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    cv2.imshow("preview", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

