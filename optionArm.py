import time
import serial
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget4
import csv
import ctypes
import pandas as pd
import serial.tools.list_ports



class Ui_ArmsWindow(object):
    
    def setupUi(self, ArmsWindow):
        
        ArmsWindow.setObjectName("ArmsWindow")
        ArmsWindow.resize(1427, 969)
        ArmsWindow.move(488, 3)
        ArmsWindow.setWindowIcon(QtGui.QIcon("icons/logoapp702.ico"))

        self.centralwidget = QtWidgets.QWidget(ArmsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.plot = MplWidget4(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(480, 71, 920, 881))
        self.plot.setObjectName("plot")        

        self.namelabel = QtWidgets.QLabel(self.centralwidget)
        self.namelabel.setGeometry(QtCore.QRect(40, 70, 170, 30))
        self.namelabel.setObjectName("namelabel")       
        
        self.nameEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(280, 70, 150, 30))
        self.nameEdit.setObjectName("nameEdit")

        self.datelabel = QtWidgets.QLabel(self.centralwidget)
        self.datelabel.setGeometry(QtCore.QRect(40, 670, 211, 30))
        self.datelabel.setObjectName("datelabel")
      
        self.dateEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(280, 670, 150, 30))
        self.dateEdit.setObjectName("dateEdit")

        self.deadhanglabel = QtWidgets.QLabel(self.centralwidget)
        self.deadhanglabel.setGeometry(QtCore.QRect(40, 110, 220, 30))
        self.deadhanglabel.setObjectName("deadhanglabel")        

        self.deadhangBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.deadhangBox.setGeometry(QtCore.QRect(330, 110, 100, 30))
        self.deadhangBox.setMaximum(100)
        self.deadhangBox.setObjectName("deadhangBox")

        self.maxweightpulluplabel = QtWidgets.QLabel(self.centralwidget)
        self.maxweightpulluplabel.setGeometry(QtCore.QRect(40, 150, 220, 30))
        self.maxweightpulluplabel.setObjectName("maxweightpulluplabel")        

        self.maxweightpullupBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.maxweightpullupBox .setGeometry(QtCore.QRect(330, 150, 100, 30))
        self.maxweightpullupBox .setMaximum(200)
        self.maxweightpullupBox .setObjectName("maxweightpullupBox ")

        self.maxpulluplabel = QtWidgets.QLabel(self.centralwidget)
        self.maxpulluplabel.setGeometry(QtCore.QRect(40, 190, 220, 30))
        self.maxpulluplabel.setObjectName("maxpulluplabel")        

        self.maxpullupBox = QtWidgets.QSpinBox(self.centralwidget)
        self.maxpullupBox.setGeometry(QtCore.QRect(330, 190, 100, 30))
        self.maxpullupBox.setMaximum(100)
        self.maxpullupBox.setObjectName("maxpullupBox")

        self.maxweightdiplabel = QtWidgets.QLabel(self.centralwidget)
        self.maxweightdiplabel.setGeometry(QtCore.QRect(40, 230, 220, 30))
        self.maxweightdiplabel.setObjectName("maxweightdiplabel")        

        self.maxweightdipBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.maxweightdipBox .setGeometry(QtCore.QRect(330, 230, 100, 30))
        self.maxweightdipBox .setMaximum(200)
        self.maxweightdipBox .setObjectName("maxweightdipBox ")
        
        self.maxdipslabel = QtWidgets.QLabel(self.centralwidget)
        self.maxdipslabel.setGeometry(QtCore.QRect(40, 270, 220, 30))
        self.maxdipslabel.setObjectName("maxdipslabel")
       
        self.maxdipsBox = QtWidgets.QSpinBox(self.centralwidget)
        self.maxdipsBox.setGeometry(QtCore.QRect(330, 270, 100, 30))
        self.maxdipsBox.setMaximum(100)
        self.maxdipsBox.setObjectName("maxdipsBox")

        self.frontleveroptionlabel = QtWidgets.QLabel(self.centralwidget)
        self.frontleveroptionlabel.setGeometry(QtCore.QRect(40, 310, 270, 30))
        self.frontleveroptionlabel.setObjectName("frontleveroptionlabel")

        self.frontleveroptionbox = QtWidgets.QComboBox(self.centralwidget)
        self.frontleveroptionbox.setGeometry(QtCore.QRect(330, 310, 100, 30))
        self.frontleveroptionbox.setObjectName("frontleveroptionbox")
        self.frontleveroptionbox.addItems(['', 'bend', 'straight'])

        self.frontleverlabel = QtWidgets.QLabel(self.centralwidget)
        self.frontleverlabel.setGeometry(QtCore.QRect(40, 350, 230, 30))
        self.frontleverlabel.setObjectName("frontleverlabel")        
        
        self.frontleverBox = QtWidgets.QSpinBox(self.centralwidget)
        self.frontleverBox.setGeometry(QtCore.QRect(330, 350, 100, 30))
        self.frontleverBox.setMaximum(100)
        self.frontleverBox.setObjectName("frontleverBox")      
        
        self.tlabel = QtWidgets.QLabel(self.centralwidget)
        self.tlabel.setGeometry(QtCore.QRect(40, 390, 230, 30))
        self.tlabel.setObjectName("notelabel")

        self.tBox = QtWidgets.QSpinBox(self.centralwidget)
        self.tBox.setGeometry(QtCore.QRect(330, 390, 100, 30))
        self.tBox.setMaximum(100)
        self.tBox.setObjectName("ageBox")        

        self.splitlabel = QtWidgets.QLabel(self.centralwidget)
        self.splitlabel.setGeometry(QtCore.QRect(40, 430, 230, 30))
        self.splitlabel.setObjectName("notelabel")

        self.splitBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.splitBox.setGeometry(QtCore.QRect(330, 430, 100, 30))
        self.splitBox.setMaximum(200)
        self.splitBox.setObjectName("weightBox")

        self.techlabel = QtWidgets.QLabel(self.centralwidget)
        self.techlabel.setGeometry(QtCore.QRect(40, 470, 230, 30))
        self.techlabel.setObjectName("techlabel")

        self.techBox = QtWidgets.QSpinBox(self.centralwidget)
        self.techBox.setGeometry(QtCore.QRect(330, 470, 100, 30))
        self.techBox.setMaximum(100)
        self.techBox.setObjectName("techBox")        

        self.coordlabel = QtWidgets.QLabel(self.centralwidget)
        self.coordlabel.setGeometry(QtCore.QRect(40, 510, 230, 30))
        self.coordlabel.setObjectName("coordlabel")

        self.coordBox = QtWidgets.QSpinBox(self.centralwidget)
        self.coordBox.setGeometry(QtCore.QRect(330, 510, 100, 30))
        self.coordBox.setMaximum(200)
        self.coordBox.setObjectName("coordBox")           
       
        self.Titlelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_2.setGeometry(QtCore.QRect(85, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.Titlelabel_2.setFont(font)
        self.Titlelabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_2.setObjectName("Titlelabel_2")

        self.Titlelabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.Titlelabel_4.setGeometry(QtCore.QRect(795, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(65)
        self.Titlelabel_4.setFont(font)
        self.Titlelabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Titlelabel_4.setObjectName("Titlelabel_4")          

        self.viewButt = QtWidgets.QPushButton(self.centralwidget)
        self.viewButt.setGeometry(QtCore.QRect(185, 720, 96, 45))
        self.viewButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 135px; width: 115px; border-radius: 22px; border: 1px solid grey;}"
                                     "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.viewButt.setObjectName("viewButt")
        self.viewButt.setIcon(QtGui.QIcon("pushbutt/iconpush40.png"))
        self.viewButt.setIconSize(QtCore.QSize(55, 55))        
        self.viewButt.clicked.connect(self.clicked_view)        

        self.ClearButt = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButt.setGeometry(QtCore.QRect(130, 600, 96, 45))
        self.ClearButt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 96px; border-radius: 22px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 96px; border-radius: 22px; border: 1px solid dimgrey;}")
        self.ClearButt.setObjectName("clearButt")
        self.ClearButt.setIcon(QtGui.QIcon("pushbutt/ziconpush8.png"))
        self.ClearButt.setIconSize(QtCore.QSize(90, 90))        
        self.ClearButt.clicked.connect(self.clicked_clear)        
         
        self.savebutt = QtWidgets.QPushButton(self.centralwidget)
        self.savebutt.setGeometry(QtCore.QRect(240, 600, 90, 45))
        self.savebutt.setStyleSheet("QPushButton {background-color: gainsboro; height: 45px; width: 90px; border-radius: 6px; border: 1px solid grey;}"
                                       "QPushButton:pressed {background-color: silver; height: 45px; width: 90px; border-radius: 6px; border: 1px solid dimgrey;}")
        self.savebutt.setObjectName("savebutt")
        self.savebutt.setIcon(QtGui.QIcon("pushbutt/ziconpush9.png"))
        self.savebutt.setIconSize(QtCore.QSize(90, 90))
        self.savebutt.clicked.connect(self.clicked_save)

       

        ArmsWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(ArmsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 18))
        self.menubar.setObjectName("menubar")

        ArmsWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ArmsWindow)
        self.statusbar.setObjectName("statusbar")

        ArmsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ArmsWindow)
        QtCore.QMetaObject.connectSlotsByName(ArmsWindow)

    def retranslateUi(self, ArmsWindow):
        _translate = QtCore.QCoreApplication.translate
        ArmsWindow.setWindowTitle(_translate("ArmsWindow", "General data analyse"))
        self.namelabel.setText(_translate("ArmsWindow", "<html><head/><body><p>First name, Last name :</p></body></html>"))
        self.maxweightpulluplabel.setText(_translate("ArmsWindow", "<html><head/><body><p>1 max weighted pull-up (Kg) :</p></body></html>"))
        self.deadhanglabel.setText(_translate("ArmsWindow", "<html><head/><body><p>7 sec 2 arms dead hang (kg) :</p></body></html>"))
        self.maxweightdiplabel.setText(_translate("ArmsWindow", "<html><head/><body><p>1 max weighted dip (kg) :</p></body></html>"))
        self.frontleveroptionlabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Front lever option :</p></body></html>"))
        self.maxdipslabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Max dips (rep) :</p></body></html>"))
        self.maxpulluplabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Max pull-up (rep) :</p></body></html>"))
        self.Titlelabel_4.setText(_translate("ArmsWindow", "<html><head/><body><p>SKILLS BALANCE GRAPHIC</p></body></html>"))
        self.Titlelabel_2.setText(_translate("ArmsWindow", "<html><head/><body><p>BODY MEASURES</p></body></html>"))
        self.frontleverlabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Front lever (sec) :</p></body></html>"))
        self.tlabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Butterfly on bench 5kg (rep) :</p></body></html>"))
        self.splitlabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Front split (cm) :</p></body></html>"))
        self.techlabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Climbing technic (%) :</p></body></html>"))
        self.coordlabel.setText(_translate("ArmsWindow", "<html><head/><body><p>Climbing coordination (%) :</p></body></html>"))
        self.datelabel.setText(_translate("Option1", "<html><head/><body><p>File date (YYYY-MM-DD)</p></body></html>"))

        
    def clicked_clear(self):
        
        self.nameEdit.clear()
        self.deadhangBox.setValue(0.00)
        self.maxweightpullupBox.setValue(0.00)
        self.maxpullupBox.setValue(0)
        self.maxweightdipBox.setValue(0.00)
        self.maxdipsBox.setValue(0)
        self.frontleveroptionbox.clear()
        self.frontleveroptionbox.addItems(['', 'bend', 'straight'])
        self.frontleverBox.setValue(0)
        self.tBox.setValue(0)
        self.splitBox.setValue(0.00)
        


    def clicked_save(self):
        v = Thread(target = self.save2)
        v.start()

    def clicked_view(self):
        
        e = Thread(target = self.plotview)
        e.start()        
       
    def plotview(self):
        self.dates = self.dateEdit.toPlainText()
        self.name = self.nameEdit.toPlainText()
        self.plot.plot_data(self.name, self.dates)
      
           
    def save(self):
        self.name = self.nameEdit.toPlainText()
        self.deadhang = self.deadhangBox.value()
        self.maxweightpullup = self.maxweightpullupBox.value()
        self.maxpullup = self.maxpullupBox.value()        
        self.maxweightdip = self.maxweightdipBox.value()
        self.maxdips = self.maxdipsBox.value()        
        self.frontleveroption = str(self.frontleveroptionbox.currentText())
        self.frontlever = self.frontleverBox.value()
        self.TRX = self.tBox.value()
        self.split = self.splitBox.value()
        ctypes.windll.user32.MessageBoxW(0, "personnal data saved", "Saved", 1)

        personnal_data = {
            
            "name": pd.Series([self.name]),
            "2 hands dead hang": pd.Series([self.deadhang]),
            "1 max weighted pull-up": pd.Series([self.maxweightpullup]),
            "max pull-up": pd.Series([self.maxpullup]),
            "1 max weighted dip": pd.Series([self.maxweightdip]),
            "max dips": pd.Series([self.maxdips]),
            "front lever option": pd.Series([self.frontleveroption]),
            "front lever": pd.Series([self.frontlever]),
            "T on TRX": pd.Series([self.TRX]),
            "front split": pd.Series([self.split])
            
        }
        df = pd.DataFrame(personnal_data)
        df.to_csv("%s_arms.csv"%self.name, header = True, index = False)

    def save2(self):
        
        self.name = self.nameEdit.toPlainText()
        self.deadhang = self.deadhangBox.value()
        self.maxweightpullup = self.maxweightpullupBox.value()
        self.maxpullup = self.maxpullupBox.value()        
        self.maxweightdip = self.maxweightdipBox.value()
        self.maxdips = self.maxdipsBox.value()        
        self.frontleveroption = str(self.frontleveroptionbox.currentText())
        self.frontlever = self.frontleverBox.value()
        self.TRX = self.tBox.value()
        self.split = self.splitBox.value()
        self.tech = self.techBox.value()
        self.coord = self.coordBox.value()
        

        df = pd.read_csv("%s.csv"%self.name)
        data1 = [self.deadhang]
        df["2 hands dead hang"] = data1
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data2 = [self.maxweightpullup]
        df["1 max weighted pull-up"] = data2
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data3 = [self.maxpullup]
        df["max pull-up"] = data3
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data4 = [self.maxweightdip]
        df["1 max weighted dip"] = data4
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data5 = [self.maxdips]
        df["max dips"] = data5
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        df = pd.read_csv("%s.csv"%self.name)
        data6 = [self.frontleveroption]
        df["front lever option"] = data6
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
       
        df = pd.read_csv("%s.csv"%self.name)
        data7 = [self.frontlever]
        df["front lever"] = data7
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")            

        df = pd.read_csv("%s.csv"%self.name)
        data8 = [self.TRX]
        df["T on TRX"] = data8
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

        df = pd.read_csv("%s.csv"%self.name)
        data9 = [self.split]
        df["front split"] = data9
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

        df = pd.read_csv("%s.csv"%self.name)
        data10 = [self.tech]
        df["climbing technic"] = data10
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")

        df = pd.read_csv("%s.csv"%self.name)
        data11 = [self.coord]
        df["climbing coordination"] = data11
        df.to_csv("%s.csv"%self.name, header = True, index = False, na_rep = "")
        
        ctypes.windll.user32.MessageBoxW(0, "Exo body data saved", "Saved", 0x00000000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ArmsWindow = QtWidgets.QMainWindow()
    ui = Ui_ArmsWindow()
    ui.setupUi(ArmsWindow)
    ArmsWindow.show()
    sys.exit(app.exec_())










    
