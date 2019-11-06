'''
对于视角变换，我们需要一个 3x3 变换矩阵。在变换前后直线还是直线。
要构建这个变换矩阵，你需要在输入图像上找 4 个点，以及他们在输出图
像上对应的位置。这四个点中的任意三个都不能共线。这个变换矩阵可以有
函数 cv2.getPerspectiveTransform() 构建。然后把这个矩阵传给函数
cv2.warpPerspective。

https://www.imooc.com/article/27535
https://blog.csdn.net/i_chaoren/article/details/78324184  我感觉这里透视变换图很不错，在结合仿射变换类似坐标轴改变，理解两者区别
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat500.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows, cols, ch = img.shape
#应该和14.4一样我觉得 如果这里错了的话呢我14.4理解也是错的
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img, M, (300,300))

plt.subplot(121)
plt.imshow(img)
plt.title('input')
plt.subplot(122)
plt.imshow(dst)
plt.title('output')
plt.show()