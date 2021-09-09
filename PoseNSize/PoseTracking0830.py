import cv2
import mediapipe as mp
import math
import time

def boneLength(x1, y1, z1, x2, y2, z2):
    ret = (x1 - x2) * (x1 - x2)
    ret += (y1 - y2) * (y1 - y2)
    ret += (z1 - z2) * (z1 - z2)
    return math.sqrt(ret)

video = cv2.VideoCapture("C:/mtest/test.mp4")

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

frameCnt = 0

cap = cv2.VideoCapture(0)

f = open("C:/mtest/pose.txt", 'w')
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

        if frameCnt == 1:
            data = str("=\n")
            wiestLength = boneLength((lm[23].x + lm[24].x) / 2, (lm[23].z + lm[24].z) / 2, (lm[23].y + lm[24].y) / 2,
                               (lm[11].x + lm[12].x + lm[23].x + lm[24].x) / 4,
                               (lm[11].z + lm[12].z + lm[23].z + lm[24].z) / 4,
                               (lm[11].y + lm[12].y + lm[23].y + lm[24].y) / 4)
            #wiest
            data += str(wiestLength / 2) + "\n"
            #hip
            data += str(wiestLength / 2) + "\n"
            #chest
            data += str(wiestLength) + "\n"
            #head
            data += str(boneLength((lm[11].x + lm[12].x) / 2,
                        (lm[11].z + lm[12].z) / 2,
                        (lm[11].y + lm[12].y) / 2,
                        (lm[1].x + lm[4].x) / 2,
                        (lm[1].z + lm[4].z) / 2,
                        (lm[1].y + lm[4].y) / 2
                        )) + "\n"
            #upperarm
            data += str(boneLength(lm[11].x, lm[11].z, lm[11].y, lm[13].x, lm[13].z, lm[13].y)) + "\n"
            data += str(boneLength(lm[12].x, lm[12].z, lm[12].y, lm[14].x, lm[14].z, lm[14].y)) + "\n"
            #lowerarm
            data += str(boneLength(lm[15].x, lm[15].z, lm[15].y, lm[13].x, lm[13].z, lm[13].y)) + "\n"
            data += str(boneLength(lm[16].x, lm[16].z, lm[16].y, lm[14].x, lm[14].z, lm[14].y)) + "\n"
            #upperleg
            data += str(boneLength(lm[23].x, lm[23].z, lm[23].y, lm[25].x, lm[25].z, lm[25].y)) + "\n"
            data += str(boneLength(lm[24].x, lm[24].z, lm[24].y, lm[26].x, lm[26].z, lm[26].y)) + "\n"
            #lowerleg
            data += str(boneLength(lm[27].x, lm[27].z, lm[27].y, lm[25].x, lm[25].z, lm[25].y)) + "\n"
            data += str(boneLength(lm[28].x, lm[28].z, lm[28].y, lm[26].x, lm[26].z, lm[26].y)) + "\n"
            f.write(data)
            id = 0
            for landmark in lm:
                print(id)
                print(landmark)
                id += 1


        data = str("=\n")

        # weist
        data += str((lm[23].x + lm[24].x) / 2) + " " + str((lm[23].z + lm[24].z) / 2) + " " + str(
            (lm[23].y + lm[24].y) / 2) + "\n"

        #hellikk
        data += str(lm[29].x) + " " + str(lm[29].z) + " " + str(lm[29].y) + "\n"
        data += str(lm[30].x) + " " + str(lm[30].z) + " " + str(lm[30].y) + "\n"

        #KTF
        data += str(lm[11].x) + " " + str(lm[11].z) + " " + str(lm[11].y) + "\n"
        data += str(lm[12].x) + " " + str(lm[12].z) + " " + str(lm[12].y) + "\n"

        '''
        #hip
        data += str((lm[11].x + lm[12].x + lm[23].x + lm[24].x) / 4) + " " + \
                str((lm[11].z + lm[12].z + lm[23].z + lm[24].z) / 4) + " " + \
                str((lm[11].y + lm[12].y + lm[23].y + lm[24].y) / 4) + "\n"
        #chest
        data += str((lm[11].x + lm[12].x) / 2) + " " + str((lm[11].z + lm[12].z) / 2) + " " + \
                str((lm[11].y + lm[12].y) / 2) + "\n"
        #upperarm
        data += str(lm[13].x) + " " + str(lm[13].z) + " " + str(lm[13].y) + "\n"
        data += str(lm[14].x) + " " + str(lm[14].z) + " " + str(lm[14].y) + "\n"
        #lowerarm
        data += str(lm[15].x) + " " + str(lm[15].z) + " " + str(lm[15].y) + "\n"
        data += str(lm[16].x) + " " + str(lm[16].z) + " " + str(lm[16].y) + "\n"
        #upperleg
        data += str(lm[27].x) + " " + str(lm[27].z) + " " + str(lm[27].y) + "\n"
        data += str(lm[28].x) + " " + str(lm[28].z) + " " + str(lm[28].y) + "\n"
'''
        f.write(data)


    #mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
    cv2.imshow("Image", img)

    if cv2.waitKey(5) & 0xFF == 27:
        break


f.write("&\n")
print(frameCnt)
f.write(str(frameCnt))
f.close()
cap.release()

