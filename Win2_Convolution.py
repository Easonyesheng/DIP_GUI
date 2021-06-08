# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 22:57
# @Author  : tangxl
# @FileName: Win2_Convolution.py
# @Software: PyCharm
"""
project 2 window
Convolution
"""
import cv2
import numpy as np
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Win3_DE import DEwin
from settings import *


class Convolution(QWidget):
    def __init__(self):
        super(Convolution, self).__init__()

        # Window
        self.resize(big_window_size[0], big_window_size[1])
        self.setWindowTitle('Convlution')
        self.setWindowIcon(QIcon(''))

        # label1 -- filename
        self.label_fiilename = QLabel(self)
        self.label_fiilename.setFixedSize(file_name_size[0], file_name_size[1])
        self.label_fiilename.move(file_name_loc[0], file_name_loc[1])
        self.label_fiilename.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_filetxt = QLabel(self)
        self.label_filetxt.setFixedSize(file_txt_size[0], file_txt_size[1])
        self.label_filetxt.move(file_txt_loc[0], file_txt_loc[1])
        self.label_filetxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_filetxt.setText('File Name:')

        # label2 -- original pic
        self.label_OriPic = QLabel(self)
        self.label_OriPic.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_OriPic.move(sub_window_loc_lu[0], sub_window_loc_lu[1])
        self.label_OriPic.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_Oritxt = QLabel(self)
        self.label_Oritxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Oritxt.move(sub_window_loc_lu[0] + title_dis[0], sub_window_loc_lu[1] + title_dis[1])  # +150,-20
        self.label_Oritxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Oritxt.setAlignment(Qt.AlignCenter)
        self.label_Oritxt.setText('Original Picture')

        # label3 -- Gray pic
        self.label_GrayPic = QLabel(self)
        self.label_GrayPic.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_GrayPic.move(sub_window_loc_ru[0], sub_window_loc_ru[1])
        self.label_GrayPic.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_Graytxt = QLabel(self)
        self.label_Graytxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Graytxt.move(sub_window_loc_ru[0]+title_dis[0], sub_window_loc_ru[1]+title_dis[1])
        self.label_Graytxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Graytxt.setAlignment(Qt.AlignCenter)
        self.label_Graytxt.setText('Gray Picture')

        # label4 -- Edge Detection
        self.label_ED = QLabel(self)
        self.label_ED.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_ED.move(sub_window_loc_ld[0], sub_window_loc_ld[1])
        self.label_ED.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_EDtxt = QLabel(self)
        self.label_EDtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_EDtxt.move(sub_window_loc_ld[0]+title_dis[0], sub_window_loc_ld[1]+title_dis[1])
        self.label_EDtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_EDtxt.setAlignment(Qt.AlignCenter)
        self.label_EDtxt.setText('Edge Detection')

        # label5 -- Noise Reduction
        self.label_NR = QLabel(self)
        self.label_NR.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_NR.move(sub_window_loc_rd[0], sub_window_loc_rd[1])
        self.label_NR.setStyleSheet(
            "QLabel{background:white}" 
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Time New Roman;}")
        self.label_NRtxt = QLabel(self)
        self.label_NRtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_NRtxt.move(sub_window_loc_rd[0]+title_dis[0], sub_window_loc_rd[1]+title_dis[1])
        self.label_NRtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_NRtxt.setAlignment(Qt.AlignCenter)
        self.label_NRtxt.setText('Noise Reduction')

        # ----------------------------------------------button
        # button -- quit
        btn_q = QPushButton(self)
        btn_q.setText('Quit')
        btn_q.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_q.setFixedSize(button_size[0], button_size[1])
        btn_q.move(quit_loc[0], quit_loc[1])
        btn_q.clicked.connect(QCoreApplication.instance().quit)

        # button -- change window
        btn_CW2 = QPushButton(self)
        btn_CW2.setText('Next: Morphology')
        btn_CW2.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_CW2.setFixedSize(button_size[0] + 80, button_size[1])
        btn_CW2.move(quit_loc[0] - 40, quit_loc[1] + button_vertical_dis)
        btn_CW2.clicked.connect(self.ChangeWin2)

        button_index = 0

        # button -- imread
        btn_ir = QPushButton(self)
        btn_ir.setText('Open Image')
        btn_ir.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_ir.setFixedSize(button_size[0], button_size[1])
        btn_ir.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_ir.clicked.connect(self.openimage)
        button_index += 1

        # Edge Detection
        ED_loc = start_button_loc[1]+2*button_vertical_dis
        self.label_ED2txt = QLabel(self)
        self.label_ED2txt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_ED2txt.move(start_button_loc[0], ED_loc+button_index*button_vertical_dis)
        self.label_ED2txt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_ED2txt.setText('Edge Detection:')
        button_index += 1

        # button -- Edge Detection -- Roberts
        btn_E_R = QPushButton(self)
        btn_E_R.setText('Roberts')
        btn_E_R.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_E_R.setFixedSize(button_size[0], button_size[1])
        btn_E_R.move(start_button_loc[0], ED_loc + button_index * button_vertical_dis)
        btn_E_R.clicked.connect(self.ED_Roberts)
        button_index += 1

        # button -- Edge Detection -- Prewitt
        btn_E_P = QPushButton(self)
        btn_E_P.setText('Prewitt')
        btn_E_P.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_E_P.setFixedSize(button_size[0], button_size[1])
        btn_E_P.move(start_button_loc[0], ED_loc+button_index*button_vertical_dis)
        btn_E_P.clicked.connect(self.ED_Prewitt)
        button_index += 1

        # button -- Edge Detection -- Sobel
        btn_E_S = QPushButton(self)
        btn_E_S.setText('Sobel')
        btn_E_S.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_E_S.setFixedSize(button_size[0], button_size[1])
        btn_E_S.move(start_button_loc[0], ED_loc+button_index*button_vertical_dis)
        btn_E_S.clicked.connect(self.ED_Sobel)
        button_index += 1

        # Blur
        Bl_loc = start_button_loc[1]+3*button_vertical_dis
        self.label_Bltxt = QLabel(self)
        self.label_Bltxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Bltxt.move(start_button_loc[0], Bl_loc + button_index * button_vertical_dis)
        self.label_Bltxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Bltxt.setText('Blur:')
        button_index += 1

        # button -- blur -- Gaussian
        btn_B_G = QPushButton(self)
        btn_B_G.setText("Gaussian")
        btn_B_G.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_B_G.setFixedSize(button_size[0], button_size[1])
        btn_B_G.move(start_button_loc[0], Bl_loc+button_index*button_vertical_dis)
        btn_B_G.clicked.connect(self.B_Gus)
        button_index += 1

        # button -- blur -- Median
        btn_B_M = QPushButton(self)
        btn_B_M.setText("Median")
        btn_B_M.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_B_M.setFixedSize(button_size[0], button_size[1])
        btn_B_M.move(start_button_loc[0], Bl_loc+button_index*button_vertical_dis)
        btn_B_M.clicked.connect(self.B_Med)
        button_index += 2

        # button -- DIY convolution
        btn_DIY = QPushButton(self)
        btn_DIY.setText("DIY Convolution")
        btn_DIY.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_DIY.setFixedSize(button_size[0], button_size[1])
        btn_DIY.move(start_button_loc[0], Bl_loc+button_index*button_vertical_dis)
        btn_DIY.clicked.connect(self.DIY_Conv)

    # function--------------------------------------------------

    def ChangeWin2(self):
        self.hide()
        self.DE = DEwin()
        self.DE.show()

    # open image button-pushed event
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "Open Image", "", "All Files(*);;*.jpg;;*.png")
        img = QtGui.QPixmap(imgName).scaled(
            self.label_OriPic.width(),
            self.label_OriPic.height())
        Image = cv2.imread(imgName)
        self.label_fiilename.setText(imgName)
        self.img_gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('Gray',img_gray)

        # cv img convert to QImage
        QApplication.processEvents()
        height, width = self.img_gray.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            self.img_gray.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_GrayPic.width(),
            self.label_GrayPic.height())
        self.label_OriPic.setPixmap(img)
        self.label_GrayPic.setPixmap(pixmap_Gray)

    # Edge Detection - Roberts
    def ED_Roberts(self):
        Roberts_1 = np.array(([-1, 0], [0, 1]))
        Roberts_2 = np.array(([0, -1], [1, 0]))
        # 不对称卷积核旋转180度
        Roberts_1 = np.rot90(Roberts_1, 2)
        Roberts_2 = np.rot90(Roberts_2, 2)

        Img_ED_R1 = cv2.filter2D(self.img_gray, -1, Roberts_1)
        Img_ED_R2 = cv2.filter2D(self.img_gray, -1, Roberts_2)

        Img_ED_R = Img_ED_R1 + Img_ED_R2

        # show in label
        QApplication.processEvents()
        height, width = Img_ED_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Img_ED_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_ED.width(), self.label_ED.height())
        self.label_ED.setPixmap(pixmap_Gray)
        self.label_EDtxt.setText('Roberts')

    # Edge Detection - Prewitt
    def ED_Prewitt(self):
        Prewitt1 = np.array(([-1, -1, -1], [0, 0, 0], [1, 1, 1]))
        Prewitt2 = np.array(([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))

        # 卷积核旋转
        Prewitt1 = np.rot90(Prewitt1, 2)
        Prewitt2 = np.rot90(Prewitt2, 2)

        Img_ED_P1 = cv2.filter2D(self.img_gray, -1, Prewitt1)
        Img_ED_P2 = cv2.filter2D(self.img_gray, -1, Prewitt2)

        Img_ED_P = Img_ED_P1 + Img_ED_P2

        # show
        QApplication.processEvents()
        height, width = Img_ED_P.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Img_ED_P.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_ED.width(), self.label_ED.height())
        self.label_ED.setPixmap(pixmap_Gray)
        self.label_EDtxt.setText('Prewitt')

    # Edge Detection - Sobel
    def ED_Sobel(self):
        Sobel1 = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]))
        Sobel2 = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]))

        # 卷积核旋转
        Sobel1 = np.rot90(Sobel1, 2)
        Sobel2 = np.rot90(Sobel2, 2)

        Img_ED_S1 = cv2.filter2D(self.img_gray, -1, Sobel1)
        Img_ED_S2 = cv2.filter2D(self.img_gray, -1, Sobel2)

        Img_ED_S = Img_ED_S1 + Img_ED_S2

        # show
        QApplication.processEvents()
        height, width = Img_ED_S.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Img_ED_S.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_ED.width(), self.label_ED.height())
        self.label_ED.setPixmap(pixmap_Gray)
        self.label_EDtxt.setText('Sobel')

    # Blur - Gaussian filter
    def B_Gus(self):
        size, ok1 = QInputDialog.getText(
            self, "Input Guassian Filter Size", "Size:")
        if ok1:
            size = int(size)
            delta, ok2 = QInputDialog.getText(
                self, "Input Variance", "Varience:")
            if ok2:
                delta = float(delta)

                Img_B_G = cv2.GaussianBlur(self.img_gray, (size, size), delta)

                # show
                QApplication.processEvents()
                height, width = Img_B_G.shape
                bytesPerLine = width
                QImg_Gray = QImage(
                    Img_B_G.data,
                    width,
                    height,
                    bytesPerLine,
                    QImage.Format_Grayscale8)
                pixmap_Gray = QPixmap.fromImage(QImg_Gray)
                pixmap_Gray = pixmap_Gray.scaled(
                    self.label_ED.width(), self.label_ED.height())
                self.label_NR.setPixmap(pixmap_Gray)
                self.label_NRtxt.setText('Gaussian')

    # Blur - Median filter
    def B_Med(self):
        size, ok = QInputDialog.getText(self, "Input Filter Size", "Size:")
        if ok:
            size = int(size)
            Med = np.ones(size)
            Med = Med / size
            Img_B_M = cv2.filter2D(self.img_gray, -1, Med)

            # show
            QApplication.processEvents()
            height, width = Img_B_M.shape
            bytesPerLine = width
            QImg_Gray = QImage(
                Img_B_M.data,
                width,
                height,
                bytesPerLine,
                QImage.Format_Grayscale8)
            pixmap_Gray = QPixmap.fromImage(QImg_Gray)
            pixmap_Gray = pixmap_Gray.scaled(
                self.label_ED.width(), self.label_ED.height())
            self.label_NR.setPixmap(pixmap_Gray)
            self.label_NRtxt.setText('Median')

    # Convlution with DIY Filter
    def DIY_Conv(self):
        size, ok = QInputDialog.getText(self, "Input Your Size (x*x)", "Size:")
        if ok:
            size = int(size)

            # input a matrix
            num_len = size * size
            filter = np.empty([1, num_len], dtype=float)
            for i in range(num_len):
                filter[0][i], ok = QInputDialog.getText(
                    self, "Input Matrix", "A element in matrix:")
                if ok:
                    continue
                else:
                    break

            filter = np.reshape(filter, [size, size])
            filter = np.rot90(filter, 2)
            # print(filter)
            Img_DIY_Conv = cv2.filter2D(self.img_gray, -1, filter)

            # show
            QApplication.processEvents()
            height, width = Img_DIY_Conv.shape
            bytesPerLine = width
            QImg_Gray = QImage(
                Img_DIY_Conv.data,
                width,
                height,
                bytesPerLine,
                QImage.Format_Grayscale8)
            pixmap_Gray = QPixmap.fromImage(QImg_Gray)
            pixmap_Gray = pixmap_Gray.scaled(
                self.label_ED.width(), self.label_ED.height())
            self.label_NR.setPixmap(pixmap_Gray)
            self.label_NRtxt.setText('DIY Convlution')
