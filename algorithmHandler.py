from ui.comms import Comms
from algorithms import dijkstra


class AlgorithmHandler(object):
    def __init__(self):
        self.comms = None
        self.algorithms = ["Dijkstra"]
        self.selectedAlgorithm = "Dijkstra"

    def initComms(self, comms: Comms):
        self.comms = comms
        self.comms.selectedAlgorithm.connect(self.setAlgorithm)
        self.comms.runAlgorithm.connect(self.runAlgorithm)

    def setAlgorithm(self, alg):
        self.selectedAlgorithm = alg
        self.comms.print.emit("[AlgorithmHandler] Selected " + alg)

    def runAlgorithm(self):
        self.comms.print.emit("[AlgorithmHandler] Throwing Thread for " + self.selectedAlgorithm + " algorithm")
