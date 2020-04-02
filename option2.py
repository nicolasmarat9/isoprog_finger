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

        self.plot = MplWidget(parent = self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(255, 71, 921, 691))
        self.plot.setObjectName("plot")

        self.displaylabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_2.setGeometry(QtCore.QRect(530, 5, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        self.displaylabel_2.setFont(font)
        self.displaylabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_2.setObjectName("displaylabel_2")

        self.displaylabel_22 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_22.setGeometry(QtCore.QRect(530, 5, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.displaylabel_22.setFont(font)
        self.displaylabel_22.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_22.setObjectName("displaylabel_22")        

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.startButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_2.setGeometry(QtCore.QRect(10, 70, 71, 41))
        self.startButt_2.setObjectName("startButt_2")
        self.startButt_2.clicked.connect(self. clicked1_2)

        self.stopButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_2.setGeometry(QtCore.QRect(10, 130, 71, 41))
        self.stopButt_2.setObjectName("stopButt_2")
        self.stopButt_2.clicked.connect(self. clicked2_2)

        self.title_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.title_2.setObjectName("title_2")

        self.backButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_2.setGeometry(QtCore.QRect(20, 730, 211, 31))
        self.backButt_2.setObjectName("backButt_2")
        self.backButt_2.clicked.connect(self. clicked3_2)

        self.saveButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_2.setGeometry(QtCore.QRect(20, 690, 211, 31))
        self.saveButt_2.setObjectName("saveButt_2")
        self.saveButt_2.clicked.connect(self. clicked4_2)

        self.peaklabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.peaklabel_2.setGeometry(QtCore.QRect(120, 180, 120, 31))
        self.peaklabel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.peaklabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.peaklabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.peaklabel_2.setObjectName("peaklabel_2")

        self.evelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.evelabel_2.setGeometry(QtCore.QRect(120, 230, 120, 31))
        self.evelabel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.evelabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.evelabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.evelabel_2.setObjectName("evelabel_2")

        self.peakloadlabel = QtWidgets.QLabel(self.centralwidget)
        self.peakloadlabel.setGeometry(QtCore.QRect(20, 180, 110, 31))
        self.peakloadlabel.setObjectName("peakloadlabel")

        self.everadgelabel = QtWidgets.QLabel(self.centralwidget)
        self.everadgelabel.setGeometry(QtCore.QRect(20, 230, 81, 31))
        self.everadgelabel.setObjectName("everadgelabel")

        self.namelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_2.setGeometry(QtCore.QRect(20, 650, 211, 30))
        self.namelabel_2.setObjectName("namelabel_2")        
        
        self.nameEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_2.setGeometry(QtCore.QRect(100, 650, 131, 30))
        self.nameEdit_2.setObjectName("nameEdit_2")        
               
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
        self.startButt_2.setText(_translate("Option2", "START"))
        self.stopButt_2.setText(_translate("Option2", "STOP"))
        self.title_2.setText(_translate("Option2", "<html><head/><body><p><span style=\" font-size:12pt;\">MAX STRENGTH</span></p></body></html>"))
        self.backButt_2.setText(_translate("Option2", "BACK TO OPTIONS"))
        self.saveButt_2.setText(_translate("Option2", "SAVE"))
        self.peakloadlabel.setText(_translate("Option2", "<html><head/><body><p>Peak load</p></body></html>"))
        self.everadgelabel.setText(_translate("Option2", "<html><head/><body><p>Everadge</p></body></html>"))
        self.namelabel_2.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
 

    def clicked1_2(self):
        e = Thread(target = self.connect)
        e.start()

    def clicked2_2(self):
        f = Thread(target = self.disconnect)
        f.start()
        
    def clicked3_2(self):
        h = Thread(target = self.close)
        h.start()

    def clicked4_2(self):
        g = Thread(target = self.save)
        g.start()     
                
        

    def connect(self):
        ser = ardconnect2.ardconnect()
        krono = Thread(target = self.timer)
        krono.start()
               
        while True:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            self.maxstrength.append(value)
            self.peakload = max(self.peakload, value)
                       
            self.lcdNumber_2.display(value)
            self.plot.update_graph(value, self.i)
            self.i += 1
            



    def timer(self):
        
        self.displaylabel_2.setText("Get ready")    
        time.sleep(1)            
        self.displaylabel_2.setText(str(5))    
        time.sleep(1)
        self.displaylabel_2.setText(str(4))    
        time.sleep(1)
        self.displaylabel_2.setText(str(3))    
        time.sleep(1)
        self.displaylabel_2.setText(str(2))    
        time.sleep(1)
        self.displaylabel_2.setText(str(1))    
        time.sleep(1)
        self.displaylabel_2.setText("START")    
        time.sleep(1)
        self.displaylabel_2.setText(str(7))    
        time.sleep(1)
        self.displaylabel_2.setText(str(6))    
        time.sleep(1)
        self.displaylabel_2.setText(str(5))    
        time.sleep(1)
        self.displaylabel_2.setText(str(4))    
        time.sleep(1)
        self.displaylabel_2.setText(str(3))    
        time.sleep(1)
        self.displaylabel_2.setText(str(2))    
        time.sleep(1)
        self.displaylabel_2.setText(str(1))    
        time.sleep(1)
        self.displaylabel_2.setText("STOP")    
        time.sleep(3)
        self.displaylabel_2.setText("")
                                    
        self.disconnect()
        
        peak = str(self.peakload)
        self.peaklabel_2.setText(peak)
        
        
        
        
    def disconnect(self):
        False

        
    def save(self):
        self.name = self.nameEdit_2.toPlainText()        
        
        with open("%s.csv"%self.name,"a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),self.maxstrength])
        self.displaylabel_22.setText("peak load saved")                

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
