# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 8:47
# @Author  : tangxl
# @FileName: Win3_DE.py
# @Software: PyCharm
"""
Project 3 Window
aimed at doing the image erosion and dialation
And Open, Close
distance transform & skeleton get
"""

import os
import cv2
import numpy as np
import time
import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from utils.Distance_Skeleton import *
from Win4_GrayDE import GDEWin
from settings import *


class DEwin(QWidget):
    def __init__(self):
        super(DEwin, self).__init__()

        # for show
        self.path = './temp/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        # SE default
        self.SE = np.ones([5, 5], dtype='bool')

        # Window
        self.resize(big_window_size[0], big_window_size[1])
        self.setWindowTitle('Morphology')
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

        # label3 -- basic operation
        self.label_BO = QLabel(self)
        self.label_BO.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_BO.move(sub_window_loc_ru[0], sub_window_loc_ru[1])
        self.label_BO.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_BOtxt = QLabel(self)
        self.label_BOtxt.setFixedSize(label_fixsize[0]+80, label_fixsize[1])
        self.label_BOtxt.move(sub_window_loc_ru[0]+title_dis[0]-40, sub_window_loc_ru[1]+title_dis[1])
        self.label_BOtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_BOtxt.setAlignment(Qt.AlignCenter)
        self.label_BOtxt.setText('Basic Morphology Operation')

        # label4 -- skeleton
        self.count = 0
        self.label_S = QLabel(self)
        self.label_S.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_S.move(sub_window_loc_ld[0], sub_window_loc_ld[1])
        self.label_S.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_Stxt = QLabel(self)
        self.label_Stxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Stxt.move(sub_window_loc_ld[0]+title_dis[0], sub_window_loc_ld[1]+title_dis[1])
        self.label_Stxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Stxt.setAlignment(Qt.AlignCenter)
        self.label_Stxt.setText('Skeleton')

        # label5 -- distance
        self.label_D = QLabel(self)
        self.label_D.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_D.move(sub_window_loc_rd[0], sub_window_loc_rd[1])
        self.label_D.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_Dtxt = QLabel(self)
        self.label_Dtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Dtxt.move(sub_window_loc_rd[0] + title_dis[0], sub_window_loc_rd[1] + title_dis[1])
        self.label_Dtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Dtxt.setAlignment(Qt.AlignCenter)
        self.label_Dtxt.setText('Distance')

        # button ---------------------------------------------------
        # button -- quit
        btn_q = QPushButton(self)
        btn_q.setText('Quit')
        btn_q.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_q.setFixedSize(button_size[0], button_size[1])
        btn_q.move(quit_loc[0], quit_loc[1])
        btn_q.clicked.connect(QCoreApplication.instance().quit)

        # button -- change window
        btn_CW3 = QPushButton(self)
        btn_CW3.setText('Next: Gray Morphology')
        btn_CW3.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_CW3.setFixedSize(button_size[0]+80, button_size[1])
        btn_CW3.move(quit_loc[0]-40, quit_loc[1]+button_vertical_dis)
        btn_CW3.clicked.connect(self.ChangeWin3)

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

        # label -- time
        self.label_Ttxt = QLabel(self)
        self.label_Ttxt.setFixedSize(button_size[0], button_size[1])
        self.label_Ttxt.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        self.label_Ttxt.setText('Time:')
        self.label_Ttxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")

        self.label_T = QLabel(self)
        self.label_T.move(start_button_loc[0]+button_size[0]-file_txt_size[0],
                          start_button_loc[1]+button_index*button_vertical_dis)
        self.label_T.setFixedSize(file_txt_size[0], file_txt_size[1])
        self.label_T.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        button_index += 1

        # Basic Operation -----------------------------------------
        # label -- 'Basic Operation' txt
        self.label_titile_BOtxt = QLabel(self)
        self.label_titile_BOtxt.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis+20)
        self.label_titile_BOtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_titile_BOtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_titile_BOtxt.setText('Basic Operation:')
        button_index += 1

        # label -- SE
        self.label_SEtxt = QLabel(self)
        self.label_SEtxt.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        self.label_SEtxt.setFixedSize(button_size[0], button_size[1])
        self.label_SEtxt.setText('SE size:')
        self.label_SEtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")

        self.label_SEvalue = QLabel(self)
        self.label_SEvalue.move(start_button_loc[0] + button_size[0] - 100,
                                start_button_loc[1] + button_index * button_vertical_dis)
        self.label_SEvalue.setFixedSize(100, file_txt_size[1])
        self.label_SEvalue.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_SEvalue.setText('%d' % self.SE.shape[0])
        button_index += 1

        # button -- SE get
        btn_SGget = QPushButton(self)
        btn_SGget.setText('get SE')
        btn_SGget.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_SGget.setFixedSize(button_size[0], button_size[1])
        btn_SGget.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_SGget.clicked.connect(self.SEget)
        button_index += 1

        # button -- Basic Operation -- Dilation
        btn_DI = QPushButton(self)
        btn_DI.setText('Dilation')
        btn_DI.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_DI.setFixedSize(button_size[0], button_size[1])
        btn_DI.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_DI.clicked.connect(self.Dilation)
        button_index += 1

        # button -- Basic Operation -- Erosion
        btn_E = QPushButton(self)
        btn_E.setText('Erosion')
        btn_E.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_E.setFixedSize(button_size[0], button_size[1])
        btn_E.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_E.clicked.connect(self.Erosion)
        button_index += 1

        # button -- Basic Operation -- Open
        btn_O = QPushButton(self)
        btn_O.setText('Opening')
        btn_O.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_O.setFixedSize(button_size[0], button_size[1])
        btn_O.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_O.clicked.connect(self.Open)
        button_index += 1

        # button -- Basic Operation -- Close
        btn_C = QPushButton(self)
        btn_C.setText('Closing')
        btn_C.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_C.setFixedSize(button_size[0], button_size[1])
        btn_C.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_C.clicked.connect(self.Close)
        button_index += 2

        # button -- skeleton get
        btn_SK = QPushButton(self)
        btn_SK.setText('Skeleton')
        btn_SK.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_SK.setFixedSize(button_size[0], button_size[1])
        btn_SK.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_SK.clicked.connect(self.SKeleWin)
        button_index += 1

        # button -- internal edge
        btn_IE = QPushButton(self)
        btn_IE.setText('Internal Edge')
        btn_IE.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_IE.setFixedSize(button_size[0], button_size[1])
        btn_IE.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_IE.clicked.connect(self.InEdge)
        button_index += 1

        # button -- external egde
        btn_EE = QPushButton(self)
        btn_EE.setText('External Edge')
        btn_EE.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_EE.setFixedSize(button_size[0], button_size[1])
        btn_EE.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_EE.clicked.connect(self.ExEdge)
        button_index += 1

        # button -- standard edge
        btn_StdE = QPushButton(self)
        btn_StdE.setText('Standard Edge')
        btn_StdE.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_StdE.setFixedSize(button_size[0], button_size[1])
        btn_StdE.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis)
        btn_StdE.clicked.connect(self.StaEdge)
        button_index += 2

        # button -- Distance Transform
        btn_DT = QPushButton(self)
        btn_DT.setText('Distance Transfrom')
        btn_DT.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_DT.setFixedSize(button_size[0], button_size[1])
        btn_DT.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_DT.clicked.connect(self.DisTransWin)
        button_index += 1

        # button -- Conditional Dilation
        btn_CD = QPushButton(self)
        btn_CD.setText('Conditional Dilation')
        btn_CD.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_CD.setFixedSize(button_size[0], button_size[1])
        btn_CD.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_CD.clicked.connect(self.Con_Dia)

    # function--------------------------------------------------

    def ChangeWin3(self):
        self.hide()
        self.GDE = GDEWin()
        self.GDE.show()

    # open image button-pushed event
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "Open Binary Image", "", "All Files(*);;*.jpg;;*.png")
        img = QtGui.QPixmap(imgName).scaled(
            self.label_OriPic.width(),
            self.label_OriPic.height())
        Image = cv2.imread(imgName, -1)
        self.label_fiilename.setText(imgName)
        if len(Image.shape) != 2:
            self.img_gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        else:
            self.img_gray = Image
        # 转化为二值图像
        none, self.img_gray = cv2.threshold(self.img_gray, 0, 255, cv2.THRESH_BINARY)
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
            self.label_OriPic.width(),
            self.label_OriPic.height())
        self.label_OriPic.setPixmap(pixmap_Gray)

    # get SE size
    def SEget(self):
        size, ok = QInputDialog.getText(self, "Input Your SE Size", "SE Size:")
        if ok:
            size = int(size)
            self.SE = np.ones([size, size], dtype='bool')
            self.label_SEvalue.setText('%d' % size)

    # Dialate button pushed
    def Dilation(self):
        """
        # input your SE
        size, ok = QInputDialog.getText(self, "Input Your SE Size", "SE Size:")
        if ok :
            size = int(size)

            # input a matrix
            num_len = size*size
            SE = np.empty([1,num_len], dtype = float)
            for i in range(num_len):
                SE[0][i], ok = QInputDialog.getText(self, "Input SE Matrix", "A element in matrix:")
                if ok:
                    continue
                else:
                    break

            SE = np.reshape(SE,[size,size])
            SE = SE.astype(bool)
        """
        # use defalut SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_DR = DilationGet(self.img_gray, SE)
        toc = time.time()
        none, Img_DR_b = cv2.threshold(Img_DR, 0, 255, cv2.THRESH_BINARY)
        height, width = Img_DR.shape
        # save & read to solve the pixmap_show_problem

        name = self.path + 'Dia2.jpg'
        cv2.imwrite(name, Img_DR_b)
        Im_show = cv2.imread(name, -1)
        QApplication.processEvents()
        bytesPerLine = width
        QImg_D = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(
            self.label_BO.width(),
            self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Dilation')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    def Erosion(self):
        """
        #input your SE

        size, ok = QInputDialog.getText(self, "Input Your SE Size", "SE Size:")
        if ok :
            size = int(size)

            # input a matrix
            num_len = size*size
            SE = np.empty([1,num_len], dtype = float)
            for i in range(num_len):
                SE[0][i], ok = QInputDialog.getText(self, "Input SE Matrix", "A element in matrix:")
                if ok:
                    continue
                else:
                    break

            SE = np.reshape(SE,[size,size])
            SE = SE.astype(bool)
        """
        # use default SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_ER = ErosionGet(self.img_gray, SE)
        toc = time.time()
        none, Img_ER_b = cv2.threshold(Img_ER, 0, 255, cv2.THRESH_BINARY)

        # save & read to solve the pixmap_show_problem

        name = self.path + 'Ero2.jpg'
        cv2.imwrite(name, Img_ER_b)
        Im_show = cv2.imread(name, -1)

        QApplication.processEvents()
        height, width = Img_ER.shape
        bytesPerLine = width
        QImg_D = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(
            self.label_BO.width(),
            self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Erosion')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    def Open(self):
        # use default SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_ER = ErosionGet(self.img_gray, SE)
        none, Img_ER = cv2.threshold(Img_ER, 0, 255, cv2.THRESH_BINARY)
        Img_ER_DR = DilationGet(Img_ER, SE)
        toc = time.time()
        none, Img_ER_DR = cv2.threshold(Img_ER_DR, 0, 255, cv2.THRESH_BINARY)

        name = self.path + 'Open.jpg'
        cv2.imwrite(name, Img_ER_DR)
        Im_show = cv2.imread(name, -1)
        QApplication.processEvents()
        height, width = Img_ER.shape
        bytesPerLine = width
        QImg_D = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(
            self.label_BO.width(),
            self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Opening')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    def Close(self):
        # use default SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_DR = DilationGet(self.img_gray, SE)
        none, Img_DR = cv2.threshold(Img_DR, 0, 255, cv2.THRESH_BINARY)
        Img_DR_ER = ErosionGet(Img_DR, SE)
        toc = time.time()
        none, Img_DR_ER = cv2.threshold(Img_DR_ER, 0, 255, cv2.THRESH_BINARY)

        name = self.path + 'Close.jpg'
        cv2.imwrite(name, Img_DR_ER)
        Im_show = cv2.imread(name, -1)
        QApplication.processEvents()
        height, width = Img_DR_ER.shape
        bytesPerLine = width
        QImg_D = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(
            self.label_BO.width(),
            self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Closing')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    def DisTransWin(self):
        tic = time.time()
        Img_R = DisTrans(self.img_gray)
        toc = time.time()
        name = os.path.join(self.path, 'DisTrans.jpg')
        cv2.imwrite(name, Img_R)

        # show
        Im_show = cv2.imread(name, -1)
        QApplication.processEvents()
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_D.width(), self.label_D.height())
        self.label_D.setPixmap(pixmap_Gray)
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    def SKeleWin(self):
        tic = time.time()
        Img_R, self.count = SkeGet(self.img_gray)
        toc = time.time()

        name = self.path + 'SKeleton.jpg'
        cv2.imwrite(name, Img_R)

        # show
        QApplication.processEvents()
        Im_show = cv2.imread(name, -1)
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_S.width(), self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    def InEdge(self):
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        Img_ER = ErosionGet(self.img_gray, SE)
        none, Img_ER = cv2.threshold(Img_ER, 0, 255, cv2.THRESH_BINARY)
        Img_R = self.img_gray - Img_ER
        name = self.path + 'InE.jpg'
        cv2.imwrite(name, Img_R)

        # show
        QApplication.processEvents()
        Im_show = cv2.imread(name, -1)
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_S.width(), self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)
        self.label_Stxt.setText('Internal Edge')

    def ExEdge(self):
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        Img_DR = DilationGet(self.img_gray, SE)
        none, Img_DR = cv2.threshold(Img_DR, 0, 255, cv2.THRESH_BINARY)
        Img_R = Img_DR - self.img_gray
        name = self.path + 'ExE.jpg'
        cv2.imwrite(name, Img_R)

        # show
        QApplication.processEvents()
        Im_show = cv2.imread(name, -1)
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_S.width(), self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)
        self.label_Stxt.setText('External Edge')

    def StaEdge(self):
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        Img_ER = ErosionGet(self.img_gray, SE)
        none, Img_ER = cv2.threshold(Img_ER, 0, 255, cv2.THRESH_BINARY)
        Img_DR = DilationGet(self.img_gray, SE)
        none, Img_DR = cv2.threshold(Img_DR, 0, 255, cv2.THRESH_BINARY)
        Img_R = Img_DR - Img_ER
        name = self.path + 'StaE.jpg'
        cv2.imwrite(name, Img_R)

        # show
        QApplication.processEvents()
        Im_show = cv2.imread(name, -1)
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            Im_show.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_S.width(), self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)

    # Conditional Dilation
    def Con_Dia(self):
        size, ok = QInputDialog.getText(self, "Input 0~1", "LineLocation:")
        if ok:
            SE = np.ones([11, 11], dtype='bool')
            w, h = self.img_gray.shape
            '''
            input lines waiting codes
            '''
            line = float(size)
            if line > 1 or line < 0:
                print('Input Error')
                return -1
            img_line = np.zeros([w, h], dtype='int')
            img_line[:, int(h * line)] = 255
            cv2.imwrite(self.path + 'line.jpg', img_line)
            # show line img
            Im_show = cv2.imread(self.path + 'line.jpg', 0)
            height, width = Im_show.shape
            bytesPerLine = width
            QImg_Gray = QImage(
                Im_show.data,
                width,
                height,
                bytesPerLine,
                QImage.Format_Grayscale8)
            pixmap_Gray = QPixmap.fromImage(QImg_Gray)
            pixmap_Gray = pixmap_Gray.scaled(
                self.label_S.width(), self.label_S.height())
            self.label_S.setPixmap(pixmap_Gray)
            self.label_Stxt.setText('Line')

            # conditional dialate
            temp = np.zeros([w, h], dtype='int')
            c = 0
            img_grayt = self.img_gray.astype(np.bool)
            # print(img_grayt.dtype)
            a = 0
            b = 0
            tic = time.time()
            while (True):
                # print(c)
                img_line = DilationGet(img_line, SE).astype(np.int)
                temp = img_line.copy()
                # print(temp.dtype)
                # temp = temp.astype(np.int)
                # img_line = img_line.astype(np.bool)
                img_line = img_line & img_grayt  # 0 & 1
                img_line = img_line.astype(np.int)
                # print(img_line.dtype)

                c += 1
                # print((temp == img_line).all())
                res = temp == img_line
                a = np.sum(res == False)
                if (a == b):
                    break
                b = a

            img_l = img_line * 255
            toc = time.time()
            # cv2.imwrite(self.path+'/ConD/'+str(c)+'.jpg',img_l)
            if not os.path.exists(os.path.join(self.path, 'ConD')):
                os.mkdir(os.path.join(self.path, 'ConD'))
            cv2.imwrite(os.path.join(self.path, 'ConD', str(c) + '.jpg'), img_l)

            # show img_R
            QApplication.processEvents()
            Im_show = cv2.imread(os.path.join(self.path, 'ConD', str(c) + '.jpg'), 0)
            height, width = Im_show.shape
            bytesPerLine = width
            QImg_Gray = QImage(
                Im_show.data,
                width,
                height,
                bytesPerLine,
                QImage.Format_Grayscale8)
            pixmap_Gray = QPixmap.fromImage(QImg_Gray)
            pixmap_Gray = pixmap_Gray.scaled(
                self.label_D.width(), self.label_D.height())
            self.label_D.setPixmap(pixmap_Gray)
            self.label_Dtxt.setText('Conditional Dialation')
            self.label_T.setText('%d ms' % int(1000*(toc-tic)))
