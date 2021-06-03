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
    
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    
    
    if len(lmList) != 0:

        if int(count + 0.5) < 9:
            # Right Arm
            angle = detector.findAngle(img, 12, 14, 16,draw=False)
            

            
            per = np.interp(angle, (65, 160), (100, 0))
            bar = np.interp(angle, (65, 160), (100, 650))
            # print(angle, per,bar)

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
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1150, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1150, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1080, 75), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
            cv2.line(img,(1140,170),(1172,170),(0,0,0),2)
            cv2.putText(img, "Contract", (1175, 175), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0) , 2)
            cv2.line(img, (1140, 545), (1172, 545), (0, 0, 0), 2)
            cv2.putText(img, "Relax", (1175, 550), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 2)

            # posture
            cv2.rectangle(img, (1, 200), (400, 450), (0, 0, 0), cv2.FILLED)
            cv2.rectangle(img, (1, 200), (400, 450), (255, 255, 255), 2)
            cv2.putText(img, "Posture ", (100, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 215, 255), 3)
            cv2.line(img, (100, 260), (300, 260), (255, 255, 255), 2, 1)

            # head
            cv2.putText(img, "Head: ", (20, 300), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)
            head_angle = 360 - detector.findAngle(img, 8, 12, 24, draw=False)

            if head_angle < 140:
                cv2.putText(img, "InCorrect  ", (130, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "Correct  ", (130, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # Back
            cv2.putText(img, "Back: ", (20, 340), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)
            back_angle = 360 - detector.findAngle(img, 12, 24, 26, draw=False)

            if back_angle > 193:
                cv2.putText(img, "InCorrect  ", (130, 340), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "Correct  ", (130, 340), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # Wrist
            cv2.putText(img, "Wrist: ", (20, 380), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)
            wrist_angle = 360 - detector.findAngle(img, 14, 16, 18, draw=False)

            if wrist_angle >= 160 and wrist_angle <= 200:
                cv2.putText(img, "Correct  ", (130, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            else:
                cv2.putText(img, "InCorrect  ", (130, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # Elbow
            cv2.putText(img, "Elbow: ", (20, 420), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)

            k1=lmList[12][1]
            k2 = lmList[14][1]

            cv2.circle(img, (lmList[12][1], lmList[12][2]), 13, (0, 255, 255), 2)
            cv2.circle(img, (lmList[12][1], lmList[12][2]), 8, (0, 0, 255), cv2.FILLED)

            cv2.circle(img, (lmList[14][1], lmList[14][2]), 13, (0, 255, 255), 2)
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 8, (0, 0, 255), cv2.FILLED)

            elbow_angle= k1 - k2
            print(elbow_angle)
            if -30 < elbow_angle < 25:
                cv2.putText(img, "Correct ", (130, 420), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            else:
                cv2.putText(img, "InCorrect ", (130, 420), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


        # Draw Curl Count
        cv2.rectangle(img, (0, 520), (200, 720), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, str(int(count + 0.5)), (60, 650), cv2.FONT_HERSHEY_PLAIN, 8, (0, 255, 255), 10)

        

        if int(count + 0.5) != 9:
            cv2.rectangle(img, (0, 675), (200, 720), (255, 255, 255), cv2.FILLED)
        else:
            cv2.rectangle(img, (0, 675), (200, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Target = 9", (0, 710), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)




    cv2.rectangle(img, (0, 0), (500, 100), (0, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (0, 0), (500, 100), (255, 255, 255), 2)
    cv2.putText(img, "Bicep Curl", (30, 75), cv2.FONT_HERSHEY_PLAIN, 5, (192, 192, 192), 5)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
