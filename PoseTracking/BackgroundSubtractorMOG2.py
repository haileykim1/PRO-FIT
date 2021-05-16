import numpy as np
import cv2

#각 픽셀에 대해 알맞는 가우시안 분포의 수 선택
#조명 변화로 인한 다양한 장면에 대해 더 나은 적응력 보임

cap = cv2.VideoCapture('C:/mtest/Boy.mp4')

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while(1):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))
    foregroundMask = fgbg.apply(frame)
    print(foregroundMask)
    print("======")
    cv2.imshow('frameResult', foregroundMask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()