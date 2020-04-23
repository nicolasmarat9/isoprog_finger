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
import pandas as pd
import serial.tools.list_ports
import datetime


class Ui_Option2(object):
   
    def setupUi(self, Option2):
        
        ### variables ###
        
        self.i = 0
        self.peak2_1 = 0
        self.peak2_2 = 0
        self.peakload2 = 0
        self.average = 0
        self.average1 = 0
        self.average2 = 0
        self.value = 0
        
        self.maxbyte = []
        self.maxbyte_2 = []
        self.maxbytex = []
        self.maxbytex_2 = []        
        self.everadge = []
        
        self.statemain2 = 0
        self.statedisplay2 = 0
        self.stateclean2 = 0
        
        ### option 2 max strength ###

            ## window setting ##
        
        Option2.setObjectName("Option2")
        Option2.resize(1427, 969)
        Option2.move(488, 3)
        Option2.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option2)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(parent = self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

            ## titles and display labels ##        

        self.MaxStrengthTitlelabel = QtWidgets.QLabel(self.centralwidget)
        self.MaxStrengthTitlelabel.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.MaxStrengthTitlelabel.setFont(font)          
        self.MaxStrengthTitlelabel.setObjectName("MaxStrengthTitlelabel")

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

        self.displaylabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_2.setGeometry(QtCore.QRect(655, 5, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displaylabel_2.setFont(font)
        self.displaylabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_2.setObjectName("displaylabel_2")

        self.timerlabel = QtWidgets.QLabel(self.centralwidget)
        self.timerlabel.setGeometry(QtCore.QRect(130, 325, 110, 31))
        self.timerlabel.setObjectName("timerlabel")   

        self.stopWatchlabel = QtWidgets.QLabel(self.centralwidget)
        self.stopWatchlabel.setGeometry(QtCore.QRect(29 ,330, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.stopWatchlabel.setFont(font)
        self.stopWatchlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stopWatchlabel.setObjectName("stopWatchlabel")
        

        self.peakaveragelabelright = QtWidgets.QLabel(self.centralwidget)
        self.peakaveragelabelright.setGeometry(QtCore.QRect(36, 210, 100, 51))
        self.peakaveragelabelright.setAlignment(QtCore.Qt.AlignCenter)
        self.peakaveragelabelright.setObjectName("peakaveragelabelright")     

        self.displayPeakRightlabel = QtWidgets.QLabel(self.centralwidget)
        self.displayPeakRightlabel.setGeometry(QtCore.QRect(45, 260, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displayPeakRightlabel.setFont(font)
        self.displayPeakRightlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayPeakRightlabel.setObjectName("displayPeakRightlabel")

        self.peakaveragelabelleft = QtWidgets.QLabel(self.centralwidget)
        self.peakaveragelabelleft.setGeometry(QtCore.QRect(170, 210, 100, 51))
        self.peakaveragelabelleft.setAlignment(QtCore.Qt.AlignCenter)        
        self.peakaveragelabelleft.setObjectName("peakaveragelabelleft")        

        self.displayPeakLeftlabel = QtWidgets.QLabel(self.centralwidget)
        self.displayPeakLeftlabel.setGeometry(QtCore.QRect(179, 260, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displayPeakLeftlabel.setFont(font)        
        self.displayPeakLeftlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.displayPeakLeftlabel.setObjectName("displayPeakLeftlabel")

        self.namelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_2.setGeometry(QtCore.QRect(40, 840, 211, 30))
        self.namelabel_2.setObjectName("namelabel_2")        
        
        self.nameEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_2.setGeometry(QtCore.QRect(130, 840, 131, 30))
        self.nameEdit_2.setObjectName("nameEdit_2")

        self.handlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_2.setGeometry(QtCore.QRect(40, 700, 130, 30))
        self.handlabel_2.setObjectName("handlabel_2")
        
        self.handbox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.handbox_2.setGeometry(QtCore.QRect(130, 700, 131, 30))
        self.handbox_2.setObjectName("handbox_2")
        self.handbox_2.addItems(['', 'Drag', 'Half crimp', 'Full crimp'])

        self.notelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_2.setGeometry(QtCore.QRect(40, 750, 211, 30))
        self.notelabel_2.setObjectName("notelabel_2")
        
        self.noteEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_2.setGeometry(QtCore.QRect(130, 750, 131, 70))
        self.noteEdit_2.setObjectName("noteEdit_2")        


        self.startButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_2.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.startButt_2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt_2.setObjectName("startButt_2")
        self.startButt_2.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt_2.setIconSize(QtCore.QSize(90, 90))         
        self.startButt_2.clicked.connect(self.clicked_startMeasures)

        self.stopButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_2.setGeometry(QtCore.QRect(30, 150, 90, 45))
        self.stopButt_2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt_2.setObjectName("stopButt_2")
        self.stopButt_2.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt_2.setIconSize(QtCore.QSize(90, 90))         
        self.stopButt_2.clicked.connect(self.clicked_stop_clear)

        self.saveButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_2.setGeometry(QtCore.QRect(30, 890, 90, 45))
        self.saveButt_2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.saveButt_2.setObjectName("saveButt_2")
        self.saveButt_2.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.saveButt_2.setIconSize(QtCore.QSize(90, 90))          
        self.saveButt_2.clicked.connect(self.clicked_saveMeasures)
        

               
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
        self.MaxStrengthTitlelabel.setText(_translate("Option2", "<html><head/><body><p><span style=\" font-size:12pt;\">MAX STRENGTH</span></p></body></html>"))
        self.peakaveragelabelright.setText("Peak average\nright")
        self.peakaveragelabelleft.setText("Peak average\nleft")
        self.namelabel_2.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.handlabel_2.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_2.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
        self.timerlabel.setText("Timer")
        self.currentWeightlabel.setText("Current weight")         

        ### click functions ###

    def clicked_startMeasures(self):
        e = Thread(target = self.connect)
        e.start()

    def clicked_stop_clear(self):
        f = Thread(target = self.disconnect)
        f.start()

    def clicked_saveMeasures(self):
        g = Thread(target = self.save)
        g.start()     
                
        ### function ###         

    def connect(self):

        ## connect arduino ##
        
        self.statedisplay2 = 0
        self.stateclean2 = 0

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
                        self.displaylabel_2.setText("Found Sensor on " + portName)
                        time.sleep(2)
                        self.displaylabel_2.setText("")
                        #print("Found Sensor on " + portName)                        
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_2.setText("No Sensor found")
            time.sleep(2)
            self.displaylabel_2.setText("")        
            raise IOError("No Sensor found")            
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)

        
        krono = Thread(target = self.timer)
        krono.start()

        ser_bytes = ser.readline()
        valueP1 = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        
        
        
        if(self.statemain2 == 0):
            self.displaylabel_2.setText("RIGHT HAND") 
            
            while (self.stateclean2 == 0):
                            
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                self.value = round(valueP - valueP1, 1)
         
                
                self.peakload2 = max(self.peakload2, self.value)
                self.maxbyte.append(self.value)
                self.maxbytex.append(round(self.i, 1))
                
                self.displayWeightlabel.setText(str(self.value))
                self.plot.update_graph(self.value, self.i)
                
                self.i += 0.1
                
        elif(self.statemain2 == 1):
            self.displaylabel_2.setText("LEFT HAND")

            while (self.stateclean2 == 0):
                            
                ser_bytes = ser.readline()
                valueP = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                self.value = round(valueP - valueP1, 1)

                
                
                self.peakload2 = max(self.peakload2, self.value)
                self.maxbyte_2.append(self.value)
                self.maxbytex_2.append(round(self.i, 1))
                           
                self.displayWeightlabel.setText(str(self.value))
                self.plot.update_graph(self.value, self.i)
                
                self.i += 0.1
                

    def timer(self):
        
        if(self.statedisplay2 == 0):
            self.stopWatchlabel.setText("Get\nready")    
            time.sleep(1)
        if(self.statedisplay2 == 0):    
            self.stopWatchlabel.setText(str(5))    
            time.sleep(1)
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText(str(4))    
            time.sleep(1)
        if(self.statedisplay2 == 0):             
            self.stopWatchlabel.setText(str(3))    
            time.sleep(1)
        if(self.statedisplay2 == 0):             
            self.stopWatchlabel.setText(str(2))    
            time.sleep(1)
        if(self.statedisplay2 == 0):             
            self.stopWatchlabel.setText(str(1))    
            time.sleep(1)
        if(self.statedisplay2 == 0):
            self.stopWatchlabel.setText("START")    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):      
            self.stopWatchlabel.setText(str(7))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0): 
            self.stopWatchlabel.setText(str(6))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText(str(5))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText(str(4))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText(str(3))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText(str(2))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):      
            self.stopWatchlabel.setText(str(1))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)            
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText("STOP")
            self.average = sum(self.everadge) / len(self.everadge)
            time.sleep(3)
        if(self.statedisplay2 == 0):     
            self.stopWatchlabel.setText("")
            self.displaylabel_2.setText("")
            

            if(self.statemain2 == 0):
                self.peak2_1 = str(self.peakload2)
                self.displayPeakRightlabel.setText(str(round(self.average, 2)))
                self.average1 = round(self.average, 2)
                self.statemain2 = 1
                time.sleep(1)
                self.end()
                                
            elif(self.statemain2 == 1):
                self.peak2_2 = str(self.peakload2)
                self.displayPeakLeftlabel.setText(str(round(self.average, 2)))
                self.average2 = round(self.average, 2)
                self.statemain2 = 0
                time.sleep(1)
                self.end()
                
           
    def everadgedata(self):
        while True:
            self.everadge.append(self.value)
  

        
    def end(self):


        self.i = 0
        self.stateclean2 = 1
        self.peakload2 = 0
        self.average = 0
        
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.linehand.clear()
        self.everadge.clear()

       
    def disconnect(self):
        
        self.statedisplay2 = 1
        self.statemain2 = 0
        self.stateclean2 = 1
        self.i = 0
        self.average = 0
               
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.linehand.clear()
        
        self.maxbyte.clear()
        self.maxbyte_2.clear()
        self.everadge.clear()
        
        self.displaylabel_2.setText("reset max strength")
        self.stopWatchlabel.setText("")
        self.displayPeakRightlabel.setText("")
        self.displayPeakLeftlabel.setText("")
        time.sleep(2.5)
        self.displaylabel_2.setText("")
        
        
    def save(self):
        self.name = self.nameEdit_2.toPlainText()
        self.notes = self.noteEdit_2.toPlainText()
        self.hand = str(self.handbox_2.currentText())
        dates = datetime.date.today()

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data1 = [self.notes]
        df["max strength notes"] = data1
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data2 = [self.hand]
        df["max strength style"] = data2
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data3 = [self.peak2_1]
        df["maxstr load right"] = data3
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data4 = [self.peak2_2]
        df["maxstr load left"] = data4
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data5 = [self.average1]
        df["maxstr average right"] = data5
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data6 = [self.average2]
        df["maxstr average left"] = data6
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data7 = [self.maxbyte]
        df["right maxstr pulling data"] = data7
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data8 = [self.maxbyte_2]
        df["left maxstr pulling data"] = data8
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
           
        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data9 = [self.maxbytex]
        df["right maxstr x pulling data"] = data9
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")            

        df = pd.read_csv("{0}/{0}%s.csv".format(self.name)%dates)
        data10 = [self.maxbytex_2]
        df["left maxstr x pulling data"] = data10
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False, na_rep = "")
           
            
        ctypes.windll.user32.MessageBoxW(0, "maximal strength data saved", "Saved", 1)               
        self.nameEdit_2.clear()
        self.noteEdit_2.clear()
        self.handbox_2.clear()
 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option2 = QtWidgets.QMainWindow()
    ui = Ui_Option2()
    ui.setupUi(Option2)
    Option2.show()
    sys.exit(app.exec_())
