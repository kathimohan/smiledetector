import numpy as np
import cv2
s=0
n=0
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
image = cv2.imread("694.jpg")
n=n+1
    
smile = smileCascade.detectMultiScale(
            image,
            scaleFactor= 1.1,
            minNeighbors=3,
            minSize=(10, 10),
            )
print(smile)
if len(smile)>1:
    s=s+1
    print("smile detected")
