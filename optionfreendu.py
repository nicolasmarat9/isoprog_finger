import serial
import time
import csv
import matplotlib 
matplotlib.use("tkAgg") 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
from threading import Thread
from stopwatch import Stopwatch
import serial.tools.list_ports

class Ui_Option6(object):
    
    def setupUi(self, Option6):
        
        ### variables ###        

        self.i = 0
        self.spn = 0
        self.state = 0
        self.state2 = 0
        self.val = 0
        self.teeth = 0        
        self.timepoint = 0
        self.intens = 0
        self.timer = -1
        self.peakload = 0
        self.everadge = []
        self.average = 0
        
        ### option 3 straight endurance ###

            ## window setting ##
        
        Option6.setObjectName("Option6")
        Option6.resize(1427, 969)
        Option6.move(488, 3)
        Option6.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option6)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

            ## titles and display labels ##        

        self.FreeEndutitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.FreeEndutitlelabel.setGeometry(QtCore.QRect(30, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.FreeEndutitlelabel.setFont(font)         
        self.FreeEndutitlelabel.setObjectName("FreeEndutitlelabel")
        
        self.currentWeightlabel = QtWidgets.QLabel(self.centralwidget)
        self.currentWeightlabel.setGeometry(QtCore.QRect(161, 60, 110, 31))
        self.currentWeightlabel.setObjectName("currentWeightlabel")
        
        self.displayWeightlabel= QtWidgets.QLabel(self.centralwidget)
        self.displayWeightlabel.setGeometry(QtCore.QRect(88 ,20 , 246, 200))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setWeight(65)
        self.displayWeightlabel.setFont(font)
        self.displayWeightlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayWeightlabel.setObjectName("displayWeightlabel")
        
        self.peakloadlabel = QtWidgets.QLabel(self.centralwidget)
        self.peakloadlabel.setGeometry(QtCore.QRect(50, 220, 110, 31))
        self.peakloadlabel.setObjectName("peakloadlabel")
        
        self.displayPeakloadlabel = QtWidgets.QLabel(self.centralwidget)
        self.displayPeakloadlabel.setGeometry(QtCore.QRect(25 ,230, 120, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        self.displayPeakloadlabel.setFont(font)
        self.displayPeakloadlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayPeakloadlabel.setObjectName("displayPeakloadlabel")

        self.averagelabel = QtWidgets.QLabel(self.centralwidget)
        self.averagelabel.setGeometry(QtCore.QRect(185, 220, 110, 31))
        self.averagelabel.setObjectName("averagelabel")
        
        self.displayAveragelabel = QtWidgets.QLabel(self.centralwidget)
        self.displayAveragelabel.setGeometry(QtCore.QRect(155 ,230, 120, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        self.displayAveragelabel.setFont(font)
        self.displayAveragelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayAveragelabel.setObjectName("displayAveragelabel")
        
        self.displaylabel_F_E = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_F_E.setGeometry(QtCore.QRect(700, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        self.displaylabel_F_E.setFont(font)
        self.displaylabel_F_E.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_F_E.setObjectName("displaylabel_F_E")        

        self.timerlabel = QtWidgets.QLabel(self.centralwidget)
        self.timerlabel.setGeometry(QtCore.QRect(130, 360, 110, 31))
        self.timerlabel.setObjectName("timerlabel")
        
        self.displaytimerlabel= QtWidgets.QLabel(self.centralwidget)
        self.displaytimerlabel.setGeometry(QtCore.QRect(25 ,330, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.displaytimerlabel.setFont(font)
        self.displaytimerlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displaytimerlabel.setObjectName("displaytimerlabel")
        
            ## buttons ##  

        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(30, 70, 90, 45))
        self.startButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt.setObjectName("startButt_3")
        self.startButt.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt.setIconSize(QtCore.QSize(90, 90))        
        self.startButt.clicked.connect(self.clicked_startMeasures)

        self.stopButt = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt.setGeometry(QtCore.QRect(30, 130, 90, 45))
        self.stopButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt.setObjectName("stopButt_3")
        self.stopButt.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt.setIconSize(QtCore.QSize(90, 90))       
        self.stopButt.clicked.connect(self.clicked_stop_clear)
        
        Option6.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Option6)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        Option6.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Option6)
        self.statusbar.setObjectName("statusbar")

        Option6.setStatusBar(self.statusbar)

        self.retranslateUi(Option6)
        QtCore.QMetaObject.connectSlotsByName(Option6)

    def retranslateUi(self, Option6):
        _translate = QtCore.QCoreApplication.translate
        Option6.setWindowTitle(_translate("Option6", "Free endurance"))
        self.FreeEndutitlelabel.setText(_translate("Option6", "<html><head/><body><p><span style=\" font-size:12pt;\">FREE ENDURANCE</span></p></body></html>"))
        self.peakloadlabel.setText("Peakload")
        self.averagelabel.setText("Average")
        self.timerlabel.setText("Timer")
        self.currentWeightlabel.setText("Current weight")        
        
    def clicked_startMeasures(self):
        k = Thread(target = self.connect_F_E)
        k.start()

    def clicked_stop_clear(self):
        l = Thread(target = self.disconnect)
        l.start()
                
    def connect_F_E(self):
        self.state = 0
        if(self.state == 0):
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
                            self.displaylabel_F_E.setText("Found Sensor on " + portName)
                            print("Found Sensor on " + portName)
                            time.sleep(2)
                            self.displaylabel_F_E.setText("")
                            break
                        
                        int1 = int1 + 1
                            
                else:
                    break

            if portName == '':
                self.displaylabel_F_E.setText("No Sensor found")
                raise IOError("No Sensor found")
                time.sleep(2)
                self.displaylabel_F_E.setText("")        
      
            baudrate = 9600
            ser = serial.Serial(portName, baudrate)

            u = Thread(target = self.timersec)
            u.start()
            
            ser_bytes = ser.readline()
            valueP1 = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        
            
            while(self.state == 0):
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                value = round(valueP - valueP1, 1)
                
                self.peakload = max(self.peakload, value)
                self.displayPeakloadlabel.setText(str(self.peakload))

                self.everadge.append(value)
                self.average = sum(self.everadge) / len(self.everadge)
                self.displayAveragelabel.setText(str(round(self.average, 1)))
                
                self.displayWeightlabel.setText(str(value))
                self.plot.update_graph4(value, self.i)
                s = Thread(target = self.plotvalue)
                s.start()

    def plotvalue(self):
        self.i += 1

    def timersec(self):
        time.sleep(1)
        self.displaytimerlabel.setText("START")
        while(self.state == 0):
            self.timer += 1
            time.sleep(1)
            self.displaytimerlabel.setText(str(int(self.timer)))    
            
    def disconnect(self):
        self.state = 1
        self.timer = -1
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.canvas.draw()
        self.i = 0

        self.peakload = 0
        self.everadge = []
        self.average = 0
        self.displayAveragelabel.setText("")
        self.displaytimerlabel.setText("")
        self.displayPeakloadlabel.setText("")
        self.displaylabel_F_E.setText("")        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option6 = QtWidgets.QMainWindow()
    ui = Ui_Option6()
    ui.setupUi(Option6)
    Option6.show()
    sys.exit(app.exec_())





    
