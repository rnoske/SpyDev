# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from dSAPgui import Ui_dSAP
from dSAPprogHandler import dSAP
import sys
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
from pylab import *              # Matplotlib's pylab interface
ion()                            # Turned on Matplotlib's interactive mode
import scipy.io


class dSAPguiHandler(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_dSAP()
        self.ui.setupUi(self)
        self.dsap = dSAP()
       
    def openMatFiles(self):
        _pfad = 'D:\Raimund Buero\Python'
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Select one or more files to open', _pfad, 'Converted mat files (*.txt)')
        print filepath
        _file = open(filepath, 'r')
        import csv
        reader = csv.reader(_file, delimiter='\t')
        _arr = [[]]
        for i, row in enumerate(reader):
            _arr.append([])
            for j, item in enumerate(row):
                
                item = item.lstrip(' ')
                if item == ' ' or item == '\n' or item == '':
                    item = '0'
                #print i, j
                _arr[i].append(float(item))
                #print item
        print _arr
        _file.close()
        
        
if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = dSAPguiHandler()
   myapp.show()
   sys.exit(app.exec_())