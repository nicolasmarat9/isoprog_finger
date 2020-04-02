
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



class Ui_Free(object):
   

    
    def setupUi(self, Free):
        
        self.peakload = 0
        
        Free.setObjectName("Free")
        Free.resize(800, 601)
        
        self.centralwidget = QtWidgets.QWidget(Free)
        self.centralwidget.setObjectName("centralwidget")

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(255, 71, 521, 491))
        self.MplWidget.setObjectName("MplWidget")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.lcdNumber.setObjectName("lcdNumber")

        self.lcdNumber2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber2.setGeometry(QtCore.QRect(100, 130, 141, 41))
        self.lcdNumber2.setObjectName("lcdNumber2") 
        
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
  
        
        Free.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(Free)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        
        Free.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(Free)
        self.statusbar.setObjectName("statusbar")
        
        Free.setStatusBar(self.statusbar)

        self.retranslateUi(Free)
        QtCore.QMetaObject.connectSlotsByName(Free)

      
        
    def retranslateUi(self, Free):
        _translate = QtCore.QCoreApplication.translate
        Free.setWindowTitle(_translate("Free", "peakload"))
        self.butt1.setText(_translate("Free", "START"))
        self.butt2.setText(_translate("Free", "CLEAR"))
        self.title.setText(_translate("Free", "<html><head/><body><p><span style=\" font-size:12pt;\">PEAK LOAD</span></p></body></html>"))
        self.butt3.setText(_translate("Free", "BACK TO OPTIONS"))

        
    def clicked1(self):
        t = Thread(target = self.connect)
        t.start()

    def clicked2(self):
        d = Thread(target = self.disconnect)
        d.start()
        
    def clicked3(self):
        v = Thread(target = self.close)
        v.start()


    def connect(self):
        ser = ardconnect2.ardconnect()
               
        while True:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.peakload = max(self.peakload, value)
            
            self.lcdNumber.display(value)
            self.lcdNumber2.display(self.peakload)
            self.MplWidget.update_bargraph(value, self.peakload)

       
 
                

            

                
    def disconnect(self):
        self.peakload = 0


    def close(self):
        Option1.close()

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Free = QtWidgets.QMainWindow()
    ui = Ui_Free()
    ui.setupUi(Free)
    Free.show()
    sys.exit(app.exec_())