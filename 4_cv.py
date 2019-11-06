import numpy as np
import cv2

img = cv2.imread('lena512color.tiff',1)

#1
cv2.imshow('img',img)

#2
cv2.namedWindow('image', cv2.WINDOW_NORMAL)  #窗口可调
cv2.imshow('image',img)

cv2.imwrite('lena_writeTest.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


