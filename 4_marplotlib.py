import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena512color.tiff',0)
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([]) #取消x，y轴
plt.show()