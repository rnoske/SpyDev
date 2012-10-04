# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BBAgui.ui'
#
# Created: Thu Sep 27 14:13:12 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BBA(object):
    def setupUi(self, BBA):
        BBA.setObjectName(_fromUtf8("BBA"))
        BBA.resize(800, 494)
        self.centralwidget = QtGui.QWidget(BBA)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.PlotButton = QtGui.QPushButton(self.centralwidget)
        self.PlotButton.setGeometry(QtCore.QRect(560, 0, 151, 41))
        self.PlotButton.setObjectName(_fromUtf8("PlotButton"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 524, 411))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ImageList = QtGui.QListWidget(self.widget)
        self.ImageList.setObjectName(_fromUtf8("ImageList"))
        self.verticalLayout.addWidget(self.ImageList)
        self.OpenImages = QtGui.QPushButton(self.widget)
        self.OpenImages.setObjectName(_fromUtf8("OpenImages"))
        self.verticalLayout.addWidget(self.OpenImages)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.currentImage = QtGui.QLineEdit(self.widget)
        self.currentImage.setObjectName(_fromUtf8("currentImage"))
        self.verticalLayout_2.addWidget(self.currentImage)
        self.BildViewer = QtGui.QGraphicsView(self.widget)
        self.BildViewer.setObjectName(_fromUtf8("BildViewer"))
        self.verticalLayout_2.addWidget(self.BildViewer)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        BBA.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BBA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMein_test = QtGui.QMenu(self.menubar)
        self.menuMein_test.setObjectName(_fromUtf8("menuMein_test"))
        BBA.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BBA)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BBA.setStatusBar(self.statusbar)
        self.actionOpen_Images = QtGui.QAction(BBA)
        self.actionOpen_Images.setObjectName(_fromUtf8("actionOpen_Images"))
        self.actionOpen_Image_directory = QtGui.QAction(BBA)
        self.actionOpen_Image_directory.setObjectName(_fromUtf8("actionOpen_Image_directory"))
        self.actionClose = QtGui.QAction(BBA)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuMein_test.addAction(self.actionOpen_Images)
        self.menuMein_test.addAction(self.actionOpen_Image_directory)
        self.menuMein_test.addAction(self.actionClose)
        self.menubar.addAction(self.menuMein_test.menuAction())

        self.retranslateUi(BBA)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), BBA.close)
        QtCore.QObject.connect(self.OpenImages, QtCore.SIGNAL(_fromUtf8("clicked()")), BBA.openImages)
        QtCore.QObject.connect(self.ImageList, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), BBA.filepathClicked)
        QtCore.QObject.connect(self.PlotButton, QtCore.SIGNAL(_fromUtf8("clicked()")), BBA.plot_totalInt)
        QtCore.QMetaObject.connectSlotsByName(BBA)

    def retranslateUi(self, BBA):
        BBA.setWindowTitle(QtGui.QApplication.translate("BBA", "BBA", None, QtGui.QApplication.UnicodeUTF8))
        self.PlotButton.setText(QtGui.QApplication.translate("BBA", "Plot totalInt", None, QtGui.QApplication.UnicodeUTF8))
        self.OpenImages.setText(QtGui.QApplication.translate("BBA", "Open Images", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMein_test.setTitle(QtGui.QApplication.translate("BBA", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Images.setText(QtGui.QApplication.translate("BBA", "Open Images", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Image_directory.setText(QtGui.QApplication.translate("BBA", "Open Image directory", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("BBA", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BBA = QtGui.QMainWindow()
    ui = Ui_BBA()
    ui.setupUi(BBA)
    BBA.show()
    sys.exit(app.exec_())

