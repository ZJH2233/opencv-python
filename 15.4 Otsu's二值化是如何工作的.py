'''
https://blog.csdn.net/jinzhichaoshuiping/article/details/51207942
这个比PPT公式讲的明白多了
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('noisy2.png',0)
blur = cv2.GaussianBlur(img,(5,5),0)

# find normalized_histogram, and its cumulative distribution function
# 计算归一化直方图
#CalcHist(image, accumulate=0, mask=NULL)
hist = cv2.calcHist([blur],[0],None,[256],[0,256])   #https://blog.csdn.net/YZXnuaa/article/details/79231817  计算直方图   https://blog.csdn.net/keith_bb/article/details/56680997 这个开头也能看一下理解一下
#plt.plot(hist)#print(hist)
hist_norm = hist.ravel()/hist.max() #先扁平化在归一化  大概了解了一下归一化https://blog.csdn.net/u010555688/article/details/25551255  但是这里为什么归一化还是不知道
#plt.plot(hist_norm),print(hist_norm)
Q = hist_norm.cumsum()    #类似求和符号   如 a = [0 1 2 3 4 5 6 7], b = a.cumsum(), b = [ 0  1  3  6 10 15 21 28]

bins = np.arange(256)

fn_min = np.inf  #无穷大

thresh = -1     #阈值

for i in range(256):
    p1,p2 = np.hsplit(hist_norm,[i])# probabilitie 概率 可能性   将归一化后的灰度直方图数列划分成2部分 p1，p2
    q1,q2 = Q[i],Q[255]-Q[i]# cum sum of classes
    b1,b2 = np.hsplit(bins,[i]) # weights    https://blog.csdn.net/miaoyanmm/article/details/80188994   https://blog.csdn.net/weixin_41010198/article/details/89103982   x = weight = col =列 切分

    # finding means and variances    会报错可能是除零错误
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

    # find otsu's threshold value with OpenCV function
ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  #opencv 函数计算得到的阈值和我们自己计算的阈值比较
cv2.imshow('img',otsu)
cv2.waitKey(0)
print(thresh,ret)
#plt.show()