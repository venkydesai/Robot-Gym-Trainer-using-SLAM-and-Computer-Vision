import cv2
import numpy as np
import time
import pose as pm
import math

cap = cv2.VideoCapture("vid_add")

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0



while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(img.shape)
    # print(lmList[15][2])
    if len(lmList) != 0:

        if int(count) < 6:
            # Right Arm
            point= lmList[15][2]
            x1 = lmList[19][1]
            y1 = lmList[19][2]

            per = np.interp(point, (100 , 280), (0, 100))
            bar = np.interp(point, (100, 280), (500, 100))
            # print(point, per,bar)

            # Check for the dumbbell curls
            color = (0, 0, 255)
            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0
            # print(count)
            #
            # # Draw Bar
            cv2.rectangle(img, (100, 100), (150, 500), color, 3)
            cv2.rectangle(img, (100, int(bar)), (150, 500), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (100, 75), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            cv2.line(img, (82, 170), (120, 170), (0, 0, 0), 2)
            cv2.putText(img, "Contract", (0, 175), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
            cv2.line(img, (82, 445), (120, 445), (0, 0, 0), 2)
            cv2.putText(img, "Relax", (20, 450), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)

            #Circle
            cv2.circle(img, (x1, y1), 8, (0, 255, 255), 2)
            cv2.circle(img, (x1, y1), 4, (0, 0, 255), cv2.FILLED)

            # posture
            cv2.rectangle(img, (880, 200), (1280, 375), (0, 0, 0), cv2.FILLED)
            cv2.rectangle(img, (880, 200), (1280, 375), (255, 255, 255), 2)
            cv2.putText(img, "Posture ", (975, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 215, 255), 3)
            cv2.line(img, (950, 260), (1175, 260), (255, 255, 255), 2, 1)

            # head
            cv2.putText(img, "Head: ", (900, 300), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)
            head_angle = detector.findAngle(img, 7, 11, 23, draw=False)
            print(head_angle)

            if head_angle < 155:
                cv2.putText(img, "InCorrect  ", (1000, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "Correct  ", (1000, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # Back
            cv2.putText(img, "Back: ", (900, 340), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)
            back_angle = detector.findAngle(img, 25, 23, 11, draw=False)

            if back_angle > 110:
                cv2.putText(img, "InCorrect  ", (1000, 340), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "Correct  ", (1000, 340), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


        # Draw Curl Count
        cv2.rectangle(img, (0, 520), (200, 720), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (60, 650), cv2.FONT_HERSHEY_PLAIN, 8, (0, 255, 255), 10)


        if int(count) != 6:
            cv2.rectangle(img, (0, 675), (200, 720), (255, 255, 255), cv2.FILLED)
        else:
            cv2.rectangle(img, (0, 675), (200, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Target = 6", (0, 710), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)



    cv2.rectangle(img, (780, 0), (1280, 100), (0, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (780, 0), (1280, 100), (255, 255, 255), 2)
    cv2.putText(img, "Latt Pull Down", (790, 75), cv2.FONT_HERSHEY_PLAIN, 4, (192, 192, 192), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
