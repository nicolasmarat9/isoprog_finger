
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np 
import ardconnect2
import serial
from threading import Thread
import time
import csv
from mplwidget import MplWidget
from math import nan as nan
import pandas as pd


class Ui_Option1(object):
   

    
    def setupUi(self, Option1):
        
        self.exit = 0
        self.peakload = 0
        self.state = 0
        self.picr1 = 0
        self.picl1 = 0
        self.picr2 = 0
        self.picl2 = 0
        self.clean = 0

        
        Option1.setObjectName("Option1")
        Option1.resize(1000, 801)
        
        self.centralwidget = QtWidgets.QWidget(Option1)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(255, 71, 721, 691))
        self.plot.setObjectName("plot")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.startButt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_1.setGeometry(QtCore.QRect(10, 70, 71, 41))
        self.startButt_1.setObjectName("startButt_1")
        self.startButt_1.clicked.connect(self. clicked1)
        
        self.stopButt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_1.setGeometry(QtCore.QRect(10, 130, 71, 41))
        self.stopButt_1.setObjectName("stopButt_1")
        self.stopButt_1.clicked.connect(self. clicked2)
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.title.setObjectName("title")
        
        self.backButt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_1.setGeometry(QtCore.QRect(20, 730, 211, 31))
        self.backButt_1.setObjectName("backButt_1")
        self.backButt_1.clicked.connect(self. clicked3)
        
        self.picr1label = QtWidgets.QLabel(self.centralwidget)
        self.picr1label.setGeometry(QtCore.QRect(135, 180, 100, 31))
        self.picr1label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picr1label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picr1label.setAlignment(QtCore.Qt.AlignCenter)
        self.picr1label.setObjectName("picr1label")
        
        self.picl1label = QtWidgets.QLabel(self.centralwidget)
        self.picl1label.setGeometry(QtCore.QRect(135, 230, 100, 31))
        self.picl1label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picl1label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picl1label.setAlignment(QtCore.Qt.AlignCenter)
        self.picl1label.setObjectName("picl1label")
        
        self.right1label = QtWidgets.QLabel(self.centralwidget)
        self.right1label.setGeometry(QtCore.QRect(20, 180, 110, 31))
        self.right1label.setObjectName("right1label")

        self.displaylabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_1.setGeometry(QtCore.QRect(480, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.displaylabel_1.setFont(font)
        self.displaylabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_1.setObjectName("displaylabel_1")
        
        self.left1label = QtWidgets.QLabel(self.centralwidget)
        self.left1label.setGeometry(QtCore.QRect(20, 230, 81, 31))
        self.left1label.setObjectName("left1label")
        
        self.picr2label = QtWidgets.QLabel(self.centralwidget)
        self.picr2label.setGeometry(QtCore.QRect(135, 280, 100, 31))
        self.picr2label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picr2label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picr2label.setAlignment(QtCore.Qt.AlignCenter)
        self.picr2label.setObjectName("picr2label")
        
        self.picl2label = QtWidgets.QLabel(self.centralwidget)
        self.picl2label.setGeometry(QtCore.QRect(135, 330, 100, 31))
        self.picl2label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picl2label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picl2label.setAlignment(QtCore.Qt.AlignCenter)
        self.picl2label.setObjectName("picl2label")
        
        self.right2label = QtWidgets.QLabel(self.centralwidget)
        self.right2label.setGeometry(QtCore.QRect(20, 280, 110, 31))
        self.right2label.setObjectName("right2label")
        
        self.left2label = QtWidgets.QLabel(self.centralwidget)
        self.left2label.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.left2label.setObjectName("left2label")
        
        self.namelabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_1.setGeometry(QtCore.QRect(20, 650, 211, 30))
        self.namelabel_1.setObjectName("namelabel_1")
           
        self.savebutt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.savebutt_1.setGeometry(QtCore.QRect(20, 690, 211, 31))
        self.savebutt_1.setObjectName("savebutt_1")
        self.savebutt_1.clicked.connect(self. clicked4)

        self.nameEdit_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_1.setGeometry(QtCore.QRect(100, 650, 131, 30))
        self.nameEdit_1.setObjectName("nameEdit_1")
        
        Option1.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(Option1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        
        Option1.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(Option1)
        self.statusbar.setObjectName("statusbar")
        
        Option1.setStatusBar(self.statusbar)

        self.retranslateUi(Option1)
        QtCore.QMetaObject.connectSlotsByName(Option1)

      
        
    def retranslateUi(self, Option1):
        _translate = QtCore.QCoreApplication.translate
        Option1.setWindowTitle(_translate("Option1", "peakload"))
        self.startButt_1.setText(_translate("Option1", "START"))
        self.stopButt_1.setText(_translate("Option1", "STOP"))
        self.title.setText(_translate("Option1", "<html><head/><body><p><span style=\" font-size:12pt;\">PEAK LOAD</span></p></body></html>"))
        self.backButt_1.setText(_translate("Option1", "BACK TO OPTIONS"))
        self.right1label.setText(_translate("Option1", "<html><head/><body><p>Right hand 1</p></body></html>"))
        self.left1label.setText(_translate("Option1", "<html><head/><body><p>Left hand 1</p></body></html>"))
        self.right2label.setText(_translate("Option1", "<html><head/><body><p>Right hand 2</p></body></html>"))
        self.left2label.setText(_translate("Option1", "<html><head/><body><p>Left hand 2</p></body></html>"))
        self.namelabel_1.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.savebutt_1.setText(_translate("Option1", "SAVE"))
       

        
    def clicked1(self):
        a = Thread(target = self.connect)
        a.start()

    def clicked2(self):
        b = Thread(target = self.disconnect)
        b.start()
        
    def clicked3(self):
        c = Thread(target = self.close)
        c.start()

    def clicked4(self):
        d = Thread(target = self.save)
        d.start()     
        

    def connect(self):
        self.exit = 0
        ser = ardconnect2.ardconnect()
               
        while self.exit == 0:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.peakload = max(self.peakload, value)
            
            self.lcdNumber.display(value)
            self.plot.update_bargraph(value, self.peakload)

       
            if(self.state == 0) and(value > 5):
                self.state = 1

            elif(self.state == 1) and(value < 0.3):
                time.sleep(1)
                self.picr1 = self.peakload
                picr1 = str(self.picr1)
                self.picr1label.setText(picr1)
                self.peakload = 0
                self.state = 2
                
            elif(self.state == 2) and(value > 5):
                self.state = 3

            elif(self.state == 3) and(value < 0.3):
                time.sleep(1)
                self.picl1 = self.peakload
                picl1 = str(self.picl1)
                self.picl1label.setText(picl1)
                self.peakload = 0
                self.state = 4                 

            elif(self.state == 4) and(value > 5):
                self.state = 5

            elif(self.state == 5) and(value < 0.3):
                time.sleep(1)
                self.picr2 = self.peakload
                picr2 = str(self.picr2)
                self.picr2label.setText(picr2)
                self.peakload = 0
                self.state = 6
                
            elif(self.state == 6) and(value > 5):
                self.state = 7

            elif(self.state == 7) and(value < 0.3):
                time.sleep(1)
                self.picl2 = self.peakload
                picl2 = str(self.picl2)
                self.picl2label.setText(picl2)                
                self.peakload = 0
                self.state = 8
                
            elif(self.state == 8):
                if(self.clean == 0):
                    self.displaylabel_1.setText("peak load test is finish")
                

            

                
    def disconnect(self):
        self.exit = 1
        self.picr1label.setText("")
        self.picl1label.setText("")
        self.picr2label.setText("")
        self.picl2label.setText("")
        self.state = 0
        self.displaylabel_1.setText("")

    def save(self):
        self.name = self.nameEdit_1.toPlainText()
        self.clean = 1
        with open("%s.csv"%self.name,"a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(["peakloadr1",self.picr1])
            writer.writerow(["peakloadl1",self.picl1])
            writer.writerow(["peakloadr2",self.picr2])
            writer.writerow(["peakloadl2",self.picl2])
        self.displaylabel_1.setText("peak load saved")
            

    def close(self):
        sys.exit()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option1 = QtWidgets.QMainWindow()
    ui = Ui_Option1()
    ui.setupUi(Option1)
    Option1.show()
    sys.exit(app.exec_())
