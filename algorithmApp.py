import sys
from PyQt5.QtWidgets import QMainWindow, QApplication # QPushButton, QSizePolicy, QApplication
from ui.uiMain import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # Runs the App and returns its exit status
    sys.exit(app.exec_())