#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2 

filePath = "F:/workdir/test.jpg"
img = cv2.imread(filePath)                      #读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #转换为灰色

#OpenCV 人脸识别分类器
classifier = cv2.CascadeClassifier(
    "F:/workdir/tool/opencv-python38/haarcascades/haarcascade_frontalface_default.xml"
)

color = (0,255,0)

faceRects = classifier.detectMultiScale(gray, 1.2, 3)

print(faceRects)
if len(faceRects):              #大于0则检测到人脸
    for faceRect in faceRects:   #单独框出没一张人脸
        x,y,w,h = faceRect
        #框出人脸
        cv2.rectangle(img, (x,y), (x+h, y+w), color, 2)
        #左眼
        #cv2.circle(img, (x+w//4,+h//4+30), min(w//8,h//8), color)
        #右眼
        #cv2.circle(img, (x+3*w//4,y+h//4+30), min(w//8, h//8),color)
        #嘴巴
        cv2.rectangle(img, (x+3*w//8, y+3*h//4),(x+5*w//8,y+7*h//8),color)
        
cv2.imshow("image", img)        #显示图像
c = cv2.waitKey(10)



cv2.waitKey(0)
cv2.destroyAllWindows()