import cv2
import numpy as np

img = cv2.imread('lena512color.tiff')  #img本身就是numpy变量所以可以用有关所有函数

print(img.shape) #图像的形状。他的返回值是一个包含行数，列数，通道数的元组。   数组里就是不同维度的大小

print(img.size)  #img.size 可以返回图像的像素数目：

print(img.dtype) #img.dtype 返回的是图像的数据类型.
                 #注意：在除虫（debug）时 img.dtype 非常重要。因为在 OpenCV�Python 代码中经常出现数据类型的不一致。

