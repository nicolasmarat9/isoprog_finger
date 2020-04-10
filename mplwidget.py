
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
        y3 = 0.4

        self.canvas.axes.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,110)
        self.canvas.axes.bar(x, y2,linewidth = 0, color = 'lavender', edgecolor= 'royalblue') 
        self.canvas.axes.bar(x, y3, bottom = y2, color = 'royalblue')
        self.canvas.axes.bar(x, y, color = 'orange') 
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()
   
        
        
    def update_graph(self, value, i):


        
        self.y.append(value)
        self.x.append(i)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,110)        
        self.canvas.axes.set_xlim(left=max(0, i-120), right= i+80)
        self.canvas.axes.plot(self.x, self.y,'b-',label='linehand')
        self.canvas.axes.fill_between(self.x, self.y, 0, facecolor = 'orange', alpha = 0.5, interpolate=True)
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()
   

        
    def update_graph2(self, value, i, spn, j):
        
        self.y.append(value)
        self.x.append(i)
        
        self.y2.append(spn)   
        self.x2.append(j)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-80), right= i+120)
        self.canvas.axes.plot(self.y2, self.x2,'-', color = 'darkorange')
        self.canvas.axes.plot(self.x, self.y,'-', color = 'blue')
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()

        
        
    def update_graph3(self, value, i, j, teeth):
        
       
        self.y.append(value)
        self.x.append(i)
        
        self.y2.append(teeth)
        self.x2.append(j)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-80), right= i+120)
        self.canvas.axes.plot(self.y2, self.x2,'-', color = 'darkorange')
        self.canvas.axes.plot(self.x, self.y,'-', color = 'blue')        
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()





    def update_graph4(self, value, i):


        
        self.y.append(value)
        self.x.append(i)
        
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-180), right= i+120)
        self.canvas.axes.plot(self.x, self.y,'b-',label='linehand')
        self.canvas.axes.fill_between(self.x, self.y, 0, facecolor='orange', alpha = 0.5, interpolate=True)
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()
   








        
        
        
