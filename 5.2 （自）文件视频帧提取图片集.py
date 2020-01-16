import numpy as np
import cv2

cap = cv2.VideoCapture("C:/Users/DELL/Desktop/datatest/2.mp4")
ret1 = cap.set(3,0)
ret2 = cap.set(4,0)
fps = cap.get(5)  #FPS
print(ret1,fps)
pauseTime = 1000/fps  #两幅画面中间间隔
cnt1 = 0
cnt2 = 0

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    cnt1 = cnt1 + 1

    if(cnt1 == 10):

        path = 'C:/Users/DELL/Desktop/datatest/2/' + 'img' + str(cnt2) + '.jpg'
        cnt1 = 0
        cnt2 += 1
        print(path)
        cv2.imwrite(path,frame)
    if(cv2.waitKey(int(pauseTime))&0xFF==ord('q') or cv2.waitKey(int(pauseTime))&0xFF==27):
        break
cap.release()
cv2.destroyAllWindows()
