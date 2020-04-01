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
        
        self.textEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(750, 70, 150, 30))
        self.textEdit.setObjectName("textEdit")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(770, 110, 130, 30))
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")

        self.spinBox2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox2.setGeometry(QtCore.QRect(770, 150, 130, 30))
        self.spinBox2.setMaximum(200)
        self.spinBox2.setObjectName("spinBox")
        
        self.butt21 = QtWidgets.QPushButton(self.centralwidget)
        self.butt21.setGeometry(QtCore.QRect(660, 150, 100, 30))
        self.butt21.setObjectName("butt4")
        self.butt21.clicked.connect(self.clicked_6)        
 
        self.textEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(770, 310, 130, 30))
        self.textEdit_3.setObjectName("textEdit")

        self.cSex = QtWidgets.QComboBox(self.centralwidget)
        self.cSex.setGeometry(QtCore.QRect(770, 190, 130, 30))
        self.cSex.setObjectName("cSex")
        self.cSex.addItems(['', 'Female', 'Male'])
        
        self.textEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(770, 230, 130, 30))
        self.textEdit_4.setObjectName("textEdit")
        
        self.textEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(770, 270, 130, 30))
        self.textEdit_5.setObjectName("textEdit")
        
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(500, 70, 170, 30))
        self.label_1.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 110, 170, 30))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 150, 170, 30))
        self.label_3.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(500, 190, 170, 30))
        self.label_4.setObjectName("label_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 230, 230, 30))
        self.label_5.setObjectName("label_2")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 270, 230, 30))
        self.label_6.setObjectName("label_2")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 310, 230, 30))
        self.label_7.setObjectName("label_2")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(85, 20, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_2")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_2")        

        self.pushButton11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton11.setGeometry(QtCore.QRect(60, 70, 281, 51))
        self.pushButton11.setObjectName("pushButton")
        self.pushButton11.clicked.connect(self.clicked_1)

        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(60, 140, 281, 51))
        self.pushButton_22.setObjectName("pushButton_2")
        self.pushButton_22.clicked.connect(self.clicked_2)

        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(60, 210, 281, 51))
        self.pushButton_33.setObjectName("pushButton_3")
        self.pushButton_33.clicked.connect(self.clicked_3)

        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(60, 280, 281, 51))
        self.pushButton_44.setObjectName("pushButton_4")
        self.pushButton_44.clicked.connect(self.clicked_4)
        
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setGeometry(QtCore.QRect(60, 350, 281, 51))
        self.pushButton_55.setObjectName("pushButton_4")
        self.pushButton_55.clicked.connect(self.clicked_7)
        
        
        self.butt12 = QtWidgets.QPushButton(self.centralwidget)
        self.butt12.setGeometry(QtCore.QRect(560, 530, 261, 31))
        self.butt12.setObjectName("butt4")
        self.butt12.clicked.connect(self.clicked_5)

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
        self.pushButton11.setText(_translate("MainWindow", "Mesure Peak Load"))
        self.pushButton_22.setText(_translate("MainWindow", "Mesure Max Strength"))
        self.pushButton_33.setText(_translate("MainWindow", "Mesure Straight Endurance"))
        self.pushButton_44.setText(_translate("MainWindow", "Mesure Interval Endurance"))
        self.pushButton_55.setText(_translate("MainWindow", "FREE"))
        self.butt12.setText(_translate("MainWindow", "SAVE"))
        self.butt21.setText(_translate("MainWindow", "START"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p>First name, Last name :</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Weight (Kg) :</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Age :</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Hight, Apeindex :</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Climbing (Highest: R.P, O.S) :</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Bouldering (Highest: R.P, O.S) :</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>sex :</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>TRAINING OPTIONS</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>PERSONAL INFORMATIONS</p></body></html>"))


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
                self.spinBox2.setValue(self.weight)
                
                
        
    def saves(self):
        self.name = self.textEdit.toPlainText()
        self.age = self.spinBox.value()
        self.weight = self.spinBox2.value()
        self.size = self.textEdit_3.toPlainText()
        self.climb = self.textEdit_4.toPlainText()
        self.bould = self.textEdit_5.toPlainText()
        self.sex = str(self.cSex.currentText())
         
        with open("new_data.csv","a") as f:
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
