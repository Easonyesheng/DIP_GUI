'''
project 2 window
Convlution
'''
import cv2
import numpy as np
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#from ImageInput import picture




class Convlution(QWidget):
    def __init__(self):
        super(Convlution,self).__init__()
        
        # Window
        self.resize(1200,1050)
        self.setWindowTitle('IGST-Project2')
        self.setWindowIcon(QIcon('/Users/zhangyesheng/Desktop/Icon.jpg'))

        #label1 -- original pic
        self.label_OriPic = QLabel(self)
        self.label_OriPic.setFixedSize(400,400)
        self.label_OriPic.move(120,50)
        self.label_OriPic.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Oritxt = QLabel(self)
        self.label_Oritxt.move(270,30) #+150,-20
        self.label_Oritxt.setText('Original Picture')


        #label2 -- filename
        self.label_fiilename = QLabel(self)
        self.label_fiilename.setFixedSize(500,20)
        self.label_fiilename.move(370,10)
        self.label_fiilename.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_filetxt = QLabel(self)
        self.label_filetxt.move(300,10)
        self.label_filetxt.setText('File Name:')

        #label3 -- Gray pic
        self.label_GrayPic = QLabel(self)
        self.label_GrayPic.setFixedSize(400,400)
        self.label_GrayPic.move(540,50)
        self.label_GrayPic.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Graytxt = QLabel(self)
        self.label_Graytxt.move(690,30)
        self.label_Graytxt.setText('Gray Picture')
        
        #label4 -- Edge Detection
        self.label_ED = QLabel(self)
        self.label_ED.setFixedSize(400,400)
        self.label_ED.move(120,470)
        self.label_ED.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_EDtxt = QLabel(self)
        self.label_EDtxt.move(270,450)
        self.label_EDtxt.setText('Edge Detection')


        #label5 -- Noise Reduction
        self.label_NR = QLabel(self)
        self.label_NR.setFixedSize(400,400)
        self.label_NR.move(540,470)
        self.label_NR.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_NRtxt = QLabel(self)
        self.label_NRtxt.move(690,450)
        self.label_NRtxt.setText('Noise Reduction')

        #----------------------------------------------button
        # button -- change window
        btn_CW2 = QPushButton(self)
        btn_CW2.setText('Project3')
        btn_CW2.move(0,70)
        btn_CW2.clicked.connect(self.ChangeWin2)

        #button -- imread
        btn_ir = QPushButton(self)
        btn_ir.setText('Open Image')
        btn_ir.move(0,45)
        btn_ir.clicked.connect(self.openimage)

        #button -- quit
        btn_q = QPushButton(self)
        btn_q.setText('Quit')
        btn_q.move(1000,45)
        btn_q.clicked.connect(QCoreApplication.instance().quit)

        #button -- Edge Detection -- Roberts
        btn_E_R = QPushButton(self)
        btn_E_R.setText('Roberts')
        btn_E_R.move(0,500)
        btn_E_R.clicked.connect(self.ED_Roberts)

        #button -- Edge Detection -- Prewitt
        btn_E_P = QPushButton(self)
        btn_E_P.setText('Prewitt')
        btn_E_P.move(0,530)
        btn_E_P.clicked.connect(self.ED_Prewitt)

        #button -- Edge Detection -- Sobel
        btn_E_S = QPushButton(self)
        btn_E_S.setText('Sobel')
        btn_E_S.move(0,560)
        btn_E_S.clicked.connect(self.ED_Sobel)


    #--------------------------------------------------function
    def ChangeWin2(self):
        pass

    # open image button-pushed event
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self,"Open Image","","*.jpg;;*.png;;All Files(*)")
        img = QtGui.QPixmap(imgName).scaled(self.label_OriPic.width(),self.label_OriPic.height())
        Image = cv2.imread(imgName)
        self.label_fiilename.setText(imgName)
        self.img_gray = cv2.cvtColor(Image,cv2.COLOR_RGB2GRAY)
        #cv2.imshow('Gray',img_gray)

        #cv img convert to QImage
        '''
        PyQt5 显示灰度图
        用cv去读取图片
        通过cv转换为灰度图
        从cv转换到QImage-->QPixmap
        reference:
        https://doc.qt.io/qtforpython/PySide2/QtGui/QImage.html#PySide2.QtGui.PySide2.QtGui.QImage.Format
        https://zhuanlan.zhihu.com/p/31810054
        '''
        height, width = self.img_gray.shape
        bytesPerLine = width
        QImg_Gray = QImage(self.img_gray.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_GrayPic.width(),self.label_GrayPic.height())
        self.label_OriPic.setPixmap(img)
        self.label_GrayPic.setPixmap(pixmap_Gray)
        
    # Edge Detection using Roberts masks when Button Roberts pushed
    def ED_Roberts(self):
        Roberts_1 = np.array(([-1,0],[0,1]))
        Roberts_2 = np.array(([0,-1],[1,0]))
        # 不对称卷积核旋转180度
        Roberts_1 = np.rot90(Roberts_1,2)
        Roberts_2 = np.rot90(Roberts_2,2)

        Img_ED_R1 = cv2.filter2D(self.img_gray,-1,Roberts_1)
        Img_ED_R2 = cv2.filter2D(self.img_gray,-1,Roberts_2)

        Img_ED_R = Img_ED_R1 + Img_ED_R2

        # show in label
        height, width = Img_ED_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(Img_ED_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_ED.width(),self.label_ED.height())
        self.label_ED.setPixmap(pixmap_Gray)
        self.label_EDtxt.setText('Roberts')

    # Edge Detection using Prewitt operator masks
    def ED_Prewitt(self):
        Prewitt1 = np.array(([-1,-1,-1],[0,0,0],[1,1,1]))
        Prewitt2 = np.array(([-1,0,1],[-1,0,1],[-1,0,1]))

        # 卷积核旋转
        Prewitt1 = np.rot90(Prewitt1,2)
        Prewitt2 = np.rot90(Prewitt2,2)

        Img_ED_P1 = cv2.filter2D(self.img_gray,-1,Prewitt1)
        Img_ED_P2 = cv2.filter2D(self.img_gray,-1,Prewitt2)

        Img_ED_P = Img_ED_P1 + Img_ED_P2

        # show
        height, width = Img_ED_P.shape
        bytesPerLine = width
        QImg_Gray = QImage(Img_ED_P.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_ED.width(),self.label_ED.height())
        self.label_ED.setPixmap(pixmap_Gray)
        self.label_EDtxt.setText('Prewitt')

    # Edge Detection using Sobel operator masks
    def ED_Sobel(self):
        Sobel1 = np.array(([-1,-2,-1],[0,0,0],[1,2,1]))
        Sobel2 = np.array(([-1,0,1],[-2,0,2],[-1,0,1]))

        # 卷积核旋转
        Sobel1 = np.rot90(Sobel1,2)
        Sobel2 = np.rot90(Sobel2,2)

        Img_ED_S1 = cv2.filter2D(self.img_gray,-1,Sobel1)
        Img_ED_S2 = cv2.filter2D(self.img_gray,-1,Sobel2)

        Img_ED_S = Img_ED_S1 + Img_ED_S2

        # show
        height, width = Img_ED_S.shape
        bytesPerLine = width
        QImg_Gray = QImage(Img_ED_S.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_ED.width(),self.label_ED.height())
        self.label_ED.setPixmap(pixmap_Gray)
        self.label_EDtxt.setText('Sobel')