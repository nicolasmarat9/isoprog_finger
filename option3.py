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
import ctypes
import importlib
import serial.tools.list_ports
import datetime


class Ui_Option3(object):
    
    def setupUi(self, Option3):

        ### variables ###
        
        self.rang = 0
        self.rang2 = 0
        self.i = 0
        self.j = 3.5
        self.spn = 0
        self.state = 0
        self.state2 = 0
        self.state3 = 0
        self.mainstate = 0
        self.straight = []
        self.straightx = []
        self.straight_2 = []
        self.straight_2x = []
        
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
        self.state4 = 0
        
        ### option 3 straight endurance ###

            ## window setting ##        
        
        Option3.setObjectName("Option3")
        Option3.resize(1427, 969)
        Option3.move(488, 3)
        Option3.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option3)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

            ## titles and display labels ##

        self.StraightEnduTitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.StraightEnduTitlelabel.setGeometry(QtCore.QRect(30, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.StraightEnduTitlelabel.setFont(font)                
        self.StraightEnduTitlelabel.setObjectName("StraightEnduTitlelabel")        

        self.displaylabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_3.setGeometry(QtCore.QRect(610, 5, 490, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displaylabel_3.setFont(font)
        self.displaylabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_3.setObjectName("displaylabel_3")

        self.timerlabel = QtWidgets.QLabel(self.centralwidget)
        self.timerlabel.setGeometry(QtCore.QRect(127, 365, 110, 31))
        self.timerlabel.setObjectName("timerlabel") 

        self.displaytimerlabel= QtWidgets.QLabel(self.centralwidget)
        self.displaytimerlabel.setGeometry(QtCore.QRect(25 ,340, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.displaytimerlabel.setFont(font)
        self.displaytimerlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displaytimerlabel.setObjectName("displaytimerlabel")

        self.currentWeightlabel = QtWidgets.QLabel(self.centralwidget)
        self.currentWeightlabel.setGeometry(QtCore.QRect(161, 80, 110, 31))
        self.currentWeightlabel.setObjectName("currentWeightlabel")

        self.displayWeightlabel= QtWidgets.QLabel(self.centralwidget)
        self.displayWeightlabel.setGeometry(QtCore.QRect(88 ,40 , 246, 200))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setWeight(65)
        self.displayWeightlabel.setFont(font)
        self.displayWeightlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayWeightlabel.setObjectName("displayWeightlabel")

        self.timeRightlabel = QtWidgets.QLabel(self.centralwidget)
        self.timeRightlabel.setGeometry(QtCore.QRect(36, 250, 100, 51))
        self.timeRightlabel.setAlignment(QtCore.Qt.AlignCenter) 
        self.timeRightlabel.setObjectName("timeRightlabel")
        
        self.displayTimeRightlabel = QtWidgets.QLabel(self.centralwidget)
        self.displayTimeRightlabel.setGeometry(QtCore.QRect(45, 300, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displayTimeRightlabel.setFont(font)           
        self.displayTimeRightlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayTimeRightlabel.setObjectName("displayTimeRightlabel")
        
        self.timeLeftlabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLeftlabel.setGeometry(QtCore.QRect(170, 250, 100, 51))
        self.timeLeftlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLeftlabel.setObjectName("timeLeftlabel")

        self.displayTimeLeftlabel = QtWidgets.QLabel(self.centralwidget)
        self.displayTimeLeftlabel.setGeometry(QtCore.QRect(179, 300, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displayTimeLeftlabel.setFont(font)        
        self.displayTimeLeftlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayTimeLeftlabel.setObjectName("displayTimeLeftlabel")

        self.namelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_3.setGeometry(QtCore.QRect(40, 840, 211, 30))
        self.namelabel_3.setObjectName("namelabel_3")
        
        self.nameEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_3.setGeometry(QtCore.QRect(130, 840, 131, 30))
        self.nameEdit_3.setObjectName("nameEdit_3")

        self.handlabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_3.setGeometry(QtCore.QRect(40, 700, 130, 30))
        self.handlabel_3.setObjectName("handlabel_3")

        self.handbox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.handbox_3.setGeometry(QtCore.QRect(130, 700, 131, 30))
        self.handbox_3.setObjectName("handbox_3")
        self.handbox_3.addItems(['', 'Drag', 'Half crimp', 'Full crimp']) 

        self.notelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_3.setGeometry(QtCore.QRect(40, 750, 211, 30))
        self.notelabel_3.setObjectName("notelabel_3")

        self.noteEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_3.setGeometry(QtCore.QRect(130, 750, 131, 70))
        self.noteEdit_3.setObjectName("noteEdit_3")
        
        self.goallabel = QtWidgets.QLabel(self.centralwidget)
        self.goallabel.setGeometry(QtCore.QRect(40, 650, 100, 30))
        self.goallabel.setObjectName("goallabel")

        self.displayGoallabel = QtWidgets.QLabel(self.centralwidget)
        self.displayGoallabel.setGeometry(QtCore.QRect(130, 650, 55, 35))
        self.displayGoallabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.displayGoallabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.displayGoallabel.setAlignment(QtCore.Qt.AlignCenter)        
        self.displayGoallabel.setObjectName("displayGoallabel")

        self.goalBox = QtWidgets.QSpinBox(self.centralwidget)
        self.goalBox.setGeometry(QtCore.QRect(200, 650, 60, 35))
        self.goalBox.setMaximum(200)
        self.goalBox.setObjectName("goalBox")
        
            ## buttons ##

        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.startButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt.setObjectName("startButt")
        self.startButt.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt.setIconSize(QtCore.QSize(90, 90))          
        self.startButt.clicked.connect(self.clicked_startMeasures)

        self.stopButt = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt.setGeometry(QtCore.QRect(30, 200, 90, 45))
        self.stopButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt.setObjectName("stopButt")
        self.stopButt.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt.setIconSize(QtCore.QSize(90, 90))         
        self.stopButt.clicked.connect(self.clicked_stop_clear)

        self.saveButt = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt.setGeometry(QtCore.QRect(30, 890, 90, 45))
        self.saveButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.saveButt.setObjectName("saveButt")
        self.saveButt.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.saveButt.setIconSize(QtCore.QSize(90, 90))        
        self.saveButt.clicked.connect(self.clicked_saveMeasures)        
        
        self.nextButt = QtWidgets.QPushButton(self.centralwidget)
        self.nextButt.setGeometry(QtCore.QRect(30, 145, 90, 45))
        self.nextButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.nextButt.setObjectName("nextButt")
        self.nextButt.setIcon(QtGui.QIcon("pushbutt/ziconpush11.png"))
        self.nextButt.setIconSize(QtCore.QSize(90, 90))        
        self.nextButt.clicked.connect(self.clicked_nextMeasures)
 
        self.rightButt = QtWidgets.QPushButton(self.centralwidget)
        self.rightButt.setGeometry(QtCore.QRect(50, 590, 90, 45))
        self.rightButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.rightButt.setObjectName("rightButt")
        self.rightButt.setIcon(QtGui.QIcon("pushbutt/ziconpush13.png"))
        self.rightButt.setIconSize(QtCore.QSize(90, 90))        
        self.rightButt.clicked.connect(self.clicked_getRightPeak)

        self.leftButt = QtWidgets.QPushButton(self.centralwidget)
        self.leftButt.setGeometry(QtCore.QRect(160, 590, 90, 45))
        self.leftButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.leftButt.setObjectName("leftButt")
        self.leftButt.setIcon(QtGui.QIcon("pushbutt/ziconpush12.png"))
        self.leftButt.setIconSize(QtCore.QSize(90, 90))          
        self.leftButt.clicked.connect(self.clicked_getLeftPeak)        
            
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
        self.StraightEnduTitlelabel.setText(_translate("Option3", "<html><head/><body><p><span style=\" font-size:12pt;\">STRAIGHT ENDURANCE</span></p></body></html>"))
        self.timeRightlabel.setText("Time right\n(sec)")
        self.timeLeftlabel.setText("Time left\n(sec)")
        self.namelabel_3.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.handlabel_3.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_3.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
        self.goallabel.setText(_translate("Option1", "<html><head/><body><p>Goal line</p></body></html>"))  
        self.timerlabel.setText("Timer")
        self.currentWeightlabel.setText("Current weight") 
       
    def clicked_startMeasures(self):
        k = Thread(target = self.connect_3)
        k.start()

    def clicked_stop_clear(self):
        l = Thread(target = self.disconnect)
        l.start()

    def clicked_saveMeasures(self):
        n = Thread(target = self.save)
        n.start()     
                
    def clicked_nextMeasures(self):
        n = Thread(target = self.next)
        n.start()
        
    def clicked_getLeftPeak(self):
        slup = Thread(target = self.getLeftPeak)
        slup.start()                                     
        
    def clicked_getRightPeak(self):
        m = Thread(target = self.getRightPeak)
        m.start()

    def connect_3(self):
        self.clean = 0
        self.spn = 0
        self.state = 0
        self.state2 = 0

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
                        time.sleep(2)
                        self.displaylabel_3.setText("")
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_3.setText("No Sensor found")
            time.sleep(2)
            self.displaylabel_3.setText("")        
            raise IOError("No Sensor found")            
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)

        z = Thread(target = self.timersec)
        z.start() 

        ser_bytes = ser.readline()
        valueP1 = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        

        if(self.state3 == 0):
            self.displaylabel_3.setText("RIGHT HAND")
            
            while(self.state == 0):
                
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                value = round(valueP - valueP1, 1)
               
                self.straight.append(value)
                self.straightx.append(round(self.i, 1))
                
                self.displayWeightlabel.setText(str(value))
                self.plot.update_graph2(value, self.i, self.j, self.spn)
                
                self.i += 0.1
                self.j += 0.1
               
                if(self.state4 == 0):
                    self.spn = self.goalBox.value()
                elif(self.state4 == 1):
                    self.spn = self.averagepeakright
                elif(self.state4 == 2):
                    self.spn = self.averagepeakleft 
                self.rang  = self.spn -5
                self.rang2 = self.spn +8

                v = Thread(target = self.timesim)
                v.start()

                if(self.state2 == 0) and (self.timepoint > 50) and (value < self.rang) or (value > self.rang2) : 
                    self.pulltime = self.timer
                    self.displayTimeRightlabel.setText(str(int(self.pulltime)))
                    self.displaylabel_3.setText("Straight endurance test is finished")
                    self.intens = self.spn
                    self.state2 = 1

        elif(self.state3 == 1):
            self.displaylabel_3.setText("LEFT HAND")

            while(self.state == 0):
                            
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                value = round(valueP - valueP1, 1)

                
                self.straight_2.append(value)
                self.straight_2x.append(round(self.i, 1))
                
                self.displayWeightlabel.setText(str(value))
                self.plot.update_graph2(value, self.i, self.j, self.spn)
                
                self.i += 0.1
                self.j += 0.1
                
                if(self.state4 == 0):
                    self.spn = self.goalBox.value()
                elif(self.state4 == 1):
                    self.spn = self.averagepeakright
                elif(self.state4 == 2):
                    self.spn = self.averagepeakleft                    
                self.rang  = self.spn -5
                self.rang2 = self.spn +8

                v = Thread(target = self.timesim)
                v.start()
                   
                if(self.state2 == 0) and (self.timepoint > 50) and (value < self.rang) or (value > self.rang2) : 
                    self.pulltime_2 = self.timer
                    self.displayTimeLeftlabel.setText(str(int(self.pulltime_2)))
                    self.displaylabel_3.setText("Straight endurance test is finished")
                    self.intens2 = self.spn
                    self.state2 = 1
                
    def timesim(self):
        if(self.state2 == 0):
            self.timepoint += 1

    def timersec(self):
        time.sleep(2)
        while(self.clean == 0):
            self.timer += 1
            time.sleep(1)
            self.displaytimerlabel.setText(str(int(self.timer)))         

    def next(self):
        if(self.state3 == 0):
            self.state3 = 1
        elif(self.state3 == 1):
            self.state3 = 0
        self.clean = 1
        self.timer = 0
        self.state = 1
        self.state2 = 1
        self.state4 = 0
        self.displaylabel_3.setText("wait...") 
        self.displaytimerlabel.setText("")
        
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()
        self.plot.canvas.axes.set_ylim(0,90)
        self.plot.canvas.draw()
        
        self.i = 0
        self.j = 3.5        
        self.timepoint = 0
        self.val = 0
        self.rang = 0
        self.rang2 = 0
        time.sleep(2)
        self.displaylabel_3.setText("")
           
    def disconnect(self):
        self.state = 1
        self.state2 = 1
        self.clean = 1
        self.spn = 0
        self.state3 = 0
        self.state4 = 0      
        self.timer = 0
        time.sleep(1)
        
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()
        self.plot.canvas.axes.clear()
        self.plot.canvas.axes.set_ylim(0,90)
        self.plot.canvas.draw()
        
        self.i = 0
        self.j = 3.5        
        self.displayTimeRightlabel.setText("")
        self.displayTimeLeftlabel.setText("")
        self.displaylabel_3.setText("reset straight endurance")
        self.displaytimerlabel.setText("")
        self.displayGoallabel.setText("")

        self.straight.clear()
        self:straight_2.clear()
        self.rang = 0
        self.rang2 = 0
        self.pulltime = 0
        self.pulltime_2 = 0
        self.timepoint = 0
        self.intens = 0
        self.intens2 = 0
        self.peakloadleft = []
        self.peakloadright = []
        self.averagepeakright = 0
        self.averagepeakleft = 0
        self.goalBox.setValue(0)
        
        time.sleep(2.5)
        self.displaylabel_3.setText("")
       
    def save(self):
        self.name = self.nameEdit_3.toPlainText()
        self.notes = self.noteEdit_3.toPlainText()
        self.hand = str(self.handbox_3.currentText())
        dates = datetime.date.today()

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data1 = [self.notes]
        df["straight endurance notes"] = data1
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data2 = [self.hand]
        df["straight endurance style"] = data2
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data3 = [self.intens]
        df["right strend intensity"] = data3
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data4 = [self.intens2]
        df["left strend intensity"] = data4
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data5 = [self.pulltime]
        df["right strend pulling time"] = data5
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data6 = [self.pulltime_2]
        df["left strend pulling time"] = data6
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data7 = [self.straight]
        df["right strend pulling data"] = data7
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data9 = [self.straightx]
        df["right strend x pulling data"] = data9
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data8 = [self.straight_2]
        df["left strend pulling data"] = data8
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data10 = [self.straight_2x]
        df["left strend x pulling data"] = data10
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
    
        ctypes.windll.user32.MessageBoxW(0, "straight endurance data saved", "Saved", 0x00000000)
        self.nameEdit_3.clear()
        self.noteEdit_3.clear()
        self.handbox_3.clear()

    def getRightPeak(self):
        dates = datetime.date.today()
        self.name = self.nameEdit_3.toPlainText()
        with open("{0}/{0}%s.csv".format(self.name)%dates,"r") as f:
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
                self.displayGoallabel.setText(str(self.averagepeakright))
                self.state4 = 1

    def getLeftPeak(self):
        dates = datetime.date.today()
        self.name = self.nameEdit_3.toPlainText()
        with open("{0}/{0}%s.csv".format(self.name)%dates,"r") as f:
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
                self.displayGoallabel.setText(str(self.averagepeakleft))
                self.state4 = 2
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option3 = QtWidgets.QMainWindow()
    ui = Ui_Option3()
    ui.setupUi(Option3)
    Option3.show()
    sys.exit(app.exec_())





    
