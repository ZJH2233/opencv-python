'''
在前面的部分我们使用是全局阈值，整幅图像采用同一个数作为阈值。当
时这种方法并不适应与所有情况，尤其是当同一幅图像上的不同部分的具有不
同亮度时。这种情况下我们需要采用自适应阈值。此时的阈值是根据图像上的
每一个小区域计算与其对应的阈值。因此在同一幅图像上的不同区域采用的是
不同的阈值，从而使我们能在亮度不同的情况下得到更好的结果。
这种方法需要我们指定三个参数，返回值只有一个。
• Adaptive Method- 指定计算阈值的方法。
– cv2.ADPTIVE_THRESH_MEAN_C：阈值取自相邻区域的平
均值
– cv2.ADPTIVE_THRESH_GAUSSIAN_C：阈值取值相邻区域
的加权和，权重为一个高斯窗口。
• Block Size - 邻域大小（用来计算阈值的区域大小）。 这个数不能为偶数且要大于1
• C - 这就是是一个常数，阈值就等于的平均值或者加权平均值减去这个常
数。

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cat500.jpg',0)
# 中值滤波
img = cv2.medianBlur(img,5)

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为 Block size, 2 为 C 值
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,41,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks(())#
    plt.yticks([])#一样的
plt.show()
