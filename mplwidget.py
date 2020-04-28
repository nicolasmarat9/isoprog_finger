
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
import csv
import datetime
    
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
        self.canvas.axes.set_ylim(0,110)
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
        self.canvas.axes.set_xlim(left=max(0, i-12), right= i+8)
        self.canvas.axes.plot(self.x, self.y,'b-',label='linehand')
        self.canvas.axes.fill_between(self.x, self.y, 0, facecolor = 'orange', alpha = 0.5, interpolate=True)
        self.canvas.axes.set_title('pull') 
        self.canvas.draw()

class MplWidgetBis(QWidget ):
    
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
        self.canvas.axes.set_ylim(0,90)
        self.canvas.axes.set_xlim(0,60)
        self.setLayout(vertical_layout)
        self.canvas.axes.tick_params(axis = 'x', which = 'both', bottom = False, top = False, labelbottom = False)

        
    def update_graph2(self, value, i, spn, j):
        self.y.append(value)
        self.x.append(i)
        self.y2.append(spn)   
        self.x2.append(j)
        
        self.canvas.axes.clear()
        self.canvas.axes.set_ylim(0,90)        
        self.canvas.axes.set_xlim(left=max(0, i-8), right= i+12)
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
        self.canvas.axes.set_xlim(left=max(0, i-8), right= i+12)
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


class MplWidget2(QWidget ):
    
    def __init__( self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(2,1,1)
        self.setLayout(vertical_layout)
        self.canvas.axes.set_ylim(0,80)
        self.canvas.axes.set_xlim(0,200)        
        self.canvas.axes.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes.set_ylabel(ylabel = "kg")       
        
        self.canvas.axes2 = self.canvas.figure.add_subplot(2,1,2)
        self.setLayout(vertical_layout)
        self.canvas.axes2.set_xlim(0,200)
        self.canvas.axes2.set_ylim(0,80)
        self.canvas.axes2.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes2.set_ylabel(ylabel = "kg")

    def plotmax(self, name, dates):
        fin = 0
        fin2 = 0
        v = []
        w = []
        v2 = []
        W2 = []
        
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["right maxstr x pulling data"]):
                    if c != '[':
                        if c != ']':
                            if c != ',':
                                string2 += c
                peakloadleft = list(str.split(string2))
                peakloadleft = [float(i) for i in peakloadleft]

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")       
            for row in reader:
                string = ''
                for d in (row["right maxstr pulling data"]):
                    if d != '[':
                        if d != ']':
                            if d != ',':
                                string += d

                peakloadleft2 = list(str.split(string))
                peakloadleft2 = [float(i) for i in peakloadleft2]

        while fin2 == 0:
            
            if len(peakloadleft2) < len(peakloadleft):
                peakloadleft2.append(0)
            elif len(peakloadleft2) > len(peakloadleft):
                peakloadleft.append(0)
            elif len(peakloadleft2) == len(peakloadleft):
                v = peakloadleft     
                w = peakloadleft2
                fin2 = 1
                
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string3 = ''
                for c in (row["left maxstr x pulling data"]):
                    if c != '[':
                        if c != ']':
                            if c != ',':
                                string3 += c
                peakloadleft3 = list(str.split(string3))
                peakloadleft3 = [float(i) for i in peakloadleft3]

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")       
            for row in reader:
                string4 = ''
                for d in (row["left maxstr pulling data"]):
                    if d != '[':
                        if d != ']':
                            if d != ',':
                                string4 += d
                peakloadleft4 = list(str.split(string4))
                peakloadleft4 = [float(i) for i in peakloadleft4]

        while fin == 0:
            
            if len(peakloadleft4) < len(peakloadleft3):
                peakloadleft4.append(0)
            elif len(peakloadleft4) > len(peakloadleft3):
                peakloadleft3.append(0)
            elif len(peakloadleft4) == len(peakloadleft3):
                
                v2 = peakloadleft3     
                w2 = peakloadleft4
                fin =1
                
        if len(peakloadleft3) > len(peakloadleft):
            k = len(peakloadleft3)/10 + 15
        elif len(peakloadleft3) <= len(peakloadleft):
            k = len(peakloadleft)/10 + 15

        self.canvas.axes.clear()
        self.canvas.axes.plot(v, w,'-', color = 'darkorange', label = 'max strength right')
        self.canvas.axes.fill_between(v, w, 0, facecolor = 'darkorange', alpha = 0.1, interpolate = True)
        self.canvas.axes.legend(loc = 'best')
        self.canvas.axes.set_ylim(0,90)
        self.canvas.axes.set_xlim(xmin = 0, xmax = k)
        self.canvas.axes.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes.set_ylabel(ylabel = "kg")
        self.canvas.axes.set_xticks(np.arange(0, k, step=1))
        self.canvas.axes.set_yticks(np.arange(0, 90, step=10))        

        self.canvas.axes2.clear()
        self.canvas.axes2.plot(v2, w2,'-', color = 'darkorange', label = 'max strength left')
        self.canvas.axes2.fill_between(v2, w2, 0, facecolor = 'darkorange', alpha = 0.1, interpolate=True)
        self.canvas.axes2.legend(loc = 'best')
        self.canvas.axes2.set_ylim(0,90)
        self.canvas.axes2.set_xlim(xmin = 0, xmax = k)
        self.canvas.axes2.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes2.set_ylabel(ylabel = "kg")
        self.canvas.axes2.set_xticks(np.arange(0, k, step=1))
        self.canvas.axes2.set_yticks(np.arange(0, 90, step=10))         
        
        self.canvas.figure.savefig("{0}/{0}_max_%s.png".format(name)%dates)    
        self.canvas.draw()

    def plotstr(self, name, dates):
        fin = 0
        fin2 = 0
        v = []
        w = []
        v2 = []
        w2 = []

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["right strend x pulling data"]):
                    if c != '[':
                        if c != ']':
                            if c != ',':
                                string2 += c
                peakloadleft = list(str.split(string2))
                peakloadleft = [float(i) for i in peakloadleft]

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")       
            for row in reader:
                string = ''
                for d in (row["right strend pulling data"]):
                    if d != '[':
                        if d != ']':
                            if d != ',':
                                string += d
                peakloadleft2 = list(str.split(string))
                peakloadleft2 = [float(i) for i in peakloadleft2]

        while fin2 == 0:
            
            if len(peakloadleft2) < len(peakloadleft):
                peakloadleft2.append(0)
            elif len(peakloadleft2) > len(peakloadleft):
                peakloadleft.append(0)
            elif len(peakloadleft2) == len(peakloadleft):
                v = peakloadleft     
                w = peakloadleft2
                fin2 = 1

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string3 = ''
                for c in (row["left strend x pulling data"]):
                    if c != '[':
                        if c != ']':
                            if c != ',':
                                string3 += c
                peakloadleft3 = list(str.split(string3))
                peakloadleft3 = [float(i) for i in peakloadleft3]

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")       
            for row in reader:
                string4 = ''
                for d in (row["left strend pulling data"]):
                    if d != '[':
                        if d != ']':
                            if d != ',':
                                string4 += d
                peakloadleft4 = list(str.split(string4))
                peakloadleft4 = [float(i) for i in peakloadleft4]
                
        while fin == 0:
            
            if len(peakloadleft4) < len(peakloadleft3):
                peakloadleft4.append(0)
            elif len(peakloadleft4) > len(peakloadleft3):
                peakloadleft3.append(0)
            elif len(peakloadleft4) == len(peakloadleft3):
                v2 = peakloadleft3     
                w2 = peakloadleft4
                fin = 1

        if len(peakloadleft3) > len(peakloadleft):
            k = len(peakloadleft3)/10
        elif len(peakloadleft3) <= len(peakloadleft):
            k = len(peakloadleft)/10

        self.canvas.axes.clear()
        self.canvas.axes.plot(v, w,'-', color = 'darkorange', label = 'max strength right')
        self.canvas.axes.fill_between(v, w, 0, facecolor = 'darkorange', alpha = 0.1, interpolate = True)
        self.canvas.axes.legend(loc = 'best')
        self.canvas.axes.set_ylim(0,60)
        self.canvas.axes.set_xlim(xmin = 0, xmax = k)
        self.canvas.axes.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes.set_ylabel(ylabel = "kg")
        
        self.canvas.axes2.clear()
        self.canvas.axes2.plot(v2, w2,'-', color = 'darkorange', label = 'max strength left')
        self.canvas.axes2.fill_between(v2, w2, 0, facecolor = 'darkorange', alpha = 0.1, interpolate=True)
        self.canvas.axes2.legend(loc = 'best')
        self.canvas.axes2.set_ylim(0,60)
        self.canvas.axes2.set_xlim(xmin = 0, xmax = k)
        self.canvas.axes2.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes2.set_ylabel(ylabel = "kg")

        self.canvas.figure.savefig("{0}/{0}_str_%s.png".format(name)%dates)     
        self.canvas.draw()

    def plotint(self, name, dates):
        fin = 0
        fin2 = 0
        v = []
        w = []
        v2 = []
        w2 = []

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["right intend x pulling data"]):
                    if c != '[':
                        if c != ']':
                            if c != ',':
                                string2 += c
                peakloadleft = list(str.split(string2))
                peakloadleft = [float(i) for i in peakloadleft]

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")       
            for row in reader:
                string = ''
                for d in (row["right intend pulling data"]):
                    if d != '[':
                        if d != ']':
                            if d != ',':
                                string += d
                peakloadleft2 = list(str.split(string))
                peakloadleft2 = [float(i) for i in peakloadleft2]

        while fin2 == 0:
            
            if len(peakloadleft2) < len(peakloadleft):
                peakloadleft2.append(0)
            elif len(peakloadleft2) > len(peakloadleft):
                peakloadleft.append(0)
            elif len(peakloadleft2) == len(peakloadleft):
                v = peakloadleft     
                w = peakloadleft2
                fin2 = 1

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string3 = ''
                for c in (row["left intend x pulling data"]):
                    if c != '[':
                        if c != ']':
                            if c != ',':
                                string3 += c
                peakloadleft3 = list(str.split(string3))
                peakloadleft3 = [float(i) for i in peakloadleft3]

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")       
            for row in reader:
                string4 = ''
                for d in (row["left intend pulling data"]):
                    if d != '[':
                        if d != ']':
                            if d != ',':
                                string4 += d
                peakloadleft4 = list(str.split(string4))
                peakloadleft4 = [float(i) for i in peakloadleft4]
                
        while fin == 0:
            
            if len(peakloadleft4) < len(peakloadleft3):
                peakloadleft4.append(0)
            elif len(peakloadleft4) > len(peakloadleft3):
                peakloadleft3.append(0)
            elif len(peakloadleft4) == len(peakloadleft3):
                v2 = peakloadleft3     
                w2 = peakloadleft4
                fin = 1

        if len(peakloadleft3) > len(peakloadleft):
            k = len(peakloadleft3)/10
        elif len(peakloadleft3) <= len(peakloadleft):
            k = len(peakloadleft)/10
                
        self.canvas.axes.clear()
        self.canvas.axes.plot(v, w,'-', color = 'darkorange', label = 'max strength right')
        self.canvas.axes.fill_between(v, w, 0, facecolor = 'darkorange', alpha = 0.1, interpolate = True)
        self.canvas.axes.legend(loc = 'best')
        self.canvas.axes.set_ylim(0,60)
        self.canvas.axes.set_xlim(xmin = 0, xmax = k)
        self.canvas.axes.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes.set_ylabel(ylabel = "kg")
        
        self.canvas.axes2.clear()
        self.canvas.axes2.plot(v2, w2,'-', color = 'darkorange', label = 'max strength left')
        self.canvas.axes2.fill_between(v2, w2, 0, facecolor = 'darkorange', alpha = 0.1, interpolate=True)
        self.canvas.axes2.legend(loc = 'best')
        self.canvas.axes2.set_ylim(0,60)
        self.canvas.axes2.set_xlim(xmin = 0, xmax = k)
        self.canvas.axes2.set_xlabel(xlabel = "time (sec)")
        self.canvas.axes2.set_ylabel(ylabel = "kg")
        
        self.canvas.figure.savefig("{0}/{0}_int_%s.png".format(name)%dates)     
        self.canvas.draw()

            
class MplWidget3(QWidget ):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        labels = ['alactic','aerobic', 'lactic', 'recovering']   
        
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111, polar = True)
        self.setLayout(vertical_layout)
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles,[angles[0]]))
        self.canvas.axes.set_thetagrids(angles * 180/np.pi, labels, fontsize = 7)
        self.canvas.axes.set_yticklabels([])

    def plotfingers(self, name, dates):

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["sex"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.sex = str(string1)        

                   ########## VALUE 1 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string = ''
                for c in (row["weight"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string += c
                weight = float(str(string))

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["peakloadleft"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.peakloadleft = list(str.split(string2))
                self.peakloadleft = [float(i) for i in self.peakloadleft]
                self.averagepeakleft = sum(self.peakloadleft) / len(self.peakloadleft)

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string4 = ''
                for c in (row["peakloadright"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string4 += c
                self.peakloadright = list(str.split(string4))
                self.peakloadright = [float(i) for i in self.peakloadright]
                self.averagepeakright = sum(self.peakloadright) / len(self.peakloadright)
                averageboth = (self.averagepeakright + self.averagepeakleft) / 2
                valp2 = (averageboth / weight) * 100
                if self.sex == "Male":
                    valp3 = 150 / valp2
                    val1 = 100 / valp3
                elif self.sex == "Female":
                    valp3 = 130 / valp2
                    val1 = 100 / valp3

                   ########## VALUE 2 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["left strend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.strendleft = float(str(string2))

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string4 = ''
                for c in (row["right strend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string4 += c
                self.strendright = float(str(string4))
                averagestrend = (self.strendright + self.strendleft) / 2
                if self.sex == "Male":
                    sup = 300 / averagestrend
                    val = 100 / sup
                elif self.sex == "Female":
                    sup = 270 / averagestrend
                    val = 100 / sup                    

                   ########## VALUE 3 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["left intend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.intendleft = float(str(string2))

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string4 = ''
                for c in (row["right intend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string4 += c
                self.intendright = float(str(string4))
                averageintend = (self.intendright + self.intendleft) / 2
                if self.sex == "Male":
                    sup2 = 480 / averageintend
                    val2 = 100 / sup2
                    aero = (averageintend + averagestrend) / 2
                    sup3 = 390 / aero
                    val3 = 100 / sup3
                elif self.sex == "Female":
                    sup2 = 450 / averageintend
                    val2 = 100 / sup2
                    aero = (averageintend + averagestrend) / 2
                    sup3 = 340 / aero
                    val3 = 100 / sup3                    
                    
        labels = ['alactic','aerobic', 'lactic', 'recovering']        
        value = [val1, val3, val, val2, val1]
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles,[angles[0]]))
        self.canvas.axes.fill(angles, value, alpha=0.25)
        self.canvas.axes.set_thetagrids(angles * 180/np.pi, labels, fontsize = 7)
        self.canvas.axes.set_yticklabels([])
        self.canvas.axes.plot(angles, value)
        self.canvas.figure.savefig("{0}/{0}_feedback_%s.png".format(name)%dates)
        self.canvas.draw()



class MplWidget4(QWidget ):
    
    
    def __init__(self, parent = None):


        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        labels = ['technic','coordination', 'back strength', 'core strength', 'arms strength', 'arms endurance', 'fingers strength', 'fingers endurance']   
        
        vertical_layout = QVBoxLayout() 
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111, polar = True)
        self.setLayout(vertical_layout)
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles,[angles[0]]))
        self.canvas.axes.set_thetagrids(angles * 180/np.pi, labels, fontsize = 10)
        self.canvas.axes.set_yticklabels([])

    def plot_data(self, name, dates):

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["sex"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.sex = str(string1)

                   ########## VALUE 1 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["weight"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                weight = float(str(string1))

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["peakloadleft"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.peakloadleft = list(str.split(string2))
                self.peakloadleft = [float(i) for i in self.peakloadleft]
                self.averagepeakleft = sum(self.peakloadleft) / len(self.peakloadleft)

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string3 = ''
                for c in (row["peakloadright"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string3 += c
                self.peakloadright = list(str.split(string3))
                self.peakloadright = [float(i) for i in self.peakloadright]
                self.averagepeakright = sum(self.peakloadright) / len(self.peakloadright)
                valp = (self.averagepeakright + self.averagepeakleft) / 2
                valp2 = (valp / weight) * 100
                if self.sex == "Male":
                    valp3 = 150 / valp2
                    val1 = 100 / valp3
                elif self.sex == "Female":
                    valp3 = 130 / valp2
                    val1 = 100 / valp3                    

                   ########## VALUE 2 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["left strend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.strendleft = float(str(string1))

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["right strend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.strendright = float(str(string2))
                averagestrend = (self.strendright + self.strendleft) / 2
                if self.sex == "Male":
                    sup = 360 / averagestrend
                    val = 100 / sup
                elif self.sex == "Female":
                    sup = 320 / averagestrend
                    val = 100 / sup
                    

                   ########## VALUE 2 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["left intend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.intendleft = float(str(string1))

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["right intend pulling time"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.intendright = float(str(string2))
                averageintend = (self.intendright + self.intendleft) / 2               
                aero = (averageintend + averagestrend) / 2
                if self.sex == "Male":
                    sup3 = 480 / aero
                    val2 = 100 / sup3
                elif self.sex == "Female":
                    sup3 = 450 / aero
                    val2 = 100 / sup3
                    

                   ########## VALUE 3 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["1 max weighted pull-up"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.maxwpullup = float(str(string1))
                valp2 = (self.maxwpullup / weight) * 100
                if self.sex == "Male":                
                    valp3 = 130 / valp2
                    valp1 = 100 / valp3
                elif self.sex == "Female":                
                    valp3 = 115 / valp2
                    valp1 = 100 / valp3
                    
                
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["1 max weighted dip"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.maxdip = float(str(string2))
                valp2 = (self.maxwpullup / weight) * 100
                if self.sex == "Male":                
                    valp3 = 140 / valp2
                    valp4 = 100 / valp3
                    val3 = (valp4 + valp1) / 2
                elif self.sex == "Female":                
                    valp3 = 110 / valp2
                    valp4 = 100 / valp3
                    val3 = (valp4 + valp1) / 2
                    

                   ########## VALUE 4 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["max pull-up"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.maxwpullup = float(str(string1))
                if self.sex == "Male": 
                    sup2 = 50 / self.maxwpullup
                    valp1 = 100 / sup2
                elif self.sex == "Female": 
                    sup2 = 43 / self.maxwpullup
                    valp1 = 100 / sup2
                    

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["max dips"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.maxwpullup = float(str(string2))
                if self.sex == "Male":                
                    sup2 = 50 / self.maxwpullup
                    valp2 = 100 / sup2
                    val4 = (valp2 + valp1) / 2
                elif self.sex == "Female":                
                    sup2 = 42 / self.maxwpullup
                    valp2 = 100 / sup2
                    val4 = (valp2 + valp1) / 2
                    

                   ########## VALUE 5 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string1 = ''
                for c in (row["front lever option"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string1 += c
                self.frontopt = str(string1)           

        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string2 = ''
                for c in (row["front lever"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string2 += c
                self.frontlev = float(str(string2))
                if self.sex == "Male":                
                    if self.frontopt == "straight":
                        sup2 = 45 / self.frontlev
                        val5 = (80 / sup2) + 20   
                    elif self.frontopt == "bend":
                        sup2 = 45 / self.frontlev
                        val5 = 80 / sup2
                elif self.sex == "Female":                
                    if self.frontopt == "straight":
                        sup2 = 40 / self.frontlev
                        val5 = (80 / sup2) + 20   
                    elif self.frontopt == "bend":
                        sup2 = 40 / self.frontlev
                        val5 = 80 / sup2                        

                   ########## VALUE 6 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string = ''
                for c in (row["T on TRX"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string += c
                self.TRX = float(str(string))
                if self.sex == "Male":                
                    sup2 = 60 / self.TRX
                    val6 = 100 / sup2
                elif self.sex == "Female":                
                    sup2 = 50 / self.TRX
                    val6 = 100 / sup2                    

                   ########## VALUE 7 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string = ''
                for c in (row["front split"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string += c
                self.split = float(str(string))
                if self.sex == "Male":                
                    sup2 = 100 / self.split
                    val7 = 100 - sup2
                elif self.sex == "Female":                
                    sup2 = 90 / self.split
                    val7 = 100 - sup2
                    

                   ########## VALUE 8 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string = ''
                for c in (row["climbing technic"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string += c
                self.split = float(str(string))
                if self.sex == "Male":                
                    sup2 = 100 / self.split
                    val8 = 100 / sup2
                elif self.sex == "Female":                
                    sup2 = 90 / self.split
                    val8 = 100 / sup2                    

                   ########## VALUE 9 ##########
        with open("{0}/{0}%s.csv".format(name)%dates,"r") as f:
            reader = csv.DictReader(f, delimiter = ",")
            for row in reader:
                string = ''
                for c in (row["climbing coordination"]):
                    if c != '(':
                        if c != ')':
                            if c != ',':
                                string += c
                self.split = float(str(string))
                if self.sex == "Male":                
                    sup2 = 100 / self.split
                    val9 = 100 / sup2
                elif self.sex == "Female":                
                    sup2 = 90 / self.split
                    val9 = 100 / sup2                    
                
        labels = ['technic','coordination', 'flexibility', 'back strength', 'core strength', 'arms strength', 'arms endurance', 'fingers strength', 'fingers endurance']   
 
        value = [val8,val9,val7, val6, val5, val3, val4, val1, val2, val8]
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles,[angles[0]]))
        self.canvas.axes.fill(angles, value, alpha=0.25)
        self.canvas.axes.set_thetagrids(angles * 180/np.pi, labels, fontsize = 7)
        self.canvas.axes.set_yticklabels([])
        self.canvas.axes.plot(angles, value)
        self.canvas.figure.savefig("{0}/{0}_globalfeedback_%s.png".format(name)%dates)
        self.canvas.draw()        
        
        
