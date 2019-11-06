'''
与名字一样，这种方法非常简单。但像素值高于阈值时，我们给这个像素
赋予一个新值（可能是白色），否则我们给它赋予另外一种颜色（也许是黑色）。
这个函数就是 cv2.threshhold()。这个函数的第一个参数就是原图像，原图
像应该是灰度图。第二个参数就是用来对像素值进行分类的阈值。第三个参数
就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值。OpenCV
提供了多种不同的阈值方法，这是有第四个参数来决定的。这些方法包括：
• cv2.THRESH_BINARY
• cv2.THRESH_BINARY_INV
• cv2.THRESH_TRUNC
• cv2.THRESH_TOZERO
• cv2.THRESH_TOZERO_INV

这个函数有两个返回值，第一个为 retVal，我们后面会解释。第二个就是
阈值化之后的结果图像了。

pdf 的p66 或者 搜15.1 图解参数区别
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Gray-scale figure256.png',0)
# !!!注意这里可以不加0读入，此时还是会变成三维数组，虽然我图片保存的是二维的代码如下
# 三维读入也可以做阈值操作但是会和二维不一样，，你可以尝试用
# img = cv2.imread('Gray-scale figure256.png')代替上一行代码，就知道了，没有正确划分阈值
# 所以以后阈值划分推荐还是先变成灰度图
'''灰度图生产代码
import cv2
import numpy as np

img = np.zeros((256,256),np.uint8)
for i in range(0,256):
    img[:, i:i+1] = i
cv2.imwrite('Gray-scale figure.png',img)
print(img)
'''

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#print(thresh3)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()