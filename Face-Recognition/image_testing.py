# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:03:09 2020

@author: Siddhardhan S
"""

import cv2
import os
import numpy as np
import face_recognition as fr

test_img=cv2.imread('E:/Face Recogition/Test Images/test.jpg')
faces_detected,gray_img = fr.faceDetection(test_img)
print('face detected:', faces_detected)

# comment these lines when you are running the code from the second time
faces, faceID = fr.labels_for_training_images('E:\Face Recogition\TrainingImages')
face_recognizer = fr.train_classifier(faces, faceID)
face_recognizer.write('F:/Face detection/trainingData.yml')


# uncomment these lines while running the code from second time onwards
#face_recognizer=cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('F:/Face detection/trainingData.yml')

name = {0:'SIMRAN'} # creating dictionary containing names for label

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label, confidence = face_recognizer.predict(roi_gray) #predicts the label of the image
    
    fr.draw_rect(test_img, face)
    predicted_name = name[label]
    
    if (confidence>35): #if confidence is greater than 35, don't print the name
        continue
    
    fr.put_text(test_img, predicted_name, x, y)
    print('Confidence:', confidence)
    print('label', label)
    resized_img = cv2.resize(test_img,(500,700))
    cv2.imshow('face detection',resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows
