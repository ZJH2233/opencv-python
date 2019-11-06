import cv2
import numpy as np

'''
插值法的第一次都是相同的，计算新图的坐标点对应原图中哪个坐标点来填充，计算公式为：
srcX = dstX* (srcWidth/dstWidth)
srcY = dstY * (srcHeight/dstHeight)
srcWidth/dstWidth和srcHeight/dstHeight分别表示宽和高的放缩比。
那么问题来了，通过这个公式算出来的srcX,scrY有可能是小数，但是坐标点是不存在小数的，都是整数，得想办法把它转换成整数才行。
不同的插值法的区别就体现在srcX,scrY是小数时，怎么变成整数去取原图片中的像素值。
最邻近：看名字就很直白，四舍五入选取最接近的整数。这样的做法就会导致像素的变化不连续，在图像中的体现就是会有锯齿。
双线性插值：双线性就是利用与坐标轴平行的两条直线去把小数坐标分解到相邻的四个整数坐标点的和，权重为距离。
'''
def INTER_NEAREST(src,dsth,dstw):
    dst = np.zeros((dsth,dstw,3),dtype=np.uint8)
    for i in range(dsth):
        for j in range(dstw):
            srcx = round((i+1) * (srch/dsth))
            srcy = round((j+1) * (srcw/dstw))
            dst[i,j] = src[srcx-1,srcy-1]
    return dst

#https://blog.csdn.net/qq_37577735/article/details/80041586  双线性这个说得好  INTER_LINEAR - 双线性插值
def INTER_LINEAR(src,dsth,dstw):  #自己写的效率奇差，先理解原理的说
    dst = np.zeros((dsth,dstw,3),dtype=np.uint8)

    scale_x = float(srcw)/dstw
    scale_y = float(srch)/dsth

    for k in range(3): #channels .......其实应该不用，速度更快，内部优化
        for j in range(dsth):
            for i in range(dstw):
                # Original coords
                srcx = (i+0.5) * scale_x - 0.5  #0.5是为了源图像和目标图像几何中心的对齐　　具体看链接
                srcy = (j+0.5) * scale_y - 0.5  #得到在原图中应该取什么点
                # INTER_LINEAR:
                # 2*2 neighbors.     2*2领域中开始使用双线性插值
                src_x_0 = int(np.floor(srcx))
                src_y_0 = int(np.floor(srcy))  #比如 x,y=1.2,1.4 呢么在他的领域中 左上（x0，y0）点取值
                src_x_1 = min(src_x_0 + 1, srcw - 1)
                src_y_1 = min(src_y_0 + 1, srch - 1) #在取得x1,y1点，且避免超出图像范围
                #按公式计算.....其实python应该不用拆开通道计算的，直接运算没问题，这里抄别人的也没改
                value0 = (src_x_1 - srcx) * src[src_y_0, src_x_0, k] + (srcx - src_x_0) * src[src_y_0, src_x_1, k]
                value1 = (src_x_1 - srcx) * src[src_y_1, src_x_0, k] + (srcx - src_x_0) * src[src_y_1, src_x_1, k]
                dst[j, i, k] = int((src_y_1 - srcy) * value0 + (srcy - src_y_0) * value1)
    return dst

'''
假设源图像A大小为m*n，缩放后的目标图像B的大小为M*N。那么根据比例我们可以得到B(X,Y)在A上的的 
对应坐标为A(x,y)=A(X*(m/M),Y*(n/N))。在双线性插值法中，我们选取A(x,y)的最近四个点。而在双立方 
插值法中，我们选取的是最近的16个像素点作为计算目标图像B(X,Y)处像素值的参数。
'''
def BiBubic(x ,A = -1):  #采样公式 产生权值具体可看链接https://blog.csdn.net/u010979495/article/details/78428898
    if(x<=1):
        return 1 - (A + 3) * x**2 + (A + 2) * x**3
    elif(x<2):
        return -4 * A + 8 * A * abs(x) - 5 * A * x**2 + A * x**3
    else:
        return 0


def INTER_CUBIC(src,dsth,dstw):  #效果最好，先计算dst i,j 在 src 中的位置， 在该位置做卷积??(感觉不是卷积吧，就是个加权和) ，权值计算后得到值返回给dst i,j
    dst = np.zeros((dsth,dstw,3),dtype=np.uint8)
    # 有问题懒得写了反正肯定速度奇慢无比，写的没opencv好也就算了，网上好多错，真想在做去看看github 或者 opencv源码
    # for i in range(dsth):
    #     for j in range(dstw):
    #         srcx = j*(srcw/dstw) #计算在原图中的位置
    #         srcy = i*(srch/dsth)
    #         x = int(np.floor(srcx))  #取出整数   np.floor和math.floor不同 给的还是小数 4. -2. 0. 10.   这样
    #         y = int(np.floor(srcy))
    #         u = srcx - x        #取出小数
    #         v = srcy - y
    #         tmp = 0
    #         for ii in range(-1,3):    #原代码参考里写的是for ii in range(-1,2)  错了 左闭右开
    #             for jj in range(-1,3): #计算16格的权值和了
    #                if(x+ii<0 or y+jj<0 or x+ii>srch or y+jj>=srcw):
    #                    continue
    #                tmp +=srcimg[x+ii,y+jj]*BiBubic(ii-u)*BiBubic(jj-v)
    #         dst[i,j] = np.clip(tmp,0,255)
    return dst


def myself(src,dsth,dstw):  #自己瞎写的效果比ret1邻近域插值法还好
    dst = np.zeros((dsth,dstw,3),dtype=np.uint8)
    for i in range(dsth):
        for j in range(dstw):
            srcx = int(i*(srch/dsth))
            srcy = int(j * (srcw / dstw))
            dst[i,j]=srcimg[srcx,srcy]
    return dst








srcimg = cv2.imread('akagi.jpg')
srch,srcw = srcimg.shape[:2]  #height = row =y             wwight = col =x
dsth = srch * 2
dstw = srcw * 2
ret1 = INTER_NEAREST(srcimg, dsth, dstw)
#ret2 = INTER_LINEAR(srcimg,dsth,dstw)        写的超级垃圾 速度超级慢 虽然结果出来了
ret3 = INTER_CUBIC(srcimg,dsth,dstw)



cv2.imshow('img',srcimg)
cv2.imshow('ret1',ret1)
#cv2.imshow('ret2',ret2)
cv2.imshow('ret3',ret3)
cv2.waitKey(0)
cv2.destroyAllWindows()
