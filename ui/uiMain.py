from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, QStatusBar, QWidget, QPlainTextEdit, QPushButton, QFrame, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from ui.drawingBoard import DrawingBoard

MIN_WINDOW_WIDTH = 600
MIN_WINDOW_HEIGHT = 400
MAX_WINDOW_WIDTH = 2000
MAX_WINDOW_HEIGHT = 2000

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow

        # Window Configurations
        self.mainWindow.setObjectName("MainWindow")
        self.mainWindow.resize(800, 600)
        self.mainWindow.setMinimumSize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)

        # Central Widget Configurations
        self.centralLayout = QVBoxLayout()
        self.centralwidget = QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Problem Widget Configurations
        self.problemwidget = DrawingBoard(self.mainWindow)
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

        self.bottomButtonsLayout = QVBoxLayout()
        self.bottomButtonswidget = QWidget()
        self.bottomButtonswidget.setAutoFillBackground(True)
        self.bottomButtonswidget.setObjectName("bottomButtonswidget")

        # Console
        self.textBrowser = QPlainTextEdit()
        self.textBrowser.setObjectName("textBrowser")

        # Buttons
        self.pushButton_lockGrid = QPushButton()
        self.pushButton_lockGrid.setObjectName("pushButton_lockGrid")

        self.pushButton_unlockGrid = QPushButton()
        self.pushButton_unlockGrid.setObjectName("pushButton_unlockGrid")
        self.pushButton_unlockGrid.setEnabled(False)

        # Lines
        self.line = QFrame(self.bottomInteractionwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        self.bottomButtonsLayout.addWidget(self.pushButton_lockGrid)
        self.bottomButtonsLayout.addWidget(self.pushButton_unlockGrid)
        self.bottomButtonswidget.setLayout(self.bottomButtonsLayout)

        self.bottomInteractionLayout.addWidget(self.textBrowser)
        self.bottomInteractionLayout.addWidget(self.bottomButtonswidget)
        self.bottomInteractionwidget.setLayout(self.bottomInteractionLayout)

        self.bottomLayout.addWidget(self.line)
        self.bottomLayout.addWidget(self.bottomInteractionwidget)
        self.bottomwidget.setLayout(self.bottomLayout)        

        self.centralLayout.addWidget(self.problemwidget)
        self.centralLayout.addWidget(self.bottomwidget)
        self.centralwidget.setLayout(self.centralLayout)

        self.mainWindow.setCentralWidget(self.centralwidget)

        # Menus
        self.menubar = QMenuBar(self.mainWindow)
        self.menubar.setGeometry(0, 0, 600, 25)
        self.menubar.setObjectName("menubar")

        self.menuAlgorithm = QMenu(self.menubar)
        self.menuAlgorithm.setObjectName("menuAlgorithm")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.mainWindow.setMenuBar(self.menubar)

        self.actionDijkstra = QAction(self.mainWindow)
        self.actionDijkstra.setObjectName("actionDijkstra")
        self.actionExport = QAction(self.mainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionSave = QAction(self.mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QAction(self.mainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QAction(self.mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuAlgorithm.addAction(self.actionDijkstra)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())

        # Status Bar
        self.statusbar = QStatusBar(self.mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.mainWindow.setStatusBar(self.statusbar)

        self.setTextsUi(self.mainWindow)

        self.problemwidget.setOutput(self.textBrowser)
        self.problemwidget.setStatusBar(self.statusbar)

    def setGridAndLockResize(self):
        self.problemwidget.setFullGrid()
        self.mainWindow.setFixedSize(self.mainWindow.width(), self.mainWindow.height())
        self.pushButton_lockGrid.setEnabled(False)
        self.pushButton_unlockGrid.setEnabled(True)

    def clearGridAndUnlockResize(self):
        self.problemwidget.clearGrid()
        self.mainWindow.setMinimumSize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        self.mainWindow.setMaximumSize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)
        self.pushButton_lockGrid.setEnabled(True)
        self.pushButton_unlockGrid.setEnabled(False)

    def initActions(self):
        self.pushButton_lockGrid.clicked.connect(self.setGridAndLockResize)
        self.pushButton_unlockGrid.clicked.connect(self.clearGridAndUnlockResize)

    def setTextsUi(self, MainWindow):
        self.mainWindow.setWindowTitle("Path Finding Algorithms")
        self.pushButton_lockGrid.setText("Generate Grid")
        self.pushButton_unlockGrid.setText("Clear Grid")
        self.menuAlgorithm.setTitle("Algorithm")
        self.menuFile.setTitle("File")
        self.actionDijkstra.setText("Dijkstra")
        self.actionExport.setText("Export..")
        self.actionSave.setText("Save")
        self.actionLoad.setText("Load")
        self.actionExit.setText("Exit")
        self.textBrowser.appendPlainText("<Begining of Output Console>")
