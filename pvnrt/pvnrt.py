# -*- coding: utf-8 -*-

#standard library imports
import logging
import sys

#related third party imports
import numpy as np # NumPy (multidimensional arrays, linear algebra, ...)
from PyQt4 import QtCore, QtGui

#local application/library specific imports
import bouncingballs


class Pvnrt(QtGui.QMainWindow):
    """ pv = nrt class
    
    """
    def __init__(self, parent = None):
        """ Initialisation
        
        """
        QtGui.QWidget.__init__(self, parent)
        self.ui = bouncingballs.BouncingBalls()
        #self.ui.setupUi(self)
        #self.show()




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myBB = Pvnrt()
    #myspecfit.show()
    sys.exit(app.exec_())