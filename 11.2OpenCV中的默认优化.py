import cv2
import numpy as np
# check if optimization is enabled
#这是控制台代码，这里就演示一下告诉你开了优化好处
# In[5]: cv2.useOptimized()
# Out[5]: True
# In [6]: %timeit res = cv2.medianBlur(img,49)
# 10 loops, best of 3: 34.9 ms per loop
# # Disable it
# In [7]: cv2.setUseOptimized(False)
# In [8]: cv2.useOptimized()
# Out[8]: False
# In [9]: %timeit res = cv2.medianBlur(img,49)
# 10 loops, best of 3: 64.1 ms per loop
