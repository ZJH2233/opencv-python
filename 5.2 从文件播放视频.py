import numpy as np
import cv2

cap = cv2.VideoCapture("C:/Users/DELL/Desktop/data/1.mp4")
ret1 = cap.set(3,0)
ret2 = cap.set(4,0)
fps = cap.get(5)  #FPS
print(ret1,ret2)
pauseTime = 1000/fps  #两幅画面中间间隔
while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if(cv2.waitKey(int(pauseTime))&0xFF==ord('q') or cv2.waitKey(int(pauseTime))&0xFF==27): #OpenCV新手常犯的一个错误是调用cv::imshow()遍历视频帧，而不使用cv::waitKey(30)跟踪每一次绘制。在这种情况下，屏幕上什么也不会显示，因为highgui从来没有时间来处理来自cv::imshow()的draw请求。
        break
cap.release()
cv2.destroyAllWindows()

