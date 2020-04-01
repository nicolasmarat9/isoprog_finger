

from PyQt5 import QtCore, QtGui, QtWidgets
from option import Ui_Option1
from option2 import Ui_Option2
from option3 import Ui_Option3
from option4 import Ui_Option4



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 261, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 120, 261, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.clicked2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 210, 261, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clicked3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 300, 261, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.clicked4)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Mesure Peak Load"))
        self.pushButton_2.setText(_translate("MainWindow", "Mesure Max Strength"))
        self.pushButton_3.setText(_translate("MainWindow", "Mesure Straight Endurance"))
        self.pushButton_4.setText(_translate("MainWindow", "Mesure Interval Endurance"))


    def clicked1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option1()
        self.ui.setupUi(self.window)
        self.window.show()

    def clicked2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option2()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option3()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def clicked4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Option4()
        self.ui.setupUi(self.window)
        self.window.show()
   



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
