import cv2
import numpy as np
# green=np.uint8([0,255,0])
# hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
# error: /builddir/build/BUILD/opencv-2.4.6.1/
# modules/imgproc/src/color.cpp:3541:
# error: (-215) (scn == 3 || scn == 4) && (depth == CV_8U || depth == CV_32F)
# in function cvtColor
#scn (the number of channels of the source),
#i.e. self.img.channels(), is neither 3 nor 4.
#
#depth (of the source),
#i.e. self.img.depth(), is neither CV_8U nor CV_32F.
# 所以不能用 [0,255,0]，而要用 [[[0,255,0]]]
# 这里的三层括号应该分别对应于 cvArray，cvMat，IplImage
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)
print()

# 其实就是rgb转HSV而以 意义不大 不是取得跟踪物体的hsv