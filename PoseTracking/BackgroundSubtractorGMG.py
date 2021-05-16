import numpy as np
import cv2

#통계적 배경 이미지 제거 + 픽셀 단위의 베이지안 분할
#처음 120개 프레임을 배경 모델링 하는데 사용

cap = cv2.VideoCapture('C:/mtest/Boy.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (400, 400))
    fgmask = fgbg.apply(frame)

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #print(fgmask)
    print(frame)
    print("======")
    cv2.imshow('frameResult',  fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()