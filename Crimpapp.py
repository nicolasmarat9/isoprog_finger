import time
import serial
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from optionfree import Ui_Free
from option1 import Ui_Option1
from option2 import Ui_Option2
from option3 import Ui_Option3
from option4 import Ui_Option4
from optionfreendu import Ui_Option6
from optionview import Ui_Option5
from optionArm import Ui_ArmsWindow
import csv
import ctypes
import pandas as pd
import serial.tools.list_ports
import pushbutt
import os
import datetime



class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):

        ### variables ###
                
        self.state = 0
        self.weight = 0
        self.finalweight = 0
        self.clean = 0
        self.peakloadvalue = 0
        self.statescale = 0

        ### mainwindow ###

            ## window setting ##
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 969)
        MainWindow.move(3, 3)
        MainWindow.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

            ## titles and display labels ##

        self.Displaylabel = QtWidgets.QLabel(self.centralwidget)
        self.Displaylabel.setGeometry(QtCore.QRect(85, 40, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(55)
        self.Displaylabel.setFont(font)
        self.Displaylabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Displaylabel.setObjectName("Displaylabel")

        self.FingerOptionlabel = QtWidgets.QLabel(self.centralwidget)
        self.FingerOptionlabel.setGeometry(QtCore.QRect(85, 520, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.FingerOptionlabel.setFont(font)
        self.FingerOptionlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FingerOptionlabel.setObjectName("FingerOptionlabel")
        
        self.PersoInformationlabel = QtWidgets.QLabel(self.centralwidget)
        self.PersoInformationlabel.setGeometry(QtCore.QRect(85, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.PersoInformationlabel.setFont(font)
        self.PersoInformationlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PersoInformationlabel.setObjectName("PersoInformationlabel")

        self.DataVisualisationlabel = QtWidgets.QLabel(self.centralwidget)
        self.DataVisualisationlabel.setGeometry(QtCore.QRect(85, 850, 330, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.DataVisualisationlabel.setFont(font)
        self.DataVisualisationlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DataVisualisationlabel.setObjectName("DataVisualisationlabel")
        
            ## personal data filling ##

        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(40, 70, 170, 30))
        self.namelabel.setObjectName("namelabel")        
        
        self.nameEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(280, 70, 150, 30))
        self.nameEdit.setObjectName("nameEdit")

        
        self.agelabel = QtWidgets.QLabel(self.centralwidget)
        self.agelabel.setGeometry(QtCore.QRect(40, 110, 170, 30))
        self.agelabel.setObjectName("agelabel")        

        self.ageBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ageBox.setGeometry(QtCore.QRect(300, 110, 130, 30))
        self.ageBox.setMaximum(100)
        self.ageBox.setObjectName("ageBox")
        
        
        self.weightlabel = QtWidgets.QLabel(self.centralwidget)
        self.weightlabel.setGeometry(QtCore.QRect(40, 150, 140, 30))
        self.weightlabel.setObjectName("weightlabel")

        self.WeightDisplaylabel = QtWidgets.QLabel(self.centralwidget)
        self.WeightDisplaylabel.setGeometry(QtCore.QRect(270, 150, 60, 30))
        self.WeightDisplaylabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WeightDisplaylabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.WeightDisplaylabel.setAlignment(QtCore.Qt.AlignCenter)        
        self.WeightDisplaylabel.setObjectName("WeightDisplaylabel")         

        self.weightBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weightBox.setGeometry(QtCore.QRect(340, 150, 90, 30))
        self.weightBox.setMaximum(200)
        self.weightBox.setObjectName("weightBox")


        self.sexlabel = QtWidgets.QLabel(self.centralwidget)
        self.sexlabel.setGeometry(QtCore.QRect(40, 190, 170, 30))
        self.sexlabel.setObjectName("sexlabel")

        self.Sexbox = QtWidgets.QComboBox(self.centralwidget)
        self.Sexbox.setGeometry(QtCore.QRect(300, 190, 130, 30))
        self.Sexbox.setObjectName("Sexbox")
        self.Sexbox.addItems(['', 'Female', 'Male'])
        

        self.sizelabel = QtWidgets.QLabel(self.centralwidget)
        self.sizelabel.setGeometry(QtCore.QRect(40, 230, 230, 30))
        self.sizelabel.setObjectName("sizelabel")
 
        self.sizeEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sizeEdit.setGeometry(QtCore.QRect(300, 230, 130, 30))
        self.sizeEdit.setObjectName("sizeEdit")
        

        self.bouldlabel = QtWidgets.QLabel(self.centralwidget)
        self.bouldlabel.setGeometry(QtCore.QRect(40, 270, 230, 30))
        self.bouldlabel.setObjectName("bouldlabel")
        
        self.bouldEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.bouldEdit.setGeometry(QtCore.QRect(300, 270, 130, 30))
        self.bouldEdit.setObjectName("bouldEdit")

        
        self.climblabel = QtWidgets.QLabel(self.centralwidget)
        self.climblabel.setGeometry(QtCore.QRect(40, 310, 230, 30))
        self.climblabel.setObjectName("climblabel")
        
        self.climbEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.climbEdit.setGeometry(QtCore.QRect(300, 310, 130, 30))
        self.climbEdit.setObjectName("climbEdit")
        

        self.notelabel = QtWidgets.QLabel(self.centralwidget)
        self.notelabel.setGeometry(QtCore.QRect(40, 350, 230, 30))
        self.notelabel.setObjectName("notelabel")

        self.noteEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit.setGeometry(QtCore.QRect(130, 350, 300, 90))
        self.noteEdit.setObjectName("noteEdit")
        
            ## personal data buttons ##
        
        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(160, 142, 90, 45))
        self.startButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt.setObjectName("startButt")
        self.startButt.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt.setIconSize(QtCore.QSize(90, 90))
        self.startButt.clicked.connect(self.clicked_startscale)        

        self.clearButt = QtWidgets.QPushButton(self.centralwidget)
        self.clearButt.setGeometry(QtCore.QRect(130, 450, 96, 45))
        self.clearButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 96px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 96px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.clearButt.setObjectName("clearButt")
        self.clearButt.setIcon(QtGui.QIcon("pushbutt/ziconpush8.png"))
        self.clearButt.setIconSize(QtCore.QSize(90, 90))        
        self.clearButt.clicked.connect(self.clicked_cleardata)        
         
        self.savebutt = QtWidgets.QPushButton(self.centralwidget)
        self.savebutt.setGeometry(QtCore.QRect(240, 450, 90, 45))
        self.savebutt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.savebutt.setObjectName("savebutt")
        self.savebutt.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.savebutt.setIconSize(QtCore.QSize(90, 90))
        self.savebutt.clicked.connect(self.clicked_save)

            ## measures options buttons ## 
        
        self.peakButt = QtWidgets.QPushButton(self.centralwidget)
        self.peakButt.setGeometry(QtCore.QRect(50, 565, 115, 125))
        self.peakButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                    "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.peakButt.setObjectName("peakButt")
        self.peakButt.setIcon(QtGui.QIcon("pushbutt/ziconpush1.png"))
        self.peakButt.setIconSize(QtCore.QSize(130, 130))          
        self.peakButt.clicked.connect(self.clicked_Option1)

        self.maxButt = QtWidgets.QPushButton(self.centralwidget)
        self.maxButt.setGeometry(QtCore.QRect(175, 565, 115, 125))
        self.maxButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                   "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.maxButt.setObjectName("maxButt")
        self.maxButt.setIcon(QtGui.QIcon("pushbutt/ziconpush2.png"))
        self.maxButt.setIconSize(QtCore.QSize(130, 130))        
        self.maxButt.clicked.connect(self.clicked_Option2)

        self.straightButt = QtWidgets.QPushButton(self.centralwidget)
        self.straightButt.setGeometry(QtCore.QRect(300, 565, 115, 125))
        self.straightButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                        "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.straightButt.setObjectName("straightButt")
        self.straightButt.setIcon(QtGui.QIcon("pushbutt/ziconpush3.png"))
        self.straightButt.setIconSize(QtCore.QSize(130, 130))        
        self.straightButt.clicked.connect(self.clicked_Option3)

        self.interButt = QtWidgets.QPushButton(self.centralwidget)
        self.interButt.setGeometry(QtCore.QRect(50, 700, 115, 125))
        self.interButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                     "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.interButt.setObjectName("interButt")
        self.interButt.setIcon(QtGui.QIcon("pushbutt/ziconpush4.png"))
        self.interButt.setIconSize(QtCore.QSize(130, 130))        
        self.interButt.clicked.connect(self.clicked_Option4)
        
        self.freeButt = QtWidgets.QPushButton(self.centralwidget)
        self.freeButt.setGeometry(QtCore.QRect(175, 700, 115, 125))
        self.freeButt.setStyleSheet("QPushButton {background-color: orange; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                    "QPushButton:pressed {background-color: darkorange; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.freeButt.setObjectName("freeButt")
        self.freeButt.setIcon(QtGui.QIcon("pushbutt/iconpush5.png"))
        self.freeButt.setIconSize(QtCore.QSize(130, 130))        
        self.freeButt.clicked.connect(self.clicked_Free)

        self.freendButt = QtWidgets.QPushButton(self.centralwidget)
        self.freendButt.setGeometry(QtCore.QRect(300, 700, 115, 125))
        self.freendButt.setStyleSheet("QPushButton {background-color: orange; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: darkorange; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.freendButt.setObjectName("freendButt")
        self.freendButt.setIcon(QtGui.QIcon("pushbutt/iconpush6.png"))
        self.freendButt.setIconSize(QtCore.QSize(120, 120))        
        self.freendButt.clicked.connect(self.clicked_Freend)

            ## visualisation buttons ##

        self.viewButt = QtWidgets.QPushButton(self.centralwidget)
        self.viewButt.setGeometry(QtCore.QRect(150, 890, 80, 48))
        self.viewButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 16px; border: 1px solid grey;}"
                                     "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 16px; border: 1px solid dimgrey;}")
        self.viewButt.setObjectName("viewButt")
        self.viewButt.setIcon(QtGui.QIcon("pushbutt/iconpush22.png"))
        self.viewButt.setIconSize(QtCore.QSize(60, 60))        
        self.viewButt.clicked.connect(self.clicked_View)
        
        self.armButt = QtWidgets.QPushButton(self.centralwidget)
        self.armButt.setGeometry(QtCore.QRect(240, 890, 80, 48))
        self.armButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 16px; border: 1px solid grey;}"
                                     "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 16px; border: 1px solid dimgrey;}")
        self.armButt.setObjectName("viewButt")
        self.armButt.setIcon(QtGui.QIcon("pushbutt/iconpush23.png"))
        self.armButt.setIconSize(QtCore.QSize(50, 50))        
        self.armButt.clicked.connect(self.clicked_Arm)

            ## main window setting ##
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 18))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Training Protocole"))

        self.namelabel.setText(_translate("MainWindow", "<html><head/><body><p>First name, Last name :</p></body></html>"))
        self.weightlabel.setText(_translate("MainWindow", "<html><head/><body><p>Weight (Kg) :</p></body></html>"))
        self.agelabel.setText(_translate("MainWindow", "<html><head/><body><p>Age :</p></body></html>"))
        self.sizelabel.setText(_translate("MainWindow", "<html><head/><body><p>Hight, Apeindex :</p></body></html>"))
        self.climblabel.setText(_translate("MainWindow", "<html><head/><body><p>Climbing (Highest: R.P, O.S) :</p></body></html>"))
        self.bouldlabel.setText(_translate("MainWindow", "<html><head/><body><p>Bouldering (Highest: R.P, O.S) :</p></body></html>"))
        self.sexlabel.setText(_translate("MainWindow", "<html><head/><body><p>sex :</p></body></html>"))
        self.FingerOptionlabel.setText(_translate("MainWindow", "<html><head/><body><p>FINGERS OPTIONS</p></body></html>"))
        self.PersoInformationlabel.setText(_translate("MainWindow", "<html><head/><body><p>PERSONAL INFORMATIONS</p></body></html>"))
        self.DataVisualisationlabel.setText(_translate("MainWindow", "<html><head/><body><p>DATA VISIUALISATIONS/ANALYSES</p></body></html>"))
        self.notelabel.setText(_translate("MainWindow", "<html><head/><body><p>Notes :</p></body></html>"))

        ### click functions ###

            ## calling of the options ##

    def clicked_Option1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option1()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def clicked_Option2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option2()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_Option3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option3()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_Option4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option4()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_Free(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Free()
        self.ui.setupUi(self.window)
        self.window.show()
                
    def clicked_Freend(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option6()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_View(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option5()
        self.ui.setupUi(self.window)
        self.window.show()

    def clicked_Arm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ArmsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

            ## click start save clear ##        

    def clicked_startscale(self):
        t = Thread(target = self.connection)
        t.start()

    def clicked_save(self):
        v = Thread(target = self.saves)
        v.start()

    def clicked_cleardata(self):
        self.nameEdit.clear()
        self.sizeEdit.clear()
        self.climbEdit.clear()
        self.bouldEdit.clear()
        self.noteEdit.clear()
        self.ageBox.setValue(0)
        self.weightBox.setValue(0.00)
        self.Sexbox.clear()
        self.Sexbox.addItems(['', 'Female', 'Male'])
        self.statescale = 0
        self.WeightDisplaylabel.setText('')

        ### function ### 

    def connection(self):

        ## connect arduino ##
        
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
                        self.Displaylabel.setText("Found Sensor on " + portName)
                        time.sleep(2)
                        self.Displaylabel.setText("")
                        #print("Found Sensor on " + portName)
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            self.Displaylabel.setText("No Sensor found")
            time.sleep(2)
            self.Displaylabel.setText("")
            raise IOError("No Sensor found")
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)

       
        self.state = 0

        ## measure weight ##
                      
        while True :
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.weight = max(self.weight, value)

            if(self.state == 0) and(value > 5):
                self.state = 1

            elif(self.state == 1) and(value < 0.3):
                time.sleep(1)
                self.WeightDisplaylabel.setText(str(self.weight))
                self.statescale = 1
                break
  
        
    def saves(self):
       

        ## save data in csv file ##
        
        self.name = self.nameEdit.toPlainText()
        self.age = self.ageBox.value()
        if(self.statescale == 0):
            self.finalweight = self.weightBox.value()
        elif(self.statescale == 1):
            self.finalweight = self.weight
        self.size = self.sizeEdit.toPlainText()
        self.climb = self.climbEdit.toPlainText()
        self.bould = self.bouldEdit.toPlainText()
        self.sex = str(self.Sexbox.currentText())
        self.notes = self.noteEdit.toPlainText()


        if not os.path.exists("%s"%self.name):
            os.mkdir("%s"%self.name)
        elif os.path.exists("%s"%self.name):
            self.Displaylabel.setText("File name already exist")
            time.sleep(2)
            self.Displaylabel.setText("")

        personnal_data = {
            
            "name": pd.Series([self.name]),
            "sex": pd.Series([self.sex]),
            "age": pd.Series([self.age]),
            "size": pd.Series([self.size]),
            "weight": pd.Series([self.finalweight]),
            "climbing": pd.Series([self.climb]),
            "bouldering": pd.Series([self.bould]),
            "notes": pd.Series([self.notes])
        }
        dates = datetime.date.today()
           
        df = pd.DataFrame(personnal_data)
        df.to_csv("{0}/{0}%s.csv".format(self.name)%dates, header = True, index = False)
        ctypes.windll.user32.MessageBoxW(0, "personnal data saved", "Saved", 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())










    
