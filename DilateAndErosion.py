'''
Code to realize Dilation and Erosion
Input : Binary image & Structure Element

'''

import numpy as np
import cv2

def DilationGet(img, SE):
    w,h = img.shape
    img = img/255 # 0-1 transform
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
            mat = GetTheLittle(SE_h,img,i,j)
            
            #print('mat:' ,mat)
            # print('SE',SE)
            DR = mat & SE
            #print(DR)
            c = 0 # count
            se_row = np.reshape(SE,([1,SE_h*SE_w])) # 转换成行向量
            if True in DR: # 满足膨胀要求
                # print(DR)
                for x in range(i-gap,i+gap+1):
                    for y in range(j-gap,j+gap+1):
                        img_R[x][y] = bool(img[x][y]) | bool(se_row[0][c])
                        c += 1
    return img_R








# A Function to get the SE size from the picture
# size = SE's size
def GetTheLittle(size,pic,i,j):
    mat = np.empty(([1,size*size]))
    gap = int(size/2)
    
    c = 0
    for x in range(i-gap,i+gap+1):
        for y in range(j-gap,j+gap+1):
            mat[0][c] = pic[x][y]
            
            c += 1
    
    mat = mat.reshape(size,size)
    mat = mat.astype(np.int16)
    #print(mat)
    return mat




if __name__ == "__main__":
    # a = np.array(([1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1]))
    # b = GetTheLittle(3,a,2,2)
    # print(a)
    # print(b)
    B_Pic_Path = '/Users/zhangyesheng/Desktop/Binary.png'
    img = cv2.imread(B_Pic_Path,flags=0)
    img = cv2.resize(img,(256,256),)
    #转化为二值图像
    none, img = cv2.threshold(img,1,255,cv2.THRESH_BINARY)
    # print(type(img))
    # print(img.shape)
    

    SE = np.ones(([3,3]),dtype='bool')
    #print(SE.shape)
    
    #print(SE)
    img_R = DilationGet(img,SE)
    # print(img_R)
    cv2.imshow('imgR',img_R)
    cv2.imshow('img',img)
    cv2.waitKey(0)