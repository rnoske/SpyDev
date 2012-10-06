# -*- coding: utf-8 -*-

import logging
from bild import Bild
import collections

class bilderdict:
    """ Dict class for holding and managing bild objects
    
    """
    def __init__(self):
        """ Create an empty orderd dict
        
        Creates:
            bdict (ordered dict)
        
        """
        self.bdict = collections.OrderedDict()
        
    def add_image_to_array(self, pfad):
        """ Add given image to dict
        
        prad (str): complete file path to image
        
        """
        _Bild = Bild(pfad)
        _name = _Bild.att['name']
        self.bdict[_name] = _Bild
        logging.info('Bild hinzugefuegt')
        
    def calc_totalInt(self):
        """ Calculate total Intensity for every image in the array
        
        """
        for k, v in self.bdict.iteritems():
            try:
                v.calc_totalInt()
                _msg = 'Total Int von ' + str(k) + 'wurde berechnet'
                logging.debug(_msg)
                
            except:
                _errmsg = 'Total Int von ' + str(k) + 'konnte nicht berechnet \
                werden'
                logging.error(_errmsg)
        
    def get_attList(self):
        """ Get attributes of images in the dict
        
        Return:
            array: 3 columns; number, name, totalInt
            
        """
        self.calc_totalInt()
        _tmp = []
        for k, v in self.bdict.iteritems():
            _entry = [v.att['bid'], v.att['name'], v.att['totalInt']]
            _tmp.append(_entry)
        return _tmp