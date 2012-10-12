# -*- coding: utf-8 -*-

""" My Input and Output IO clas/file

"""
#standard library imports
import numpy as np
import logging
#related third party imports

#local application/library specific imports


class RnIo():
    """ My IO class
    
    """
    
    def __init__(self, workspace = ''):
        """ IO initialisation
        
        """
        self.workspace = workspace
    
    def write_nparray_csv(self, nparray, header = [], 
                            speichername = 'test.csv', 
                            delimiter = ';'):
        """ Write 2D nparray to ascii file
        
        nparray (nparray): 2D numpy data array
        header (arr): 1D python array of header
        speichername (str): name of file to write
        delimiter (str): delimiter which shall be used
        
        """
        #Assertions
        try:
            assert(isinstance(nparray, np.ndarray))
            assert(isinstance(header, list))
            assert(isinstance(speichername, str))
            assert(isinstance(delimiter, str))
        except AssertionError:
            logging.error('ein paramter hat nicht das passende format')
        
        #Code
        filepath = self.workspace + speichername
        with open(filepath, 'wb') as f:
            #check if header exists
            if len(header) > 0:
                _row = ''
                for entry in header:
                    _row += str(entry) + delimiter
                _row += '\n'
                f.write(_row)
                    
            for y in xrange(nparray.shape[0]):
                _row = ''
                for x in xrange(nparray.shape[1]):
                    _row += str(nparray[y, x]) + delimiter
                _row += '\n'
                f.write(_row)
            
    def read_csv_nparray(self, name = 'test.csv', 
                         header = False, 
                         delimiter = ';'):
        """ Reads csv file
        
        name (str): file name of file e.g. test.csv
        header (bool): if file has 1 line header set as True
        delimiter: delimiter of file
        
        Returns:
            header (arr)
            nparray
        
        """
        _header = []
        _arr = []
        filepath = self.workspace + name
        with open(filepath, 'rb') as f:
            #read header
            if header == True:
                _row = f.readline()
                _header = _row.split(delimiter)
                _header.pop() #remove \n element
                
            #read data
            for line in f.xreadlines():
                line = line.split(delimiter)
                line.pop() #remove new line char
                try:
                    line = [float(x) for x in line] #convert string to float
                except ValueError:
                    logging.error("""coud no convert string to float, wrong data
                    format ist given back!""")
                _arr.append(line)

        _arr = np.array(_arr)          
        return _header, _arr
                
    def read_fits_nparray(self, name = 'test.fit', number = 0):
        """ Read .fits file from iStar camera
        
        name (str): file name
        number (int): number of hdulist (usually 0)
        
        Returns:
            _header (pyfits.header.Header): dictionary type something
            _arr (numpy.ndarray): numpy array
        
        """
        import pyfits
        _file =self. workspace + name
        _fits = pyfits.open(_file)
        _header = _fits[number].header
        _arr = _fits[number].data
        return _header, _arr


if __name__ == "__main__":
    """
    a = [[1,2,3], [4,5,6]]
    a = np.array(a)
    h = ['bla', 'blub', 'bloeb']
    myIO = RnIo()
    myIO.write_nparray_csv(a, header = h, delimiter = ';')
    nh, na = myIO.read_csv_nparray(header = True)
    print nh
    print na
    """
    myIO= RnIo()
    _h, _arr = myIO.read_fits_nparray()
    print _h['temp'], _arr
    print _arr.shape
