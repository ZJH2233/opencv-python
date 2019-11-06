import cv2
import numpy as np

#加载图像
img1 = cv2.imread('245.PNG')
img2 = cv2.imread('cat512.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img1.shape
roi = img2[0:rows,0:cols]   #这是截取出了一个区域，生成了一张图类似于    Mat rectImage = image(Rect(originalPoint, processPoint)); //子图像显示

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  #将图片灰度画存在img2gray里
ret, mask = cv2.threshold(img2gray,100,255,cv2.THRESH_BINARY_INV) #threshold阈值功能
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
# 取 roi 中与 mask 中不为零的值对应的像素的值，其他值为 0
# 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略

# img = np.zeros((rows,cols,1),np.uint8)
# img[:]=255;
# print(img.shape,mask.shape)
# print(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)  #从背景里扣掉一块

# 取 roi 中与 mask_inv 中不为零的值对应的像素的值，其他值为 0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img1,img1,mask = mask_inv)  #把舰娘图像扣出来

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)   #扣掉一块的图和抠出来的舰娘图合并成为一个完整的嵌入图
img2[0:rows, 0:cols ] = dst      #把这一块放回原图


cv2.imshow('img1',img1_bg)
cv2.imshow('img2',img2_fg)
cv2.imshow('img3',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

