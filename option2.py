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


class Ui_Option2(object):
   
    def setupUi(self, Option2):
        
        # definitions:
        
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
        self.everadge = []
        
        self.statemain2 = 0
        self.statedisplay2 = 0
        self.stateclean2 = 0
        
        # Option1 window:
        
        Option2.setObjectName("Option2")
        Option2.resize(1427, 969)
        Option2.move(488, 3)
        Option2.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option2)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget(parent = self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(295, 71, 1115, 881))
        self.plot.setObjectName("plot")

        self.displaylabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_2.setGeometry(QtCore.QRect(25 ,330, 246, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setWeight(50)
        self.displaylabel_2.setFont(font)
        self.displaylabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_2.setObjectName("displaylabel_2")

        self.displaylabel_22 = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel_22.setGeometry(QtCore.QRect(655, 5, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.displaylabel_22.setFont(font)
        self.displaylabel_22.setAlignment(QtCore.Qt.AlignCenter)
        self.displaylabel_22.setObjectName("displaylabel_22")        

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(140, 90, 131, 61))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.startButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_2.setGeometry(QtCore.QRect(30, 90, 90, 45))
        self.startButt_2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt_2.setObjectName("startButt_2")
        self.startButt_2.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt_2.setIconSize(QtCore.QSize(90, 90))         
        self.startButt_2.clicked.connect(self.clicked1_2)

        self.stopButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_2.setGeometry(QtCore.QRect(30, 150, 90, 45))
        self.stopButt_2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt_2.setObjectName("stopButt_2")
        self.stopButt_2.setIcon(QtGui.QIcon("pushbutt/iconpush10.png"))
        self.stopButt_2.setIconSize(QtCore.QSize(90, 90))         
        self.stopButt_2.clicked.connect(self.clicked2_2)

        self.title_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.title_2.setFont(font)          
        self.title_2.setObjectName("title_2")

        self.saveButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_2.setGeometry(QtCore.QRect(30, 890, 90, 45))
        self.saveButt_2.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.saveButt_2.setObjectName("saveButt_2")
        self.saveButt_2.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.saveButt_2.setIconSize(QtCore.QSize(90, 90))          
        self.saveButt_2.clicked.connect(self.clicked4_2)

        self.peaklabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.peaklabel_2.setGeometry(QtCore.QRect(45, 260, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.peaklabel_2.setFont(font)
        self.peaklabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.peaklabel_2.setObjectName("peaklabel_2")

        self.peaklabel2_2 = QtWidgets.QLabel(self.centralwidget)
        self.peaklabel2_2.setGeometry(QtCore.QRect(179, 260, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(65)
        self.peaklabel2_2.setFont(font)        
        self.peaklabel2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.peaklabel2_2.setObjectName("peaklabel2_2")

        self.peakloadlabel = QtWidgets.QLabel(self.centralwidget)
        self.peakloadlabel.setGeometry(QtCore.QRect(36, 210, 100, 51))
        self.peakloadlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.peakloadlabel.setObjectName("peakloadlabel")

        self.peakloadlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.peakloadlabel_2.setGeometry(QtCore.QRect(170, 210, 100, 51))
        self.peakloadlabel_2.setAlignment(QtCore.Qt.AlignCenter)        
        self.peakloadlabel_2.setObjectName("everadgelabel")

        self.namelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_2.setGeometry(QtCore.QRect(40, 840, 211, 30))
        self.namelabel_2.setObjectName("namelabel_2")
        
        self.handlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.handlabel_2.setGeometry(QtCore.QRect(40, 700, 130, 30))
        self.handlabel_2.setObjectName("handlabel_2")
        
        self.nameEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_2.setGeometry(QtCore.QRect(130, 840, 131, 30))
        self.nameEdit_2.setObjectName("nameEdit_2")
        
        self.notelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.notelabel_2.setGeometry(QtCore.QRect(40, 750, 211, 30))
        self.notelabel_2.setObjectName("notelabel_2")
        
        self.noteEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit_2.setGeometry(QtCore.QRect(130, 750, 131, 70))
        self.noteEdit_2.setObjectName("noteEdit_2")
        
        self.handbox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.handbox_2.setGeometry(QtCore.QRect(130, 700, 131, 30))
        self.handbox_2.setObjectName("handbox_2")
        self.handbox_2.addItems(['', 'Drag', 'Half crimp', 'Full crimp'])
               
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
        #self.startButt_2.setText(_translate("Option2", "START"))
        #self.stopButt_2.setText(_translate("Option2", "RESET"))
        self.title_2.setText(_translate("Option2", "<html><head/><body><p><span style=\" font-size:12pt;\">MAX STRENGTH</span></p></body></html>"))
        #self.saveButt_2.setText(_translate("Option2", "SAVE"))
        self.peakloadlabel.setText("Peak average\nright")
        self.peakloadlabel_2.setText("peak average\nleft")
        self.namelabel_2.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.handlabel_2.setText(_translate("Option1", "<html><head/><body><p>Holding</p></body></html>"))
        self.notelabel_2.setText(_translate("Option1", "<html><head/><body><p>Notes</p></body></html>"))
  

    def clicked1_2(self):
        e = Thread(target = self.connect_22)
        e.start()

    def clicked2_2(self):
        f = Thread(target = self.disconnect)
        f.start()

    def clicked4_2(self):
        g = Thread(target = self.save)
        g.start()     
                
        

    def connect_22(self):
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
                        self.displaylabel_22.setText("Found Sensor on " + portName)
                        print("Found Sensor on " + portName)
                        time.sleep(2)
                        self.displaylabel_22.setText("")
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.displaylabel_22.setText("No Sensor found")
            raise IOError("No Sensor found")
            time.sleep(2)
            self.displaylabel_22.setText("")        
            
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)

        
        krono = Thread(target = self.timer)
        krono.start()
        
        if(self.statemain2 == 0):
            self.displaylabel_22.setText("RIGHT HAND") 
            
            while (self.stateclean2 == 0):
                            
                ser_bytes = ser.readline()
                self.value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                
                
                self.peakload2 = max(self.peakload2, self.value)
                self.maxbyte.append(self.value)
                           
                self.lcdNumber_2.display(self.value)
                self.plot.update_graph(self.value, self.i)
                
                self.i += 1
                
        elif(self.statemain2 == 1):
            self.displaylabel_22.setText("LEFT HAND")

            while (self.stateclean2 == 0):
                            
                ser_bytes = ser.readline()
                self.value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                
                
                self.peakload2 = max(self.peakload2, self.value)
                self.maxbyte_2.append(self.value)
                           
                self.lcdNumber_2.display(self.value)
                self.plot.update_graph(self.value, self.i)
                
                self.i += 1
                

    def timer(self):
        
        if(self.statedisplay2 == 0):
            self.displaylabel_2.setText("Get\nready")    
            time.sleep(1)
        if(self.statedisplay2 == 0):    
            self.displaylabel_2.setText(str(5))    
            time.sleep(1)
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText(str(4))    
            time.sleep(1)
        if(self.statedisplay2 == 0):             
            self.displaylabel_2.setText(str(3))    
            time.sleep(1)
        if(self.statedisplay2 == 0):             
            self.displaylabel_2.setText(str(2))    
            time.sleep(1)
        if(self.statedisplay2 == 0):             
            self.displaylabel_2.setText(str(1))    
            time.sleep(1)
        if(self.statedisplay2 == 0):
            self.displaylabel_2.setText("START")    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):      
            self.displaylabel_2.setText(str(7))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0): 
            self.displaylabel_2.setText(str(6))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText(str(5))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText(str(4))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText(str(3))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText(str(2))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)
        if(self.statedisplay2 == 0):      
            self.displaylabel_2.setText(str(1))    
            time.sleep(0.49)
            self.everadge.append(self.value)
            time.sleep(0.49)
            self.everadge.append(self.value)            
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText("STOP")
            self.average = sum(self.everadge) / len(self.everadge)
            time.sleep(3)
        if(self.statedisplay2 == 0):     
            self.displaylabel_2.setText("")
            self.displaylabel_22.setText("")
            

            if(self.statemain2 == 0):
                self.peak2_1 = str(self.peakload2)
                self.peaklabel_2.setText(str(round(self.average, 2)))
                self.average1 = self.average
                self.statemain2 = 1
                time.sleep(1)
                self.end()
                                
            elif(self.statemain2 == 1):
                self.peak2_2 = str(self.peakload2)
                self.peaklabel2_2.setText(str(round(self.average, 2)))
                self.average2 = self.average
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
        self.average
               
        self.plot.canvas.axes.clear()
        self.plot.x.clear()
        self.plot.y.clear()
        self.plot.linehand.clear()
        
        self.maxbyte.clear()
        self.maxbyte_2.clear()
        self.everadge.clear()
        
        self.displaylabel_22.setText("reset max strength")
        self.displaylabel_2.setText("")
        self.peaklabel_2.setText("")
        self.peaklabel2_2.setText("")
        time.sleep(2.5)
        self.displaylabel_22.setText("")
        
        
    def save(self):
        self.name = self.nameEdit_2.toPlainText()
        self.notes = self.noteEdit_2.toPlainText()
        self.hand = str(self.handbox_2.currentText())


        df = pd.read_csv("%s.csv"%self.name)
        data1 = [self.notes]
        df["max strength notes"] = data1
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data2 = [self.hand]
        df["max strength style"] = data2
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data3 = [self.peak2_1]
        df["maxstr load right"] = data3
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data4 = [self.peak2_2]
        df["maxstr load left"] = data4
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

        df = pd.read_csv("%s.csv"%self.name)
        data5 = [self.average1]
        df["maxstr average right"] = data5
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data6 = [self.average2]
        df["maxstr average left"] = data6
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data7 = [self.maxbyte]
        df["right maxstr pulling data"] = data7
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data8 = [self.maxbyte_2]
        df["left maxstr pulling data"] = data8
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
           
            
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
