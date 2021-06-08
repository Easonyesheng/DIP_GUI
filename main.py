# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 15:45
# @Author  : tangxl
# @FileName: main.py
# @Software: PyCharm
"""
主程序
界面定义，图片读取+灰度图转换
"""
import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from utils import ToolsGet
from Win2_Convolution import Convolution
from settings import *


# 界面对象 -- project 1 Window
class picture(QMainWindow):
    def __init__(self):
        super(picture, self).__init__()

        # image
        self.Image = []
        # for show
        self.path = './temp/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        # window
        self.resize(big_window_size[0], big_window_size[1])
        self.setWindowTitle('Histogram')

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

        # label4 -- Histogram
        self.label_His = QLabel(self)
        self.label_His.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_His.move(sub_window_loc_ld[0], sub_window_loc_ld[1])
        self.label_His.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_Histxt = QLabel(self)
        self.label_Histxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_Histxt.move(sub_window_loc_ld[0]+title_dis[0], sub_window_loc_ld[1]+title_dis[1])
        self.label_Histxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_Histxt.setAlignment(Qt.AlignCenter)
        self.label_Histxt.setText('Histogram')

        # label5 -- Threshold Way
        self.label_TH = QLabel(self)
        self.label_TH.setFixedSize(sub_window_size[0], sub_window_size[1])
        self.label_TH.move(sub_window_loc_rd[0], sub_window_loc_rd[1])
        self.label_TH.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        self.label_THtxt = QLabel(self)
        self.label_THtxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_THtxt.move(sub_window_loc_rd[0]+title_dis[0], sub_window_loc_rd[1]+title_dis[1])
        self.label_THtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_THtxt.setAlignment(Qt.AlignCenter)
        self.label_THtxt.setText('Threshold')

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
        btn_CW = QPushButton(self)
        btn_CW.setText('Next: Convolution')
        btn_CW.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_CW.setFixedSize(button_size[0] + 80, button_size[1])
        btn_CW.move(quit_loc[0] - 40, quit_loc[1] + button_vertical_dis)
        btn_CW.clicked.connect(self.ChangeWin)

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

        thrd_loc = start_button_loc[1]+8*button_vertical_dis
        # label6 -- 'Threshold Ways' txt
        self.label_THretxt = QLabel(self)
        self.label_THretxt.move(start_button_loc[0], thrd_loc+button_index*button_vertical_dis)
        self.label_THretxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        self.label_THretxt.setFixedSize(label_fixsize[0], label_fixsize[1])
        self.label_THretxt.setText('Threshold Ways:')
        button_index += 1

        # button -- OTSU
        btn_OS = QPushButton(self)
        btn_OS.setText('OTSU')
        btn_OS.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_OS.setFixedSize(button_size[0], button_size[1])
        btn_OS.move(start_button_loc[0], thrd_loc + button_index * button_vertical_dis)
        btn_OS.clicked.connect(self.OTSUSET)
        button_index += 1
        # label7 -- OTSU threshold txt
        self.label_OStxt = QLabel(self)
        self.label_OStxt.setFixedSize(button_size[0], button_size[1])
        self.label_OStxt.move(start_button_loc[0], thrd_loc+button_index*button_vertical_dis-10)
        self.label_OStxt.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        button_index += 1

        # button -- entropy
        btn_En = QPushButton(self)
        btn_En.setText('Entropy')
        btn_En.setStyleSheet(
            "QPushButton{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        btn_En.setFixedSize(button_size[0], button_size[1])
        btn_En.move(start_button_loc[0], thrd_loc + button_index * button_vertical_dis)
        btn_En.clicked.connect(self.EntroSET)
        button_index += 1
        # label8 -- Entropy threshold txt
        self.label_ETtxt = QLabel(self)
        self.label_ETtxt.setFixedSize(button_size[0], button_size[1])
        self.label_ETtxt.move(start_button_loc[0], thrd_loc + button_index * button_vertical_dis-10)
        self.label_ETtxt.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")
        button_index += 1

        # gray threshold
        self.label_GVtxt = QLabel(self)
        self.label_GVtxt.move(start_button_loc[0], thrd_loc + button_index * button_vertical_dis)
        self.label_GVtxt.setFixedSize(button_size[0], button_size[1])
        self.label_GVtxt.setText('Gray Threshold:')
        self.label_GVtxt.setStyleSheet(
            "QLabel{color:rgb(20,20,20);font-size:36px;font-family:Times New Roman;}")
        button_index += 1

        # slide -- change the sheld value
        sld_Gray = QSlider(Qt.Horizontal, self)
        sld_Gray.setFocusPolicy(Qt.NoFocus)
        sld_Gray.setFixedSize(button_size[0], button_size[1]/2)
        sld_Gray.move(start_button_loc[0], thrd_loc + button_index * button_vertical_dis-10)
        sld_Gray.valueChanged[int].connect(self.changeGray)
        button_index += 1

        # label9 -- gray thresheld show
        self.label_GrayValue = QLabel(self)
        self.label_GrayValue.setFixedSize(button_size[0], button_size[1])
        self.label_GrayValue.move(start_button_loc[0], thrd_loc + button_index * button_vertical_dis-30)
        self.label_GrayValue.setStyleSheet(
            "QLabel{background:white}"
            "QLabel{color:rgb(20,20,20);font-size:36px;font-weight:bold;font-family:Times New Roman;}")

    # Function --------------------------------------------------------

    def ChangeWin(self):
        self.hide()
        self.Con = Convolution()
        self.Con.show()

    # open image button-pushed event
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(
            self, "Open Image", "", "*.jpg;;*.png;;All Files(*)")
        img = QtGui.QPixmap(imgName).scaled(
            self.label_OriPic.width(),
            self.label_OriPic.height())

        Image = cv2.imread(imgName)
        # cv2.imshow('Gray', IMQ)
        # print(type(Image))
        self.label_fiilename.setText(imgName)
        self.img_gray = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)

        # cv img convert to QImage
        '''
        PyQt5 显示灰度图
        用cv去读取图片
        通过cv转换为灰度图
        从cv转换到QImage-->QPixmap
        '''
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
        # imgGray = RGB2Gray(img)
        # self.label_GrayPic.setPixmap(imgGray)
        '''
        调用His得到灰度直方图
        存储，再读出显示在GUI上
        '''
        ToolsGet.His(self.img_gray, self.path+'/his.png')
        Hisimg = cv2.imread(self.path+'/his.png')
        # cv2.imshow('H',Hisimg)
        Hisheight, Hiswidth, HisbytesPerComponent = Hisimg.shape
        HisbytesPerLine = 3 * Hiswidth
        Hisimg = cv2.cvtColor(Hisimg, cv2.COLOR_BGR2RGB)
        QImg_His = QImage(
            Hisimg.data,
            Hiswidth,
            Hisheight,
            HisbytesPerLine,
            QImage.Format_RGB888)
        pixmap_His = QPixmap.fromImage(QImg_His)
        pixmap_His = pixmap_His.scaled(
            self.label_His.width(),
            self.label_His.height())
        self.label_His.setPixmap(pixmap_His)

    # change the slide value then change the gray sheld
    # value: 0-100
    def changeGray(self, value):
        # show text
        self.Gray = int(value / 100 * 258)
        self.label_GrayValue.setText(str(self.Gray))
        # get image
        # Gc -- Gray change
        imgtemp = self.img_gray
        otsu, GcImage = cv2.threshold(
            imgtemp, self.Gray, 255, cv2.THRESH_BINARY)
        Gcheight, Gcwidth = GcImage.shape
        GcBytesPerLine = Gcwidth
        QImg_Gc = QImage(
            GcImage.data,
            Gcwidth,
            Gcheight,
            GcBytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_Gc = QPixmap.fromImage(QImg_Gc)
        pixmap_Gc = pixmap_Gc.scaled(
            self.label_TH.width(),
            self.label_TH.height())
        self.label_TH.setPixmap(pixmap_Gc)
        self.label_THtxt.setText('Threshold')

    # OTSU button pushed and get the result and show
    # OS = OTSU
    def OTSUSET(self):
        self.label_GrayValue.setText("")
        T = ToolsGet.OTSU(self.img_gray)
        self.label_OStxt.setText(str(T))
        ot, OSimg = cv2.threshold(self.img_gray, T, 255, cv2.THRESH_BINARY)
        QApplication.processEvents()
        OSheight, OSwidth = OSimg.shape
        OSBytesPerLine = OSwidth
        Qimg_OS = QImage(
            OSimg.data,
            OSwidth,
            OSheight,
            OSBytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_OS = QPixmap.fromImage(Qimg_OS)
        pixmap_OS = pixmap_OS.scaled(
            self.label_TH.width(),
            self.label_TH.height())
        self.label_TH.setPixmap(pixmap_OS)
        self.label_THtxt.setText('OTSU')

    # Entropy button pushed and get the result and show
    # EN = Entropy
    def EntroSET(self):
        T = ToolsGet.Entropy(self.img_gray)
        self.label_ETtxt.setText(str(T))
        ot, ENimg = cv2.threshold(self.img_gray, T, 255, cv2.THRESH_BINARY)
        QApplication.processEvents()
        ENheight, ENwidth = ENimg.shape
        ENBytesPerLine = ENwidth
        Qimg_EN = QImage(
            ENimg.data,
            ENwidth,
            ENheight,
            ENBytesPerLine,
            QImage.Format_Grayscale8)
        pixmap_EN = QPixmap.fromImage(Qimg_EN)
        pixmap_EN = pixmap_EN.scaled(
            self.label_TH.width(),
            self.label_TH.height())
        self.label_TH.setPixmap(pixmap_EN)
        self.label_THtxt.setText('Entropy')


if __name__ == "__main__":
    # QtCore.QCoreApplication.setLibraryPaths("")
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()

    sys.exit(app.exec_())
