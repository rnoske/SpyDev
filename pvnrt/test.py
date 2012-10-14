# -*- coding: utf-8 -*-

import random
from PyQt4.QtCore import pyqtProperty
from PyQt4.QtGui import *



class BouncingWidget(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        self.balls = []
        random.seed()
    
    def number(self):
    
        return len(self.balls)
    
    def setNumber(self, number):
    
        if 0 <= number < len(self.balls):
            self.balls = self.balls[:number]
        elif number > len(self.balls):
            while len(self.balls) < number:
                self.balls.append(
                    (random.random(), random.random(),
                     random.choice((-0.025, 0.025)), random.choice((-0.025, 0.025)))
                    )
    
    number = pyqtProperty("int", number, setNumber)
    
    def paintEvent(self, event):
    
        w = self.width()
        h = self.height()
        
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QColor(0, 0, 100))
        painter.setBrush(QBrush(QColor(200, 255, 200)))
        painter.setPen(QPen(QColor(0, 32, 0)))
        for x, y, dx, dy in self.balls:
            painter.drawEllipse((x - 0.1) * w, (y - 0.1) * h, w/10.0, h/10.0)
        painter.end()
    
    def showEvent(self, event):
    
        self.timer_id = self.startTimer(40)
    
    def hideEvent(self, event):
    
        self.killTimer(self.timer_id)
    
    def timerEvent(self, event):
    
        x1 = 0.1
        x2 = 0.9
        y1 = 0.1
        y2 = 0.9
        
        i = 0
        while i < len(self.balls):
        
            x, y, dx, dy = self.balls[i]
            
            x = min(max(x1, x + dx), x2)
            y = min(max(y1, y + dy), y2)
            if x <= x1:
                dx = 0.025
            elif x >= x2:
                dx = -0.025
            if y <= y1:
                dy = 0.025
            elif y >= y2:
                dy = -0.025
            
            self.balls[i] = x, y, dx, dy
            i += 1
        
        self.update()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    BBA = QMainWindow()
    ui = BouncingWidget()
    #ui.setupUi(BBA)
    BBA.show()
    sys.exit(app.exec_())