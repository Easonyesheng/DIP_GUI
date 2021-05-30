


import cv2
import numpy as np
import math
import matplotlib.pyplot as plt



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

#EN = entropy
def Entropy_get(img):
    T_EN = 0 # OTSU Threshold 
    H = []
    # get the list of every pixel probability
    w,h = img.shape
    pixsum = w*h #pixel sum 
    data = np.zeros((256),dtype=int)
    for i in range(0,w):
        for j in range(0,h):
            data[int(img[i,j])]+=1
    data = data/pixsum 

    for j in range(0,256):
        if data[j] == 0:
            data[j] = 1


    for t in range(1,256):
        Hb = -1*sum(data[i]*math.log(data[i]) for i in range(0,t))
        Hw = -1*sum(data[i]*math.log(data[i]) for i in range(t,255))
        H.append(Hb+Hw)

    T_EN = H.index(max(H))
    
    return T_EN

def OTSU_GET(img):
    T_OTSU = 0 # OTSU Threshold 
    delta = []
    # get the list of every pixel probability
    w,h = img.shape
    pixsum = w*h #pixel sum 
    data = np.zeros((256),dtype=int)
    for i in range(0,w):
        for j in range(0,h):
            data[int(img[i,j])]+=1
    data = data/pixsum 

    for t in range(1,256):

        w0 = sum(data[0:t])
        if w0 == 0:
            u0 = 0
        else:
            u0 = sum(i*data[i] for i in range(0,t))/w0

        w1 = sum(data[t:255])
        if w1 == 0:
            u1 = 0
        else:
            u1 = sum(j*data[j] for j in range(t,255))/w1

        delta.append(w0*w1*(u1-u0)*(u1-u0))
    
    max_de = max(delta)
    T_OTSU = delta.index(max_de)

    return T_OTSU




    





# if __name__ == "__main__":
#     img = cv2.imread('/Users/zhangyesheng/Desktop/DOG.JPG')
#     imgG = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#     T = OTSU_GET(imgG)
#     T_idea,imgd = cv2.threshold(imgG, T, 255, cv2.THRESH_BINARY)
#     #print(T,'*',T_idea)
#     cv2.imshow('H',imgd)
#     cv2.waitKey(0)
    