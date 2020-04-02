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
from stopwatch import Stopwatch


class Ui_Option3(object):
    
    def setupUi(self, Option3):
        
        self.rang = 0
        self.rang2 = 0
        self.clean3 = 0
        self.i = 0
        self.j = 35
        self.spn = 0
        self.state = 0
        self.stopwatch = Stopwatch()
        self.straight = []
        
        Option3.setObjectName("Option3")
        Option3.resize(1200, 801)
        
        self.centralwidget = QtWidgets.QWidget(Option3)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(255, 71, 921, 691))
        self.plot.setObjectName("plot")

        self.displaylabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_3.setGeometry(QtCore.QRect(580, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        self.displaylabel_3.setFont(font)
        self.displaylabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_3.setObjectName("displaylabel_3")        

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.lcdNumber_3.setObjectName("lcdNumber")

        self.startButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_3.setGeometry(QtCore.QRect(10, 70, 71, 41))
        self.startButt_3.setObjectName("startButt_3")
        self.startButt_3.clicked.connect(self. clicked1_3)

        self.stopButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_3.setGeometry(QtCore.QRect(10, 130, 71, 41))
        self.stopButt_3.setObjectName("stopButt_3")
        self.stopButt_3.clicked.connect(self. clicked2_3)

        self.title_3 = QtWidgets.QLabel(self.centralwidget)
        self.title_3.setGeometry(QtCore.QRect(10, 10, 401, 41))
        self.title_3.setObjectName("title")

        self.backButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_3.setGeometry(QtCore.QRect(20, 730, 211, 31))
        self.backButt_3.setObjectName("backButt_3")
        self.backButt_3.clicked.connect(self. clicked3_3)

        self.saveButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_3.setGeometry(QtCore.QRect(20, 690, 211, 31))
        self.saveButt_3.setObjectName("saveButt_4")
        self.saveButt_3.clicked.connect(self. clicked4_3)

        self.displaylabel1_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel1_3.setGeometry(QtCore.QRect(120, 180, 120, 31))
        self.displaylabel1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel1_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel1_3.setObjectName("displaylabel1_3")

        self.displaylabel2_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel2_3.setGeometry(QtCore.QRect(120, 230, 120, 31))
        self.displaylabel2_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel2_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel2_3.setObjectName("displaylabel2_3")

        self.timelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.timelabel_3.setGeometry(QtCore.QRect(20, 180, 110, 31))
        self.timelabel_3.setObjectName("timelabel_3")

        self.everadgelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.everadgelabel_3.setGeometry(QtCore.QRect(20, 230, 81, 31))
        self.everadgelabel_3.setObjectName("everadgelabel_3")

        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(20, 300, 211, 35))
        self.spinBox_3.setMaximum(200)
        self.spinBox_3.setObjectName("spinBox_3")

        self.namelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_3.setGeometry(QtCore.QRect(20, 650, 211, 30))
        self.namelabel_3.setObjectName("namelabel_3")        
        
        self.fileEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fileEdit_3.setGeometry(QtCore.QRect(100, 650, 131, 30))
        self.fileEdit_3.setObjectName("fileEdit_3")           
               
        Option3.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Option3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        Option3.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Option3)
        self.statusbar.setObjectName("statusbar")

        Option3.setStatusBar(self.statusbar)

        self.retranslateUi(Option3)
        QtCore.QMetaObject.connectSlotsByName(Option3)

    def retranslateUi(self, Option3):
        _translate = QtCore.QCoreApplication.translate
        Option3.setWindowTitle(_translate("Option3", "Straight endurance"))
        self.startButt_3.setText(_translate("Option3", "START"))
        self.stopButt_3.setText(_translate("Option3", "STOP"))
        self.title_3.setText(_translate("Option3", "<html><head/><body><p><span style=\" font-size:12pt;\">STRAIGHT ENDURANCE</span></p></body></html>"))
        self.backButt_3.setText(_translate("Option3", "BACK TO OPTIONS"))
        self.saveButt_3.setText(_translate("Option3", "SAVE"))
        self.timelabel_3.setText(_translate("Option3", "<html><head/><body><p>Time (sec)</p></body></html>"))
        self.everadgelabel_3.setText(_translate("Option3", "<html><head/><body><p>Everadge</p></body></html>"))
        self.namelabel_3.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
 

        
    def clicked1_3(self):
        k = Thread(target = self.connect)
        k.start()

    def clicked2_3(self):
        l = Thread(target = self.disconnect)
        l.start()
        
    def clicked3_3(self):
        m = Thread(target = self.close)
        m.start()

    def clicked4_3(self):
        n = Thread(target = self.save)
        n.start()     
                
                
        

    def connect(self):
        self.clean3 = 0
        ser = ardconnect2.ardconnect()
               
        while self.clean3 == 0:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            self.straight.append(value)
                        
            self.lcdNumber_3.display(value)
            self.plot.update_graph2(value, self.i, self.j, self.spn)
            self.i += 1
            self.j += 1
            self.spn = self.spinBox_3.value()
            self.rang  = self.spn -5
            self.rang2 = self.spn +5

            if(self.state == 0) and (value < self.rang ) :
                continue
            elif(self.state == 0) and (value in range(self.rang, self.rang2)) :
                self.state = 1
                
            
            elif(self.state == 1) and (value in range(self.rang, self.rang2)):
                self.stopwatch.start()
                self.displaylabel_3.setText("start")
                
                
            elif(self.state == 1) and (value < self.rang) :
                self.stopwatch.stop()
                self.pulltime = int(self.stopwatch.duration)
                self.displaylabel1_3.setText(str(int(self.pulltime)))
                self.displaylabel_3.setText("Straight endurance test is finish")

             
            
    def disconnect(self):
        self.clean3 = 1
        self.displaylabel1_3.setText("")
        self.displaylabel_3.setText("")
        self.plot.canvas.axes.clear()
        self.state = 0
        
    def save(self):
        
        self.clean3 = 1
        self.name = self.fileEdit_3.toPlainText()        
        
        with open("%s.csv"%self.name,"a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([self.pulltime,self.straight])
        self.displaylabel_3.setText("Straight endurance saved")
            

    def close(self):
        Option1.close()    

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option3 = QtWidgets.QMainWindow()
    ui = Ui_Option3()
    ui.setupUi(Option3)
    Option3.show()
    sys.exit(app.exec_())





    
