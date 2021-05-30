'''
Code to realize Dilation and Erosion & conditional dilation
Input : Binary image & Structure Element
Do not waste time in meaningless calculate!
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt 



# function used to dialate img
'''

input : Binary img and SE
output : Binary img_R 0&1 | dtype = int

'''
def DilationGet(img, SE):
    w,h = img.shape
    
    if np.max(img) == 255:
        img = img/255
    #     img = img_convert(img) # 0-1 transform
    #img.dtype = 'bool'
    (SE_w, SE_h) = SE.shape
    #print(SE)
    img_R = np.array([w,h])
    img_R = img.copy()
   
    if (SE_w != SE_w) or (SE_w%2 == 0):
        print("Structure Element Error")
        return -1

    # Dilation 
    gap = int(SE_w/2)
    
    for i in range(gap,w-gap):
        for j in range(gap, h-gap):
            if img[i][j] == 1:
                mat = GetTheLittle(SE_h,img,i,j)
                if 0 in mat:
                    #print('mat:' ,mat)
                    # print('SE',SE)
                    DR = mat & SE
                    #print(DR)
                    c = 0 # count
                    se_row = np.reshape(SE,([1,SE_h*SE_w])) # 转换成行向量
                    if True in DR: # 满足膨胀要求
                        # print(DR)
                        # 可以用数组切片加速 施工中
                        # img_R[i-gap:i+gap+1,j-gap:j+gap+1] = SE.astype(np.int64)
                        for x in range(i-gap,i+gap+1):
                            for y in range(j-gap,j+gap+1):
                                if img_R[x][y] == 0:
                                    img_R[x][y] = int(se_row[0,c])
                                c += 1
            
    return img_R


# funtion used to Erosion Binary image
'''
input : Binary img and SE (0 &255)
output : Binary img_R 0&1.0
'''

def ErosionGet(img, SE):
    w,h = img.shape
    # img = img_convert(img) # 0-1 transform
    #img.dtype = 'bool'
    img = img/255
    (SE_w, SE_h) = SE.shape
    #print(SE)
    img_R = np.array([w,h])
    img_R = img.copy()
    if (SE_w != SE_w) or (SE_w%2 == 0):
        print("Structure Element Error")
        return -1

    # Dilation 
    gap = int(SE_w/2)
    
    for i in range(gap,w-gap):
        for j in range(gap, h-gap):
            if img[i][j] == 1:
                mat = GetTheLittle(SE_h,img,i,j)
                if 0 in mat:
                    #print('mat:' ,mat)
                    # print('SE',SE)
                    DR = mat & SE
                    
                    #print(DR)
                  
                    if not ((SE == DR).all()): # 满足腐蚀要求
                        img_R[i][j] = 0
                        
    return img_R



# A Function to get the SE size from the picture
# size = SE's size
def GetTheLittle(size,pic,i,j):

    gap = int(size/2)
    mat = pic[i-gap:i+gap+1,j-gap:j+gap+1]

    mat = mat.astype(np.int16)
    #print(mat)
    return mat

def img_convert(img):
    w,h = img.shape
    img_R = img.copy()
    for i in range(w):
        for j in range(h):
            if img[i,j] == 255:
                img_R[i][j] == 1
            else:
                img_R[i][j] == 0
    return img_R

'''
conditional dialate
input : img & line's position
output : img_R
'''
def ConDia(img,line):
    path = '/Users/zhangyesheng/Desktop/temp/ConD/'
    cv2.imwrite(path+'Ori.jpg',img)
    w,h = img.shape
    img = img_convert(img)
    # cv2.imwrite(path+'Ori.jpg',img*255)
    img = img.astype(np.int)
    img_line = np.zeros([w,h],dtype='int')
    img_line[:,int(h*line)] = 1
    
    
    temp = np.zeros([w,h],dtype='int')
    SE = np.ones([11,11],dtype='bool')
    c = 0
    img_grayt = img.astype(np.bool)
    # print(img_grayt.dtype)
    
    # img_graytl = img_grayt*255
    a = 0
    b = 0
    while(True):
        print(c)
        img_line = DilationGet(img_line,SE)
        temp = img_line.copy()
        # print(temp.dtype)
        # temp = temp.astype(np.int)
        # img_line = img_line.astype(np.bool)
        img_line = img_line & img_grayt # 0 & 1
        img_line = img_line.astype(np.int)
        # print(img_line.dtype)
        img_l = img_line*255
    
        cv2.imwrite(path+str(c)+'.jpg',img_l)
        c+=1
        # print((temp == img_line).all())
        res = temp == img_line
        a = np.sum(res == False)
        if (a == b):
            break
        b = a
        
    return img_line.astype(np.int)



# distance transform
def DisTrans(img ):
    w,h = img.shape
    
    SE = np.ones([3,3],dtype = 'bool')
    # remove the points in the border
    img[0,:] = 0
    img[:,0] = 0
    img[w-1,:] = 0
    img[:,h-1] = 0


    Img_R = img.copy()
    Img_R = Img_R/255 # all is 1 or 0
    c = 2
    while(img.any() == 1):
        img = ErosionGet(img,SE)
        none, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
        [x,y] = np.where(Img_R == 1)
        for i in range(len(x)):
            if(img[x[i]][y[i]] == 0):
                Img_R[x[i]][y[i]] = c
        c+=1
    Img_R = (Img_R/Img_R.max())*255
    return Img_R


# get the skeleton
def SkeGet(img):
    w,h = img.shape
    Img_R = np.zeros([w,h])
    SE = np.ones([3,3],dtype='bool')
    # remove the points in the border
    img[0,:] = 0
    img[:,0] = 0
    img[w-1,:] = 0
    img[:,h-1] = 0
    c = 0
    while(img.any() == 1):

        #Erosion
        img = ErosionGet(img,SE)
        none, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
        temp = img.copy()

        # open
        temp = ErosionGet(temp,SE)
        none, temp = cv2.threshold(temp,0,255,cv2.THRESH_BINARY)
        temp = DilationGet(temp,SE)
        none, temp = cv2.threshold(temp,0,255,cv2.THRESH_BINARY)

        temp = img - temp

        # set result
        Img_R  += temp
        c += 1
    return Img_R, c
   