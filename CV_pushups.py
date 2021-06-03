import cv2
import numpy as np
import time
import pose as pm

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
    # print(lmList)
    if len(lmList) != 0:
        if int(count -0.5 ) < 5:

            angle = detector.findAngle(img, 12, 14, 16,draw= False)


            per = np.interp(angle, (75, 165), (100, 0))
            bar = np.interp(angle, (75, 165), (100, 650))
            #print(angle, per, bar)
            
            # # Check for the dumbbell curls
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
            print(count)


            # Posture
            cv2.rectangle(img, (1, 100), (375, 220), (0, 0, 0), cv2.FILLED)
            cv2.putText(img, "Posture ", (100, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 215, 255), 3)
            

            # Back
            cv2.putText(img, "Back: ", (20, 200), cv2.FONT_HERSHEY_PLAIN, 2, (128, 84, 231), 2)
            back_angle = detector.findAngle(img, 12, 24, 26)

            if back_angle < 170:
                cv2.putText(img, "InCorrect  ", (130, 200), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "Correct  ", (130, 200), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)



    # Draw Curl Count
    cv2.rectangle(img, (0, 520), (200, 720), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, str(int(count-0.5 )), (60, 650), cv2.FONT_HERSHEY_PLAIN, 8, (0, 255, 255), 10)

    # Target
    if int(count - 0.5) != 5:
        cv2.rectangle(img, (0, 675), (200, 720), (255, 255, 255), cv2.FILLED)
    else:
        cv2.rectangle(img, (0, 675), (200, 720), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Target = 5", (0, 710), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    #Pushups
    cv2.rectangle(img, (0, 0), (500, 100), (0, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (0, 0), (500, 100), (255, 255, 255), 2)
    cv2.putText(img, "Pushups", (30, 75), cv2.FONT_HERSHEY_PLAIN, 5, (192, 192, 192), 5)






    cv2.imshow("Image", img)
    cv2.waitKey(1)
