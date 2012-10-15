# -*- coding: utf-8 -*-

#standard library imports
#import logging
import sys
import random

#related third party imports
#import numpy as np # NumPy (multidimensional arrays, linear algebra, ...)
from PyQt4 import QtCore, QtGui

#local application/library specific imports


class Atom(QtGui.QGraphicsEllipseItem):
    """ Creates custom QGraphics Item widget with atom attributes
    
    """
    def __init__(self, x, y, breite, hoehe):
        #Erbe von EllipseItem
        QtGui.QGraphicsEllipseItem.__init__(self, x, y, breite, hoehe)
        
        #Ordnungszahl
        self.oz = 1
        #Gewicht
        self.m = 2 #g/mol
        #Geschwindigkeit
        self.v = 10 #m/s
        #Direction
        self.dx = 0.5 #x direction
        self.dy = 0.5 #y direction
        #Energie
        self.e_kin = 0.5 * self.w * self.v
        
