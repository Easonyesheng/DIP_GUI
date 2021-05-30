'''
Entropy method
input : gray pic(cv2 image)
output : Threshold
'''

import cv2
import numpy as np
import math

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



# if __name__ == "__main__":
#     img = cv2.imread('/Users/zhangyesheng/Desktop/Icon.JPG')
#     imgG = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#     T = Entropy_get(imgG)
#     T_idea,imgd = cv2.threshold(imgG, T, 255, cv2.THRESH_BINARY)
#     #print(T,'*',T_idea)
#     cv2.imshow('H',imgd)
#     cv2.waitKey(0)