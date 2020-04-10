import time
import serial
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from free import Ui_Free
from option1 import Ui_Option1
from option2 import Ui_Option2
from option3 import Ui_Option3
from option4 import Ui_Option4
from freendu import Ui_Option6
import csv
import ctypes
import pandas as pd
import serial.tools.list_ports
import pushbutt


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        self.state = 0
        self.weight = 0
        self.weight2 = 0
        self.clean = 0
        self.peakloadvalue = 0
        self.state4 = 0
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 969)
        MainWindow.move(3, 3)
        MainWindow.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.nameEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(280, 70, 150, 30))
        self.nameEdit.setObjectName("nameEdit")

        self.ageBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ageBox.setGeometry(QtCore.QRect(300, 110, 130, 30))
        self.ageBox.setMaximum(100)
        self.ageBox.setObjectName("ageBox")

        self.weightBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weightBox.setGeometry(QtCore.QRect(340, 150, 90, 30))
        self.weightBox.setMaximum(200)
        self.weightBox.setObjectName("weightBox")

        self.scalelabel = QtWidgets.QLabel(self.centralwidget)
        self.scalelabel.setGeometry(QtCore.QRect(270, 150, 60, 30))
        self.scalelabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scalelabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scalelabel.setAlignment(QtCore.Qt.AlignCenter)        
        self.scalelabel.setObjectName("scalelabel")        
        
        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(160, 142, 90, 45))
        self.startButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt.setObjectName("startButt")
        self.startButt.setIcon(QtGui.QIcon("pushbutt/ziconpush7.png"))
        self.startButt.setIconSize(QtCore.QSize(90, 90))
        self.startButt.clicked.connect(self.clicked_6)        
 
        self.sizeEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sizeEdit.setGeometry(QtCore.QRect(300, 230, 130, 30))
        self.sizeEdit.setObjectName("sizeEdit")

        self.Sexbox = QtWidgets.QComboBox(self.centralwidget)
        self.Sexbox.setGeometry(QtCore.QRect(300, 190, 130, 30))
        self.Sexbox.setObjectName("Sexbox")
        self.Sexbox.addItems(['', 'Female', 'Male'])
        
        self.climbEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.climbEdit.setGeometry(QtCore.QRect(300, 310, 130, 30))
        self.climbEdit.setObjectName("climbEdit")
        
        self.bouldEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.bouldEdit.setGeometry(QtCore.QRect(300, 270, 130, 30))
        self.bouldEdit.setObjectName("bouldEdit")

        self.noteEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.noteEdit.setGeometry(QtCore.QRect(130, 350, 300, 140))
        self.noteEdit.setObjectName("noteEdit")        
        
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(40, 70, 170, 30))
        self.namelabel.setObjectName("namelabel")

        self.agelabel = QtWidgets.QLabel(self.centralwidget)
        self.agelabel.setGeometry(QtCore.QRect(40, 110, 170, 30))
        self.agelabel.setObjectName("agelabel")

        self.weightlabel = QtWidgets.QLabel(self.centralwidget)
        self.weightlabel.setGeometry(QtCore.QRect(40, 150, 140, 30))
        self.weightlabel.setObjectName("weightlabel")

        self.sexlabel = QtWidgets.QLabel(self.centralwidget)
        self.sexlabel.setGeometry(QtCore.QRect(40, 190, 170, 30))
        self.sexlabel.setObjectName("sexlabel")

        self.sizelabel = QtWidgets.QLabel(self.centralwidget)
        self.sizelabel.setGeometry(QtCore.QRect(40, 230, 230, 30))
        self.sizelabel.setObjectName("sizelabel")
        
        self.bouldlabel = QtWidgets.QLabel(self.centralwidget)
        self.bouldlabel.setGeometry(QtCore.QRect(40, 270, 230, 30))
        self.bouldlabel.setObjectName("bouldlabel")

        self.notelabel = QtWidgets.QLabel(self.centralwidget)
        self.notelabel.setGeometry(QtCore.QRect(40, 350, 230, 30))
        self.notelabel.setObjectName("notelabel")
        
        self.climblabel = QtWidgets.QLabel(self.centralwidget)
        self.climblabel.setGeometry(QtCore.QRect(40, 310, 230, 30))
        self.climblabel.setObjectName("climblabel")

        self.Titlelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_3.setGeometry(QtCore.QRect(85, 570, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(55)
        self.Titlelabel_3.setFont(font)
        self.Titlelabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_3.setObjectName("Titlelabel_3")

        self.Titlelabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_1.setGeometry(QtCore.QRect(85, 610, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.Titlelabel_1.setFont(font)
        self.Titlelabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_1.setObjectName("Titlelabel_1")
        
        self.Titlelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_2.setGeometry(QtCore.QRect(85, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.Titlelabel_2.setFont(font)
        self.Titlelabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_2.setObjectName("Titlelabel_2")        

        self.peakButt = QtWidgets.QPushButton(self.centralwidget)
        self.peakButt.setGeometry(QtCore.QRect(50, 655, 115, 135))
        self.peakButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                    "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.peakButt.setObjectName("peakButt")
        self.peakButt.setIcon(QtGui.QIcon("pushbutt/ziconpush1.png"))
        self.peakButt.setIconSize(QtCore.QSize(130, 130))          
        self.peakButt.clicked.connect(self.clicked_1)

        self.maxButt = QtWidgets.QPushButton(self.centralwidget)
        self.maxButt.setGeometry(QtCore.QRect(175, 655, 115, 135))
        self.maxButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                   "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.maxButt.setObjectName("maxButt")
        self.maxButt.setIcon(QtGui.QIcon("pushbutt/ziconpush2.png"))
        self.maxButt.setIconSize(QtCore.QSize(130, 130))        
        self.maxButt.clicked.connect(self.clicked_2)

        self.straightButt = QtWidgets.QPushButton(self.centralwidget)
        self.straightButt.setGeometry(QtCore.QRect(300, 655, 115, 135))
        self.straightButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                        "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.straightButt.setObjectName("straightButt")
        self.straightButt.setIcon(QtGui.QIcon("pushbutt/ziconpush3.png"))
        self.straightButt.setIconSize(QtCore.QSize(130, 130))        
        self.straightButt.clicked.connect(self.clicked_3)

        self.interButt = QtWidgets.QPushButton(self.centralwidget)
        self.interButt.setGeometry(QtCore.QRect(50, 800, 115, 135))
        self.interButt.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                     "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.interButt.setObjectName("interButt")
        self.interButt.setIcon(QtGui.QIcon("pushbutt/ziconpush4.png"))
        self.interButt.setIconSize(QtCore.QSize(130, 130))        
        self.interButt.clicked.connect(self.clicked_4)
        
        self.freeButt = QtWidgets.QPushButton(self.centralwidget)
        self.freeButt.setGeometry(QtCore.QRect(175, 800, 115, 135))
        self.freeButt.setStyleSheet("QPushButton {background-color: orange; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                    "QPushButton:pressed {background-color: darkorange; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.freeButt.setObjectName("freeButt")
        self.freeButt.setIcon(QtGui.QIcon("pushbutt/iconpush5.png"))
        self.freeButt.setIconSize(QtCore.QSize(130, 130))        
        self.freeButt.clicked.connect(self.clicked_7)

        self.freendButt = QtWidgets.QPushButton(self.centralwidget)
        self.freendButt.setGeometry(QtCore.QRect(300, 800, 115, 135))
        self.freendButt.setStyleSheet("QPushButton {background-color: orange; height: 135px; width: 115px; border-radius: 20px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: darkorange; height: 45px; width: 90px; border-radius: 20px; border: 1px solid dimgrey;}")
        self.freendButt.setObjectName("freendButt")
        self.freendButt.setIcon(QtGui.QIcon("pushbutt/iconpush6.png"))
        self.freendButt.setIconSize(QtCore.QSize(120, 120))        
        self.freendButt.clicked.connect(self.clicked_9)        

        self.clearButt = QtWidgets.QPushButton(self.centralwidget)
        self.clearButt.setGeometry(QtCore.QRect(130, 500, 96, 45))
        self.clearButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 96px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 96px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.clearButt.setObjectName("clearButt")
        self.clearButt.setIcon(QtGui.QIcon("pushbutt/ziconpush8.png"))
        self.clearButt.setIconSize(QtCore.QSize(90, 90))        
        self.clearButt.clicked.connect(self.clicked_8)        
         
        self.savebutt = QtWidgets.QPushButton(self.centralwidget)
        self.savebutt.setGeometry(QtCore.QRect(240, 500, 90, 45))
        self.savebutt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.savebutt.setObjectName("savebutt")
        self.savebutt.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.savebutt.setIconSize(QtCore.QSize(90, 90))
        self.savebutt.clicked.connect(self.clicked_5)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(460, 20, 50, 1000))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line") 
        

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Fingers Protocole"))
        #self.peakButt.setText(_translate("MainWindow", "Mesure Peak Load"))
        #self.maxButt.setText(_translate("MainWindow", "Mesure Max Strength"))
        #self.straightButt.setText(_translate("MainWindow", "Mesure Straight Endurance"))
        #self.interButt.setText(_translate("MainWindow", "Mesure Interval Endurance"))
        #self.freeButt.setText(_translate("MainWindow", "FREE PEAK"))
        #self.freendButt.setText(_translate("MainWindow", "FREE ENDU"))        
        #self.clearButt.setText(_translate("MainWindow", "CLEAR"))
        #self.savebutt.setText(_translate("MainWindow", "SAVE"))
        #self.startButt.setText(_translate("MainWindow", "START"))
        self.namelabel.setText(_translate("MainWindow", "<html><head/><body><p>First name, Last name :</p></body></html>"))
        self.weightlabel.setText(_translate("MainWindow", "<html><head/><body><p>Weight (Kg) :</p></body></html>"))
        self.agelabel.setText(_translate("MainWindow", "<html><head/><body><p>Age :</p></body></html>"))
        self.sizelabel.setText(_translate("MainWindow", "<html><head/><body><p>Hight, Apeindex :</p></body></html>"))
        self.climblabel.setText(_translate("MainWindow", "<html><head/><body><p>Climbing (Highest: R.P, O.S) :</p></body></html>"))
        self.bouldlabel.setText(_translate("MainWindow", "<html><head/><body><p>Bouldering (Highest: R.P, O.S) :</p></body></html>"))
        self.sexlabel.setText(_translate("MainWindow", "<html><head/><body><p>sex :</p></body></html>"))
        self.Titlelabel_1.setText(_translate("MainWindow", "<html><head/><body><p>TRAINING OPTIONS</p></body></html>"))
        self.Titlelabel_2.setText(_translate("MainWindow", "<html><head/><body><p>PERSONAL INFORMATIONS</p></body></html>"))
        self.notelabel.setText(_translate("MainWindow", "<html><head/><body><p>Notes :</p></body></html>"))


    def clicked_1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option1()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def clicked_2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option2()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option3()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option4()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_9(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option6()
        self.ui.setupUi(self.window)
        self.window.show()

    def clicked_6(self):
        t = Thread(target = self.connecte)
        t.start()

    def clicked_5(self):
        v = Thread(target = self.saves)
        v.start()

    def clicked_7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Free()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked_8(self):
        self.nameEdit.clear()
        self.sizeEdit.clear()
        self.climbEdit.clear()
        self.bouldEdit.clear()
        self.noteEdit.clear()
        self.ageBox.setValue(0)
        self.weightBox.setValue(0.00)
        self.Sexbox.clear()
        self.Sexbox.addItems(['', 'Female', 'Male'])
        self.state4 = 0
        self.scalelabel.setText('')

    def connecte(self):
        
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
                        print("Found Sensor on " + portName)
                        self.Titlelabel_3.setText("Found Sensor on " + portName)
                        time.sleep(2)
                        self.Titlelabel_3.setText("")
                        break
                    
                    int1 = int1 + 1
                        
            else:
                break

        if portName == '':
            raise IOError("No Sensor found")
            self.Titlelabel_3.setText("No Sensor found")
            time.sleep(2)
            self.Titlelabel_3.setText("")
        
        baudrate = 9600
        ser = serial.Serial(portName, baudrate)

       
        self.state = 0
                      
        while True :
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.weight = max(self.weight, value)

            if(self.state == 0) and(value > 5):
                self.state = 1

            elif(self.state == 1) and(value < 0.3):
                time.sleep(1)
                self.scalelabel.setText(str(self.weight))
                self.state4 = 1
                break
       
        
    def saves(self):
        self.name = self.nameEdit.toPlainText()
        self.age = self.ageBox.value()
        if(self.state4 == 0):
            self.weight2 = self.weightBox.value()
        elif(self.state4 == 1):
            self.weight2 = self.weight
        self.size = self.sizeEdit.toPlainText()
        self.climb = self.climbEdit.toPlainText()
        self.bould = self.bouldEdit.toPlainText()
        self.sex = str(self.Sexbox.currentText())
        self.notes = self.noteEdit.toPlainText()
        ctypes.windll.user32.MessageBoxW(0, "personnal data saved", "Saved", 1)

        personnal_data = {
            
            "name": pd.Series([self.name]),
            "sex": pd.Series([self.sex]),
            "age": pd.Series([self.age]),
            "size": pd.Series([self.size]),
            "weight": pd.Series([self.weight2]),
            "climbing": pd.Series([self.climb]),
            "bouldering": pd.Series([self.bould]),
            "notes": pd.Series([self.notes])
        }
        df = pd.DataFrame(personnal_data)
        df.to_csv("%s.csv"%self.name, header = True, index = False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())










    