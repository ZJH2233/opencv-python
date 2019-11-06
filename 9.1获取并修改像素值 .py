import cv2
import numpy as np

img = cv2.imread('lena512color.tiff')
cv2.imshow('image',img)

px = img[100,100]           #查看图片某像素值
print(px)
blue = img[100,100,0]
print(blue)

#img[100,100]=[255,255,255] #修改像素值
#print(img[100,100])





# 警告：Numpy 是经过优化了的进行快速矩阵运算的软件包。所以我们不推荐
# 逐个获取像素值并修改，这样会很慢，能有矩阵运算就不要用循环。

#获取像素值及修改的更好方法。
print(img.item(100,100,0))  #查看像素值
img.itemset((100,100,0),100)#修改像素值
print(img.item(100,100,0))
cv2.waitKey(0)
cv2.destroyAllWindows()
