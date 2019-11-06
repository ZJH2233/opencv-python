import cv2
import numpy as np

img = cv2.imread('lena512color.tiff')

b,g,r=cv2.split(img)
img=cv2.merge(b,g,r)
#警告：cv2.split() 是一个比较耗时的操作。只有真正需要时才用它，能用
#Numpy 索引就尽量用。

#或者 numpy有类似合并函数的忘了啥
b=img[:,:,0]
g=img[:,:,1]
r=img[:,:,2]

#假如你想使所有像素的红色通道值都为 0，你不必先拆分再赋值。你可以直接使用 Numpy 索引，这会更快。numpy索引和分割是同一语法只不过分割分完后赋值出去了
img[:,:,2]=0