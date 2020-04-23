
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np 
import serial
from threading import Thread
import time
import csv
from mplwidget import MplWidget
from math import nan as nan
import pandas as pd
import serial.tools.list_ports


class Ui_Free(object):
   

    
    def setupUi(self, Free):
        
        self.peakload = 0
        
        Free.setObjectName("Free")
        Free.resize(1427, 969)
        Free.move(488, 3)
        Free.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Free)
        self.centralwidget.setObjectName("centralwidget")

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(420, 71, 860, 881))
        self.MplWidget.setObjectName("MplWidget")

        self.poidlabel3 = QtWidgets.QLabel(self.centralwidget)
        self.poidlabel3.setGeometry(QtCore.QRect(161, 80, 110, 31))
        self.poidlabel3.setObjectName("rightlabel3")        

        self.poidlabel_F= QtWidgets.QLabel(self.centralwidget)
        self.poidlabel_F.setGeometry(QtCore.QRect(88 ,40 , 246, 200))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setWeight(65)
        self.poidlabel_F.setFont(font)
        self.poidlabel_F.setAlignment(QtCore.Qt.AlignCenter)
        self.poidlabel_F.setObjectName("poidlabel_F") 

        self.poidlabel4 = QtWidgets.QLabel(self.centralwidget)
        self.poidlabel4.setGeometry(QtCore.QRect(181, 190, 110, 31))
        self.poidlabel4.setObjectName("rightlabel3")        

        self.poidlabel_F2= QtWidgets.QLabel(self.centralwidget)
        self.poidlabel_F2.setGeometry(QtCore.QRect(88 ,150 , 246, 200))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(55)
        self.poidlabel_F2.setFont(font)
        self.poidlabel_F2.setAlignment(QtCore.Qt.AlignCenter)
        self.poidlabel_F2.setObjectName("poidlabel_F") 
        
        self.butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.butt1.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.butt1.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.butt1.setObjectName("butt1")
        self.butt1.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.butt1.setIconSize(QtCore.QSize(90, 90))           
        self.butt1.clicked.connect(self. clicked1)
        
        self.butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.butt2.setGeometry(QtCore.QRect(30, 150, 90, 45))
        self.butt2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.butt2.setObjectName("butt2")
        self.butt2.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.butt2.setIconSize(QtCore.QSize(90, 90))          
        self.butt2.clicked.connect(self. clicked2)
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.title.setFont(font)         
        self.title.setObjectName("title")

        self.displaylabel_11 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_11.setGeometry(QtCore.QRect(705, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.displaylabel_11.setFont(font)
        self.displaylabel_11.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_11.setObjectName("displaylabel_11")
        
  
        
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
        #self.butt1.setText(_translate("Free", "START"))
        #self.butt2.setText(_translate("Free", "CLEAR"))
        self.title.setText(_translate("Free", "<html><head/><body><p><span style=\" font-size:12pt;\">FREE PEAK LOAD</span></p></body></html>"))
        self.poidlabel3.setText("Current weight")
        self.poidlabel4.setText("Peakload")         
      
    def clicked1(self):
        t = Thread(target = self.connect)
        t.start()

    def clicked2(self):
        d = Thread(target = self.disconnect)
        d.start()

 
    def connect(self):
        
        portName = ""
        str2 = ""
        
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if portName == '':    
                int1 = 0
                while int1 <= 20:   
                    if "USB Serial Device" in p[1]:  
                        
                        str2 = str(int1) 
                        portName = "COM" + str2 
                        
                    if "USB Serial Device" in p[1] and portName in p[1]:
                        self.displaylabel_11.setText("Found Sensor on " + portName)
                        print("Found Sensor on " + portName)
                        time.sleep(2)
                        self.displaylabel_11.setText("")
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_11.setText("No Sensor found")
            raise IOError("No Sensor found")
            time.sleep(2)
            self.displaylabel_11.setText("")        
            
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)
        
        ser_bytes = ser.readline()
        valueP1 = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        

        
               
        while True:
                        
            ser_bytes = ser.readline()
            valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            value = round(valueP - valueP1, 1)

                       
            self.peakload = max(self.peakload, value)
            
            self.poidlabel_F.setText(str(value))
            self.poidlabel_F2.setText(str(self.peakload))
            self.MplWidget.update_bargraph(value, self.peakload)

                
    def disconnect(self):
        self.peakload = 0

      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Free = QtWidgets.QMainWindow()
    ui = Ui_Free()
    ui.setupUi(Free)
    Free.show()
    sys.exit(app.exec_())
