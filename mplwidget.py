
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
    
class MplWidget(QWidget ):
    
    
    def __init__( self, parent = None):


        QWidget.__init__(self, parent)
        
        self.x = []
        self.y = []
        self.x2 = []
        self.y2 = []
        
        self.canvas = FigureCanvas(Figure())
                
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(1,1,1)
        self.linehand = self.canvas.axes.plot(self.x, self.y)
        self.lineprog = self.canvas.axes.plot(self.x2, self.y2)
        self.canvas.axes.set_ylim(0,100)
        self.canvas.axes.set_xlim(0,60)
        self.setLayout(vertical_layout)
        self.canvas.axes.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)
       
        
            
    def update_bargraph(self, value, peakload):
        
        x = 1
        y = value
        y2 = peakload

        self.canvas.axes.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,100)
        self.canvas.axes.bar(x, y2) 
        self.canvas.axes.bar(x, y) 
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()
   
        
        
    def update_graph(self, value, i):


        
        self.y.append(value)
        self.x.append(i)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-40), right= i+60)
        self.canvas.axes.plot(self.x, self.y,'-',label='linehand')
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()
   

        
    def update_graph2(self, value, i, spn, j):
        
        self.y.append(value)
        self.x.append(i)
        
        self.y2.append(spn)   
        self.x2.append(j)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-40), right= i+60)
        self.canvas.axes.plot(self.x, self.y,'-')
        self.canvas.axes.plot(self.y2, self.x2,'-')
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()

        
        
    def update_graph3(self, value, i, j, teeth):
        
       
        self.y.append(value)
        self.x.append(i)
        
        self.y2.append(teeth)
        self.x2.append(j)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-40), right= i+60)
        self.canvas.axes.plot(self.x, self.y,'-')
        self.canvas.axes.plot(self.y2, self.x2,'-')
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()














        
        
        
