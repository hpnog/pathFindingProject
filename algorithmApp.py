import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.uiMain import Ui_MainWindow
from ui.comms import Comms
from algorithmHandler import AlgorithmHandler

if __name__ == "__main__":
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    comms = Comms()
    algorithmHandler = AlgorithmHandler()
    algorithmHandler.initComms(comms)

    MainWindow.show()

    ui.initComms(comms)
    ui.initActions()

    # Runs the App and returns its exit status
    sys.exit(app.exec_())
