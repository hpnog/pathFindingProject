import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui.uiMain import Ui_MainWindow
from ui.comms import Comms

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    comms = Comms()

    MainWindow.show()
    
    ui.addComms(comms)
    ui.initActions()

    # Runs the App and returns its exit status
    sys.exit(app.exec_())