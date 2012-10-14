# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BBui.ui'
#
# Created: Sun Oct 14 10:23:44 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BB(object):
    def setupUi(self, BB):
        BB.setObjectName(_fromUtf8("BB"))
        BB.resize(800, 600)
        self.bbwidget = QtGui.QWidget(BB)
        self.bbwidget.setObjectName(_fromUtf8("bbwidget"))
        self.bbview = QtGui.QGraphicsView(self.bbwidget)
        self.bbview.setGeometry(QtCore.QRect(90, 10, 681, 551))
        self.bbview.setObjectName(_fromUtf8("bbview"))
        BB.setCentralWidget(self.bbwidget)
        self.menubar = QtGui.QMenuBar(BB)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BB.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BB)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BB.setStatusBar(self.statusbar)

        self.retranslateUi(BB)
        QtCore.QMetaObject.connectSlotsByName(BB)

    def retranslateUi(self, BB):
        BB.setWindowTitle(QtGui.QApplication.translate("BB", "BB", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BB = QtGui.QMainWindow()
    ui = Ui_BB()
    ui.setupUi(BB)
    BB.show()
    sys.exit(app.exec_())

