import cv2
import mediapipe as mp
import time

video = cv2.VideoCapture("C:/mtest/Boy.mp4")

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while(video.isOpened()):
    ret, img = video.read()

    if not ret:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if results.pose_world_landmarks:
        lm = results.pose_world_landmarks
        for id, ldm in enumerate(lm.landmark):
            if(id >= 11):
                print(id, ldm.x, ldm.y, ldm.z)

    #mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()