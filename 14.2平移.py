import cv2
import numpy as np

img = cv2.imread('lena512color.tiff')
rows,cols,_=img.shape
#row = 行 = y = height  cols = 列 = x = weight
#理论上可以自己写一个循环移动，但是速度过慢，这里一个是用了什么数学原理优化了
#具体平移原理是每一个点（x，y）乘以矩阵M就可以算出对应平移点，更具体的百度
M = np.float32([[1,0,100],[0,1,50]])
# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img,M,(cols,rows))
#dst = cv2.warpAffine(img,M,(2*cols,2*rows))  和生成图片窗口大小有关

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()