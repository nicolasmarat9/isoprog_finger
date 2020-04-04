
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import matplotlib
import itertools 
import numpy as np
import random
import pandas as pd
from mainwindow import Ui_MainWindow
from option1 import Ui_Option_1


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class Option1(QtWidgets.QMainWindow, Ui_trainsys):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)


    def changeWindow(w1, w2):
    w1.hide()
    w2.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    trainsys = Trainsys()

    main.btn_TrainSys.clicked.connect(lambda: changeWindow(main, trainsys))
    trainsys.btn_Backtrain.clicked.connect(lambda: changeWindow(trainsys, main))

    main.show()
    sys.exit(app.exec_())
    
