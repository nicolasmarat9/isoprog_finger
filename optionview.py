import serial
import time
import csv
import matplotlib 
matplotlib.use("tkAgg") 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget2
from mplwidget import MplWidget3
from threading import Thread
import ctypes
import pandas as pd
import serial.tools.list_ports


class Ui_Option5(object):
   
    def setupUi(self, Option5):
        
        
       
        # Option1 window:
        
        Option5.setObjectName("Option5")
        Option5.resize(1427, 969)
        Option5.move(488, 3)
        Option5.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))
        
        self.centralwidget = QtWidgets.QWidget(Option5)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget2(parent = self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(30, 311, 1380, 641))
        self.plot.setObjectName("plot")

        self.plot2 = MplWidget3(parent = self.centralwidget)
        self.plot2.setGeometry(QtCore.QRect(970, 10, 440, 370))
        self.plot2.setObjectName("plot2")        

        self.startButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.startButt_2.setGeometry(QtCore.QRect(30, 180, 90, 45))
        self.startButt_2.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.startButt_2.setObjectName("startButt_2")
        self.startButt_2.setIcon(QtGui.QIcon("pushbutt/iconpush14.png"))
        self.startButt_2.setIconSize(QtCore.QSize(75, 75))         
        self.startButt_2.clicked.connect(self.clicked1_2)

        self.stopButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.stopButt_2.setGeometry(QtCore.QRect(150, 180, 90, 45))
        self.stopButt_2.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.stopButt_2.setObjectName("stopButt_2")
        self.stopButt_2.setIcon(QtGui.QIcon("pushbutt/iconpush15.png"))
        self.stopButt_2.setIconSize(QtCore.QSize(75, 75))         
        self.stopButt_2.clicked.connect(self.clicked2_2)

        self.title_2 = QtWidgets.QLabel(self.centralwidget)
        self.title_2.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(65)
        self.title_2.setFont(font)          
        self.title_2.setObjectName("title_2")

        self.saveButt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_2.setGeometry(QtCore.QRect(270, 180, 90, 45))
        self.saveButt_2.setStyleSheet("QPushButton {background-color: lightsteelblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: cornflowerblue; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.saveButt_2.setObjectName("saveButt_2")
        self.saveButt_2.setIcon(QtGui.QIcon("pushbutt/iconpush16.png"))
        self.saveButt_2.setIconSize(QtCore.QSize(75, 75))          
        self.saveButt_2.clicked.connect(self.clicked4_2)

        self.saveButt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButt_3.setGeometry(QtCore.QRect(390, 180, 90, 45))
        self.saveButt_3.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 22px; border: 1px solid grey;}"
                                      "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.saveButt_3.setObjectName("saveButt_2")
        self.saveButt_3.setIcon(QtGui.QIcon("pushbutt/iconpush40.png"))
        self.saveButt_3.setIconSize(QtCore.QSize(55, 55))          
        self.saveButt_3.clicked.connect(self.clicked5_2)

        self.namelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.namelabel_2.setGeometry(QtCore.QRect(30, 90, 211, 30))
        self.namelabel_2.setObjectName("namelabel_2")
      
        self.nameEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit_2.setGeometry(QtCore.QRect(230, 90, 131, 30))
        self.nameEdit_2.setObjectName("nameEdit_2")

        self.datelabel = QtWidgets.QLabel(self.centralwidget)
        self.datelabel.setGeometry(QtCore.QRect(30, 130, 211, 30))
        self.datelabel.setObjectName("datelabel")
      
        self.dateEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(230, 130, 131, 30))
        self.dateEdit.setObjectName("dateEdit")


               
        Option5.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Option5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        Option5.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Option5)
        self.statusbar.setObjectName("statusbar")

        Option5.setStatusBar(self.statusbar)

        self.retranslateUi(Option5)
        QtCore.QMetaObject.connectSlotsByName(Option5)

        #self.name = self.nameEdit_2.toPlainText()

    def retranslateUi(self, Option5):
        _translate = QtCore.QCoreApplication.translate
        Option5.setWindowTitle(_translate("Option5", "Finger data analyse"))
        self.title_2.setText(_translate("Option5", "<html><head/><body><p><span style=\" font-size:12pt;\">VISUALISATION</span></p></body></html>"))
        self.namelabel_2.setText(_translate("Option1", "<html><head/><body><p>File name</p></body></html>"))
        self.datelabel.setText(_translate("Option1", "<html><head/><body><p>File date (YYYY-MM-DD)</p></body></html>"))
               

    def clicked1_2(self):
        
        e = Thread(target = self.plotmaxx)
        e.start()

    def clicked2_2(self):
        
        f = Thread(target = self.plotmaxx2)
        f.start()

    def clicked4_2(self):
        g = Thread(target = self.plotmaxx3)
        g.start()

    def clicked5_2(self):
        g = Thread(target = self.plotmaxx4)
        g.start()

    def plotmaxx(self):
        self.dates = self.dateEdit.toPlainText()
        self.name = self.nameEdit_2.toPlainText()
        self.plot.plotmax(self.name, self.dates)

    
    def plotmaxx2(self):
        self.dates = self.dateEdit.toPlainText()
        self.name = self.nameEdit_2.toPlainText()        
        self.plot.plotstr(self.name, self.dates)
        

    def plotmaxx3(self):
        self.dates = self.dateEdit.toPlainText()
        self.name = self.nameEdit_2.toPlainText()        
        self.plot.plotint(self.name, self.dates)        

    def plotmaxx4(self):
        self.dates = self.dateEdit.toPlainText()
        self.name = self.nameEdit_2.toPlainText()        
        self.plot2.plotfingers(self.name, self.dates)                
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option5 = QtWidgets.QMainWindow()
    ui = Ui_Option5()
    ui.setupUi(Option5)
    Option5.show()
    sys.exit(app.exec_())
