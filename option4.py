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

class Ui_Option4(object):
    
    def setupUi(self,Option4 ):
        
        self.rang = 0
        self.rang2 =  0
        self.state = 0
        self.state2 = 0
        self.state3 = 0
        self.clean = 0
        self.clean2 = 0

        self.value = 0
        self.teeth = 0
        self.val = 0    
        self.i = 0
        self.j = 25
        self.spn = 0
        self.timer = 0
        
        self.intens = 0
        self.intens2 = 0
        self.inter = []
        self.inter2 = []
        self.interm = []
        self.interm2 = []
        self.timepoint = 0
        self.pulltime = 0
        self.pulltime2 = 0
        self.peakloadleft = []
        self.peakloadright = []
        self.averagepeakright = 0
        self.averagepeakleft = 0        
        self.state4 = 0       
        
        
        Option4.setObjectName("Option4")
        Option4.resize(1427, 969)
        Option4.move(488, 3)
       
        self.centralwidget = QtWidgets.QWidget(Option4)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(130, 90, 141, 61))
        self.lcdNumber_4.setObjectName("lcdNumber")

        self.startButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_4.setGeometry(QtCore.QRect(30, 90, 71, 41))
        self.startButt_4.setObjectName("butt1")
        self.startButt_4.clicked.connect(self. clicked1)

        self.stopButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_4.setGeometry(QtCore.QRect(30, 150, 71, 41))
        self.stopButt_4.setObjectName("stopButt_4")
        self.stopButt_4.clicked.connect(self. clicked2)

        self.nextButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.nextButt_4.setGeometry(QtCore.QRect(170, 160, 80, 41))
        self.nextButt_4.setObjectName("next_4")
        self.nextButt_4.clicked.connect(self. clicked5)        

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.title.setFont(font)                                     
        self.title.setObjectName("title")

        self.backButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_4.setGeometry(QtCore.QRect(30, 890, 115, 31))
        self.backButt_4.setObjectName("backButt_4")
        self.backButt_4.clicked.connect(self. clicked3)

        self.backButt2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt2_4.setGeometry(QtCore.QRect(150, 890, 115, 31))
        self.backButt2_4.setObjectName("backButt2_4")
        self.backButt2_4.clicked.connect(self. clicked7_3)           

        self.saveButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_4.setGeometry(QtCore.QRect(30, 840, 235, 31))
        self.saveButt_4.setObjectName("saveButt_4")
        self.saveButt_4.clicked.connect(self. clicked4)

        self.displaylabel1_4 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel1_4.setGeometry(QtCore.QRect(170, 210, 80, 31))
        self.displaylabel1_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel1_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel1_4.setObjectName("displaylabel1_4")

        self.displaylabel2_4 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel2_4.setGeometry(QtCore.QRect(170, 260, 80, 31))
        self.displaylabel2_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displaylabel2_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displaylabel2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel2_4.setObjectName("displaylabel2_4")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 210, 200, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 200, 31))
        self.label_2.setObjectName("label_2")

        self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_7.setGeometry(QtCore.QRect(205, 320, 60, 35))
        self.spinBox_7.setMaximum(200)
        self.spinBox_7.setObjectName("spinBox")

        self.peaklabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.peaklabel_4.setGeometry(QtCore.QRect(130, 320, 60, 35))
        self.peaklabel_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.peaklabel_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.peaklabel_4.setAlignment(QtCore.Qt.AlignCenter)        
        self.peaklabel_4.setObjectName("peaklabel_4")
        
        self.goallabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.goallabel_4.setGeometry(QtCore.QRect(40, 320, 100, 30))
        self.goallabel_4.setObjectName("goallabel_4")        
               
        Option4.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Option4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        
        self.filename4 = QtWidgets.QLabel(self.centralwidget)
        self.filename4.setGeometry(QtCore.QRect(40, 790, 211, 30))
        self.filename4.setObjectName("filename4")        
        
        self.fileEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fileEdit_4.setGeometry(QtCore.QRect(130, 790, 131, 30))
        self.fileEdit_4.setObjectName("fileEdit_4")

        self.handlabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_4.setGeometry(QtCore.QRect(40, 650, 130, 30))
        self.handlabel_4.setObjectName("handlabel_4") 

        self.notelabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_4.setGeometry(QtCore.QRect(40, 700, 211, 30))
        self.notelabel_4.setObjectName("notelabel_4")

        self.noteEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_4.setGeometry(QtCore.QRect(130, 700, 131, 70))
        self.noteEdit_4.setObjectName("noteEdit_4")

        self.handbox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.handbox_4.setGeometry(QtCore.QRect(130, 650, 131, 30))
        self.handbox_4.setObjectName("handbox_3")
        self.handbox_4.addItems(['', 'Drag', 'Half crimp', 'Full crimp'])         

        self.displaylabel_4= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_4.setGeometry(QtCore.QRect(655, 5, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.displaylabel_4.setFont(font)
        self.displaylabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_4.setObjectName("displaylabel_4")
               
        self.displaylabel3_4= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel3_4.setGeometry(QtCore.QRect(25 ,360, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.displaylabel3_4.setFont(font)
        self.displaylabel3_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel3_4.setObjectName("displaylabel3_4")
        

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
        self.stopButt_4.setText(_translate("Option4", "RESET"))
        self.title.setText(_translate("Option4", "<html><head/><body><p><span style=\" font-size:12pt;\">INTERVAL ENDURANCE</span></p></body></html>"))
        self.backButt_4.setText(_translate("Option4", "PEAK RIGHT"))
        self.backButt2_4.setText(_translate("Option4", "PEAK LEFT"))        
        self.saveButt_4.setText(_translate("Option4", "SAVE"))
        self.nextButt_4.setText(_translate("Option4", "NEXT"))
        self.label.setText(_translate("Option4", "<html><head/><body><p>Time right (sec)</p></body></html>"))
        self.label_2.setText(_translate("Option4", "<html><head/><body><p>Time left (sec)</p></body></html>"))
        self.filename4.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.handlabel_4.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_4.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
        self.goallabel_4.setText(_translate("Option1", "<html><head/><body><p>Goal line</p></body></html>"))  
        

        
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
        
    def clicked5(self):
        n = Thread(target = self.next)
        n.start()
        
    def clicked7_3(self):
        guh = Thread(target = self.close2)
        guh.start()                       

    def connect(self):
        self.displaylabel3_4.setText("")
        self.state2 = 0
        self.spn = 0
        self.clean = 0
        self.clean2 = 0
        ser = ardconnect2.ardconnect()
        w = Thread(target = self.timersec)
        w.start()
        
        if self.state3 == 0:
            
            while (self.clean2 == 0):
                            
                ser_bytes = ser.readline()
                self.value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                self.inter.append(self.value)
              
                            
                self.lcdNumber_4.display(self.value)
                self.plot.update_graph3(self.value, self.i, self.teeth, self.j)
                s = Thread(target = self.plotvalue)
                u = Thread(target = self.timesim)
                
                s.start()
                u.start()         

                s.join()
                u.join()

                if(self.state2 == 0) and (self.timepoint > 50) and (self.state == 1) and (self.val < 22) and (self.value < self.rang) :
                    self.pulltime = self.timer
                    self.displaylabel1_4.setText(str(int(self.pulltime)))
                    self.displaylabel_4.setText("Interval endurance test is finished")
                    self.interm = self.inter
                    self.intens = self.spn
                    self.state2 = 1
            
                elif(self.state2 == 0) and (self.timepoint > 50) and (self.state == 2) and (self.val < 22) and (self.value < self.rang) :
                    self.pulltime = self.timer
                    self.displaylabel1_4.setText(str(int(self.pulltime)))
                    self.displaylabel_4.setText("Interval endurance test is finished")
                    self.interm = self.inter
                    self.intens = self.spn
                    self.state2 = 1
                    
        if self.state3 == 1:
            
            while (self.clean2 == 0):
                            
                ser_bytes = ser.readline()
                self.value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                self.inter2.append(self.value)
                                           
                self.lcdNumber_4.display(self.value)
                self.plot.update_graph3(self.value, self.i, self.teeth, self.j)
                s = Thread(target = self.plotvalue)
                u = Thread(target = self.timesim)
                               
                s.start()
                u.start()
                
                s.join()
                u.join()
                   
                if(self.state2 == 0) and (self.timepoint > 50) and (self.state == 1) and (self.val < 22) and (self.value < self.rang) :
                    self.pulltime2 = self.timer 
                    self.displaylabel2_4.setText(str(int(self.pulltime2)))
                    self.displaylabel_4.setText("Interval endurance test is finish")
                    self.interm2 = self.inter2
                    self.intens2 = self.spn
                    self.state2 = 1
            
                elif(self.state2 == 0) and (self.timepoint > 50) and (self.state == 2) and (self.val < 22) and (self.value < self.rang) :
                    self.pulltime2 = self.timer 
                    self.displaylabel2_4.setText(str(int(self.pulltime2)))
                    self.displaylabel_4.setText("Interval endurance test is finish")
                    self.interm2 = self.inter2
                    self.intens2 = self.spn
                    self.state2 = 1


    def plotvalue(self):
    
        self.i += 1
        self.j += 1
        if(self.state4 == 0):
            self.spn = self.spinBox_7.value()
        elif(self.state4 == 1):
            self.spn = self.averagepeakright
        elif(self.state4 == 2):
            self.spn = self.averagepeakleft 
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

    def timersec(self):
        time.sleep(6)
        while(self.clean == 0):
            self.timer += 1
            time.sleep(1)
            self.displaylabel3_4.setText(str(int(self.timer)))
            

    def next(self):
       
        if(self.state3 == 0):
            self.state3 = 1
        elif(self.state3 == 1):
            self.state3 = 0
        self.clean = 1    
        self.clean2 = 1
        self.timer = 0
        self.displaylabel_4.setText("")
        self.displaylabel3_4.setText("")

        self.i = 0
        self.j = 25        
        self.timepoint = 0
        self.state = 0
        self.val = 0
        self.teeth = 0
        self.value = 0
        
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()        

        
   
    def disconnect(self):
        
        self.state2 = 1
        self.clean = 1
        self.clean2 = 1
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.inter.clear()
        self.inter2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()
        
        self.i = 0
        self.j = 25        
        self.displaylabel1_4.setText("")
        self.displaylabel2_4.setText("")
        self.displaylabel_4.setText("")
        self.displaylabel3_4.setText("") 
        self.state = 0
        self.state3 = 0
        self.val = 0
        self.teeth = 0
        self.value = 0
        self.intens = 0
        self.intens2 = 0
        self.timer = 0
        self.pulltime = 0
        self.pulltime2 = 0
        selff.peaklabel_4.setText("")
        
        
    def save(self):
        
        
        self.name = self.fileEdit_4.toPlainText()
        self.notes = self.noteEdit_4.toPlainText()
        self.hand = str(self.handbox_4.currentText())        
        

        df = pd.read_csv("%s.csv"%self.name)
        data1 = [self.notes]
        df["interval endurance notes"] = data1
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data2 = [self.hand]
        df["interval endurance style"] = data2
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data3 = [self.intens]
        df["right intend intensity"] = data3
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data4 = [self.intens2]
        df["left intend intensity"] = data4
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data5 = [self.pulltime]
        df["right intend pulling time"] = data5
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data6 = [self.pulltime2]
        df["left intend pulling time"] = data6
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data7 = [self.interm]
        df["right intend pulling data"] = data7
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data8 = [self.interm2]
        df["left intend pulling data"] = data8
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

          
        ctypes.windll.user32.MessageBoxW(0, "interval endurance data saved", "Saved", 1)
        self.fileEdit_4.clear()
        self.noteEdit_4.clear()
        self.handbox_4.clear()


    def close(self):
        self.name = self.fileEdit_4.toPlainText()
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
                self.peaklabel_4.setText(str(self.averagepeakright))
                self.state4 = 1
        
        

    def close2(self):
        self.name = self.fileEdit_4.toPlainText()
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
                self.averagepeakleft = round(self.averagepeakleft * 0.6)
                self.peaklabel_4.setText(str(self.averagepeakleft))
                self.state4 = 2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option4 = QtWidgets.QMainWindow()
    ui = Ui_Option4()
    ui.setupUi(Option4)
    Option4.show()
    sys.exit(app.exec_())
