import cv2
import numpy as np

img1 = cv2.imread('lena512color.tiff')
img2 = cv2.imread('cat512.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('merge',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
