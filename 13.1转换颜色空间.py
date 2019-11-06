import cv2


img = cv2.imread('lena512color.tiff')
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img2rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('img',img)
cv2.imshow('img2',img2gray)
cv2.imshow('img3',img2HSV)

cv2.waitKey(0)
cv2.destroyAllWindows()
