import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena512color.tiff')
rows, cols, ch = img.shape

#需要仿射变换前和后各3个点坐标  pts1 原图3个坐标点（x，y） pts2变换后3点坐标
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
#输入2组坐标后，计算出2*3的变换矩阵M
M = cv2.getAffineTransform(pts1,pts2)
#print(M)
#调用函数算乘法得到变换后图像
dst = cv2.warpAffine(img, M, (cols,rows))

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)
plt.show()