# -*- coding: utf-8 -*-

"""
Handels the control of the underlying program
Excepts commands from guiHandler und translates them to
'useable' program function calls
"""
#from bilderarray import bilderarray
from bilderdict import bilderdict


class BBA:
    """ Programm class that handles calls from guihandler
    
    """
    def __init__(self):
        """ Initialises bilderdict class
        
        """
        #self.ba = bilderarray()
        self.bd = bilderdict()
        
    def add_image_bd(self, filepath):
        """ Add one image to bilderarray class
        
        """
        self.bd.add_image_to_array(filepath)
        
    def get_imageName_list(self):
        """ Return Bild name list/array from a dict where a bild instance is 
            mapped to its bild name
            
        Return:
            array of bild names
        
        """
        _tmp = self.bd.bdict.keys()
        #_tmp = _tmp.values()
        return _tmp
        
    def get_imageByName(self, name):
        """ Return an Bild instance with the bild name as key
        
        """
        _tmp = self.bd.bdict[name]
        return _tmp
        
    def get_totalInt_list(self):
        """ Return an array with number and totalInt
        
        """
        _list = self.bd.get_attList()
        _tmpX = []
        _tmpY = []
        for entry in _list:
            _tmpX.append(entry[0])
            _tmpY.append(entry[2])
        return _tmpX, _tmpY
        