import cv2
import numpy as np

img = cv2.imread('lena512color.tiff')
# 下面的 None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
# 因此这里为 None
'''
参数解释：

src：输入，原图像，即待改变大小的图像；

dst：输出，改变大小之后的图像，这个图像和原图像具有相同的内容，只是大小和原图像不一样而已；

dsize：输出图像的大小。如果这个参数不为0，那么就代表将原图像缩放到这个Size(width，height)指定的大小；如果这个参数为0，那么原图像缩放之后的大小就要通过下面的公式来计算：

dsize = Size(round(fx*src.cols), round(fy*src.rows))

其中，fx和fy就是下面要说的两个参数，是图像width方向和height方向的缩放比例。

fx：width方向的缩放比例，如果它是0，那么它就会按照(double)dsize.width/src.cols来计算；

fy：height方向的缩放比例，如果它是0，那么它就会按照(double)dsize.height/src.rows来计算；

interpolation：这个是指定插值的方式，图像缩放之后，肯定像素要进行重新计算的，就靠这个参数来指定重新计算像素的方式，有以下几种：

INTER_NEAREST - 最邻近插值
INTER_LINEAR - 双线性插值，如果最后一个参数你不指定，默认使用这种方法
INTER_AREA - resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_CUBIC - 4x4像素邻域内的双立方插值
INTER_LANCZOS4 - 8x8像素邻域内的Lanczos插值
'''
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

#OR
# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)


cv2.imshow('res',res)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
