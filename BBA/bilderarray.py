# -*- coding: utf-8 -*-

import logging
from bild import Bild
import collections

class bilderarray():
    """
    Class for holding and managing an array full of Bild instances
    """
    def __init__(self, **kwargs):
        """
        creates an array full of images out of bilderPfadListe
        """
        self.barr = []
        self.nameList = collections.OrderedDict() #noch irgendwie doppelt gemoppelt
        
        #for pfad in bilderPfadliste:
            #self.add_image_to_array(pfad)
        
        
        
    def add_image_to_array(self, pfad):
        """
        adds an image (as specified in the file path) to the image array
        """
        try:
            _tmpBild = Bild(pfad)
            self.barr.append(_tmpBild)
            logging.info('Bild hinzugefügt')
        except:
            logging.warning('Bild konnte nicht zum array hinzugefuegt werden')
            
    def calc_name(self):
        """ 
        calculates name for every image in the array
        """
        for entry in self.barr:
            entry.calc_name()
            self.nameList[entry.att['name']] = entry
            
        
    def calc_totalInt(self):
        """
        calculates total Intensity for every image in the array
        """
        for entry in self.barr:
            entry.calc_totalInt()
        
    def get_attList(self):
        """
        Returns a numbered array with all image attributes in one row
        number, name, totalint
        """
        self.calc_totalInt()
        _tmp = []
        for i, bild in enumerate(self.barr):
            _entry = [i, bild.att['name'], bild.att['totalInt']]
            _tmp.append(_entry)
        return _tmp