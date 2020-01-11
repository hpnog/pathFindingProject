from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QStatusBar, QWidget, QPlainTextEdit, QPushButton, QFrame, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from ui.drawingBoard import DrawingBoard

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Window Configurations
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(600, 400)

        # Central Widget Configurations
        self.centralLayout = QVBoxLayout()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Problem Widget Configurations
        self.problemwidget = DrawingBoard(MainWindow)
        self.problemwidget.setAutoFillBackground(True)
        newPallete = self.problemwidget.palette()
        newPallete.setColor(self.problemwidget.backgroundRole(), QColor("#ffffffff"))
        self.problemwidget.setPalette(newPallete)
        self.problemwidget.setObjectName("problemwidget")

        # Bottom Widget Configurations
        self.bottomLayout = QVBoxLayout()
        self.bottomwidget = QWidget()
        self.bottomwidget.setAutoFillBackground(True)
        self.bottomwidget.setObjectName("bottomwidget")
        self.bottomwidget.setMaximumHeight(150)

        self.bottomInteractionLayout = QHBoxLayout()
        self.bottomInteractionwidget = QWidget()
        self.bottomInteractionwidget.setAutoFillBackground(True)
        self.bottomInteractionwidget.setObjectName("bottomInteractionwidget")

        # Console
        self.textBrowser = QPlainTextEdit()
        self.textBrowser.setObjectName("textBrowser")

        # Buttons
        self.pushButton_grid = QPushButton()
        self.pushButton_grid.setObjectName("pushButton_grid")

        # Lines
        self.line = QFrame(self.bottomInteractionwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        self.bottomInteractionLayout.addWidget(self.textBrowser)
        self.bottomInteractionLayout.addWidget(self.pushButton_grid)
        self.bottomInteractionwidget.setLayout(self.bottomInteractionLayout)

        self.bottomLayout.addWidget(self.line)
        self.bottomLayout.addWidget(self.bottomInteractionwidget)
        self.bottomwidget.setLayout(self.bottomLayout)        

        self.centralLayout.addWidget(self.problemwidget)
        self.centralLayout.addWidget(self.bottomwidget)
        self.centralwidget.setLayout(self.centralLayout)

        MainWindow.setCentralWidget(self.centralwidget)

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

        self.problemwidget.setOutput(self.textBrowser)
        self.problemwidget.setStatusBar(self.statusbar)

    def setGenerateGridAction(self):
        self.pushButton_grid.clicked.connect(self.problemwidget.triggerFullGrid)

    def setTextsUi(self, MainWindow):
        MainWindow.setWindowTitle("Path Finding Algorithms")
        self.pushButton_grid.setText("Generate Grid")
        self.menuAlgorithm.setTitle("Algorithm")
        self.menuFile.setTitle("File")
        self.actionDijkstra.setText("Dijkstra")
        self.actionExport.setText("Export..")
        self.actionSave.setText("Save")
        self.actionLoad.setText("Load")
        self.actionExit.setText("Exit")
        self.textBrowser.appendPlainText("<Begining of Output Console>")
