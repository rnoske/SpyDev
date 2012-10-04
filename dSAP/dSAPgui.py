# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dSAPgui.ui'
#
# Created: Thu Sep 27 14:24:37 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dSAP(object):
    def setupUi(self, dSAP):
        dSAP.setObjectName(_fromUtf8("dSAP"))
        dSAP.resize(800, 600)
        self.centralwidget = QtGui.QWidget(dSAP)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 258, 223))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Matlist = QtGui.QListWidget(self.widget)
        self.Matlist.setObjectName(_fromUtf8("Matlist"))
        self.verticalLayout.addWidget(self.Matlist)
        self.OpenFiles = QtGui.QPushButton(self.widget)
        self.OpenFiles.setObjectName(_fromUtf8("OpenFiles"))
        self.verticalLayout.addWidget(self.OpenFiles)
        dSAP.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(dSAP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        dSAP.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(dSAP)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        dSAP.setStatusBar(self.statusbar)

        self.retranslateUi(dSAP)
        QtCore.QObject.connect(self.OpenFiles, QtCore.SIGNAL(_fromUtf8("clicked()")), dSAP.openMatFiles)
        QtCore.QMetaObject.connectSlotsByName(dSAP)

    def retranslateUi(self, dSAP):
        dSAP.setWindowTitle(QtGui.QApplication.translate("dSAP", "dSAP", None, QtGui.QApplication.UnicodeUTF8))
        self.OpenFiles.setText(QtGui.QApplication.translate("dSAP", "Open Matlab Files", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dSAP = QtGui.QMainWindow()
    ui = Ui_dSAP()
    ui.setupUi(dSAP)
    dSAP.show()
    sys.exit(app.exec_())

