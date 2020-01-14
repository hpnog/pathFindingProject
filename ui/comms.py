from PyQt5.QtCore import QObject, pyqtSignal
from multiprocessing import Event

class Comms(QObject):
    startSelected = pyqtSignal()
    endSelected = pyqtSignal()

    print = pyqtSignal(str)

    algorithmEnd = Event()
    algorithmInterrupt = Event()
