import cv2
import mediapipe as mp
import time


video = cv2.VideoCapture("C:/mtest/Boy.mp4")

mpDrawing = mp.solutions.drawing_utils
mpPose = mp.solutions.pose

#성능에 따라 pose.py보고(Pose()함수 Ctrl + 좌클) parameter 바꾸기
#클래스는 RGB이미지만 처리가능
pose = mpPose.Pose()

while(video.isOpened()):
    ret, img = video.read()

    #RGB영상으로 convert
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results)

    mpDrawing.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


    cv2.imshow("Image", img)
    cv2.waitKey(1)



