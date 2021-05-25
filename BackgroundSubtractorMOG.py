import math

import cv2  #image processing
import mediapipe as mp  #poseestimation
import time

#Gaussian Mixture기반 전경/배경 분할 알고리즘

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

x1, x2, x3, x4 = 0, 0, 0, 0
y1, y2, y3, y4 = 0, 0, 0, 0
xstart = 0
xend = 0
ystart = 0
yend = 0
waist, shoulder = 0, 0

cap = cv2.VideoCapture('test.mp4')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()


while True:
    #동영상 읽기
    ret, img = cap.read() #frame = cv2.resize(frame, (400, 400))
    height, width, channels = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    #if results.pose_landmarks:
    #    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    if results.pose_landmarks:
        lm = results.pose_landmarks
        for id, ldm in enumerate(lm.landmark):
            height, width, channels = img.shape
            cx, cy = int(ldm.x * width), int(ldm.y * height)
            #WAIST
            if id == 24:
                x1 = cx
                y1 = cy
            if id == 23:
                x2 = cx
                y2 = cy

            #SHOULDER
            if id == 12:
                x3 = cx
                y3 = cy
            if id == 11:
                x4 = cx
                y4 = cy



    #BGFG분리
    fgmask = fgbg.apply(img)  #print(fgmask[200][200])
    #edge1 = cv2.Canny(foregroundMask, 100, 200)

    xvec = abs(x1 - x2)
    yvec = abs(y1 - y2)
    grad = int(yvec / (xvec+0.1))

    for h in range(50):
        if fgmask[x1 + h][y1 + grad * h] == 0:
            xend = x1 + grad * h
            yend = y1 + grad * h
            break
    for h in range(50):
        if fgmask[x1 - grad * h][y1 - grad * h] == 0:
            xstart = x1 - grad * h
            ystart = y1 - grad * h
            break
    #waist = math.sqrt(abs(xend - xstart)**2 + abs(yend - ystart)**2)
    waist = abs(xend - xstart) ** 2 + abs(yend - ystart) ** 2

    print(fgmask[x1][y1], fgmask[x2][y2])
    print(x1, y1, x2, y2, xvec, yvec, grad)
    print("허리길이:", waist)


    cv2.imshow('frameResult', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break




cap.release()
cv2.destroyAllWindows()