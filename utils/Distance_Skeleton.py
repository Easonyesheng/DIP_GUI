# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 10:13
# @Author  : tangxl
# @FileName: Distance_Skeleton.py
# @Software: PyCharm
"""
Distance transform & Skeleton
"""

import cv2
import numpy as np
from utils.Dilation_Erosion import DilationGet, ErosionGet


# distance transform
def DisTrans(img):
    w, h = img.shape

    SE = np.ones([3, 3], dtype='bool')
    # remove the points in the border
    img[0, :] = 0
    img[:, 0] = 0
    img[w - 1, :] = 0
    img[:, h - 1] = 0

    Img_R = img.copy()
    Img_R = Img_R / 255  # all is 1 or 0
    c = 2
    while(img.any() == 1):
        img = ErosionGet(img, SE)
        none, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
        [x, y] = np.where(Img_R == 1)
        for i in range(len(x)):
            if(img[x[i]][y[i]] == 0):
                Img_R[x[i]][y[i]] = c
        c += 1
    Img_R = (Img_R / Img_R.max()) * 255
    return Img_R


# get the skeleton
def SkeGet(img):
    w, h = img.shape
    Img_R = np.zeros([w, h])
    SE = np.ones([3, 3], dtype='bool')
    # remove the points in the border
    img[0, :] = 0
    img[:, 0] = 0
    img[w - 1, :] = 0
    img[:, h - 1] = 0
    c = 0
    while img.any() == 1:

        # Erosion
        img = ErosionGet(img, SE)
        none, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
        temp = img.copy()

        # open
        temp = ErosionGet(temp, SE)
        none, temp = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY)
        temp = DilationGet(temp, SE)
        none, temp = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY)

        temp = img - temp

        # set result
        Img_R += temp
        c += 1
    return Img_R, c


if __name__ == "__main__":
    path = './pictures/'
    imgname = 'blobs.png'

    img = cv2.imread(path + imgname, -1)
    # img = img/255
    # SE = np.ones([3,3],dtype = 'bool')
    # img = ErosionGet(img,SE)
    # img = ErosionGet(img,SE)
    # img = ErosionGet(img,SE)
    # img = ErosionGet(img,SE)
    # none, img = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    Img_R, c = SkeGet(img)
    cv2.imwrite(path + "Dis.jpg", Img_R)

    Img_Rec = SkeRecons(Img_R, c)
    cv2.imwrite(path + "Rec.jpg", Img_Rec)
