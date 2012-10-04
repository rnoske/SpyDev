# -*- coding: utf-8 -*-

"""
Handels the control of the underlying program
Excepts commands from guiHandler und translates them to
'useable' program function calls
"""
from bilderarray import bilderarray


class BBA:
    """
    Programm class that handles calls from guihandler
    """
    def __init__(self):
        """
        Initialises bilderarray class
        """
        self.ba = bilderarray()
        
    def add_image_ba(self, filepath):
        """
        adds one image to bilderarray class
        """
        self.ba.add_image_to_array(filepath)
        self.ba.calc_name()
        
    def get_imageName_list(self):
        """
        Returns Bild name list from a dict where a bild instance is mapped
        to its bild name
        """
        _tmp = self.ba.nameList
        _tmp = _tmp.keys()
        #_tmp = _tmp.values()
        return _tmp
        
    def get_imageByName(self, name):
        """
        Returns an Bild instance with the bild name as key
        """
        _tmp = self.ba.nameList[name]
        return _tmp
        
    def get_totalInt_list(self):
        """
        Returns an array with number and totalInt
        """
        _list = self.ba.get_attList()
        _tmpX = []
        _tmpY = []
        for entry in _list:
            _tmpX.append(entry[0])
            _tmpY.append(entry[2])
        return _tmpX, _tmpY
        