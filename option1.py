
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
import serial.tools.list_ports
from mplwidget import MplWidget
from math import nan as nan
import pandas as pd
import ctypes


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
        self.arduino = 0

        
        Option1.setObjectName("Option1")
        Option1.resize(1427, 969)
        Option1.move(488, 3)
        Option1.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option1)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(420, 71, 860, 881))
        self.plot.setObjectName("plot")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 90, 131, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.startButt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_1.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.startButt_1.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt_1.setObjectName("startButt_1")
        self.startButt_1.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt_1.setIconSize(QtCore.QSize(90, 90))        
        self.startButt_1.clicked.connect(self.clicked1)
        
        self.stopButt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_1.setGeometry(QtCore.QRect(30, 150, 90, 45))
        self.stopButt_1.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt_1.setObjectName("stopButt_1")
        self.stopButt_1.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt_1.setIconSize(QtCore.QSize(90, 90))        
        self.stopButt_1.clicked.connect(self.clicked2)

        self.handbox = QtWidgets.QComboBox(self.centralwidget)
        self.handbox.setGeometry(QtCore.QRect(130, 700, 131, 30))
        self.handbox.setObjectName("handbox")
        self.handbox.addItems(['', 'Drag', 'Half crimp', 'Full crimp'])
       
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.title.setFont(font)       
        self.title.setObjectName("title")
        
        self.picr1label = QtWidgets.QLabel(self.centralwidget)
        self.picr1label.setGeometry(QtCore.QRect(40, 250, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.picr1label.setFont(font)
        self.picr1label.setAlignment(QtCore.Qt.AlignCenter)
        self.picr1label.setObjectName("picr1label")
        
        self.picl1label = QtWidgets.QLabel(self.centralwidget)
        self.picl1label.setGeometry(QtCore.QRect(165, 250, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.picl1label.setFont(font)        
        self.picl1label.setAlignment(QtCore.Qt.AlignCenter)
        self.picl1label.setObjectName("picl1label")
        
        self.right1label = QtWidgets.QLabel(self.centralwidget)
        self.right1label.setGeometry(QtCore.QRect(45, 220, 110, 31))
        self.right1label.setObjectName("right1label")

        self.displaylabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_1.setGeometry(QtCore.QRect(680, 35, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displaylabel_1.setFont(font)
        self.displaylabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_1.setObjectName("displaylabel_1")
        
        self.left1label = QtWidgets.QLabel(self.centralwidget)
        self.left1label.setGeometry(QtCore.QRect(175, 220, 110, 31))
        self.left1label.setObjectName("left1label")
        
        self.picr2label = QtWidgets.QLabel(self.centralwidget)
        self.picr2label.setGeometry(QtCore.QRect(40, 330, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.picr2label.setFont(font)        
        self.picr2label.setAlignment(QtCore.Qt.AlignCenter)
        self.picr2label.setObjectName("picr2label")
        
        self.picl2label = QtWidgets.QLabel(self.centralwidget)
        self.picl2label.setGeometry(QtCore.QRect(165, 330, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.picl2label.setFont(font)        
        self.picl2label.setAlignment(QtCore.Qt.AlignCenter)
        self.picl2label.setObjectName("picl2label")
        
        self.right2label = QtWidgets.QLabel(self.centralwidget)
        self.right2label.setGeometry(QtCore.QRect(45, 300, 110, 31))
        self.right2label.setObjectName("right2label")
        
        self.left2label = QtWidgets.QLabel(self.centralwidget)
        self.left2label.setGeometry(QtCore.QRect(175, 300, 110, 31))
        self.left2label.setObjectName("left2label")
        
        self.namelabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_1.setGeometry(QtCore.QRect(40, 840, 211, 30))
        self.namelabel_1.setObjectName("namelabel_1")

        self.handlabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_1.setGeometry(QtCore.QRect(40, 700, 130, 30))
        self.handlabel_1.setObjectName("handlabel_1") 

        self.notelabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_1.setGeometry(QtCore.QRect(40, 750, 211, 30))
        self.notelabel_1.setObjectName("notelabel_1")
           
        self.savebutt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.savebutt_1.setGeometry(QtCore.QRect(30, 890, 90, 45))
        self.savebutt_1.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.savebutt_1.setObjectName("savebutt_1")
        self.savebutt_1.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.savebutt_1.setIconSize(QtCore.QSize(90, 90))     
        self.savebutt_1.clicked.connect(self.clicked4)

        self.nameEdit_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_1.setGeometry(QtCore.QRect(130, 840, 131, 30))
        self.nameEdit_1.setObjectName("nameEdit_1")

        self.noteEdit_1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_1.setGeometry(QtCore.QRect(130, 750, 131, 70))
        self.noteEdit_1.setObjectName("noteEdit_1")
                
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
        #self.startButt_1.setText(_translate("Option1", "START"))
        #self.stopButt_1.setText(_translate("Option1", "RESET"))
        self.title.setText(_translate("Option1", "<html><head/><body><p><span style=\" font-size:12pt;\">PEAK LOAD</span></p></body></html>"))
        self.right1label.setText(_translate("Option1", "<html><head/><body><p>Right hand 1</p></body></html>"))
        self.left1label.setText(_translate("Option1", "<html><head/><body><p>Left hand 1</p></body></html>"))
        self.right2label.setText(_translate("Option1", "<html><head/><body><p>Right hand 2</p></body></html>"))
        self.left2label.setText(_translate("Option1", "<html><head/><body><p>Left hand 2</p></body></html>"))
        self.namelabel_1.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        #self.savebutt_1.setText(_translate("Option1", "SAVE"))
        self.handlabel_1.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_1.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
          

        
    def clicked1(self):
        a = Thread(target = self.connect)
        a.start()

    def clicked2(self):
        b = Thread(target = self.disconnect)
        b.start()

    def clicked4(self):
        d = Thread(target = self.save)
        d.start()     
        

    def connect(self):
        self.exit = 0

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
                        self.displaylabel_1.setText("Found Sensor on " + portName)
                        print("Found Sensor on " + portName)
                        time.sleep(2)
                        self.displaylabel_1.setText("")
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_1.setText("No Sensor found")
            raise IOError("No Sensor found")
            time.sleep(2)
            self.displaylabel_1.setText("")        
            
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)
     
               
        while self.exit == 0:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.peakload = max(self.peakload, value)
            
            self.lcdNumber.display(value)
            self.plot.update_bargraph(value, self.peakload)

            if(self.state == 0) and(value < 5):
                self.displaylabel_1.setText("RIGHT HAND")
                
            elif(self.state == 0) and(value > 5):
                self.state = 1

            elif(self.state == 1) and(value < 0.3):
                time.sleep(1)
                self.picr1 = self.peakload
                picr1 = str(self.picr1)
                self.picr1label.setText(picr1)
                self.peakload = 0
                self.state = 2
                self.displaylabel_1.setText("LEFT HAND")
                
            elif(self.state == 2) and(value > 5):
                self.state = 3

            elif(self.state == 3) and(value < 0.3):
                time.sleep(1)
                self.picl1 = self.peakload
                picl1 = str(self.picl1)
                self.picl1label.setText(picl1)
                self.peakload = 0
                self.state = 4
                self.displaylabel_1.setText("RIGHT HAND")

            elif(self.state == 4) and(value > 5):
                self.state = 5

            elif(self.state == 5) and(value < 0.3):
                time.sleep(1)
                self.picr2 = self.peakload
                picr2 = str(self.picr2)
                self.picr2label.setText(picr2)
                self.peakload = 0
                self.state = 6
                self.displaylabel_1.setText("LEFT HAND")
                
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
                    self.displaylabel_1.setText("peak load test is finished")
                    self.plot.canvas.axes.clear()
                    self.plot.x.clear()
                    self.plot.y.clear()
                    break

                
    def disconnect(self):
        self.state = 0
        self.peakload = 0
        self.picr1 = 0
        self.picl1 = 0
        self.picr2 = 0
        self.picl2 = 0
        self.exit = 1
        
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        
        self.displaylabel_1.setText("reset peakload")
        self.picr1label.setText("")
        self.picl1label.setText("")
        self.picr2label.setText("")
        self.picl2label.setText("")
        time.sleep(2.5)
        self.displaylabel_1.setText("")
        

    def save(self):
        self.name = self.nameEdit_1.toPlainText()
        self.notes = self.noteEdit_1.toPlainText()
        self.hand = str(self.handbox.currentText())
        picloadr = self.picr1, self.picr2
        picloadl = self.picl1, self.picl2
        self.clean = 1

        

        df = pd.read_csv("%s.csv"%self.name)
        data1 = [self.notes]
        df["peakloadnotes"] = data1
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data2 = [self.hand]
        df["peakloadstyle"] = data2
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data3 = [picloadr]
        df["peakloadright"] = data3
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data4 = [picloadl]
        df["peakloadleft"] = data4
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

        
        ctypes.windll.user32.MessageBoxW(0, "peakload data saved", "Saved", 1)
        self.nameEdit_1.clear()
        self.noteEdit_1.clear()
        self.handbox.clear()

             

while __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option1 = QtWidgets.QMainWindow()
    ui = Ui_Option1()
    ui.setupUi(Option1)
    Option1.show()
    sys.exit(app.exec_())
