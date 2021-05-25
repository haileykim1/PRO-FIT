import numpy as np
import cv2

#Gaussian Mixture기반 전경/배경 분할 알고리즘

cap = cv2.VideoCapture('C:/mtest/Boy.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while(1):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))
    foregroundMask = fgbg.apply(frame)
    #print(foregroundMask)
    #print("======")
    #edge1 = cv2.Canny(foregroundMask, 100, 200)
    cv2.imshow('frameResult', foregroundMask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()