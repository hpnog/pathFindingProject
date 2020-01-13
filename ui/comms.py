from PyQt5.QtCore import QObject, pyqtSignal


class Comms(QObject):
    startSelected = pyqtSignal()
    endSelected = pyqtSignal()

    print = pyqtSignal(str)

    selectedAlgorithm = pyqtSignal(str)
    runAlgorithm = pyqtSignal()
