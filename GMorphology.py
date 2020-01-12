'''
Gray Morphology 
Gray
    Erosion
    Dilation
    Open
    Close

SE size is 3x3 for all situation

'''

import cv2
import numpy as np 
from DilateAndErosion import GetTheLittle
import math




def GDilation(img,SE):
    w,h = img.shape
    
    #img.dtype = 'bool'
    (SE_w, SE_h) = SE.shape
    #print(SE)
    img_R = np.array([w,h])
    img_R = img.copy()
   

    # Dilation 
    gap = int(SE_w/2)
    
    for i in range(gap,w-gap):
        for j in range(gap, h-gap):
            mat = GetTheLittle(SE_h,img,i,j)
            # if np.max(mat) != np.min(mat): # cannot become faster
            mat = mat + SE
            max = int(np.max(mat))
            # img_R[i-gap:i+gap+1,j-gap:j+gap+1] = max
            img_R[i,j] = max
    return img_R


def GErosion(img,SE ):
    w,h = img.shape
    
    #img.dtype = 'bool'
    (SE_w, SE_h) = SE.shape
    #print(SE)
    img_R = np.array([w,h])
    img_R = img.copy()
   

    # Dilation 
    gap = int(SE_w/2)
    
    for i in range(gap,w-gap):
        for j in range(gap, h-gap):    
            mat = GetTheLittle(SE_h,img,i,j)       
            mat = abs(mat - SE)
            min = int(np.min(mat))
            # img_R[i-gap:i+gap+1,j-gap:j+gap+1] = min
            img_R[i,j]=min
    
    return img_R


def GOpen(img, SE):
    
    img_RE = GErosion(img , SE )
    img_RED = GDilation(img_RE,SE )

    return img_RED


def GClose(img , SE ):
    img_RD = GDilation(img,SE)
    img_RDE = GErosion(img_RD,SE) 
    return img_RDE



def NotExcedd(img, img_mask):
    w, h = img.shape
    img_R = img.copy()
    for i in range(w):
        for j in range(h):
            if img[i,j] > img_mask[i,j]:
                img_R[i,j] = img_mask[i,j]
    return img

#Reconstruction -- OBR
'''
input : img
output : img_R
SE is pre_defined(currently)
Algorithm:
    img -open-> img_O
    img_R = np.empty([img_O.shape])
    
    while(img_O != img_R):
        GrayDilate(img_O)
        img_R = NotExcedd(img_O,img)
'''
def OBR(img):
    w,h = img.shape
    SE = np.ones([3,3],dtype='int')
    img_O = GOpen(img,SE)
    
    img_R = np.empty([w,h])
    while(True):
        img_O = GDilation(img_O, SE)
        img_R = NotExcedd(img_O, img)
        if((img_R == img_O).any()):
            break
    return img_R



#Reconstruction -- CBR
'''
input : img
output : img_R
SE is pre_defined(currently)
Algorithm:
    img -close-> img_C
    img_R = np.empty([img_C.shape])
    
    while(img_C != img_R):
        GrayDilate(img_C)
        img_R = NotExceed(img_C,img)
'''
def CBR(img):
    w,h = img.shape
    SE = np.ones([3,3],dtype='int')
    img_C = GClose(img,SE)
    
    img_R = np.empty([w,h])
    while(True):
        img_C = GDilation(img_C, SE)
        img_R = NotExcedd(img_C, img)
        if((img_R == img_C).any()):
            break
    return img_R







if __name__ == "__main__":

    imgname = '/Users/zhangyesheng/Desktop/IGST计算机辅助手术/Project1/pictures/lena512color.tiff'
    path = '/Users/zhangyesheng/Desktop/IGST计算机辅助手术/Project1/pictures/'
    img = cv2.imread(imgname,0)
    # cv2.imwrite(path+'Ori.jpg',img)
    SE = np.ones([5,5],dtype='int')
    # img_R = GClose(img, SE)
    img_R = GDilation(img,SE )
    cv2.imwrite(path+'GD.jpg',img_R)
