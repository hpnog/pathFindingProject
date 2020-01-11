# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startingPathFinding.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Window Configurations
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))

        # Central Widget Configurations
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        # Buttons
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 300, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        # Lines
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 270, 581, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        # Console
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 290, 450, 50))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        MainWindow.setCentralWidget(self.centralwidget)

        # Menus
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAlgorithm = QtGui.QMenu(self.menubar)
        self.menuAlgorithm.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menuAlgorithm.setObjectName(_fromUtf8("menuAlgorithm"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)

        self.actionDijkstra = QtGui.QAction(MainWindow)
        self.actionDijkstra.setObjectName(_fromUtf8("actionDijkstra"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuAlgorithm.addAction(self.actionDijkstra)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())

        # Status Bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Path Finding Algorithms", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.menuAlgorithm.setTitle(_translate("MainWindow", "Algorithm", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionDijkstra.setText(_translate("MainWindow", "Dijkstra", None))
        self.actionExport.setText(_translate("MainWindow", "Export..", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
