import cv2
import mediapipe as mp
import time
import numpy as np


video = cv2.VideoCapture("C:/mtest/Boy.mp4")

mpDrawing = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

#성능에 따라 pose.py보고(Pose()함수 Ctrl + 좌클) parameter 바꾸기
#클래스는 RGB이미지만 처리가능
pose = mpPose.Pose()

pTime = 0
cTime = 0

while(video.isOpened()):
    ret, img = video.read()

    #RGB영상으로 convert
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results)

    #landmark 위치 출력
    if results.pose_landmarks:
        lm = results.pose_landmarks
        for id, ldm in enumerate(lm.landmark):
            height, width, channels = img.shape
            #pixel단위 변환
            cx, cy = int(ldm.x * width), int(ldm.y * height)
            #landmark(33개 : 0~32)당 xyz위치
            print(id, cx, cy)
            #if id == ~ 으로 개별 processing

    #mpDrawing.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    mpDrawing.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    #프레임 계산 : 15~30 프레임정도 나옴
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    fgmask = fgbg.apply(img)
    #fgmask = fgbg.apply(img)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX,3,(255, 0, 255), 3)

    #cv2.imshow("Image", img)
    cv2.imshow("Image", fgmask)
    cv2.waitKey(1)



