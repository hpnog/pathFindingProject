from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from ui.drawingBoard import DrawingBoard
from constants import *

class Ui_MainWindow(object):
    def __init__(self, mainwindow):
        self.comms = None
        self.mainWindow = mainwindow
        self.grid = None
        self.gridUpdates = None
        self.centralLayout = None
        self.centralwidget = None
        self.problemwidget = None
        self.bottomLayout = None
        self.bottomwidget = None
        self.bottomInteractionLayout = None
        self.bottomInteractionwidget = None
        self.bottomButtonsLayout = None
        self.bottomButtonswidget = None
        self.textBrowser = None
        self.pushButton_lockGrid = None
        self.pushButton_unlockGrid = None
        self.pushButton_selectStart = None
        self.pushButton_selectEnd = None
        self.pushButton_drawObstacles = None
        self.pushButton_runAlgorithm = None
        self.line = None
        self.menubar = None
        self.menuAlgorithm = None
        self.actionDijkstra = None
        self.stopAlgorithm = None
        self.actionExport = None
        self.actionSave = None
        self.actionLoad = None
        self.actionExit = None
        self.menuFile = None
        self.showByStepCheckBox = None
        self.showByStepLabel = None
        # Status Bar
        self.statusbar = QStatusBar(self.mainWindow)

        self.setupUi()

    def setupUi(self):
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
        self.bottomwidget.setMaximumHeight(MAX_MENU_HEIGHT)

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

        self.pushButton_selectStart = QPushButton()
        self.pushButton_selectStart.setObjectName("pushButton_selectStart")
        self.pushButton_selectStart.setEnabled(False)

        self.pushButton_selectEnd = QPushButton()
        self.pushButton_selectEnd.setObjectName("pushButton_selectEnd")
        self.pushButton_selectEnd.setEnabled(False)

        self.pushButton_drawObstacles = QPushButton()
        self.pushButton_drawObstacles.setObjectName("pushButton_drawObstacles")
        self.pushButton_drawObstacles.setEnabled(False)

        self.pushButton_runAlgorithm = QPushButton()
        self.pushButton_runAlgorithm.setObjectName("pushButton_runAlgorithm")
        self.pushButton_runAlgorithm.setEnabled(False)

        self.showByStepCheckBoxWidget = QWidget()
        self.showByStepCheckBoxLayout = QHBoxLayout()

        self.showByStepCheckBox = QCheckBox()
        self.showByStepCheckBox.setObjectName("showByStepCheckBox")
        self.showByStepCheckBox.setChecked(True)

        self.showByStepLabel = QLabel()
        self.showByStepLabel.setText("Show Step-by-step")

        # Lines
        self.line = QFrame(self.bottomInteractionwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        self.showByStepCheckBoxLayout.addWidget(self.showByStepCheckBox)
        self.showByStepCheckBoxLayout.addWidget(self.showByStepLabel)
        self.showByStepCheckBoxWidget.setLayout(self.showByStepCheckBoxLayout)

        self.bottomButtonsLayout.addWidget(self.pushButton_lockGrid)
        self.bottomButtonsLayout.addWidget(self.pushButton_unlockGrid)
        self.bottomButtonsLayout.addWidget(self.pushButton_selectStart)
        self.bottomButtonsLayout.addWidget(self.pushButton_selectEnd)
        self.bottomButtonsLayout.addWidget(self.pushButton_drawObstacles)
        self.bottomButtonsLayout.addWidget(self.pushButton_runAlgorithm)
        self.bottomButtonsLayout.addWidget(self.showByStepCheckBoxWidget)
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
        self.menubar.setObjectName("menubar")
        self.cornerMenu = QMenuBar()
        self.cornerMenu.setObjectName("cornerMenu")

        self.menuAlgorithm = QMenu(self.menubar)
        self.menuAlgorithm.setObjectName("menuAlgorithm")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.mainWindow.setMenuBar(self.menubar)

        self.stopAlgorithm = QAction(self.mainWindow)
        self.stopAlgorithm.setObjectName("stopAlgorithm")
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

        # No actions were implemented yet for these buttons
        # self.menuFile.addAction(self.actionSave)
        # self.menuFile.addAction(self.actionLoad)
        # self.menuFile.addAction(self.actionExport)
        
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())
        self.cornerMenu.addAction(self.stopAlgorithm)
        self.menubar.setCornerWidget(self.cornerMenu)

        # Status Bar
        self.statusbar = QStatusBar(self.mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.mainWindow.setStatusBar(self.statusbar)

        self.setTextsUi()

    def setGridAndLockResize(self):
        self.problemwidget.setFullGrid()
        self.mainWindow.setFixedSize(self.mainWindow.width(), self.mainWindow.height())
        self.pushButton_lockGrid.setEnabled(False)
        self.pushButton_unlockGrid.setEnabled(True)
        self.pushButton_selectStart.setEnabled(True)
        self.pushButton_selectEnd.setEnabled(True)
        self.pushButton_drawObstacles.setEnabled(True)
        self.pushButton_runAlgorithm.setEnabled(True)

    def clearGridAndUnlockResize(self):
        self.problemwidget.clearGrid()
        self.mainWindow.setMinimumSize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        self.mainWindow.setMaximumSize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)
        self.pushButton_lockGrid.setEnabled(True)
        self.pushButton_unlockGrid.setEnabled(False)
        self.pushButton_selectStart.setEnabled(False)
        self.pushButton_selectEnd.setEnabled(False)
        self.pushButton_drawObstacles.setEnabled(False)
        self.pushButton_runAlgorithm.setEnabled(False)

    def selectStartPressed(self):
        toggle = self.problemwidget.toggleSelectStart()
        self.selectedStart(toggle)

    def selectedStart(self, toggle=False):
        self.pushButton_selectStart.setDown(toggle)

        self.pushButton_unlockGrid.setEnabled(not toggle)
        self.pushButton_selectEnd.setEnabled(not toggle)
        self.pushButton_drawObstacles.setEnabled(not toggle)
        self.pushButton_runAlgorithm.setEnabled(not toggle)

    def selectEndPressed(self):
        toggle = self.problemwidget.toggleSelectEnd()
        self.selectedEnd(toggle)

    def selectedEnd(self, toggle=False):
        self.pushButton_selectEnd.setDown(toggle)

        self.pushButton_unlockGrid.setEnabled(not toggle)
        self.pushButton_selectStart.setEnabled(not toggle)
        self.pushButton_drawObstacles.setEnabled(not toggle)
        self.pushButton_runAlgorithm.setEnabled(not toggle)

    def selectObstaclesPressed(self):
        toggle = self.problemwidget.toggleSelectObstacles()
        self.pushButton_drawObstacles.setDown(toggle)

        self.pushButton_unlockGrid.setEnabled(not toggle)
        self.pushButton_selectStart.setEnabled(not toggle)
        self.pushButton_selectEnd.setEnabled(not toggle)
        self.pushButton_runAlgorithm.setEnabled(not toggle)

    def selectedRunAlgorithm(self):
        # Checks if one of the other buttons is enabled
        toggle = self.pushButton_unlockGrid.isEnabled()

        self.pushButton_runAlgorithm.setEnabled(not toggle)

        self.pushButton_unlockGrid.setEnabled(not toggle)
        self.pushButton_selectStart.setEnabled(not toggle)
        self.pushButton_selectEnd.setEnabled(not toggle)
        self.pushButton_drawObstacles.setEnabled(not toggle)
        self.pushButton_runAlgorithm.setEnabled(not toggle)

        if toggle:
            self.problemwidget.runAlgorithmPressed(self.showByStepCheckBox.isChecked())
        else:
            self.problemwidget.joinProcessesAndThreads()

    def selectedInterruptAlgorithm(self):
        self.comms.algorithmInterrupt.set()

    def selectedDijkstraAlgorithm(self):
        self.problemwidget.algorithmHandler.setAlgorithm(0)

    def selectedExit(self):
        QApplication.exit()

    def initActions(self):
        self.pushButton_lockGrid.clicked.connect(self.setGridAndLockResize)
        self.pushButton_unlockGrid.clicked.connect(self.clearGridAndUnlockResize)

        self.pushButton_selectStart.clicked.connect(self.selectStartPressed)
        self.comms.startSelected.connect(self.selectedStart)

        self.pushButton_selectEnd.clicked.connect(self.selectEndPressed)
        self.comms.endSelected.connect(self.selectedEnd)

        self.pushButton_drawObstacles.clicked.connect(self.selectObstaclesPressed)

        self.pushButton_runAlgorithm.clicked.connect(self.selectedRunAlgorithm)
        self.stopAlgorithm.triggered.connect(self.selectedInterruptAlgorithm)
        self.actionDijkstra.triggered.connect(self.selectedDijkstraAlgorithm)
        self.actionExit.triggered.connect(self.selectedExit)


    def setTextsUi(self):
        self.mainWindow.setWindowTitle("Path Finding Algorithms")
        self.pushButton_lockGrid.setText("Generate Grid")
        self.pushButton_unlockGrid.setText("Clear Grid")
        self.pushButton_selectStart.setText("Select Start")
        self.pushButton_selectEnd.setText("Select End")
        self.pushButton_drawObstacles.setText("Draw Obstacles")
        self.pushButton_runAlgorithm.setText("Run Algorithm")
        self.menuAlgorithm.setTitle("Algorithm")
        self.menuFile.setTitle("File")
        self.actionDijkstra.setText("Dijkstra")
        self.actionExport.setText("Export..")
        self.actionSave.setText("Save")
        self.actionLoad.setText("Load")
        self.actionExit.setText("Exit")
        self.stopAlgorithm.setText("Stop Algorithm")
        self.textBrowser.appendPlainText("<Begining of Output Console>")

    def printToConsole(self, string):
        if self.textBrowser:
            self.textBrowser.appendPlainText(string)
        if self.statusbar:
            self.statusbar.showMessage(string, 1500)
        print(string)

    def initComms(self, comms):
        self.comms = comms
        self.problemwidget.initComms(comms)
        self.comms.print.connect(self.printToConsole)
        self.comms.endParallelAlgorithmsAndThreads.connect(self.selectedRunAlgorithm)

