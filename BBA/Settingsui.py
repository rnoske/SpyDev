# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settingsui.ui'
#
# Created: Thu Oct 11 21:22:48 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(303, 222)
        self.centralwidget = QtGui.QWidget(Settings)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.Nullhoehe_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Nullhoehe_label.setFont(font)
        self.Nullhoehe_label.setObjectName(_fromUtf8("Nullhoehe_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.Nullhoehe_label)
        self.Nullhoehe = QtGui.QSpinBox(self.layoutWidget)
        self.Nullhoehe.setMaximum(2000)
        self.Nullhoehe.setObjectName(_fromUtf8("Nullhoehe"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.Nullhoehe)
        self.Flammenmitte_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Flammenmitte_label.setFont(font)
        self.Flammenmitte_label.setObjectName(_fromUtf8("Flammenmitte_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.Flammenmitte_label)
        self.Flammenmitte = QtGui.QSpinBox(self.layoutWidget)
        self.Flammenmitte.setMaximum(2000)
        self.Flammenmitte.setObjectName(_fromUtf8("Flammenmitte"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.Flammenmitte)
        self.GradZwischenBildern_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GradZwischenBildern_label.setFont(font)
        self.GradZwischenBildern_label.setObjectName(_fromUtf8("GradZwischenBildern_label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.GradZwischenBildern_label)
        self.GradZwischenBildern = QtGui.QSpinBox(self.layoutWidget)
        self.GradZwischenBildern.setMaximum(360)
        self.GradZwischenBildern.setObjectName(_fromUtf8("GradZwischenBildern"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.GradZwischenBildern)
        self.Aufloesung_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Aufloesung_label.setFont(font)
        self.Aufloesung_label.setObjectName(_fromUtf8("Aufloesung_label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.Aufloesung_label)
        self.Workspace_label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Workspace_label.setFont(font)
        self.Workspace_label.setObjectName(_fromUtf8("Workspace_label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.Workspace_label)
        self.ChooseWorkspace_Button = QtGui.QPushButton(self.layoutWidget)
        self.ChooseWorkspace_Button.setObjectName(_fromUtf8("ChooseWorkspace_Button"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.ChooseWorkspace_Button)
        self.WorkspaceShow_label = QtGui.QLabel(self.layoutWidget)
        self.WorkspaceShow_label.setObjectName(_fromUtf8("WorkspaceShow_label"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.WorkspaceShow_label)
        self.Aufloesung = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.Aufloesung.setObjectName(_fromUtf8("Aufloesung"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.Aufloesung)
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Settings)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Settings.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(Settings)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(Settings)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuSettings.addAction(self.actionLoad)
        self.menuSettings.addAction(self.actionSave)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(Settings)
        QtCore.QObject.connect(self.actionLoad, QtCore.SIGNAL(_fromUtf8("triggered()")), Settings.loadSettings)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), Settings.saveSettings)
        QtCore.QObject.connect(self.ChooseWorkspace_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), Settings.chooseWorkspace)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.Nullhoehe_label.setText(QtGui.QApplication.translate("Settings", "Nullhoehe", None, QtGui.QApplication.UnicodeUTF8))
        self.Flammenmitte_label.setText(QtGui.QApplication.translate("Settings", "Flammenmitte", None, QtGui.QApplication.UnicodeUTF8))
        self.GradZwischenBildern_label.setText(QtGui.QApplication.translate("Settings", "Grad zwischen Bildern", None, QtGui.QApplication.UnicodeUTF8))
        self.Aufloesung_label.setText(QtGui.QApplication.translate("Settings", "Aufloesung", None, QtGui.QApplication.UnicodeUTF8))
        self.Workspace_label.setText(QtGui.QApplication.translate("Settings", "Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.ChooseWorkspace_Button.setText(QtGui.QApplication.translate("Settings", "Choose Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.WorkspaceShow_label.setText(QtGui.QApplication.translate("Settings", "Current Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("Settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("Settings", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("Settings", "Save", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Settings = QtGui.QMainWindow()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

