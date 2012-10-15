# -*- coding: utf-8 -*-


#standard library imports
#import logging
import sys
import random

#related third party imports
#import numpy as np # NumPy (multidimensional arrays, linear algebra, ...)
from PyQt4 import QtCore, QtGui

#local application/library specific imports
import BBui
import atom

class BouncingBalls(QtGui.QMainWindow):
    """ Bouncing Ball class
    
    """
    def __init__(self, parent = None):
        """ Initialisation
        
        """
        #this part is almost always the same for displaying the ui
        QtGui.QWidget.__init__(self, parent)
        self.ui = BBui.Ui_BB()
        self.ui.setupUi(self)
        #self.show()
        

        #define view
        self.view = self.ui.bbview
        #define scene:
        self.bbscene = QtGui.QGraphicsScene(self)
        self.view.setScene(self.bbscene)
        
        
        #add items
        self.itemlist = []
        nitems = 10
        for i in xrange(nitems):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            #item = QtGui.QGraphicsEllipseItem(x,y,20,40)
            item = atom.Atom(x, y, 10, 10)
            self.itemlist.append(item)
        
        for item in self.itemlist:
            self.bbscene.addItem(item)
        
        #Animations:
        #Create an set timer
        self.animator = QtCore.QTimer()
        #When the animator triggers it is calling the animate method
        self.animator.timeout.connect(self.animate)
        
        #to animate it once manually
        #self.animate()
        
        #start the animator. Trigger occours every x milliseconds
        self.animationlength = 1000
        self.animator.start(self.animationlength)
        

    def animate_to(self, t, item, x, y, angle):
        """ Animate an item in the given time to pos x,y
        
        """
        # The QGraphicsItemAnimation class is used to
        # animate an item in specific ways
        animation=QtGui.QGraphicsItemAnimation()

        # You create a timeline (in this case, it is 1 second long
        timeline=QtCore.QTimeLine(t*1000)

        # And it has 100 steps
        timeline.setFrameRange(0,100)

        # I want that, at time t, the item be at point x,y
        animation.setPosAt(t,QtCore.QPointF(x,y))

        # And it should be rotated at angle "angle"
        animation.setRotationAt(t,angle)

        # It should animate this specific item
        animation.setItem(item)

        # And the whole animation is this long, and has
        # this many steps as I set in timeline.
        animation.setTimeLine(timeline)
        

        # Here is the animation, use it.
        return animation
        
    
    def animate(self):
        """ Move an item
        
        """        
        #List of animations
        self.animations = []

        #duration of animation in s
        t = self.animationlength / 1000
        
        #x = 100
        #y = 0
        for item in self.itemlist:
            angle = 0 #random.randint(0, 360)
            #choose direction
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
            #choose velocity
            v = item.v * t
            #calculate new item position
            x = x*v + item.pos().x() + item.dx
            y = y*v + item.pos().y() + item.dy
            #set new position and append it to animation list
            self.animations.append(self.animate_to(t, item, x, y, angle))
            
            """
            coll_list = item.collidingItems()
            for coll_item in coll_list:
                if item.collidesWithItem(coll_item):
                    print coll_item
                    pos = item.pos()
                    print pos.x(), pos.y()
                    print item.oz
            """
            
        #Start animations?
        for animation in self.animations:
            animation.timeLine().start()
        
        #Starts the animator for 1000
        #self.animator.start(1000)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = BouncingBalls()
    myapp.show()
    sys.exit(app.exec_())




