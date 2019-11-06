import cv2
import numpy as np

img = cv2.imread('lena512color.tiff')

eye = img[200:300,200:300]

img2eye = img.copy()
img2eye[100:200,200:300] = eye

cv2.imshow('image',img)
cv2.imshow('face',eye)
cv2.imshow('img2',img2eye)

cv2.waitKey(0)
cv2.destroyAllWindows()