'''
project 2 window
Convlution
'''
import cv2
import numpy as numpy
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import HisGet
from HisGet import HistoGet
#from ImageInput import picture

Hispicdir = '/Users/zhangyesheng/Desktop/IGST计算机辅助手术/Project1/His.png'


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
        