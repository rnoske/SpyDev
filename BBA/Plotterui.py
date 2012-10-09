# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plotterui.ui'
#
# Created: Tue Oct 09 09:04:40 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Plotterui(object):
    def setupUi(self, Plotterui):
        Plotterui.setObjectName(_fromUtf8("Plotterui"))
        Plotterui.resize(803, 586)
        self.MPLArea = MplWidget(Plotterui)
        self.MPLArea.setGeometry(QtCore.QRect(110, 10, 641, 561))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MPLArea.sizePolicy().hasHeightForWidth())
        self.MPLArea.setSizePolicy(sizePolicy)
        self.MPLArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.MPLArea.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.MPLArea.setObjectName(_fromUtf8("MPLArea"))
        self.Tesplot = QtGui.QPushButton(Plotterui)
        self.Tesplot.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.Tesplot.setObjectName(_fromUtf8("Tesplot"))

        self.retranslateUi(Plotterui)
        QtCore.QObject.connect(self.Tesplot, QtCore.SIGNAL(_fromUtf8("clicked()")), Plotterui.test_plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotterui)

    def retranslateUi(self, Plotterui):
        Plotterui.setWindowTitle(QtGui.QApplication.translate("Plotterui", "Plotter", None, QtGui.QApplication.UnicodeUTF8))
        self.Tesplot.setText(QtGui.QApplication.translate("Plotterui", "Testplotter", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Plotterui = QtGui.QWidget()
    ui = Ui_Plotterui()
    ui.setupUi(Plotterui)
    Plotterui.show()
    sys.exit(app.exec_())

