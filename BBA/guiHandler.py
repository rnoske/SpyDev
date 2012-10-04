# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from BBAgui import Ui_BBA
from progHandler import BBA
import sys
import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
from pylab import *              # Matplotlib's pylab interface
ion()                            # Turned on Matplotlib's interactive mode

class guiHandler(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_BBA()
        self.ui.setupUi(self)
        self.bba = BBA()

        #handlers: gar nicht wirklich gebraucht! Einfach signal von button auf Main window ziehen
        #QtCore.QObject.connect(self.ui.buttonCalc, QtCore.SIGNAL("clicked()"), self.ui.lineEditX.clear )
        #QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.raysFunc )
    
    def raysFunc(self):
        x = int(self.ui.lineEditX.text())
        y = int(self.ui.lineEditY.text())
        self.ui.lineEditZ.setText(str(x+y))

    def openImages(self):
        filepaths = QtGui.QFileDialog.getOpenFileNames(self, 
                                                      'Select one or more files to open',
                                                      'D:\Raimund Buero\Python', 
                                                      'Images (*.bmp *png *jpg)')
        for filepath in filepaths:
            self.bba.add_image_ba(str(filepath))
        _nL = self.bba.get_imageName_list()
        for name in _nL:
            _fp = QtGui.QListWidgetItem(name, self.ui.ImageList)
            self.ui.ImageList.addItem(_fp)
            

    def filepathClicked(self):
        _tmp = self.ui.ImageList.currentItem()
        _tmp = QtGui.QListWidgetItem.text(_tmp)
        #print _tmp
        self.ui.currentImage.setText(_tmp)
        _fp = self.bba.get_imageByName(str(_tmp)).pfad
        self.update_ImageDisplay(_fp)
        
    def update_ImageDisplay(self, pfad):
        image = QtGui.QPixmap(pfad)
        view = self.ui.BildViewer
        scene = QtGui.QGraphicsScene()
        item = QtGui.QGraphicsPixmapItem(image)
        scene.addItem(item)
        view.setScene(scene)
        view.show()
        
    def plot_totalInt(self):
        _X, _Y = self.bba.get_totalInt_list()
        plt.plot(_X, _Y)
        plt.ylabel('Total Int')
        plt.show()


if __name__ == "__main__":
   app = QtGui.QApplication(sys.argv)
   myapp = guiHandler()
   myapp.show()
   sys.exit(app.exec_())