import cv2
import mediapipe as mp
import time

video = cv2.VideoCapture("C:/mtest/test.mp4")

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

frameCnt = 0

cap = cv2.VideoCapture(0)

f = open("C:/mtest/pose5.txt", 'w')
while(video.isOpened()):
    ret, img = video.read()

    if not ret:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    frameCnt += 1


    if results.pose_world_landmarks:
        lm = results.pose_world_landmarks.landmark
        print(lm)
        data = str("=\n")
        data += str(lm[0].x * 5) + " " + str(lm[0].y * 5) + " " + str(lm[0].z * 5) + "\n"
        data += str((lm[9].x + lm[10].x) / 2 * 5) + " " + str((lm[9].y + lm[10].y) / 2 * 5) + " " + \
                str((lm[9].z + lm[10].z) / 2 * 5) + "\n"
        data += str((lm[11].x + lm[12].x) / 2 * 5) + " " + str((lm[11].y + lm[12].y) / 2 * 5) + " " + \
                str((lm[11].z + lm[12].z) / 2 * 5) + "\n"
        data += str((lm[11].x + lm[12].x + lm[23].x + lm[24].x) / 4 * 5) + " " + \
                str((lm[11].y + lm[12].y + lm[23].y + lm[24].y) / 4 * 5) + " " + \
                str((lm[11].z + lm[12].z + lm[23].z + lm[24].z) / 4 * 5) + "\n"
        data += str((lm[23].x + lm[24].x) / 2 * 5) + " " + str((lm[23].y + lm[24].y) / 2 * 5) + " " + str(
            (lm[23].z + lm[24].z) / 2 * 5) + "\n"
        data += str(lm[11].x * 5) + " " + str(lm[11].y * 5) + " " + str(lm[11].z * 5) + "\n"
        data += str(lm[12].x * 5) + " " + str(lm[12].y * 5) + " " + str(lm[12].z * 5) + "\n"
        data += str(lm[13].x * 5) + " " + str(lm[13].y * 5) + " " + str(lm[13].z * 5) + "\n"
        data += str(lm[14].x * 5) + " " + str(lm[14].y * 5) + " " + str(lm[14].z * 5) + "\n"
        data += str(lm[15].x * 5) + " " + str(lm[15].y * 5) + " " + str(lm[15].z * 5) + "\n"
        data += str(lm[16].x * 5) + " " + str(lm[16].y * 5) + " " + str(lm[16].z * 5) + "\n"
        for i in range(16):
            data += str(lm[19].x * 5) + " " + str(lm[19].y * 5) + " " + str(lm[19].z * 5) + "\n"
        for i in range(16):
            data += str(lm[20].x * 5) + " " + str(lm[20].y * 5) + " " + str(lm[20].z * 5) + "\n"
        data += str(lm[23].x * 5) + " " + str(lm[23].y * 5) + " " + str(lm[23].z * 5) + "\n"
        data += str(lm[24].x * 5) + " " + str(lm[24].y * 5) + " " + str(lm[24].z * 5) + "\n"
        data += str(lm[27].x * 5) + " " + str(lm[27].y * 5) + " " + str(lm[27].z * 5) + "\n"
        data += str(lm[28].x * 5) + " " + str(lm[28].y * 5) + " " + str(lm[28].z * 5) + "\n"
        data += str(lm[25].x * 5) + " " + str(lm[25].y * 5) + " " + str(lm[25].z * 5) + "\n"
        data += str(lm[26].x * 5) + " " + str(lm[26].y * 5) + " " + str(lm[26].z * 5) + "\n"
        data += str((lm[25].x + lm[31].x) / 2 * 5) + " " + str((lm[25].y + lm[31].y) / 2 * 5) + " " + str(
            (lm[25].z + lm[31].z) / 2 * 5) + "\n"
        data += str((lm[26].x + lm[32].x) / 2 * 5) + " " + str((lm[26].y + lm[32].y) / 2 * 5) + " " + str(
            (lm[26].z + lm[32].z) / 2 * 5) + "\n"
        data += str(lm[31].x * 5) + " " + str(lm[31].y * 5) + " " + str(lm[31].z * 5) + "\n"
        data += str(lm[32].x * 5) + " " + str(lm[32].y * 5) + " " + str(lm[32].z * 5) + "\n"
        f.write(data)


    mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow("Image", img)

    if cv2.waitKey(5) & 0xFF == 27:
        break


f.write("&\n")
print(frameCnt)
f.write(str(frameCnt))
f.close()
cap.release()