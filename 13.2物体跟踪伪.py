import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #opencv的HSV和一般HSV不太一样 H 0-180 S 0-255 V 0-255  想变成一般的H 0-360 S 0-1  V 0-1 据说将bgr归一化在用cvtcolor函数就可以了

    # 设定非红色的阈值
    lower_notred = np.array([10,0,0])         #想取红色，但是红色跨2个区间 0-10 和 170-180
    upper_notred = np.array([170, 220, 220])    #所以取非红色区域，可以取反得到红色区域也可以直接对非红区域操作
    # lower_notred = np.array([10,50, 50])       这一组参数不行，几乎全部都会取进，原因是s 和 V 也是会取反的 ，但是理论上应该是基于蓝色不同饱和度和亮度才对啊，黄色黑色什么的全部都取进去了为什么 具体可能和配色有关不太清楚
    # upper_notred = np.array([170, 255, 255])
    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_notred ,upper_notred)
    mask_inv = cv2.bitwise_not(mask)

    # 对原图像和掩模进行位运算
    res = cv2.bitwise_and(frame,frame,mask=mask_inv)

    # 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask_inv)
    cv2.imshow('res',res)
    if(cv2.waitKey(5)&0xFF == 27):
        break
cv2.destroyAllWindows()
