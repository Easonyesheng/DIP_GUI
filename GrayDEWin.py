'''
project 4 window
Gray Morphology
open close erosion dilation
edge detection
reconstruction
gradient 
'''

import cv2
import numpy as np 
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from GMorphology import *
from DilateAndErosion import GetTheLittle

class GEDWin(QWidget):
    def __init__(self):
        super(GEDWin,self).__init__()

        self.path = '/Users/zhangyesheng/Desktop/temp/'

        self.SE = np.ones([5,5],dtype='int')

        # Window 1200x1050
        self.resize(1200,1050)
        self.setWindowTitle('IGST-GMorphology')
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

        #label3 -- basic operation
        self.label_BO = QLabel(self)
        self.label_BO.setFixedSize(400,400)
        self.label_BO.move(540,50)
        self.label_BO.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_BOtxt = QLabel(self)
        self.label_BOtxt.move(690,30)
        self.label_BOtxt.setText('Gary Morphology Operation')
        
        #label4 -- Gary Reconstruction
        self.label_GR = QLabel(self)
        self.label_GR.setFixedSize(400,400)
        self.label_GR.move(120,470)
        self.label_GR.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_GRtxt = QLabel(self)
        self.label_GRtxt.move(270,450)
        self.label_GRtxt.setText('Gary Reconstruction')


        #label5 -- Gradient
        self.count = 0
        self.label_G = QLabel(self)
        self.label_G.setFixedSize(400,400)
        self.label_G.move(540,470)
        self.label_G.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Gtxt = QLabel(self)
        self.label_Gtxt.move(690,450)
        self.label_Gtxt.setText('Gradient')


        #label6 -- time
        self.time = 0
        self.label_T = QLabel(self)
        self.label_T.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_T.setFixedSize(100,20)
        self.label_T.move(1020,195)
        self.label_Ttxt = QLabel(self)
        self.label_Ttxt.setFixedSize(100,20)
        self.label_Ttxt.move(980,195)
        self.label_Ttxt.setText('Time:')



        #----------------------------------------------button
        
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

        #button -- Basic Operation -- Dilation
        btn_DI = QPushButton(self)
        btn_DI.setText('Dialtion')
        btn_DI.move(1000,75)
        btn_DI.clicked.connect(self.GDilationWin)

        #button -- Basic Operation -- Erosion
        btn_E = QPushButton(self)
        btn_E.setText('Erosion')
        btn_E.move(1000,105)
        btn_E.clicked.connect(self.GErosionWin)

        #button -- Basic Operation -- Open
        btn_O = QPushButton(self)
        btn_O.setText('Open')
        btn_O.move(1000,135)
        btn_O.clicked.connect(self.GOpenWin)

        #button -- Basic Operation -- Close
        btn_C = QPushButton(self)
        btn_C.setText('Close')
        btn_C.move(1000,165)
        btn_C.clicked.connect(self.GCloseWin)


        #button -- Reconstrution OBR
        btn_OBR = QPushButton(self)
        btn_OBR.setText('OBR')
        btn_OBR.move(0,500)
        btn_OBR.clicked.connect(self.OBRWin)

        #button -- Reconstrution CBR 
        btn_CBR = QPushButton(self)
        btn_CBR.setText('CBR')
        btn_CBR.move(0,530)
        btn_CBR.clicked.connect(self.CBRWin)

        #button -- SE GET
        btn_SG = QPushButton(self)
        btn_SG.setText('SE')
        btn_SG.move(0,100)
        btn_SG.clicked.connect(self.SEGet)



        #button -- Internal Gradient
        btn_IG = QPushButton(self)
        btn_IG.setText('Inter_Grad')
        btn_IG.move(1000,500)
        btn_IG.clicked.connect(self.InGradWin)

        #button -- External Gradient
        btn_EG = QPushButton(self)
        btn_EG.setText('Exter_Grad')
        btn_EG.move(1000,530)
        btn_EG.clicked.connect(self.ExGradWin)

        #button -- standard Gradient
        btn_SG = QPushButton(self)
        btn_SG.setText('Std_Grad')
        btn_SG.move(1000,560)
        btn_SG.clicked.connect(self.StaGradWin)

        

    #--------------------------------------------------function

    # open image button-pushed event
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self,"Open Image","","All Files(*);;*.jpg;;*.png")
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
        pixmap_Gray = pixmap_Gray.scaled(self.label_OriPic.width(),self.label_OriPic.height())
        
        self.label_OriPic.setPixmap(pixmap_Gray)

    def SEGet(self):
        size, ok = QInputDialog.getText(self, "Input Your SE Size", "SE Size:")
        if ok :
            size = int(size)
            self.SE = np.ones([size,size],dtype='int')
    
    # Erosion Get
    def GErosionWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GErosion(self.img_gray,SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Erosion')
        self.label_T.setText(str((toc-tic))+'s')



    # Dilation Get
    def GDilationWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GDilation(self.img_gray,SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Dilation')
        self.label_T.setText(str((toc-tic))+'s')
        
    # open
    def GOpenWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GOpen(self.img_gray,SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Open')
        self.label_T.setText(str((toc-tic))+'s')

    #close
    def GCloseWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        tic = time.time()
        img_R = GClose(self.img_gray,SE)
        toc = time.time()
        # show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_Gray)
        self.label_BOtxt.setText('Close')
        self.label_T.setText(str((toc-tic))+'s')


    # Internal Gradient
    def InGradWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        Img_ER = GErosion(self.img_gray,SE)
        img_R = (self.img_gray - Img_ER)
        # img_R = img_R/2 # cannot do this operation
        img_R.astype(np.int)
        #show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_G.width(),self.label_G.height())
        self.label_G.setPixmap(pixmap_Gray)
        self.label_Gtxt.setText('In_Grad')


    def ExGradWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        Img_DR = GDilation(self.img_gray,SE)
        img_R = (Img_DR - self.img_gray)        
        # img_R = img_R/2 # cannot do this operation
        img_R.astype(np.int)
        #show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_G.width(),self.label_G.height())
        self.label_G.setPixmap(pixmap_Gray)
        self.label_Gtxt.setText('Ex_Grad')


    def StaGradWin(self):
        # SE = np.ones([5,5],dtype='int')
        SE = self.SE
        Img_DR = GDilation(self.img_gray,SE)
        Img_ER = GErosion(self.img_gray,SE)
        img_R = (Img_DR - Img_ER)        
        # img_R = img_R/2 # cannot do this operation
        img_R.astype(np.int)
        #show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_G.width(),self.label_G.height())
        self.label_G.setPixmap(pixmap_Gray)
        self.label_Gtxt.setText('Std_Grad')

    def OBRWin(self):
        img_R = OBR(self.img_gray)

        #show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_G.width(),self.label_G.height())
        self.label_GR.setPixmap(pixmap_Gray)
        self.label_GRtxt.setText('OBR')


    def CBRWin(self):
        img_R = CBR(self.img_gray)
        
        #show
        QApplication.processEvents()
        height, width = img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(img_R.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_G.width(),self.label_G.height())
        self.label_GR.setPixmap(pixmap_Gray)
        self.label_GRtxt.setText('CBR')

