import math
import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

#   촬영 시 일자로 선 상태(발을 붙이고 선 상태)로 촬영 후 움직임 허용
#   촬영 버튼 터치 후 신체 전부가 동영상에 찍힐 수 있게 3초 후 부터 촬영 시작
#   가이드라인에 맞춰 서도록 함
#   0번째 프레임 기준 전체, 상체, 하체 길이 추출
#   신장 : 29, 30 의 중점을 끝점으로 하고 0번 점을 포함하는 직선 기준 측정
#   상체 : 23, 24 의 중점과 11, 12의 중점의 직선 길이
#   하체 : 23, 24 의 중점과 27. 28의 중점의 직선 길이


body_height, body_upper_height, body_bottom_height = 0, 0, 0
x0, y0, x29, y29, x30, y30, x11, y11, x12, y12, x23, y23, x24, y24 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

#   'C:/mtest/test.mp4' -> 1066 * 480 / 인물 키 : 161cm
cap = cv2.VideoCapture('C:/mtest/test.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()


ret, img = cap.read()
height, width, channels = img.shape

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = pose.process(imgRGB)

#pose detection될때 까지
while x0 == 0:
    print("iteration")
    if results.pose_landmarks:
        lm = results.pose_landmarks
        for id, ldm in enumerate(lm.landmark):
            if id == 0:
                x0 = ldm.x
                y0 = ldm.y
            elif id == 11:
                x11 = ldm.x
                y11 = ldm.y
            elif id == 12:
                x12 = ldm.x
                y12 = ldm.y
            elif id == 23:
                x23 = ldm.x
                y23 = ldm.y
            elif id == 24:
                x24 = ldm.x
                y24 = ldm.y
            elif id == 27:
                x27 = ldm.x
                y27 = ldm.y
            elif id == 28:
                x28 = ldm.x
                y28 = ldm.y
    else:
        print("not yet")


    fgmask = fgbg.apply(img)
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    cv2.imshow('fgbf subtracted', img)
    if cv2.waitKey(0):
        break



print(x0, " ", y0)
print(x11, " ", y11)
print(x12, " ", y12)
print(x23, " ", y23)
print(x24, " ", y24)
print(x27, " ", y27)
print(x28, " ", y28)

body_upper_height = int(abs((y23 + y24) / 2 - (y11 + y12) / 2) * height)
body_bottom_height = int(abs((y23 + y24) / 2 - (y27 + y28) / 2) * height)

print(body_upper_height)
print(body_bottom_height)