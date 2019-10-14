'''
Histogram get function
input : cv.image is a gray image
output : matplotib.hist
save to memory and show in GUI
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np


# 灰度直方图统计
def HistoGet(img,dir):
    w,h= img.shape
    His = np.ones([256])
    for i in range(0,w):
        for j in range(0,h):
            His[img[i,j]]+=1
    
    x = np.arange(0,256,1)
    plt.plot(x,His)
    plt.xlabel('GrayLevel')
    plt.ylabel('Indensity')
    plt.savefig(dir)
    #plt.show()

    



            