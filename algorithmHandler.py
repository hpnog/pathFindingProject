from ui.comms import Comms
from algorithms.dijkstra import Dijkstra
from multiprocessing import Array

class AlgorithmHandler(object):
    def __init__(self, sharedQueue):
        self.comms = None
        self.algorithms = ["Dijkstra"]
        self.selectedAlgorithm = "Dijkstra"
        self.processes = []

        self.sharedQueue = sharedQueue

    def initComms(self, comms: Comms):
        self.comms = comms

    def setAlgorithm(self, alg):
        self.selectedAlgorithm = alg
        self.comms.print.emit("[AlgorithmHandler] Selected " + alg)

    def runAlgorithm(self, gridQueue, grid, width, height):
        self.comms.print.emit("[AlgorithmHandler] Throwing Thread for " + self.selectedAlgorithm + " algorithm")
        dijkstraProcess = Dijkstra(self.comms.algorithmEnd, gridQueue, grid, width, height)
        self.processes.append(dijkstraProcess)

        dijkstraProcess.start()

    def joinProcesses(self):
        for process in self.processes:
            process.join()
        del self.processes[:]
