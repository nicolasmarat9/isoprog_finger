
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
        
        self.peakload = 0
        self.state = 0
        self.picr1 = 0
        self.picl1 = 0
        self.picr2 = 0
        self.picl2 = 0

        
        Option1.setObjectName("Option1")
        Option1.resize(800, 601)
        
        self.centralwidget = QtWidgets.QWidget(Option1)
        self.centralwidget.setObjectName("centralwidget")

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(255, 71, 521, 491))
        self.MplWidget.setObjectName("MplWidget")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.butt1.setGeometry(QtCore.QRect(10, 70, 71, 41))
        self.butt1.setObjectName("butt1")
        self.butt1.clicked.connect(self. clicked1)
        
        self.butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.butt2.setGeometry(QtCore.QRect(10, 130, 71, 41))
        self.butt2.setObjectName("butt2")
        self.butt2.clicked.connect(self. clicked2)
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.title.setObjectName("title")
        
        self.butt3 = QtWidgets.QPushButton(self.centralwidget)
        self.butt3.setGeometry(QtCore.QRect(20, 530, 211, 31))
        self.butt3.setObjectName("butt3")
        self.butt3.clicked.connect(self. clicked3)
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(135, 180, 100, 31))
        self.label1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(135, 230, 100, 31))
        self.label2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 110, 31))
        self.label.setObjectName("label")

        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(380, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        self.label0.setFont(font)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)
        self.label0.setObjectName("label0")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 81, 31))
        self.label_2.setObjectName("label_2")
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(135, 280, 100, 31))
        self.label3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(135, 330, 100, 31))
        self.label4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 110, 31))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 81, 31))
        self.label_4.setObjectName("label_4")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 490, 211, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self. clicked4)
        
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
        self.butt1.setText(_translate("Option1", "START"))
        self.butt2.setText(_translate("Option1", "STOP"))
        self.title.setText(_translate("Option1", "<html><head/><body><p><span style=\" font-size:12pt;\">PEAK LOAD</span></p></body></html>"))
        self.butt3.setText(_translate("Option1", "BACK TO OPTIONS"))
        self.label.setText(_translate("Option1", "<html><head/><body><p>Right hand 1</p></body></html>"))
        self.label_2.setText(_translate("Option1", "<html><head/><body><p>Left hand 1</p></body></html>"))
        self.label_3.setText(_translate("Option1", "<html><head/><body><p>Right hand 2</p></body></html>"))
        self.label_4.setText(_translate("Option1", "<html><head/><body><p>Left hand 2</p></body></html>"))
        self.pushButton.setText(_translate("Option1", "SAVE"))
       

        
    def clicked1(self):
        t = Thread(target = self.connect)
        t.start()

    def clicked2(self):
        d = Thread(target = self.disconnect)
        d.start()
        
    def clicked3(self):
        v = Thread(target = self.close)
        v.start()

    def clicked4(self):
        z = Thread(target = self.save)
        z.start()     
        

    def connect(self):
        ser = ardconnect2.ardconnect()
               
        while True:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.peakload = max(self.peakload, value)
            
            self.lcdNumber.display(value)
            self.MplWidget.update_bargraph(value, self.peakload)

       
            if(self.state == 0) and(value > 5):
                self.state = 1

            elif(self.state == 1) and(value < 0.3):
                time.sleep(1)
                self.picr1 = self.peakload
                picr1 = str(self.picr1)
                self.label1.setText(picr1)
                self.peakload = 0
                self.state = 2
                
            elif(self.state == 2) and(value > 5):
                self.state = 3

            elif(self.state == 3) and(value < 0.3):
                time.sleep(1)
                self.picl1 = self.peakload
                picl1 = str(self.picl1)
                self.label2.setText(picl1)
                self.peakload = 0
                self.state = 4                 

            elif(self.state == 4) and(value > 5):
                self.state = 5

            elif(self.state == 5) and(value < 0.3):
                time.sleep(1)
                self.picr2 = self.peakload
                picr2 = str(self.picr2)
                self.label3.setText(picr2)
                self.peakload = 0
                self.state = 6
                
            elif(self.state == 6) and(value > 5):
                self.state = 7

            elif(self.state == 7) and(value < 0.3):
                time.sleep(1)
                self.picl2 = self.peakload
                picl2 = str(self.picl2)
                self.label4.setText(picl2)                
                self.peakload = 0
                self.state = 8
                
            elif(self.state == 8):
                self.label0.setText("peak load test is finish")
                

            

                
    def disconnect(self):
        self.peakload = 0


    def save(self):
        with open("test_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(["peakloadr1",self.picr1])
            writer.writerow(["peakloadl1",self.picl1])
            writer.writerow(["peakloadr2",self.picr2])
            writer.writerow(["peakloadl2",self.picl2])
            self.label0.setText("peak load saved")
            

    def close(self):
        Option1.close()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option1 = QtWidgets.QMainWindow()
    ui = Ui_Option1()
    ui.setupUi(Option1)
    Option1.show()
    sys.exit(app.exec_())
