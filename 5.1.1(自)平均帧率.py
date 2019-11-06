import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret1 = cap.set(3,1280)     #修改分辨率  高宽     实验后发现不同分辨率会影响帧率FPS，opencv的设置至少对于usb摄像头来说是真的改变了摄像头采集大小即低分辨率时可以加快速度，而不是都是采集1920*1080然后裁剪成680*420给你
ret2 = cap.set(4,1024)
a=cap.get(3)       #查看分辨率
b=cap.get(4)
c=cap.get(5)   #帧率?视频可以用这个摄像头不行得自己算
#print(a,b,c)
cnt = 10 #计数器，计算10帧平均帧率
while(True):
    # Capture frame-by-frame
    if(cnt>=10):                     #第一帧开始记录时间
        time = cv2.getTickCount()
    cnt -= 1
    ret, frame = cap.read()
    #time = cv2.getTickCount()   之前我开始时间写在这里，计算fps2000+   一脸闷逼 记住要在调用摄像头前计时
    # #getTickcount函数：返回从操作系统启动到当前所经过的毫秒数     getTickFrequency函数：返回每秒的计时周期数
    # Our operations on the frame come here
    color = frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',color)
    if(cnt<=1):
        time = (cv2.getTickCount()-time)/10/cv2.getTickFrequency()
        fps = 1.0/time
        print("resolution:{}*{},FPS:{:.0f}".format(a, b, fps))
        cnt = 10
    # if(cnt<=0):
    #     cnt = 1
    #
    #     print("resolution:{}*{},FPS:{:.0f}".format(a,b,fpstmp))
    #
    #     fpstmp = fps  # 每10帧后开始重新计算（避免之前的10帧数据干扰）  前面刚刚开始帧跳的有点厉害   tmp临时存放用来
    # else:
    #     fpstmp += fps/2
    #     print(fpstmp)
    #     cnt -=1
    if cv2.waitKey(1) & 0xFF == ord('q'):   #这东西意外的影响速率啊 没有这句话fps稳定有fps有时会高不少
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()