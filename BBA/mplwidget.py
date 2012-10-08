# -*- coding: utf-8 -*-

# for command-line arguments
import sys
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui
# Numpy functions for image creation
import numpy as np
# Matplotlib Figure object
from matplotlib.figure import Figure
# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg \
  import FigureCanvasQTAgg as FigureCanvas
# import the NavigationToolbar Qt4Agg widget
from matplotlib.backends.backend_qt4agg \
  import NavigationToolbar2QTAgg as NavigationToolbar


class Qt4MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self, parent):
        # plot definition
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.cos(2*np.pi*t)
        self.axes.plot(t, s)
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # set the parent widget
        self.setParent(parent)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self, 
                                   QtGui.QSizePolicy.Expanding, 
                                   QtGui.QSizePolicy.Expanding) 
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)
        
class MplWidget(FigureCanvas):
    def __init__(self, parent):
        # instantiate our Matplotlib canvas widget
        qmc = Qt4MplCanvas(self.main_widget)
        # instantiate the navigation toolbar
        ntb = NavigationToolbar(qmc, self.main_widget)
        # pack these widget into the vertical box
        # set the focus on the main widget
        self.main_widget.setFocus() 
        # set the central widget of MainWindow to main_widget 
        self.setCentralWidget(self.main_widget)