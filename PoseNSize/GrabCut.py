import cv2
import numpy as np

src = cv2.VideoCapture('C:/mtest/test.mp4')

while src.isOpened():
    ret, frame = src.read()
    if ret:
        print("iteration")
        height, width = frame.shape[:2]
        #mask holder
        mask = np.zeros(frame.shape[:2], np.uint8)
        #Grab Cut Object
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        rect = (90, 150, width - 150, height - 150)
        cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        #0, 2 : bgd / 1, 3 : fgd
        mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img1 = frame*mask[:,:,np.newaxis]

        #get bgd
        background = frame - img1

        background[np.where((background > [0, 0, 0]).all(axis = 2))] = [255, 255, 255]

        final = background + img1
        cv2.imshow('img', final)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break



    else:
        break

src.release()
cv2.destroyAllWindows()

