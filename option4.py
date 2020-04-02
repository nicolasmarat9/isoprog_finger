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


class Ui_Option4(object):
    
    def setupUi(self,Option4 ):
        
        self.rang = 0
        self.rang2 =  0
        self.state = 0
        self.state2 = 0
        self.teeth = 0
        self.val = 0    
        self.i = 0
        self.j = 25
        self.spn = 0
        self.inter = []
        self.stopwatch = Stopwatch()
        self.timepoint = 0
        self.clean = 0
        
        Option4.setObjectName("Option4")
        Option4.resize(1400, 801)
        
        self.centralwidget = QtWidgets.QWidget(Option4)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(255, 71, 1121, 691))
        self.plot.setObjectName("plot")

        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(100, 70, 141, 41))
        self.lcdNumber_4.setObjectName("lcdNumber")

        self.startButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_4.setGeometry(QtCore.QRect(10, 70, 71, 41))
        self.startButt_4.setObjectName("butt1")
        self.startButt_4.clicked.connect(self. clicked1)

        self.stopButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_4.setGeometry(QtCore.QRect(10, 130, 71, 41))
        self.stopButt_4.setObjectName("stopButt_4")
        self.stopButt_4.clicked.connect(self. clicked2)

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 401, 41))
        self.title.setObjectName("title")

        self.backButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_4.setGeometry(QtCore.QRect(20, 730, 211, 31))
        self.backButt_4.setObjectName("backButt_4")

        self.saveButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_4.setGeometry(QtCore.QRect(20, 690, 211, 31))
        self.saveButt_4.setObjectName("saveButt_4")

        self.displaylabel1_4 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel1_4.setGeometry(QtCore.QRect(120, 180, 120, 31))
        self.displaylabel1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel1_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel1_4.setObjectName("displaylabel1_4")

        self.displaylabel2_4 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel2_4.setGeometry(QtCore.QRect(120, 230, 120, 31))
        self.displaylabel2_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel2_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel2_4.setObjectName("displaylabel2_4")

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
        
        self.filename4 = QtWidgets.QLabel(self.centralwidget)
        self.filename4.setGeometry(QtCore.QRect(20, 650, 211, 30))
        self.filename4.setObjectName("filename4")        
        
        self.fileEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fileEdit_4.setGeometry(QtCore.QRect(100, 650, 131, 30))
        self.fileEdit_4.setObjectName("fileEdit_4")

        self.displaylabel_4= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_4.setGeometry(QtCore.QRect(580, 35, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        self.displaylabel_4.setFont(font)
        self.displaylabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_4.setObjectName("displaylabel_4")
               
        

        Option4.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Option4)
        self.statusbar.setObjectName("statusbar")

        Option4.setStatusBar(self.statusbar)

        self.retranslateUi(Option4)
        QtCore.QMetaObject.connectSlotsByName(Option4)

    def retranslateUi(self, Option4):
        _translate = QtCore.QCoreApplication.translate
        Option4.setWindowTitle(_translate("Option4", "Interval endurance"))
        self.startButt_4.setText(_translate("Option4", "START"))
        self.stopButt_4.setText(_translate("Option4", "STOP"))
        self.title.setText(_translate("Option4", "<html><head/><body><p><span style=\" font-size:12pt;\">INTERVAL ENDURANCE</span></p></body></html>"))
        self.backButt_4.setText(_translate("Option4", "BACK TO OPTIONS"))
        self.saveButt_4.setText(_translate("Option4", "SAVE"))
        self.label.setText(_translate("Option4", "<html><head/><body><p>Time (sec)</p></body></html>"))
        self.label_2.setText(_translate("Option4", "<html><head/><body><p>Everadge</p></body></html>"))
        self.filename4.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
 

        
    def clicked1(self):
        o = Thread(target = self.connect)
        o.start()

    def clicked2(self):
        p = Thread(target = self.disconnect)
        p.start()
        
    def clicked3(self):
        q = Thread(target = self.close)
        q.start()

    def clicked4(self):
        r = Thread(target = self.save)
        r.start()     
                        
        

    def connect(self):
        self.clean = 0
        
        ser = ardconnect2.ardconnect()
              
        while(self.clean == 0):
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))

            self.straight.append(value)
                
                        
            self.lcdNumber.display(value)
            self.plot.update_graph3(value, self.i, self.teeth, self.j)
            s = Thread(target = self.plotvalue)
            u = Thread(target = self.timesim)
            
            s.start()
            u.start()

            s.join()
            u.join()            

            self.stopwatch.start()
            
            
                  
            if(self.timepoint > 50) and (self.state == 1) and (self.val > 22) and (value < self.rang) :
                self.stopwatch.stop()
                self.pulltime = int(self.stopwatch.duration)
                self.displaylabel1_4.setText(str(int(self.pulltime)))
                self.displaylabel_4.setText("Interval endurance test is finish")
                
                
            elif(self.timepoint > 50) and (self.state == 2) and (self.val < 22) and (value < self.rang) :
                
                self.stopwatch.stop()
                self.pulltime = int(self.stopwatch.duration)
                self.displaylabel1_4.setText(str(int(self.pulltime)))
                self.displaylabel_4.setText("Interval endurance test is finish")


    def plotvalue(self):
    
        self.i += 1
        self.j += 1
        self.spn = self.spinBox.value()
        self.rang = self.spn - 5
        self.rang2 = self.spn + 5 

        if(self.state == 0) and (self.val == 0):
            self.state = 1
            self.val += 1
            self.teeth = 0
            
        elif(self.state == 1) and (self.val < 50):
            self.state = 1
            self.val += 1
            self.teeth = 0
           
        elif(self.state == 1) and (self.val >= 50):
            self.state = 2
            self.val -= 1
            self.teeth = self.spn
            
        elif(self.state == 2) and (self.val > 0):
            self.state = 2
            self.val -= 1
            self.teeth = self.spn
            
        elif(self.state == 2) and (self.val == 0):
            self.state = 1
            self.val += 1
            self.teeth = 0
            
    def timesim(self):
        if(self.state2 ==0):
            self.timepoint += 1

           
    def disconnect(self):
        self.clean3 = 1
        self.displaylabel1_4.setText("")
        self.displaylabel_4.setText("")
        self.plot.canvas.axes.clear()
        self.state = 0
        
    def save(self):
        
        self.clean3 = 1
        self.name = self.fileEdit_4.toPlainText()        
        
        with open("%s.csv"%self.name,"a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([self.pulltime,self.straight])
        self.displaylabel_4.setText("Straight endurance saved")
            

    def close(self):
        Ui_Option4.destroy()        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option4 = QtWidgets.QMainWindow()
    ui = Ui_Option4()
    ui.setupUi(Option4)
    Option4.show()
    sys.exit(app.exec_())
