import time
import ardconnect2
import serial
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from free import Ui_Free
from option1 import Ui_Option1
from option2 import Ui_Option2
from option3 import Ui_Option3
from option4 import Ui_Option4
import csv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.state = 0
        self.weight = 0
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.nameEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(750, 70, 150, 30))
        self.nameEdit.setObjectName("nameEdit")

        self.ageBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ageBox.setGeometry(QtCore.QRect(770, 110, 130, 30))
        self.ageBox.setMaximum(100)
        self.ageBox.setObjectName("ageBox")

        self.weightBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weightBox.setGeometry(QtCore.QRect(770, 150, 130, 30))
        self.weightBox.setMaximum(200)
        self.weightBox.setObjectName("weightBox")
        
        self.startButt = QtWidgets.QPushButton(self.centralwidget)
        self.startButt.setGeometry(QtCore.QRect(660, 150, 100, 30))
        self.startButt.setObjectName("startButt")
        self.startButt.clicked.connect(self.clicked_6)        
 
        self.sizeEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sizeEdit.setGeometry(QtCore.QRect(770, 310, 130, 30))
        self.sizeEdit.setObjectName("sizeEdit")

        self.Sexbox = QtWidgets.QComboBox(self.centralwidget)
        self.Sexbox.setGeometry(QtCore.QRect(770, 190, 130, 30))
        self.Sexbox.setObjectName("Sexbox")
        self.Sexbox.addItems(['', 'Female', 'Male'])
        
        self.climbEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.climbEdit.setGeometry(QtCore.QRect(770, 230, 130, 30))
        self.climbEdit.setObjectName("climbEdit")
        
        self.bouldEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.bouldEdit.setGeometry(QtCore.QRect(770, 270, 130, 30))
        self.bouldEdit.setObjectName("bouldEdit")
        
        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(500, 70, 170, 30))
        self.namelabel.setObjectName("namelabel")

        self.agelabel = QtWidgets.QLabel(self.centralwidget)
        self.agelabel.setGeometry(QtCore.QRect(500, 110, 170, 30))
        self.agelabel.setObjectName("agelabel")

        self.weightlabel = QtWidgets.QLabel(self.centralwidget)
        self.weightlabel.setGeometry(QtCore.QRect(500, 150, 170, 30))
        self.weightlabel.setObjectName("weightlabel")

        self.sexlabel = QtWidgets.QLabel(self.centralwidget)
        self.sexlabel.setGeometry(QtCore.QRect(500, 190, 170, 30))
        self.sexlabel.setObjectName("sexlabel")

        self.sizelabel = QtWidgets.QLabel(self.centralwidget)
        self.sizelabel.setGeometry(QtCore.QRect(500, 230, 230, 30))
        self.sizelabel.setObjectName("sizelabel")
        
        self.bouldlabel = QtWidgets.QLabel(self.centralwidget)
        self.bouldlabel.setGeometry(QtCore.QRect(500, 270, 230, 30))
        self.bouldlabel.setObjectName("bouldlabel")
        
        self.climblabel = QtWidgets.QLabel(self.centralwidget)
        self.climblabel.setGeometry(QtCore.QRect(500, 310, 230, 30))
        self.climblabel.setObjectName("climblabel")

        self.Titlelabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_1.setGeometry(QtCore.QRect(85, 20, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.Titlelabel_1.setFont(font)
        self.Titlelabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_1.setObjectName("Titlelabel_1")
        
        self.Titlelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_2.setGeometry(QtCore.QRect(540, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.Titlelabel_2.setFont(font)
        self.Titlelabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_2.setObjectName("Titlelabel_2")        

        self.peakButt = QtWidgets.QPushButton(self.centralwidget)
        self.peakButt.setGeometry(QtCore.QRect(60, 70, 281, 51))
        self.peakButt.setObjectName("peakButt")
        self.peakButt.clicked.connect(self.clicked_1)

        self.maxButt = QtWidgets.QPushButton(self.centralwidget)
        self.maxButt.setGeometry(QtCore.QRect(60, 140, 281, 51))
        self.maxButt.setObjectName("maxButt")
        self.maxButt.clicked.connect(self.clicked_2)

        self.straightButt = QtWidgets.QPushButton(self.centralwidget)
        self.straightButt.setGeometry(QtCore.QRect(60, 210, 281, 51))
        self.straightButt.setObjectName("straightButt")
        self.straightButt.clicked.connect(self.clicked_3)

        self.interButt = QtWidgets.QPushButton(self.centralwidget)
        self.interButt.setGeometry(QtCore.QRect(60, 280, 281, 51))
        self.interButt.setObjectName("interButt")
        self.interButt.clicked.connect(self.clicked_4)
        
        self.freeButt = QtWidgets.QPushButton(self.centralwidget)
        self.freeButt.setGeometry(QtCore.QRect(60, 350, 281, 51))
        self.freeButt.setObjectName("freeButt")
        self.freeButt.clicked.connect(self.clicked_7)
        
        
        self.savebutt = QtWidgets.QPushButton(self.centralwidget)
        self.savebutt.setGeometry(QtCore.QRect(560, 530, 261, 31))
        self.savebutt.setObjectName("savebutt")
        self.savebutt.clicked.connect(self.clicked_5)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 20, 50, 600))
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
        self.peakButt.setText(_translate("MainWindow", "Mesure Peak Load"))
        self.maxButt.setText(_translate("MainWindow", "Mesure Max Strength"))
        self.straightButt.setText(_translate("MainWindow", "Mesure Straight Endurance"))
        self.interButt.setText(_translate("MainWindow", "Mesure Interval Endurance"))
        self.freeButt.setText(_translate("MainWindow", "FREE"))
        self.savebutt.setText(_translate("MainWindow", "SAVE"))
        self.startButt.setText(_translate("MainWindow", "START"))
        self.namelabel.setText(_translate("MainWindow", "<html><head/><body><p>First name, Last name :</p></body></html>"))
        self.weightlabel.setText(_translate("MainWindow", "<html><head/><body><p>Weight (Kg) :</p></body></html>"))
        self.agelabel.setText(_translate("MainWindow", "<html><head/><body><p>Age :</p></body></html>"))
        self.sizelabel.setText(_translate("MainWindow", "<html><head/><body><p>Hight, Apeindex :</p></body></html>"))
        self.climblabel.setText(_translate("MainWindow", "<html><head/><body><p>Climbing (Highest: R.P, O.S) :</p></body></html>"))
        self.bouldlabel.setText(_translate("MainWindow", "<html><head/><body><p>Bouldering (Highest: R.P, O.S) :</p></body></html>"))
        self.sexlabel.setText(_translate("MainWindow", "<html><head/><body><p>sex :</p></body></html>"))
        self.Titlelabel_1.setText(_translate("MainWindow", "<html><head/><body><p>TRAINING OPTIONS</p></body></html>"))
        self.Titlelabel_2.setText(_translate("MainWindow", "<html><head/><body><p>PERSONAL INFORMATIONS</p></body></html>"))


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

    def connecte(self):
        ser = ardconnect2.ardconnect()

        
               
        while True:
                        
            ser_bytes = ser.readline()
            value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
                       
            self.weight = max(self.weight, value)

            if(self.state == 0) and(value > 5):
                self.state = 1

            elif(self.state == 1) and(value < 0.3):
                time.sleep(1)
                self.weightBox.setValue(self.weight)
                
                
        
    def saves(self):
        self.name = self.nameEdit.toPlainText()
        self.age = self.ageBox.value()
        self.weight = self.weightBox.value()
        self.size = self.sizeEdit.toPlainText()
        self.climb = self.climbEdit.toPlainText()
        self.bould = self.bouldEdit.toPlainText()
        self.sex = str(self.Sexbox.currentText())
         
        with open("%s.csv"%self.name, "a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(["weight",self.weight])
            writer.writerow(["name",self.name])
            writer.writerow(["size",self.size])
            writer.writerow(["age",self.age])
            writer.writerow(["climbing",self.climb])
            writer.writerow(["bouldering",self.bould])
            writer.writerow(["sex",self.sex])
               



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
