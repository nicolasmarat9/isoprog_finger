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
import serial.tools.list_ports
import datetime


class Ui_Option4(object):
    
    def setupUi(self,Option4 ):

        ### variables ###        
        
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
        self.j = 2.5
        self.spn = 0
        self.timer = 0
        
        self.intens = 0
        self.intens2 = 0
        self.inter = []
        self.inter2 = []
        self.inter2x = []
        self.interx = []        
        self.interm = []
        self.interm2 = []
        self.timepoint4 = 0
        self.pulltime = 0
        self.pulltime2 = 0
        self.peakloadleft = []
        self.peakloadright = []
        self.averagepeakright = 0
        self.averagepeakleft = 0        
        self.state4 = 0
        
        ### option 3 straight endurance ###

            ## window setting ##         
        
        Option4.setObjectName("Option4")
        Option4.resize(1427, 969)
        Option4.move(488, 3)
        Option4.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
       
        self.centralwidget = QtWidgets.QWidget(Option4)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

            ## titles and display labels ##

        self.IntervalEnduTitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.IntervalEnduTitlelabel.setGeometry(QtCore.QRect(30, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.IntervalEnduTitlelabel.setFont(font)                                     
        self.IntervalEnduTitlelabel.setObjectName("IntervalEnduTitlelabel")        

        self.displaylabel_4= QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_4.setGeometry(QtCore.QRect(610, 5, 490, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displaylabel_4.setFont(font)
        self.displaylabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_4.setObjectName("displaylabel_4")

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
        
        self.namelabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_4.setGeometry(QtCore.QRect(40, 840, 211, 30))
        self.namelabel_4.setObjectName("namelabel_4")        
        
        self.nameEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_4.setGeometry(QtCore.QRect(130, 840, 131, 30))
        self.nameEdit_4.setObjectName("nameEdit_4")        

        self.handlabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_4.setGeometry(QtCore.QRect(40, 700, 130, 30))
        self.handlabel_4.setObjectName("handlabel_4") 

        self.handbox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.handbox_4.setGeometry(QtCore.QRect(130, 700, 131, 30))
        self.handbox_4.setObjectName("handbox_3")
        self.handbox_4.addItems(['', 'Drag', 'Half crimp', 'Full crimp'])
        
        self.notelabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_4.setGeometry(QtCore.QRect(40, 750, 211, 30))
        self.notelabel_4.setObjectName("notelabel_4")

        self.noteEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_4.setGeometry(QtCore.QRect(130, 750, 131, 70))
        self.noteEdit_4.setObjectName("noteEdit_4")
        
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
        
        self.startButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_4.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.startButt_4.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt_4.setObjectName("butt1")
        self.startButt_4.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt_4.setIconSize(QtCore.QSize(90, 90))         
        self.startButt_4.clicked.connect(self. clicked1)

        self.stopButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_4.setGeometry(QtCore.QRect(30, 200, 90, 45))
        self.stopButt_4.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt_4.setObjectName("stopButt_4")
        self.stopButt_4.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt_4.setIconSize(QtCore.QSize(90, 90))        
        self.stopButt_4.clicked.connect(self. clicked2)

        self.nextButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.nextButt_4.setGeometry(QtCore.QRect(30, 145, 90, 45))
        self.nextButt_4.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.nextButt_4.setObjectName("next_4")
        self.nextButt_4.setIcon(QtGui.QIcon("pushbutt/ziconpush11.png"))
        self.nextButt_4.setIconSize(QtCore.QSize(90, 90))                                     
        self.nextButt_4.clicked.connect(self. clicked5)        

        self.backButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt_4.setGeometry(QtCore.QRect(50, 590, 90, 45))
        self.backButt_4.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.backButt_4.setObjectName("backButt_4")
        self.backButt_4.setIcon(QtGui.QIcon("pushbutt/ziconpush13.png"))
        self.backButt_4.setIconSize(QtCore.QSize(90, 90))                                      
        self.backButt_4.clicked.connect(self. clicked3)

        self.backButt2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.backButt2_4.setGeometry(QtCore.QRect(160, 590, 90, 45))
        self.backButt2_4.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.backButt2_4.setObjectName("backButt2_4")
        self.backButt2_4.setIcon(QtGui.QIcon("pushbutt/ziconpush12.png"))
        self.backButt2_4.setIconSize(QtCore.QSize(90, 90))                                     
        self.backButt2_4.clicked.connect(self. clicked7_3)           

        self.saveButt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_4.setGeometry(QtCore.QRect(30, 890, 90, 45))
        self.saveButt_4.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.saveButt_4.setObjectName("saveButt_4")
        self.saveButt_4.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.saveButt_4.setIconSize(QtCore.QSize(90, 90))                                     
        self.saveButt_4.clicked.connect(self. clicked4)
       
               
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
        self.IntervalEnduTitlelabel.setText(_translate("Option4", "<html><head/><body><p><span style=\" font-size:12pt;\">INTERVAL ENDURANCE</span></p></body></html>"))
        self.timeRightlabel.setText("Time right\n(sec)")
        self.timeLeftlabel.setText("Time left\n(sec)")
        self.namelabel_4.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.handlabel_4.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_4.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
        self.goallabel.setText(_translate("Option1", "<html><head/><body><p>Goal line</p></body></html>"))  
        self.timerlabel.setText("Timer")
        self.currentWeightlabel.setText("Current weight")         

        
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
        self.displaytimerlabel.setText("")
        self.state2 = 0
        self.spn = 0
        self.clean = 0
        self.clean2 = 0

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
                        self.displaylabel_4.setText("Found Sensor on " + portName)
                        time.sleep(2)
                        self.displaylabel_4.setText("")
                        #print("Found Sensor on " + portName)                        
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_4.setText("No Sensor found")
            time.sleep(2)
            self.displaylabel_4.setText("")        
            raise IOError("No Sensor found")            
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)


        w = Thread(target = self.timersec)
        w.start()

        ser_bytes = ser.readline()
        valueP1 = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        
        
        
        if (self.state3 == 0):
            self.displaylabel_4.setText("RIGHT HAND")
            while (self.clean2 == 0):
                            
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                value = round(valueP - valueP1, 1)
                
                self.inter.append(value)
                self.interx.append(round(self.i, 1))              
                            
                self.displayWeightlabel.setText(str(value))
                self.plot.update_graph3(value, self.i, self.teeth, self.j)
                s = Thread(target = self.plotvalue)
                u = Thread(target = self.timesim)
                
                s.start()
                u.start()         

                s.join()
                u.join()

                if(self.state2 == 0) and (self.timepoint4 > 50) and (self.state == 1) and (self.val < 22) and (value < self.rang) :
                    self.pulltime = self.timer
                    self.displayTimeRightlabel.setText(str(int(self.pulltime)))
                    self.displaylabel_4.setText("Interval endurance test is finished")
                    self.interm = self.inter
                    self.intens = self.spn
                    self.state2 = 1
            
                elif(self.state2 == 0) and (self.timepoint4 > 50) and (self.state == 2) and (self.val < 22) and (value < self.rang) :
                    self.pulltime = self.timer
                    self.displayTimeRightlabel.setText(str(int(self.pulltime)))
                    self.displaylabel_4.setText("Interval endurance test is finished")
                    self.interm = self.inter
                    self.intens = self.spn
                    self.state2 = 1
                    
        elif (self.state3 == 1):
            if(self.clean == 0):
                self.displaylabel_4.setText("LEFT HAND")
            while (self.clean2 == 0):
                            
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                value = round(valueP - valueP1, 1)
                
                self.inter2.append(value)
                self.inter2x.append(round(self.i, 1))                
                                           
                self.displayWeightlabel.setText(str(value))
                self.plot.update_graph3(value, self.i, self.teeth, self.j)
                s = Thread(target = self.plotvalue)
                u = Thread(target = self.timesim)
                               
                s.start()
                u.start()
                
                s.join()
                u.join()
                   
                if(self.state2 == 0) and (self.timepoint4 > 50) and (self.state == 1) and (self.val < 22) and (value < self.rang) :
                    self.pulltime2 = self.timer 
                    self.displayTimeLeftlabel.setText(str(int(self.pulltime2)))
                    self.displaylabel_4.setText("Interval endurance test is finish")
                    self.interm2 = self.inter2
                    self.intens2 = self.spn
                    self.state2 = 1
            
                elif(self.state2 == 0) and (self.timepoint4 > 50) and (self.state == 2) and (self.val < 22) and (value < self.rang) :
                    self.pulltime2 = self.timer 
                    self.displayTimeLeftlabel.setText(str(int(self.pulltime2)))
                    self.displaylabel_4.setText("Interval endurance test is finish")
                    self.interm2 = self.inter2
                    self.intens2 = self.spn
                    self.state2 = 1


    def plotvalue(self):
    
        self.i += 0.1
        self.j += 0.1
        if(self.state4 == 0):
            self.spn = self.goalBox.value()
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
            self.timepoint4 += 1

    def timersec(self):
        time.sleep(6)
        while(self.clean == 0):
            self.timer += 1
            time.sleep(1)
            self.displaytimerlabel.setText(str(int(self.timer)))
            

    def next(self):
        #self.displaylabel_4.setText("wait...")
        if(self.state3 == 0):
            self.state3 = 1
        elif(self.state3 == 1):
            self.state3 = 0
        self.clean = 1    
        self.clean2 = 1
        self.timer = 0
        self.displaylabel_4.setText("wait...")
        self.displaytimerlabel.setText("")

        self.i = 0
        self.j = 2.5        
        self.timepoint4 = 0
        self.state = 0
        self.val = 0
        self.teeth = 0

        
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.x2.clear()
        self.plot.y2.clear()
        self.plot.linehand.clear()
        self.plot.lineprog.clear()
        self.plot.canvas.axes.set_ylim(0,90)
        self.plot.canvas.draw()
        time.sleep(2)
        self.displaylabel_4.setText("")
   
    def disconnect(self):
        
        self.state2 = 1
        self.clean = 1
        self.clean2 = 1
        self.spn = 0
        self.state = 0
        self.state3 = 0
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
        
        self.inter.clear()
        self.inter2.clear()
        self.interx.clear()
        self.inter2x.clear()
        
        self.i = 0
        self.j = 2.5        
        self.displayTimeRightlabel.setText("")
        self.displayTimeLeftlabel.setText("")
        self.displaylabel_4.setText("reset interval endurance")
        self.displaytimerlabel.setText("") 
        self.val = 0
        self.teeth = 0
        self.intens = 0
        self.intens2 = 0
        self.pulltime = 0
        self.pulltime2 = 0
        self.displayGoallabel.setText("")
        self.timepoint4 = 0
        self.goalBox.setValue(0)

        
        time.sleep(2.5)
        self.displaylabel_4.setText("")

                
    def save(self):
        
        dates = datetime.date.today()
        self.name = self.nameEdit_4.toPlainText()
        self.notes = self.noteEdit_4.toPlainText()
        self.hand = str(self.handbox_4.currentText())        
        

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data1 = [self.notes]
        df["interval endurance notes"] = data1
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data2 = [self.hand]
        df["interval endurance style"] = data2
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data3 = [self.intens]
        df["right intend intensity"] = data3
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data4 = [self.intens2]
        df["left intend intensity"] = data4
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data5 = [self.pulltime]
        df["right intend pulling time"] = data5
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data6 = [self.pulltime2]
        df["left intend pulling time"] = data6
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data7 = [self.interm]
        df["right intend pulling data"] = data7
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data8 = [self.interm2]
        df["left intend pulling data"] = data8
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data9 = [self.interx]
        df["right intend x pulling data"] = data9
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data10 = [self.inter2x]
        df["left intend x pulling data"] = data10
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")

          
        ctypes.windll.user32.MessageBoxW(0, "interval endurance data saved", "Saved", 1)
        self.nameEdit_4.clear()
        self.noteEdit_4.clear()
        self.handbox_4.clear()


    def close(self):
        dates = datetime.date.today()
        self.name = self.nameEdit_4.toPlainText()
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
        
        

    def close2(self):
        dates = datetime.date.today()
        self.name = self.nameEdit_4.toPlainText()
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
    Option4 = QtWidgets.QMainWindow()
    ui = Ui_Option4()
    ui.setupUi(Option4)
    Option4.show()
    sys.exit(app.exec_())
