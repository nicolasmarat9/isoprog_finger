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
        
        Option6.setObjectName("Option6")
        Option6.resize(1427, 969)
        Option6.move(488, 3)
        Option6.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option6)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

        self.displaylabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_3.setGeometry(QtCore.QRect(700, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        self.displaylabel_3.setFont(font)
        self.displaylabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_3.setObjectName("displaylabel_3")        

        self.displaylabel3_3= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel3_3.setGeometry(QtCore.QRect(25 ,330, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.displaylabel3_3.setFont(font)
        self.displaylabel3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel3_3.setObjectName("displaylabel3_3")

        self.displaylabel3_5= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel3_5.setGeometry(QtCore.QRect(25 ,230, 120, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        self.displaylabel3_5.setFont(font)
        self.displaylabel3_5.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel3_5.setObjectName("displaylabel3_5")

        self.displaylabel3_6= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel3_6.setGeometry(QtCore.QRect(155 ,230, 120, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        self.displaylabel3_6.setFont(font)
        self.displaylabel3_6.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel3_6.setObjectName("displaylabel3_6")

        self.right2label = QtWidgets.QLabel(self.centralwidget)
        self.right2label.setGeometry(QtCore.QRect(50, 220, 110, 31))
        self.right2label.setObjectName("right2label")

        self.rightlabel = QtWidgets.QLabel(self.centralwidget)
        self.rightlabel.setGeometry(QtCore.QRect(185, 220, 110, 31))
        self.rightlabel.setObjectName("rightlabel")

        self.rightlabel3 = QtWidgets.QLabel(self.centralwidget)
        self.rightlabel3.setGeometry(QtCore.QRect(130, 350, 110, 31))
        self.rightlabel3.setObjectName("rightlabel3")         

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(140, 90, 131, 61))
        self.lcdNumber_3.setObjectName("lcdNumber")

        self.startButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_3.setGeometry(QtCore.QRect(30, 70, 90, 45))
        self.startButt_3.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt_3.setObjectName("startButt_3")
        self.startButt_3.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt_3.setIconSize(QtCore.QSize(90, 90))        
        self.startButt_3.clicked.connect(self. clicked1_3)

        self.stopButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_3.setGeometry(QtCore.QRect(30, 130, 90, 45))
        self.stopButt_3.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt_3.setObjectName("stopButt_3")
        self.stopButt_3.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt_3.setIconSize(QtCore.QSize(90, 90))       
        self.stopButt_3.clicked.connect(self. clicked2_3)

        self.title_3 = QtWidgets.QLabel(self.centralwidget)
        self.title_3.setGeometry(QtCore.QRect(30, 10, 401, 41))
        self.title_3.setObjectName("title")
  
        
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
        #self.startButt_3.setText(_translate("Option6", "START"))
        #self.stopButt_3.setText(_translate("Option6", "RESET"))
        self.title_3.setText(_translate("Option6", "<html><head/><body><p><span style=\" font-size:12pt;\">FREE ENDURANCE</span></p></body></html>"))
        self.right2label.setText("peakload")
        self.rightlabel.setText("average")
        self.rightlabel3.setText("timer")        
        
    def clicked1_3(self):
        k = Thread(target = self.connect)
        k.start()

    def clicked2_3(self):
        l = Thread(target = self.disconnect)
        l.start()
                
    def connect(self):
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
                            self.displaylabel_3.setText("Found Sensor on " + portName)
                            print("Found Sensor on " + portName)
                            time.sleep(2)
                            self.displaylabel_3.setText("")
                            break
                        
                        int1 = int1 + 1
                            
                else:
                    break

            if portName == '':
                self.displaylabel_3.setText("No Sensor found")
                raise IOError("No Sensor found")
                time.sleep(2)
                self.displaylabel_3.setText("")        
                
            
            baudrate = 9600
            ser = serial.Serial(portName, baudrate)


            u = Thread(target = self.timersec)
            u.start()
            while(self.state == 0):
                            
                ser_bytes = ser.readline()
                value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                
                self.peakload = max(self.peakload, value)
                self.displaylabel3_5.setText(str(self.peakload))

                self.everadge.append(value)
                self.average = sum(self.everadge) / len(self.everadge)
                self.displaylabel3_6.setText(str(round(self.average, 1)))
                
                self.lcdNumber_3.display(value)
                self.plot.update_graph4(value, self.i)
                s = Thread(target = self.plotvalue)
                
                s.start()


    def plotvalue(self):
    
        self.i += 1


    def timersec(self):
        time.sleep(1)
        self.displaylabel3_3.setText("START")
        while(self.state == 0):
            self.timer += 1
            time.sleep(1)
            self.displaylabel3_3.setText(str(int(self.timer)))    
        
         
        
            
    def disconnect(self):
        self.state = 1
        self.timer = -1
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        
        self.i = 0

        self.peakload = 0
        self.everadge = []
        self.average = 0
        self.displaylabel3_5.setText("")
        self.displaylabel3_3.setText("")
        self.displaylabel3_6.setText("")
        self.displaylabel_3.setText("")        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option6 = QtWidgets.QMainWindow()
    ui = Ui_Option6()
    ui.setupUi(Option6)
    Option6.show()
    sys.exit(app.exec_())





    
