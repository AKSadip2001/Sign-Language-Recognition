# Importing the Libraries Required

import cv2
import numpy as np
import os

# Creating and Collecting Word Data

mode = 'Words'
directory = 'dataSet/' + mode + '/'
minValue = 70

capture = cv2.VideoCapture(0)
interrupt = -1

while True:
    _, frame = capture.read()

    # Simulating mirror Image
    frame = cv2.flip(frame, 1)

    # Getting count of existing images
    count = {
                'images': len(os.listdir(directory+"HELLO/")),
    }

    # Printing the count of each set on the screen
    cv2.putText(frame, "images : " +str(count['images']), (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)

    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])

    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]

    cv2.imshow("Frame", frame)
    
    # Image Processing

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, image = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # Output Image after the Image Processing that is used for data collection 

    image = cv2.resize(image, (300,300))
    cv2.imshow("test", image)

    # Data Collection

    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: 
        # esc key
        break
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'HELLO/'+str(count['images'])+'.jpg', image)    
    
capture.release()
cv2.destroyAllWindows()