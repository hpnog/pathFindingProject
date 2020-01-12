from PyQt5.QtCore import QObject, pyqtSignal

class Comms(QObject):
    startSelected = pyqtSignal()     
    endSelected = pyqtSignal() 