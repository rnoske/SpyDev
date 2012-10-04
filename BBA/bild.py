# -*- coding: utf-8 -*-

"""
Basic bild class for handling taken images.
"""
#Imports:
import logging
"""
logging info:
DEBUG	Detailed information, typically of interest only when diagnosing problems.
INFO	Confirmation that things are working as expected.
WARNING	An indication that something unexpected happened, or indicative of 
    some problem in the near future (e.g. ‘disk space low’). The software is 
    still working as expected.
ERROR	Due to a more serious problem, the software has not been able to perform 
    some function.
CRITICAL	A serious error, indicating that the program itself may be unable 
    to continue running.
"""
#Scientific imports, idea taken from spyder
import os
import numpy as np # NumPy (multidimensional arrays, linear algebra, ...)
#import scipy as sp # SciPy (signal and image processing library)
#import matplotlib as mpl         # Matplotlib (2D/3D plotting library)
#import matplotlib.pyplot as plt  # Matplotlib's pyplot: MATLAB-like syntax
#from pylab import *              # Matplotlib's pylab interface
#ion()                            # Turned on Matplotlib's interactive mode

from PIL import Image as PILImage

#Actual code
class Bild:
    """
    Basic image class. All other images inherit from this class.
    """
    def __init__(self, pfad, **kwargs):
        """
        Initialize attributes
        pfad = complete file path for opening image
        """
        self.att = {} #attribute directory
        #checks if pfad is valid
        if os.path.exists(pfad) == True:
            self.pfad = pfad
            logging.info('Image pfad was set: %s', pfad)
        else:
            logging.warning('No file found under pfad %s. No image was opened',
                            pfad)
    
    def calc_name(self):
        """
        Sets a name for the image.
        """
        namen = str(self.pfad).split(os.sep) 
        name = namen.pop()
        self.att['name']=name
        
    def open_image(self):
        """
        Opens and returns an PIL image
        """
        _fp = open(self.pfad, 'rb')
        img = PILImage.open(_fp)
        #img = img.convert('L')
        _fp.close
        return img
        
    def create_array(self):
        """
        creates and numpy array from open image
        returns np.array
        """
        self.att['hoehe'] = np.array(self.open_image()).shape[0]
        self.att['breite'] = np.array(self.open_image()).shape[1]
        return np.array(self.open_image())
        
    def calc_totalInt(self):
        _arr = self.create_array()
        self.att['totalInt'] = _arr.sum()
        _apx = self.att['hoehe'] * self.att['breite']
        self.att['mittelint'] = self.att['totalInt'] / _apx
        
        
        
class ColorBild(Bild):
    """
    Image class for handling color images. Inherits from Bild class
    """
        