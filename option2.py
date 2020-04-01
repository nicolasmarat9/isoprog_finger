import serial
import time
import csv
import matplotlib 
matplotlib.use("tkAgg") 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import ardconnect2
from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
from threading import Thread
import threading


class Ui_Option2(object):
    
    
    
    def setupUi(self, Option2):
        self.i = 0
        self.maxstrength = []
        self.peakload = 0
        
        
        Option2.setObjectName("Option2")
        Option2.resize(1200, 801)
        self.centralwidget = QtWidgets.QWidget(Option2)
        self.centralwidget.setObjectName("centralwidget")

        self.Mplwidget = MplWidget(parent = self.centralwidget)
        self.Mplwidget.setGeometry(QtCore.QRect(255, 71, 921, 691))
        self.Mplwidget.setObjectName("MplWidget")

        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(627, 5, 200, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        self.label0.setFont(font)
        self.label0.setAlignment(QtCore.Qt.AlignCenter)
        self.label0.setObjectName("label0")
        

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
        self.butt1.clicked.connect(self. clicked2)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.title.setObjectName("title")

        self.butt3 = QtWidgets.QPushButton(self.centralwidget)
        self.butt3.setGeometry(QtCore.QRect(20, 730, 211, 31))
        self.butt3.setObjectName("butt3")
        self.butt3.clicked.connect(self. clicked3)

        self.butt4 = QtWidgets.QPushButton(self.centralwidget)
        self.butt4.setGeometry(QtCore.QRect(20, 690, 211, 31))
        self.butt4.setObjectName("butt4")
        self.butt4.clicked.connect(self. clicked4)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(120, 180, 120, 31))
        self.label1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(120, 230, 120, 31))
        self.label2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 110, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 81, 31))
        self.label_2.setObjectName("label_2")

        
               
        Option2.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Option2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        Option2.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Option2)
        self.statusbar.setObjectName("statusbar")

        Option2.setStatusBar(self.statusbar)

        self.retranslateUi(Option2)
        QtCore.QMetaObject.connectSlotsByName(Option2)

    def retranslateUi(self, Option2):
        _translate = QtCore.QCoreApplication.translate
        Option2.setWindowTitle(_translate("Option2", "Max Strength"))
        self.butt1.setText(_translate("Option2", "START"))
        self.butt2.setText(_translate("Option2", "STOP"))
        self.title.setText(_translate("Option2", "<html><head/><body><p><span style=\" font-size:12pt;\">MAX STRENGTH</span></p></body></html>"))
        self.butt3.setText(_translate("Option2", "BACK TO OPTIONS"))
        self.butt4.setText(_translate("Option2", "SAVE"))
        self.label.setText(_translate("Option2", "<html><head/><body><p>Peak load</p></body></html>"))
        self.label_2.setText(_translate("Option2", "<html><head/><body><p>Everadge</p></body></html>"))


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
        krono = Thread(target = self.timer)
        krono.start()
               
        while True:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            self.maxstrength.append(value)
            self.peakload = max(self.peakload, value)
                       
            self.lcdNumber.display(value)
            self.Mplwidget.update_graph(value, self.i)
            self.i += 1
            



    def timer(self):
            
        self.label0.setText(str(5))    
        time.sleep(1)
        self.label0.setText(str(4))    
        time.sleep(1)
        self.label0.setText(str(3))    
        time.sleep(1)
        self.label0.setText(str(2))    
        time.sleep(1)
        self.label0.setText(str(1))    
        time.sleep(1)
        self.label0.setText("START")    
        time.sleep(1)
        self.label0.setText(str(7))    
        time.sleep(1)
        self.label0.setText(str(6))    
        time.sleep(1)
        self.label0.setText(str(5))    
        time.sleep(1)
        self.label0.setText(str(4))    
        time.sleep(1)
        self.label0.setText(str(3))    
        time.sleep(1)
        self.label0.setText(str(2))    
        time.sleep(1)
        self.label0.setText(str(1))    
        time.sleep(1)
        self.label0.setText("STOP")    
        time.sleep(3)
        self.disconnect()
        
        peak = str(self.peakload)
        self.label1.setText(peak)
        
        
        
        
    def disconnect(self):
        False

        
    def save(self):
        
        with open("max strength","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),self.maxstrength])
                        

    def close(self):
        Option1.close()    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option2 = QtWidgets.QMainWindow()
    ui = Ui_Option2()
    ui.setupUi(Option2)
    Option2.show()
    sys.exit(app.exec_())
