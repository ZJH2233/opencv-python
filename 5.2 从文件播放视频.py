import numpy as np
import cv2

cap = cv2.VideoCapture("daily.mkv")
fps = cap.get(5)  #FPS
pauseTime = 1000/fps  #两幅画面中间间隔
while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if(cv2.waitKey(int(pauseTime))&0xFF==ord('q') or cv2.waitKey(int(pauseTime))&0xFF==27):
        break
cap.release()
cv2.destroyAllWindows()