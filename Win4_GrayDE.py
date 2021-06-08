# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 23:43
# @Author  : tangxl
# @FileName: Win4_GrayDE.py
# @Software: PyCharm
"""
project 4 window
Gray Morphology
open close erosion dilation
edge detection
reconstruction
gradient
"""

import os
import cv2
import numpy as np
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from utils.GMorphology import *
from settings import *


class GDEWin(QWidget):
    def __init__(self):
        super(GDEWin, self).__init__()

        # for show
        self.path = './temp/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        # SE default
        self.SE = np.ones([5, 5], dtype='bool')

        # Window
        self.resize(big_window_size[0], big_window_size[1])
        self.setWindowTitle('Gray Morphology')
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
            "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:Times New Roman;}")
        self.label_BOtxt = QLabel(self)
        self.label_BOtxt.setFixedSize(label_fixsize[0]+40, label_fixsize[1])
        self.label_BOtxt.move(sub_window_loc_ru[0]+title_dis[0]-20, sub_window_loc_ru[1]+title_dis[1])
        self.label_BOtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_BOtxt.setAlignment(Qt.AlignCenter)
        self.label_BOtxt.setText('Gray Morphology Operation')

        # label4 -- Gary Reconstruction
        self.label_GR = QLabel(self)
        self.label_GR.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_GR.move(sub_window_loc_ld[0], sub_window_loc_ld[1])
        self.label_GR.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:Times New Roman;}")
        self.label_GRtxt = QLabel(self)
        self.label_GRtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_GRtxt.move(sub_window_loc_ld[0]+title_dis[0], sub_window_loc_ld[1]+title_dis[1])
        self.label_GRtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_GRtxt.setAlignment(Qt.AlignCenter)
        self.label_GRtxt.setText('Gray Reconstruction')

        # label5 -- Gradient
        self.count = 0
        self.label_G = QLabel(self)
        self.label_G.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_G.move(sub_window_loc_rd[0], sub_window_loc_rd[1])
        self.label_G.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:Times New Roman;}")
        self.label_Gtxt = QLabel(self)
        self.label_Gtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Gtxt.move(sub_window_loc_rd[0]+title_dis[0], sub_window_loc_rd[1]+title_dis[1])
        self.label_Gtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Gtxt.setAlignment(Qt.AlignCenter)
        self.label_Gtxt.setText('Gradient')

        # button----------------------------------------------
        # button -- quit
        btn_q = QPushButton(self)
        btn_q.setText('Quit')
        btn_q.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_q.setFixedSize(button_size[0], button_size[1])
        btn_q.move(quit_loc[0], quit_loc[1])
        btn_q.clicked.connect(QCoreApplication.instance().quit)

        button_index = 0

        # button -- imread
        btn_ir = QPushButton(self)
        btn_ir.setText('Open Image')
        btn_ir.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_ir.setFixedSize(button_size[0], button_size[1])
        btn_ir.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_ir.clicked.connect(self.openimage)
        button_index += 1

        # label -- time
        self.label_Ttxt = QLabel(self)
        self.label_Ttxt.setFixedSize(button_size[0], button_size[1])
        self.label_Ttxt.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        self.label_Ttxt.setText('Time:')
        self.label_Ttxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")

        self.label_T = QLabel(self)
        self.label_T.move(start_button_loc[0] + button_size[0] - file_txt_size[0],
                          start_button_loc[1] + button_index * button_vertical_dis)
        self.label_T.setFixedSize(file_txt_size[0], file_txt_size[1])
        self.label_T.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        button_index += 1

        # Basic Operation -----------------------------------------
        # label -- 'Basic Operation' txt
        self.label_titile_BOtxt = QLabel(self)
        self.label_titile_BOtxt.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis + 20)
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
        btn_DI.setText('Dialtion')
        btn_DI.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_DI.setFixedSize(button_size[0], button_size[1])
        btn_DI.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_DI.clicked.connect(self.GDilationWin)
        button_index += 1

        # button -- Basic Operation -- Erosion
        btn_E = QPushButton(self)
        btn_E.setText('Erosion')
        btn_E.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_E.setFixedSize(button_size[0], button_size[1])
        btn_E.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_E.clicked.connect(self.GErosionWin)
        button_index += 1

        # button -- Basic Operation -- Open
        btn_O = QPushButton(self)
        btn_O.setText('Opening')
        btn_O.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_O.setFixedSize(button_size[0], button_size[1])
        btn_O.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_O.clicked.connect(self.GOpenWin)
        button_index += 1

        # button -- Basic Operation -- Close
        btn_C = QPushButton(self)
        btn_C.setText('Closing')
        btn_C.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_C.setFixedSize(button_size[0], button_size[1])
        btn_C.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_C.clicked.connect(self.GCloseWin)
        button_index += 2

        # Reconstruction -----------------------------------------
        # label -- 'Reconstruction' txt
        self.label_titile_RCtxt = QLabel(self)
        self.label_titile_RCtxt.move(start_button_loc[0], start_button_loc[1]+button_index*button_vertical_dis+20)
        self.label_titile_RCtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_titile_RCtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_titile_RCtxt.setText('Reconstruction:')
        button_index += 1

        # button -- Reconstrution OBR
        btn_OBR = QPushButton(self)
        btn_OBR.setText('OBR')
        btn_OBR.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_OBR.setFixedSize(button_size[0], button_size[1])
        btn_OBR.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_OBR.clicked.connect(self.OBRWin)
        button_index += 1

        # button -- Reconstrution CBR
        btn_CBR = QPushButton(self)
        btn_CBR.setText('CBR')
        btn_CBR.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_CBR.setFixedSize(button_size[0], button_size[1])
        btn_CBR.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_CBR.clicked.connect(self.CBRWin)
        button_index += 2

        # label -- 'Gradient' txt
        self.label_titile_Gtxt = QLabel(self)
        self.label_titile_Gtxt.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis + 20)
        self.label_titile_Gtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_titile_Gtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_titile_Gtxt.setText('Gradient:')
        button_index += 1

        # button -- Internal Gradient
        btn_IG = QPushButton(self)
        btn_IG.setText('Internal Grad')
        btn_IG.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_IG.setFixedSize(button_size[0], button_size[1])
        btn_IG.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_IG.clicked.connect(self.InGradWin)
        button_index += 1

        # button -- External Gradient
        btn_EG = QPushButton(self)
        btn_EG.setText('External Grad')
        btn_EG.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_EG.setFixedSize(button_size[0], button_size[1])
        btn_EG.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_EG.clicked.connect(self.ExGradWin)
        button_index += 1
        # button -- standard Gradient
        btn_SG = QPushButton(self)
        btn_SG.setText('Standard Grad')
        btn_SG.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_SG.setFixedSize(button_size[0], button_size[1])
        btn_SG.move(start_button_loc[0], start_button_loc[1] + button_index * button_vertical_dis)
        btn_SG.clicked.connect(self.StaGradWin)

    # function--------------------------------------------------

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

    # Erosion Get
    def GErosionWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GErosion(self.img_gray, SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_BO.width(), self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Erosion')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    # Dilation Get
    def GDilationWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GDilation(self.img_gray, SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_BO.width(), self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Dilation')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    # opening
    def GOpenWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GOpen(self.img_gray, SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_BO.width(), self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Opening')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    # closing
    def GCloseWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GClose(self.img_gray, SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_BO.width(), self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Closing')
        self.label_T.setText('%d ms' % int(1000*(toc-tic)))

    # Internal Gradient
    def InGradWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        Img_ER = GErosion(self.img_gray, SE)
        img_R = (self.img_gray - Img_ER)
        # img_R = img_R/2 # cannot do this operation
        img_R.astype(np.int)
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_G.width(), self.label_G.height())
        self.label_G.setPixmap(pixmap_Gray)
        self.label_Gtxt.setText('Internal Gradient')

    # External Gradient
    def ExGradWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        Img_DR = GDilation(self.img_gray, SE)
        img_R = (Img_DR - self.img_gray)
        # img_R = img_R/2 # cannot do this operation
        img_R.astype(np.int)
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_G.width(), self.label_G.height())
        self.label_G.setPixmap(pixmap_Gray)
        self.label_Gtxt.setText('External Gradient')

    # Standard Gradient
    def StaGradWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        Img_DR = GDilation(self.img_gray, SE)
        Img_ER = GErosion(self.img_gray, SE)
        img_R = (Img_DR - Img_ER)
        # img_R = img_R/2 # cannot do this operation
        img_R.astype(np.int)
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_G.width(), self.label_G.height())
        self.label_G.setPixmap(pixmap_Gray)
        self.label_Gtxt.setText('Standard Gradient')

    def OBRWin(self):
        img_R = OBR(self.img_gray)

        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_G.width(), self.label_G.height())
        self.label_GR.setPixmap(pixmap_Gray)
        self.label_GRtxt.setText('OBR')

    def CBRWin(self):
        img_R = CBR(self.img_gray)

        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(
            img_R.data,
            width,
            height,
            bytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(
            self.label_G.width(), self.label_G.height())
        self.label_GR.setPixmap(pixmap_Gray)
        self.label_GRtxt.setText('CBR')
