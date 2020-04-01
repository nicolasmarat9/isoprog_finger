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


class Ui_Option4(object):
    def setupUi(self,Option4 ):
        
        self.state = 0
        self.j = 0
        self.d = 0    
        self.i = 0
        self.w = 25
        self.spn = 0
        self.inter = []
        
        Option4.setObjectName("Option4")
        Option4.resize(1200, 801)
        
        self.centralwidget = QtWidgets.QWidget(Option4)
        self.centralwidget.setObjectName("centralwidget")

        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(255, 71, 921, 691))
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

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 401, 41))
        self.title.setObjectName("title")

        self.butt3 = QtWidgets.QPushButton(self.centralwidget)
        self.butt3.setGeometry(QtCore.QRect(20, 730, 211, 31))
        self.butt3.setObjectName("butt3")

        self.butt4 = QtWidgets.QPushButton(self.centralwidget)
        self.butt4.setGeometry(QtCore.QRect(20, 690, 211, 31))
        self.butt4.setObjectName("butt4")

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

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 300, 211, 35))
        self.spinBox.setObjectName("spinBox")
               
        Option4.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Option4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        Option4.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Option4)
        self.statusbar.setObjectName("statusbar")

        Option4.setStatusBar(self.statusbar)

        self.retranslateUi(Option4)
        QtCore.QMetaObject.connectSlotsByName(Option4)

    def retranslateUi(self, Option4):
        _translate = QtCore.QCoreApplication.translate
        Option4.setWindowTitle(_translate("Option4", "Interval endurance"))
        self.butt1.setText(_translate("Option4", "START"))
        self.butt2.setText(_translate("Option4", "STOP"))
        self.title.setText(_translate("Option4", "<html><head/><body><p><span style=\" font-size:12pt;\">INTERVAL ENDURANCE</span></p></body></html>"))
        self.butt3.setText(_translate("Option4", "BACK TO OPTIONS"))
        self.butt4.setText(_translate("Option4", "SAVE"))
        self.label.setText(_translate("Option4", "<html><head/><body><p>Peak load</p></body></html>"))
        self.label_2.setText(_translate("Option4", "<html><head/><body><p>Everadge</p></body></html>"))


        
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
            self.inter.append(value)           
                        
            self.lcdNumber.display(value)
            self.MplWidget.update_graph3(value, self.i, self.w, self.spn, self.state, self.j, self.d)
            self.i += 1
            self.w += 1
            self.spn = self.spinBox.value()         
      
        
    def disconnect(self):
        ardconnect2.disconnect(ser)
        
    def save(self):
        
        with open("test_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),self.inter])
                        

    def close(self):
        Option1.close()        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option4 = QtWidgets.QMainWindow()
    ui = Ui_Option4()
    ui.setupUi(Option4)
    Option4.show()
    sys.exit(app.exec_())
