
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

        ### variables ###        
        
        self.peakload = 0
        
        ### option 3 straight endurance ###

            ## window setting ##
        
        Free.setObjectName("Free")
        Free.resize(1427, 969)
        Free.move(488, 3)
        Free.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Free)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(420, 71, 860, 881))
        self.plot.setObjectName("plot")

            ## titles and display labels ##        
        
        self.freetitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.freetitlelabel.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.freetitlelabel.setFont(font)         
        self.freetitlelabel.setObjectName("freetitlelabel")

        self.displaylabel_F = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_F.setGeometry(QtCore.QRect(705, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.displaylabel_F.setFont(font)
        self.displaylabel_F.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_F.setObjectName("displaylabel_F")        

        self.currentWeightlabel = QtWidgets.QLabel(self.centralwidget)
        self.currentWeightlabel.setGeometry(QtCore.QRect(161, 80, 110, 31))
        self.currentWeightlabel.setObjectName("currentWeightlabel")        

        self.displayWeightlabel= QtWidgets.QLabel(self.centralwidget)
        self.displayWeightlabel.setGeometry(QtCore.QRect(88 ,40 , 246, 200))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setWeight(65)
        self.displayWeightlabel.setFont(font)
        self.displayWeightlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayWeightlabel.setObjectName("displayWeightlabel") 

        self.currentpeakloadlabel = QtWidgets.QLabel(self.centralwidget)
        self.currentpeakloadlabel.setGeometry(QtCore.QRect(181, 190, 110, 31))
        self.currentpeakloadlabel.setObjectName("currentpeakloadlabel")        

        self.displayPeakloadlabel= QtWidgets.QLabel(self.centralwidget)
        self.displayPeakloadlabel.setGeometry(QtCore.QRect(88 ,150 , 246, 200))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(55)
        self.displayPeakloadlabel.setFont(font)
        self.displayPeakloadlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayPeakloadlabel.setObjectName("displayPeakloadlabel") 

            ## buttons ##
        
        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.startButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt.setObjectName("startButt")
        self.startButt.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt.setIconSize(QtCore.QSize(90, 90))          
        self.startButt.clicked.connect(self.clicked_startMeasures)
        
        self.stopButt = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt.setGeometry(QtCore.QRect(30, 150, 90, 45))
        self.stopButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt.setObjectName("stopButt")
        self.stopButt.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt.setIconSize(QtCore.QSize(90, 90))         
        self.stopButt.clicked.connect(self.clicked_stop_clear)
       
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
        self.freetitlelabel.setText(_translate("Free", "<html><head/><body><p><span style=\" font-size:12pt;\">FREE PEAK LOAD</span></p></body></html>"))
        self.currentWeightlabel.setText("Current weight")
        self.currentpeakloadlabel.setText("Peakload")         
      
    def clicked_startMeasures(self):
        t = Thread(target = self.connect_F)
        t.start()

    def clicked_stop_clear(self):
        d = Thread(target = self.disconnect)
        d.start()

    def connect_F(self):
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
                        self.displaylabel_F.setText("Found Sensor on " + portName)
                        print("Found Sensor on " + portName)
                        time.sleep(2)
                        self.displaylabel_F.setText("")
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_F.setText("No Sensor found")
            raise IOError("No Sensor found")
            time.sleep(2)
            self.displaylabel_F.setText("")        
       
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)
        
        ser_bytes = ser.readline()
        valueP1 = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        
              
        while True:
                        
            ser_bytes = ser.readline()
            valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            value = round(valueP - valueP1, 1)
            self.peakload = max(self.peakload, value)
            
            self.displayWeightlabel.setText(str(value))
            self.displayPeakloadlabel.setText(str(self.peakload))
            self.plot.update_bargraph(value, self.peakload)
               
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
