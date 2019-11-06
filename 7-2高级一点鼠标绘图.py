import numpy as np
import cv2

# 当鼠标按下时变为 True
drawing = False
# 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
mode = True

ix,iy=-1,-1

# 创建回调函数
def draw(event,x,y,flags,param):
    global ix,iy,drawing,mode
    # 当按下左键是返回起始位置坐标
    if(event==cv2.EVENT_LBUTTONDOWN):
        drawing=True
        ix,iy=x,y
    # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下
    if(event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON):
        if(drawing==True):
            if(mode==True):
                cv2.rectangle(tmp,(ix,iy),(x,y),(0,255,0),1)
            else:
                # 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细
                cv2.circle(img,(x,y),3,(0,255,0),-1)
    # 当鼠标松开停止绘画。
    if(event==cv2.EVENT_LBUTTONUP):
        drawing==False
        if (mode == True):
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)  #保留上一个画的图型
    cv2.imshow('image', tmp)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)
while(1):
    tmp = img.copy()    #其实我不推荐这样操作，拷贝是不太好的写法，但是暂时不知道怎么不写拷贝完成任务
    # print("img" , id(img) , "tmp" , id(tmp))      tmp = img是类似引用 实际还是在操作同一个变量
    k=cv2.waitKey(1)&0xFF
    if(k==ord('m')):
        mode=not mode
    elif k == 27:
        break
