#!/usr/python3
# -*- coding: utf-8 -*-
import cv2 

#OpenCV 人脸识别分类器
classifier = cv2.CascadeClassifier(
    "F:/workdir/tool/opencv-python38/haarcascades/haarcascade_frontalface_default.xml"
)

def FaceRecognition(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceRects = classifier.detectMultiScale(gray, 1.2, 3)
    if(len(faceRects)):
        for faceRect in faceRects:
            x,y,w,h = faceRect
            cv2.rectangle(image, (x,y), (x+h, y+h), (0,0,255),2)
            
    
    cv2.imshow("image", image)
    
    

cap = cv2.VideoCapture(0)

while(1):
    ret,img = cap.read()
    FaceRecognition(img)
    c = cv2.waitKey(1) 
    #print(c)
    if c & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()