# -*- coding: utf-8 -*-


#standard library imports
#import logging
import sys

#related third party imports
#import numpy as np # NumPy (multidimensional arrays, linear algebra, ...)
from PyQt4 import QtCore, QtGui

#local application/library specific imports
import BBui

class BouncingBalls(QtGui.QMainWindow):
    """ Bouncing Ball class
    
    """
    def __init__(self, parent = None):
        """ Initialisation
        
        """
        QtGui.QWidget.__init__(self, parent)
        self.ui = BBui.Ui_BB()
        self.ui.setupUi(self)
        self.show()
        print 'bla'
        #define view
        view = self.ui.bbview
        #define scene:
        self.bbscene = QtGui.QGraphicsScene(self)
        view.setScene(self.bbscene)
        #add items
        item = QtGui.QGraphicsEllipseItem(0, 0, 60, 40)
        self.bbscene.addItem(item)
        
        

        
        print 'blub'

    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = BouncingBalls()
    sys.exit(app.exec_())




