# -*- coding: utf-8 -*-

#Guihandler!

import Fittergui
import Fitterwidget
import sys
from PyQt4 import QtCore, QtGui

class specfit(QtGui.QMainWindow):
    """ Guihandler for all of the specfit program
    
    """
    def __init__(self, parent = None):
        """ Initialisation methond
        
        """

        
        QtGui.QWidget.__init__(self, parent)
        #myFittergui = QtGui.QMainWindow()
        ui = Fittergui.Ui_Fittergui()
        ui.setupUi(self)
        #myFittergui.show()
        
        self.openWidgetWindow()
    
        
        
        

    def openWidgetWindow(self):
        self.myFitterWidget = QtGui.QMainWindow()
        self.wui = Fitterwidget.Ui_FitterWidget()
        self.wui.setupUi(self.myFitterWidget)
        self.myFitterWidget.show()
        
    def raysfunc(self):
        print 'blub'

if __name__ == "__main__":
    app2 = QtGui.QApplication(sys.argv)
    myspecfit = specfit()
    myspecfit.show()
    sys.exit(app2.exec_())
    
    #app = QtGui.QApplication(sys.argv)
    
       
    
    
    
    
    
    
    #sys.exit(app.exec_())
     