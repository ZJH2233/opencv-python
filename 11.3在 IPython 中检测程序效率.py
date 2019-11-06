# import cv2
# import numpy as np
# In [10]: x = 5
# In [11]: %timeit y=x**2
# 10000000 loops, best of 3: 73 ns per loop
# In [12]: %timeit y=x*x
# 10000000 loops, best of 3: 58.3 ns per loop
# In [15]: z = np.uint8([5])
# In [17]: %timeit y=z*z
# 1000000 loops, best of 3: 1.25 us per loop
# In [19]: %timeit y=np.square(z)
# 1000000 loops, best of 3: 1.16 us per loop


# import cv2
# import numpy as np
# In [35]: %timeit z = cv2.countNonZero(img)
# 100000 loops, best of 3: 15.8 us per loop
# In [36]: %timeit z = np.count_nonzero(img)
# 1000 loops, best of 3: 370 us per loop

# 注意：一般情况下 OpenCV 的函数要比 Numpy 函数快。所以对于相同的操
# 作最好使用 OpenCV 的函数。当然也有例外，尤其是当使用 Numpy 对视图
# （而非复制）进行操作时。

