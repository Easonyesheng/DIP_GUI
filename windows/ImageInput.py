'''
# Histogra
# m+最优二值
主程序
包括
界面的定义
图片读取+灰度图转换
'''
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import cv2

from models.ThredSeg import *
from windows.ConvolutionWin import Convlution
from settings import *


# 界面对象 -- project 1 Window
class picture(QMainWindow):
    def __init__(self):
        super(picture,self).__init__()
        
        #image
        self.Image = []

        #window
        self.resize(win_h,win_w)
        self.setWindowTitle('Basic')
        self.setWindowIcon(QIcon('/Users/zhangyesheng/Desktop/Icon.jpg'))
        
        #label1 -- original pic
        self.label_OriPic = QLabel(self)
        self.label_OriPic.setFixedSize(small_win_size,small_win_size)
        self.label_OriPic.move(120,55)
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
        self.label_GrayPic.move(540,55)
        self.label_GrayPic.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Graytxt = QLabel(self)
        self.label_Graytxt.move(690,30)
        self.label_Graytxt.setText('Gray Picture')
        
        #label4 -- Histogram
        self.label_His = QLabel(self)
        self.label_His.setFixedSize(400,400)
        self.label_His.move(120,475)
        self.label_His.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Histxt = QLabel(self)
        self.label_Histxt.move(270,450)
        self.label_Histxt.setText('Histogram')


        #label5 -- Threshold
        self.label_TH = QLabel(self)
        self.label_TH.setFixedSize(400,400)
        self.label_TH.move(540,475)
        self.label_TH.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_THtxt = QLabel(self)
        self.label_THtxt.move(690,450)
        self.label_THtxt.setText('Threshold')

        #label6 -- 'Threshold' txt
        self.label_THretxt = QLabel(self)
        # self.label_THretxt.move(1020,470)
        self.label_THretxt.move(0,470)
        self.label_THretxt.setText('Threshold Way:')

        #label7 -- gray thresheld show
        self.label_GrayValue = QLabel(self)
        self.label_GrayValue.setFixedSize(20,20)
        self.label_GrayValue.move(1100,570)
        self.label_GrayValue.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_GVtxt = QLabel(self)
        self.label_GVtxt.move(1000,570)
        self.label_GVtxt.setText('Gray Threshold:')

        # #label8 -- OTSU threshold txt
        # self.label_OStxt = QLabel(self)
        # self.label_OStxt.setFixedSize(20,20)
        # self.label_OStxt.move(1120,505)
        # self.label_OStxt.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")

        # #label9 -- Entropy threshold txt
        # self.label_ETtxt = QLabel(self)
        # self.label_ETtxt.setFixedSize(20,20)
        # self.label_ETtxt.move(1120,535)
        # self.label_ETtxt.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")

        #——----------------------------------------------------------button

        # button -- change window
        btn_CW = QPushButton(self)
        btn_CW.setText('Convolution')
        btn_CW.move(0,70)
        btn_CW.clicked.connect(self.ChangeWin)

        #button -- imread
        btn_ir = QPushButton(self)
        btn_ir.setText('Open Image')
        btn_ir.move(0,45)
        btn_ir.clicked.connect(self.openimage)

        #button -- quit
        btn_q = QPushButton(self)
        btn_q.setText('Quit')
        # btn_q.move(1000,45)
        btn_q.move(1000,45)
        btn_q.clicked.connect(QCoreApplication.instance().quit)

        #button -- OTSU
        btn_OS = QPushButton(self)
        btn_OS.setText('OTSU')
        # btn_OS.move(1020,500)
        btn_OS.move(0,500)
        btn_OS.clicked.connect(self.OTSUSET)

        #button -- entropy
        btn_En = QPushButton(self)
        btn_En.setText('Entropy')
        # btn_En.move(1020,530)
        btn_En.move(0,530)
        btn_En.clicked.connect(self.EntroGet)

        #---------------------------------------------------------slide

        #slide -- change the sheld value
        sld_Gray = QSlider(Qt.Horizontal,self)
        sld_Gray.setFocusPolicy(Qt.NoFocus)
        sld_Gray.setFixedSize(100,30)
        sld_Gray.move(1020,590)
        sld_Gray.valueChanged[int].connect(self.changeGray)



    #----------------------------------------------------------------Function
    def ChangeWin(self):
        self.hide()
        self.Con = Convlution()
        self.Con.show() 


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
        QApplication.processEvents()
        height, width = self.img_gray.shape
        bytesPerLine = width
        QImg_Gray = QImage(self.img_gray.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_GrayPic.width(),self.label_GrayPic.height())
        self.label_OriPic.setPixmap(img)
        self.label_GrayPic.setPixmap(pixmap_Gray)
        #imgGray = RGB2Gray(img)
        #self.label_GrayPic.setPixmap(imgGray)
        '''
        调用Hisget得到灰度直方图
        存储
        再读出显示再GUI上
        '''
        HistoGet(self.img_gray,Hispicdir)
        Hisimg = cv2.imread(Hispicdir)
        #cv2.imshow('H',Hisimg)
        Hisheight, Hiswidth, HisbytesPerComponent = Hisimg.shape
        HisbytesPerLine = 3 * Hiswidth
        Hisimg = cv2.cvtColor(Hisimg, cv2.COLOR_BGR2RGB)
        QImg_His = QImage(Hisimg.data, Hiswidth, Hisheight, HisbytesPerLine, QImage.Format_RGB888)
        pixmap_His = QPixmap.fromImage(QImg_His)
        pixmap_His = pixmap_His.scaled(self.label_His.width(),self.label_His.height())
        self.label_His.setPixmap(pixmap_His)
        

    #change the slide value then change the gray sheld
    #value from 0-100
    def changeGray(self,value):
        # show text
        self.Gray = int(value/100*258)
        self.label_GrayValue.setText(str(self.Gray))
        # get image
        # Gc -- Gray change
        imgtemp = self.img_gray
        otsu, GcImage = cv2.threshold(imgtemp, self.Gray, 255, cv2.THRESH_BINARY)
        Gcheight, Gcwidth = GcImage.shape
        GcBytesPerLine = Gcwidth
        QImg_Gc = QImage(GcImage.data, Gcwidth, Gcheight, GcBytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gc = QPixmap.fromImage(QImg_Gc)
        pixmap_Gc = pixmap_Gc.scaled(self.label_TH.width(),self.label_TH.height())
        self.label_TH.setPixmap(pixmap_Gc)
        self.label_THtxt.setText('Threshold')



    #OTSU button pushed and get the result and show 
    #OS = OTSU
    '''
    有一个很奇怪的现象
    按下OTSU键后要点到其他地方（不能在python上？）才能显示
    # solution : QApplication.processEvents() before the show function
    '''
    def OTSUSET(self):
        self.label_GrayValue.setText("")
        T = OTSU_GET(self.img_gray)
        self.label_OStxt.setText(str(T))
        ot, OSimg = cv2.threshold(self.img_gray,T,255,cv2.THRESH_BINARY)
        QApplication.processEvents()
        OSheight, OSwidth = OSimg.shape
        OSBytesPerLine = OSwidth
        Qimg_OS = QImage(OSimg.data, OSwidth, OSheight, OSBytesPerLine, QImage.Format_Grayscale8)
        pixmap_OS = QPixmap.fromImage(Qimg_OS)
        pixmap_OS = pixmap_OS.scaled(self.label_TH.width(),self.label_TH.height())
        self.label_TH.setPixmap(pixmap_OS)
        self.label_THtxt.setText('OTSU')




    #Entropy button pushed and get the result and show
    #EN = Entropy
    def EntroGet(self):
        T = Entropy_get(self.img_gray)
        self.label_ETtxt.setText(str(T))
        ot,ENimg = cv2.threshold(self.img_gray,T,255,cv2.THRESH_BINARY)
        QApplication.processEvents()
        ENheight,ENwidth = ENimg.shape
        ENBytesPerLine = ENwidth
        Qimg_EN = QImage(ENimg.data, ENwidth, ENheight,ENBytesPerLine,QImage.Format_Grayscale8)
        pixmap_EN = QPixmap.fromImage(Qimg_EN)
        pixmap_EN = pixmap_EN.scaled(self.label_TH.width(),self.label_TH.height())
        self.label_TH.setPixmap(pixmap_EN)
        self.label_THtxt.setText('Entropy')




if __name__ == "__main__":
    #QtCore.QCoreApplication.setLibraryPaths("")
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    
    
    sys.exit(app.exec_())
    