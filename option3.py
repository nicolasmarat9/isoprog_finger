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
import ctypes
import importlib


class Ui_Option3(object):
    
    def setupUi(self, Option3):
        
        self.rang = 0
        self.rang2 = 0
        self.i = 0
        self.j = 35
        self.spn = 0
        self.state = 0
        self.state2 = 0
        self.state3 = 0        
        self.straight = []
        self.straight_2 = []
        self.pulltime = 0
        self.pulltime_2 = 0
        self.timepoint = 0
        self.intens = 0
        self.intens2 = 0
        self.timer = 0
        self.clean = 0
        self.peakloadleft = []
        self.peakloadright = []
        self.averagepeakright = 0
        self.averagepeakleft = 0
        
        
        Option3.setObjectName("Option3")
        Option3.resize(1427, 969)
        Option3.move(488, 3)
        
        self.centralwidget = QtWidgets.QWidget(Option3)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

        self.displaylabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_3.setGeometry(QtCore.QRect(655, 5, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.displaylabel_3.setFont(font)
        self.displaylabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_3.setObjectName("displaylabel_3")

        self.displaylabel3_3= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel3_3.setGeometry(QtCore.QRect(25 ,360, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.displaylabel3_3.setFont(font)
        self.displaylabel3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel3_3.setObjectName("displaylabel3_3")

        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(130, 90, 141, 61))
        self.lcdNumber_3.setObjectName("lcdNumber")

        self.startButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_3.setGeometry(QtCore.QRect(30, 90, 71, 41))
        self.startButt_3.setObjectName("startButt_3")
        self.startButt_3.clicked.connect(self. clicked1_3)

        self.stopButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_3.setGeometry(QtCore.QRect(30, 150, 71, 41))
        self.stopButt_3.setObjectName("stopButt_3")
        self.stopButt_3.clicked.connect(self. clicked2_3)
        
        self.nextButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.nextButt_3.setGeometry(QtCore.QRect(170, 160, 80, 41))
        self.nextButt_3.setObjectName("next_3")
        self.nextButt_3.clicked.connect(self. clicked5_3)
        
        self.title_3 = QtWidgets.QLabel(self.centralwidget)
        self.title_3.setGeometry(QtCore.QRect(30, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.title_3.setFont(font)                
        self.title_3.setObjectName("title")

        self.backButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_3.setGeometry(QtCore.QRect(30, 890, 115, 31))
        self.backButt_3.setObjectName("backButt_3")
        self.backButt_3.clicked.connect(self. clicked3_3)

        self.backButt2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt2_3.setGeometry(QtCore.QRect(150, 890, 115, 31))
        self.backButt2_3.setObjectName("backButt_3")
        self.backButt2_3.clicked.connect(self. clicked7_3)        

        self.saveButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_3.setGeometry(QtCore.QRect(30, 840, 235, 31))
        self.saveButt_3.setObjectName("saveButt_4")
        self.saveButt_3.clicked.connect(self. clicked4_3)

        self.displaylabel1_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel1_3.setGeometry(QtCore.QRect(170, 210, 80, 31))
        self.displaylabel1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel1_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel1_3.setObjectName("displaylabel1_3")

        self.displaylabel2_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel2_3.setGeometry(QtCore.QRect(170, 260, 80, 31))
        self.displaylabel2_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel2_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel2_3.setObjectName("displaylabel2_3")

        self.timelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.timelabel_3.setGeometry(QtCore.QRect(40, 210, 200, 31))
        self.timelabel_3.setObjectName("timelabel_3")

        self.everadgelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.everadgelabel_3.setGeometry(QtCore.QRect(40, 260, 200, 31))
        self.everadgelabel_3.setObjectName("everadgelabel_3")

        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(50, 320, 211, 35))
        self.spinBox_3.setMaximum(200)
        self.spinBox_3.setObjectName("spinBox_3")

        self.namelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_3.setGeometry(QtCore.QRect(40, 790, 211, 30))
        self.namelabel_3.setObjectName("namelabel_3")

        self.handlabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_3.setGeometry(QtCore.QRect(40, 650, 130, 30))
        self.handlabel_3.setObjectName("handlabel_3") 

        self.notelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_3.setGeometry(QtCore.QRect(40, 700, 211, 30))
        self.notelabel_3.setObjectName("notelabel_3")

        self.noteEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_3.setGeometry(QtCore.QRect(130, 700, 131, 70))
        self.noteEdit_3.setObjectName("noteEdit_3")

        self.handbox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.handbox_3.setGeometry(QtCore.QRect(130, 650, 131, 30))
        self.handbox_3.setObjectName("handbox_3")
        self.handbox_3.addItems(['', 'Drag', 'Half crimp', 'Full crimp'])        
        
        self.fileEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fileEdit_3.setGeometry(QtCore.QRect(130, 790, 131, 30))
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
        self.backButt_3.setText(_translate("Option3", "PEAK RIGHT"))
        self.backButt2_3.setText(_translate("Option3", "PEAK LEFT"))        
        self.saveButt_3.setText(_translate("Option3", "SAVE"))
        self.nextButt_3.setText(_translate("Option3", "NEXT"))        
        self.timelabel_3.setText(_translate("Option3", "<html><head/><body><p>Time right (sec)</p></body></html>"))
        self.everadgelabel_3.setText(_translate("Option3", "<html><head/><body><p>Time left (sec)</p></body></html>"))
        self.namelabel_3.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.handlabel_3.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_3.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
  

        
    def clicked1_3(self):
        k = Thread(target = self.connect_3)
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
                
    def clicked5_3(self):
        n = Thread(target = self.next)
        n.start()
        
    def clicked7_3(self):
        slup = Thread(target = self.close2)
        slup.start()                                     
        

    def connect_3(self):
        self.clean = 0
        self.spn = 0
        self.state = 0
        self.state2 = 0
        ser = ardconnect2.ardconnect()
        z = Thread(target = self.timersec)
        z.start() 

        if(self.state3 == 0):
            
            while(self.state == 0):
                            
                ser_bytes = ser.readline()
                value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                self.straight.append(value)
                            
                self.lcdNumber_3.display(value)
                self.plot.update_graph2(value, self.i, self.j, self.spn)
                
                self.i += 1
                self.j += 1
                self.spn = self.spinBox_3.value()
                self.intens = self.spinBox_3.value()
                self.rang  = self.spn -5
                self.rang2 = self.spn +8

                v = Thread(target = self.timesim)
                v.start()
                

                
                if(self.state2 == 0) and(self.timepoint > 25):
                    self.displaylabel_3.setText("START") 
                    
                    
                    if(self.state2 == 0) and (self.timepoint > 50) and (value < self.rang) or (value > self.rang2) : 
                        self.pulltime = self.timer
                        self.displaylabel1_3.setText(str(int(self.pulltime)))
                        self.displaylabel_3.setText("Straight endurance test is finish")
                        self.state2 = 1
                        
                        
                  

        elif(self.state3 == 1):

            while(self.state == 0):
                
                            
                ser_bytes = ser.readline()
                value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                self.straight_2.append(value)
                            
                self.lcdNumber_3.display(value)
                self.plot.update_graph2(value, self.i, self.j, self.spn)
                
                self.i += 1
                self.j += 1
                self.spn = self.spinBox_3.value()
                self.intens2 = self.spinBox_3.value()
                self.rang  = self.spn -5
                self.rang2 = self.spn +8

                v = Thread(target = self.timesim)
                v.start()

                
                if(self.state2 == 0) and(self.timepoint > 25):
                    self.displaylabel_3.setText("START") 
                    
                    
                    if(self.state2 == 0) and (self.timepoint > 50) and (value < self.rang) or (value > self.rang2) : 
                        self.pulltime_2 = self.timer
                        self.displaylabel2_3.setText(str(int(self.pulltime_2)))
                        self.displaylabel_3.setText("Straight endurance test is finish")
                        self.state2 = 1
                        

    def plotvalue(self):
    
        self.i += 1
        self.j += 1
        self.spn = self.spinBox.value()
        self.rang = self.spn - 5
        self.rang2 = self.spn + 5 
                
    def timesim(self):
        if(self.state2 == 0):
            self.timepoint += 1

    def timersec(self):
        time.sleep(2)
        while(self.clean == 0):
            self.timer += 1
            time.sleep(1)
            self.displaylabel3_3.setText(str(int(self.timer)))         


    def next(self):
                     
        if(self.state3 == 0):
            self.state3 = 1
        elif(self.state3 == 1):
            self.state3 = 0
        self.clean = 1
        self.timer = 0
        self.state = 1
        self.state2 = 1
        self.displaylabel_3.setText("") 
        self.displaylabel3_3.setText("")
        
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()
        
        self.i = 0
        self.j = 35        
        self.timepoint = 0
        self.val = 0
        self.rang = 0
        self.rang2 = 0
        self.spn = 0
        
          
            
    def disconnect(self):
        self.timer = 0
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()
        
        self.i = 0
        self.j = 35        
        self.clean = 1
        self.displaylabel1_3.setText("")
        self.displaylabel2_3.setText("")
        self.displaylabel_3.setText("")
        self.displaylabel3_3.setText("")
        
        self.state = 1
        self.state2 = 1
        self.spn = 0
        self.state3 = 0
        self.straight.clear()
        self:straight_2.clear()
        self.rang = 0
        self.rang2 = 0
        self.pulltime = 0
        self.pulltime_2 = 0
        self.timepoint = 0
        self.intens = 0
        self.intens2 = 0
        
        
        
    def save(self):
        
        
        self.name = self.fileEdit_3.toPlainText()
        self.notes = self.noteEdit_3.toPlainText()
        self.hand = str(self.handbox_3.currentText())


        df = pd.read_csv("%s.csv"%self.name)
        data1 = [self.notes]
        df["straight endurance notes"] = data1
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data2 = [self.hand]
        df["straight endurance style"] = data2
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data3 = [self.intens]
        df["right strend intensity"] = data3
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data4 = [self.intens2]
        df["left strend intensity"] = data4
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data5 = [self.pulltime]
        df["right strend pulling time"] = data5
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data6 = [self.pulltime_2]
        df["left strend pulling time"] = data6
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data7 = [self.straight]
        df["right strend pulling data"] = data7
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data8 = [self.straight_2]
        df["left strend pulling data"] = data8
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

    
        ctypes.windll.user32.MessageBoxW(0, "straight endurance data saved", "Saved", 1)
        self.fileEdit_3.clear()
        self.noteEdit_3.clear()
        self.handbox_3.clear()
            

    def close(self):
        self.name = self.fileEdit_3.toPlainText()
        with open("%s.csv"%self.name,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string4 = ''
                for c in (row["peakloadright"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string4 += c
                
                self.peakloadright = list(str.split(string4))
                self.peakloadright = [float(i) for i in self.peakloadright]
                self.averagepeakright = sum(self.peakloadright) / len(self.peakloadright)
                self.averagepeakright = round(self.averagepeakright * 0.6)
                self.spinBox_3.setValue(self.averagepeakright)
                

    def close2(self):
        self.name = self.fileEdit_3.toPlainText()
        with open("%s.csv"%self.name,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["peakloadleft"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c

                self.peakloadleft = list(str.split(string2))
                self.peakloadleft = [float(i) for i in self.peakloadleft]
                self.averagepeakleft = sum(self.peakloadleft) / len(self.peakloadleft)
                self.averagepeakleft= round(self.averagepeakleft * 0.6)
                self.spinBox_3.setValue(self.averagepeakleft)
                
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option3 = QtWidgets.QMainWindow()
    ui = Ui_Option3()
    ui.setupUi(Option3)
    Option3.show()
    sys.exit(app.exec_())





    
