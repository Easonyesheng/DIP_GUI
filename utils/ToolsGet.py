# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 20:33
# @Author  : tangxl
# @FileName: ToolsGet.py
# @Software: PyCharm
"""
HisGet, OTSUGet, EntropyGet
"""

import matplotlib.pyplot as plt
import numpy as np
import math


# 灰度直方图统计
def His(img, dir):
    """
    :param img: a gray image
    :param dir:
    :return: matplotib.hist
    save to memory and show in GUI
    """
    w, h = img.shape
    His = np.ones([256])
    for i in range(0, w):
        for j in range(0, h):
            His[img[i, j]] += 1

    x = np.arange(0, 256, 1)
    plt.figure(figsize=(8, 8))
    plt.plot(x, His, linewidth=3)
    plt.xlabel('Gray Level', family='Times New Roman', weight='bold', size=36)
    plt.ylabel('Indensity', family='Times New Roman', weight='bold', size=36)
    plt.xticks(fontproperties='Times New Roman', size=30)
    plt.yticks(fontproperties='Times New Roman', size=30)
    plt.tight_layout()
    plt.savefig(dir, format='png', bbox_inches='tight')
    # plt.show()


def OTSU(img):
    """
    :param img: gray pic (cv2 Image)
    :return: Threshold
    """
    T_OTSU = 0  # OTSU Threshold
    delta = []
    # get the list of every pixel probability
    w, h = img.shape
    pixsum = w * h  # pixel sum
    data = np.zeros((256), dtype=int)
    for i in range(0, w):
        for j in range(0, h):
            data[int(img[i, j])] += 1
    data = data / pixsum

    for t in range(1, 256):

        w0 = sum(data[0:t])
        if w0 == 0:
            u0 = 0
        else:
            u0 = sum(i * data[i] for i in range(0, t)) / w0

        w1 = sum(data[t:255])
        if w1 == 0:
            u1 = 0
        else:
            u1 = sum(j * data[j] for j in range(t, 255)) / w1

        delta.append(w0 * w1 * (u1 - u0) * (u1 - u0))

    max_de = max(delta)
    T_OTSU = delta.index(max_de)

    return T_OTSU


def Entropy(img):
    T_EN = 0  # OTSU Threshold
    H = []
    # get the list of every pixel probability
    w, h = img.shape
    pixsum = w * h  # pixel sum
    data = np.zeros(256, dtype=int)
    for i in range(0, w):
        for j in range(0, h):
            data[int(img[i, j])] += 1
    data = data / pixsum

    for j in range(0, 256):
        if data[j] == 0:
            data[j] = 1

    for t in range(1, 256):
        Hb = -1 * sum(data[i] * math.log(data[i]) for i in range(0, t))
        Hw = -1 * sum(data[i] * math.log(data[i]) for i in range(t, 255))
        H.append(Hb + Hw)

    T_EN = H.index(max(H))

    return T_EN

