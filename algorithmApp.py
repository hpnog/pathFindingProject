import sys
from PyQt4 import QtGui
from ui.uiMain import Ui_MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # Runs the App and returns its exit status
    sys.exit(app.exec_())