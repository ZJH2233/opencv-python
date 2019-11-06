import cv2
import numpy as np


img1 = cv2.imread('lena512color.tiff')

e1 = cv2.getTickCount()

for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,1)  #不同窗口做中值滤波
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

print(time)