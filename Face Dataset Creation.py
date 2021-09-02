# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:07:49 2021

@author: farzt
"""

import cv2
import os
#%%
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
#%%
face_detector = cv2.CascadeClassifier("FaceRecognition.xml")
#%%
face_id = input("Enter the User Number:")
print(" Look at the Camera")
count = 0
while (True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (w+x,y+h), (0,255,0),2)
        count += 1
        cv2.imwrite("Dataset/user"+str(face_id)+"."+str(count)+".jpg", img)
        cv2.imshow("FaceRecognition",img)
    k = cv2.waitKey(100) & 0xff
    if k==27 or count>=100:
           break
    elif count>=300:
           break
print("END")
cam.release()
cv2.destroyAllWindows()