import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret1 = cap.set(3,10)     #修改分辨率  高宽
ret2 = cap.set(4,10)
a=cap.get(3)       #查看分辨率
b=cap.get(4)
c=cap.get(5)   #帧率?视频可以用这个摄像头不行得自己算
#print(a,b,c)

while(True):
    # Capture frame-by-frame

    time = cv2.getTickCount()
    ret, frame = cap.read()
    #time = cv2.getTickCount()   之前我开始时间写在这里，计算fps2000+   一脸闷逼 记住要在调用摄像头前计时
    # #getTickcount函数：返回从操作系统启动到当前所经过的毫秒数     getTickFrequency函数：返回每秒的计时周期数
    # Our operations on the frame come here
    color = frame
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',color)
    time = (cv2.getTickCount()-time)/cv2.getTickFrequency()
    fps = 1.0/time
    print("resolution:{}*{},FPS:{:.0f}".format(a, b, fps))

    if cv2.waitKey(1) & 0xFF == ord('q'):   #这东西意外的影响速率啊 没有这句话fps稳定有fps有时会高不少
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()