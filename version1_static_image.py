import numpy as np
import cv2
import os
from util1 import stackImages
img=cv2.imread(os.path.join(os.getcwd(),'pictures','12.jpeg'))
imgcanny=cv2.Canny(img,100,200)
imgblur=cv2.GaussianBlur(img,(5,5),0)
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgdilate=cv2.dilate(imgcanny,None,iterations=3)
imgerod=cv2.erode(imgcanny,None,iterations=3)
imgStack=stackImages(0.5,([imggray,imgdilate,img],[imgdilate,imgcanny,imgblur]))
cv2.imshow('image_stack',imgStack)
cv2.waitKey(0)