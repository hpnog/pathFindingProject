from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QStatusBar, QWidget, QTextBrowser, QGridLayout, QPushButton, QFrame
from PyQt5.QtGui import QColor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Window Configurations
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(600, 400)

        # Central Widget Configurations
        self.centralGrid = QGridLayout()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        newPallete = self.centralwidget.palette()
        newPallete.setColor(self.centralwidget.backgroundRole(), QColor("#bbbbbbbb"))
        self.centralwidget.setPalette(newPallete)
        self.centralwidget.setObjectName("centralwidget")

        # Bottom Widget Configurations
        self.bottomGrid = QGridLayout()
        self.bottomwidget = QWidget()
        self.bottomwidget.setAutoFillBackground(True)
        newPallete = self.bottomwidget.palette()
        newPallete.setColor(self.bottomwidget.backgroundRole(), QColor("#00000000"))
        self.bottomwidget.setPalette(newPallete)
        self.bottomwidget.setObjectName("bottomwidget")
        self.bottomwidget.setMaximumHeight(150)

        # Console
        self.textBrowser = QTextBrowser()
        self.textBrowser.setObjectName("textBrowser")

        # Buttons
        self.pushButton = QPushButton()
        self.pushButton.setObjectName("pushButton")

        # Lines
        self.line = QFrame(self.bottomwidget)
        # self.line.setGeometry(10, 270, 581, 20)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        self.bottomGrid.addWidget(self.line, 0, 0, 1, 2)
        self.bottomGrid.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.bottomGrid.addWidget(self.pushButton, 1, 1, 1, 1)
        self.bottomwidget.setLayout(self.bottomGrid)

        self.centralGrid.addWidget(self.bottomwidget)
        self.centralwidget.setLayout(self.centralGrid)

        MainWindow.setCentralWidget(self.centralwidget)
#
        # Menus
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(0, 0, 600, 25)
        self.menubar.setObjectName("menubar")

        self.menuAlgorithm = QMenu(self.menubar)
        self.menuAlgorithm.setObjectName("menuAlgorithm")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName("actionDijkstra")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAlgorithm.addAction(self.actionDijkstra)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())

        # Status Bar
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.setTextsUi(MainWindow)
#        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setTextsUi(self, MainWindow):
        MainWindow.setWindowTitle("Path Finding Algorithms")
        self.pushButton.setText("PushButton")
        self.menuAlgorithm.setTitle("Algorithm")
        self.menuFile.setTitle("File")
        self.actionDijkstra.setText("Dijkstra")
        self.actionExport.setText("Export..")
        self.actionSave.setText("Save")
        self.actionLoad.setText("Load")
        self.actionExit.setText("Exit")
        self.textBrowser.setText("<Begining of Output Console>")
