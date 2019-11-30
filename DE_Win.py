'''
Project 3 Window
aimed at doing the image erosion and dialation
And Open, Close
distance transform & skeleton get
'''

import cv2
import numpy as np
import time
import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from DilateAndErosion import DilationGet, ErosionGet, GetTheLittle
from DisAndSlec import *
from GrayDEWin import GEDWin


class DEwin(QWidget):
    def __init__(self):
        super(DEwin,self).__init__()
        


        # for show
        self.path = '/Users/zhangyesheng/Desktop/temp/'

        # SE
        self.SE = np.ones([5,5],dtype='bool')


        # Window 1200x1050
        self.resize(1200,1050)
        self.setWindowTitle('IGST-Morphology')
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
        self.label_BOtxt.setText('Basic Morphology Operation')
        
        #label4 -- distance
        self.label_D = QLabel(self)
        self.label_D.setFixedSize(400,400)
        self.label_D.move(120,470)
        self.label_D.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Dtxt = QLabel(self)
        self.label_Dtxt.move(270,450)
        self.label_Dtxt.setText('Distance')


        #label5 -- skeleton
        self.count = 0
        self.label_S = QLabel(self)
        self.label_S.setFixedSize(400,400)
        self.label_S.move(540,470)
        self.label_S.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Stxt = QLabel(self)
        self.label_Stxt.move(690,450)
        self.label_Stxt.setText('Slecton')

        #label6 -- time 1
        self.label_T = QLabel(self)
        # self.label_T.setFixedSize(20,40)
        self.label_T.move(1020,195)
        self.label_T.setFixedSize(100,20)
        self.label_T.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_Ttxt = QLabel(self)  
        self.label_Ttxt.move(980,195)
        self.label_Ttxt.setText('Time:')

        #label7 -- time2 -- DisTrans
        self.label_T2 = QLabel(self)
        self.label_T2.move(0,560)
        self.label_T2.setFixedSize(100,20)
        self.label_T2.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_T2txt = QLabel(self)
        self.label_T2txt.move(0,530)
        self.label_T2txt.setText('Time:')

        #label8 -- time3 -- Skeleton
        self.label_T3 = QLabel(self)
        self.label_T3.move(1040,530)
        self.label_T3.setFixedSize(100,20)
        self.label_T3.setStyleSheet("QLabel{background:white}" "QLabel{color:rgb(20,20,20);font-size:10px;font-weight:bold;font-family:宋体;}")
        self.label_T3txt = QLabel(self)   
        self.label_T3txt.move(1000,530)
        self.label_T3txt.setText('Time:')


        #----------------------------------------------button
        # button -- change window
        btn_CW2 = QPushButton(self)
        btn_CW2.setText('GMorpho')
        btn_CW2.move(0,70)
        btn_CW2.clicked.connect(self.ChangeWin3)

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
        btn_DI.setText('Dilation')
        btn_DI.move(1000,75)
        btn_DI.clicked.connect(self.Dilation)

        #button -- Basic Operation -- Erosion
        btn_E = QPushButton(self)
        btn_E.setText('Erosion')
        btn_E.move(1000,105)
        btn_E.clicked.connect(self.Erosion)

        #button -- Basic Operation -- Open
        btn_O = QPushButton(self)
        btn_O.setText('Open')
        btn_O.move(1000,135)
        btn_O.clicked.connect(self.Open)

        #button -- Basic Operation -- Close
        btn_C = QPushButton(self)
        btn_C.setText('Close')
        btn_C.move(1000,165)
        btn_C.clicked.connect(self.Close)


        #button -- Distance Transform
        btn_DT = QPushButton(self)
        btn_DT.setText('DisTrans')
        btn_DT.move(0,500)
        btn_DT.clicked.connect(self.DisTransWin)

        #button -- Conditional Dilation
        btn_CD = QPushButton(self)
        btn_CD.setText('Con_Dia')
        btn_CD.move(0,600)
        btn_CD.clicked.connect(self.Con_Dia)


        #button -- skeleton get
        btn_SK = QPushButton(self)
        btn_SK.setText('Skeleton')
        btn_SK.move(1000,500)
        btn_SK.clicked.connect(self.SKeleWin)

        #button -- internal edge
        btn_IE = QPushButton(self)
        btn_IE.setText('InEdge')
        btn_IE.move(1000,560)
        btn_IE.clicked.connect(self.InEdge)

        #button -- external egde 
        btn_EE = QPushButton(self)
        btn_EE.setText('ExEdge')
        btn_EE.move(1000,590)
        btn_EE.clicked.connect(self.ExEdge)

        #button -- standard edge
        btn_SE = QPushButton(self)
        btn_SE.setText('StaEdge')
        btn_SE.move(1000,620)
        btn_SE.clicked.connect(self.StaEdge)

        #button -- SE get
        btn_SG = QPushButton(self)
        btn_SG.setText('SE')
        btn_SG.move(0,100)
        btn_SG.clicked.connect(self.SEget)



        #--------------------------------------------------function
    def ChangeWin3(self):
        self.hide()
        self.DE = GEDWin()
        self.DE.show() 

    # open image button-pushed event
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self,"Open Binary Image","","All Files(*);;*.jpg;;*.png")
        img = QtGui.QPixmap(imgName).scaled(self.label_OriPic.width(),self.label_OriPic.height())
        Image = cv2.imread(imgName,-1)
        self.label_fiilename.setText(imgName)
        if len(Image.shape) != 2:
            self.img_gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
        else:
            self.img_gray = Image
        #转化为二值图像
        none, self.img_gray = cv2.threshold(self.img_gray,0,255,cv2.THRESH_BINARY)
        #cv2.imshow('Gray',img_gray)

        #cv img convert to QImage
        '''
        PyQt5 显示二值图
        用cv去读取图片
        通过cv转换为二值图
        从cv转换到QImage-->QPixmap
        reference:
        https://doc.qt.io/qtforpython/PySide2/QtGui/QImage.html#PySide2.QtGui.PySide2.QtGui.QImage.Format
        https://zhuanlan.zhihu.com/p/31810054
        '''
        height, width = self.img_gray.shape
        bytesPerLine = width
        QImg_Gray = QImage(self.img_gray.data, width, height, bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_OriPic.width(),self.label_OriPic.height())
        self.label_OriPic.setPixmap(pixmap_Gray)
        # print('O:',self.img_gray)

    # get SE size
    def SEget(self):
        size, ok = QInputDialog.getText(self, "Input Your SE Size", "SE Size:")
        if ok :
            size = int(size)
            self.SE = np.ones([size,size],dtype='bool')







    # Dialate button pushed 
    '''
    1. enter your SE size and SE
    2. doing the Dialation
    3. Show the result
    input : self.img_gray
    output : show
    '''
    def Dilation(self):
        
        '''
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

        '''
        # use defalut SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_DR = DilationGet(self.img_gray,SE)
        toc = time.time()
        none, Img_DR_b = cv2.threshold(Img_DR,0,255,cv2.THRESH_BINARY)
        height, width = Img_DR.shape
        # save & read to solve the pixmap_show_problem
        
        name = self.path+'Dia2.jpg'
        cv2.imwrite(name,Img_DR_b)
        Im_show = cv2.imread(name,-1) 
        bytesPerLine = width
        QImg_D = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Dilation')
        self.label_T.setText(str(1000*(toc-tic))+'ms')


    def Erosion(self):
        '''
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

        '''
        # use default SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_ER = ErosionGet(self.img_gray,SE)
        toc = time.time()
        none, Img_ER_b = cv2.threshold(Img_ER,0,255,cv2.THRESH_BINARY)
        
        # save & read to solve the pixmap_show_problem
        
        name = self.path+'Ero2.jpg'
        cv2.imwrite(name,Img_ER_b)
        Im_show = cv2.imread(name,-1) 

        height, width = Img_ER.shape
        bytesPerLine = width
        QImg_D = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Erosion')
        self.label_T.setText(str(1000*(toc-tic))+'ms')

    
    def Open(self):

        # use default SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_ER = ErosionGet(self.img_gray, SE) 
        none, Img_ER = cv2.threshold(Img_ER,0,255,cv2.THRESH_BINARY)
        Img_ER_DR = DilationGet(Img_ER, SE)
        toc = time.time()
        none, Img_ER_DR = cv2.threshold(Img_ER_DR,0,255,cv2.THRESH_BINARY)

        
        name = self.path+'Open.jpg'
        cv2.imwrite(name,Img_ER_DR)
        Im_show = cv2.imread(name,-1) 
        height, width = Img_ER.shape
        bytesPerLine = width
        QImg_D = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Open')
        self.label_T.setText(str(1000*(toc-tic))+'ms')



    def Close(self):
        
        # use default SE
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        tic = time.time()
        Img_DR = DilationGet(self.img_gray, SE)
        none, Img_DR = cv2.threshold(Img_DR,0,255,cv2.THRESH_BINARY)
        Img_DR_ER = ErosionGet(Img_DR, SE)
        toc = time.time()
        none, Img_DR_ER = cv2.threshold(Img_DR_ER,0,255,cv2.THRESH_BINARY)

        
        name = self.path+'Close.jpg'
        cv2.imwrite(name,Img_DR_ER)
        Im_show = cv2.imread(name,-1) 
        height, width = Img_DR_ER.shape
        bytesPerLine = width
        QImg_D = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_D = QPixmap.fromImage(QImg_D)
        pixmap_D = pixmap_D.scaled(self.label_BO.width(),self.label_BO.height())
        self.label_BO.setPixmap(pixmap_D)
        self.label_BOtxt.setText('Close')
        self.label_T.setText(str(1000*(toc-tic))+'ms')



    def DisTransWin(self):
        tic = time.time()
        Img_R = DisTrans(self.img_gray)
        toc = time.time()
        name = self.path+'DisTrans.jpg'
        cv2.imwrite(name,Img_R)

        # show
        Im_show = cv2.imread(name,-1) 
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_D.width(),self.label_D.height())
        self.label_D.setPixmap(pixmap_Gray)
        self.label_T2.setText(str(toc-tic)+'s')
        
    def SKeleWin(self):
        tic = time.time()
        Img_R,self.count = SkeGet(self.img_gray)
        toc = time.time()

        name = self.path+'SKeleton.jpg'
        cv2.imwrite(name,Img_R)

        # show
        Im_show = cv2.imread(name,-1) 
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_S.width(),self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)
        self.label_T3.setText(str(toc-tic)+'s')



    def InEdge(self):
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        Img_ER = ErosionGet(self.img_gray, SE)
        none, Img_ER = cv2.threshold(Img_ER,0,255,cv2.THRESH_BINARY)
        Img_R = self.img_gray - Img_ER
        name = self.path + 'InE.jpg'
        cv2.imwrite(name,Img_R)

        # show
        Im_show = cv2.imread(name,-1) 
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_S.width(),self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)
        self.label_Stxt.setText('Internal Edge')
        
    def ExEdge(self):
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        Img_DR = DilationGet(self.img_gray, SE)
        none, Img_DR = cv2.threshold(Img_DR,0,255,cv2.THRESH_BINARY)
        Img_R = Img_DR - self.img_gray
        name = self.path + 'ExE.jpg'
        cv2.imwrite(name,Img_R)

        # show
        Im_show = cv2.imread(name,-1) 
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_S.width(),self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)
        self.label_Stxt.setText('External Edge')

    def StaEdge(self):
        # SE = np.ones([5,5],dtype='bool')
        SE = self.SE
        Img_ER = ErosionGet(self.img_gray, SE)
        none, Img_ER = cv2.threshold(Img_ER,0,255,cv2.THRESH_BINARY)
        Img_DR = DilationGet(self.img_gray, SE)
        none, Img_DR = cv2.threshold(Img_DR,0,255,cv2.THRESH_BINARY)
        Img_R = Img_DR - Img_ER
        name = self.path + 'StaE.jpg'
        cv2.imwrite(name,Img_R)

        # show
        Im_show = cv2.imread(name,-1) 
        height, width = Img_R.shape
        bytesPerLine = width
        QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
        pixmap_Gray = QPixmap.fromImage(QImg_Gray)
        pixmap_Gray = pixmap_Gray.scaled(self.label_S.width(),self.label_S.height())
        self.label_S.setPixmap(pixmap_Gray)

    # Conditional Dilation
    def Con_Dia(self):
        size, ok = QInputDialog.getText(self, "Input 0~1", "LineLocation:")
        if ok:
            SE = np.ones([11,11],dtype='bool')
            w, h = self.img_gray.shape
            '''
            input lines waiting codes
            '''
            line = float(size)
            if line > 1 or line < 0:
                print('Input Error')
                return -1
            img_line = np.zeros([w,h],dtype='int')
            img_line[:,int(h*line )] = 255
            cv2.imwrite(self.path+'line.jpg',img_line)
            # show line img
            Im_show = cv2.imread(self.path+'line.jpg',0)
            height, width = Im_show.shape
            bytesPerLine = width
            QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
            pixmap_Gray = QPixmap.fromImage(QImg_Gray)
            pixmap_Gray = pixmap_Gray.scaled(self.label_D.width(),self.label_D.height())
            self.label_D.setPixmap(pixmap_Gray)
            self.label_Dtxt.setText('LineImg')

            # conditional dialate
            temp = np.zeros([w,h],dtype='int')
            c = 0
            img_grayt = self.img_gray.astype(np.bool)
            # print(img_grayt.dtype)
            a = 0
            b = 0
            tic = time.time()
            while(True):
                # print(c)
                img_line = DilationGet(img_line,SE).astype(np.int)
                temp = img_line.copy()
                # print(temp.dtype)
                # temp = temp.astype(np.int)
                # img_line = img_line.astype(np.bool)
                img_line = img_line & img_grayt # 0 & 1
                img_line = img_line.astype(np.int)
                # print(img_line.dtype)
                
                c+=1
                # print((temp == img_line).all())
                res = temp == img_line
                a = np.sum(res == False)
                if (a == b):
                    break
                b = a

            img_l = img_line*255
            toc = time.time()
            cv2.imwrite(self.path+'/ConD/'+str(c)+'.jpg',img_l)
                

            # show img_R
            Im_show = cv2.imread(self.path+'/ConD/'+str(c)+'.jpg',0)
            height, width = Im_show.shape
            bytesPerLine = width
            QImg_Gray = QImage(Im_show.data, width, height,bytesPerLine, QImage.Format_Grayscale8)
            pixmap_Gray = QPixmap.fromImage(QImg_Gray)
            pixmap_Gray = pixmap_Gray.scaled(self.label_D.width(),self.label_D.height())
            self.label_S.setPixmap(pixmap_Gray)
            self.label_Stxt.setText('ConDia')
            self.label_T2.setText(str(toc-tic)+'s')
        
