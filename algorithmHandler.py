from ui.comms import Comms
from algorithms.dijkstra import Dijkstra
from multiprocessing import Array

class AlgorithmHandler(object):
    def __init__(self, sharedQueue):
        self.comms = None
        self.algorithms = ["Dijkstra"]
        self.selectedAlgorithm = "Dijkstra"
        self.processes = []
        self.currQueue = None

        self.sharedQueue = sharedQueue

    def initComms(self, comms: Comms):
        self.comms = comms

    def setAlgorithm(self, alg):
        self.selectedAlgorithm = alg
        self.comms.print.emit("[AlgorithmHandler] Selected " + alg)

    def runAlgorithm(self, gridQueue, grid, width, height):
        self.currQueue = gridQueue # Needed to clear before joining process
        self.comms.print.emit("[AlgorithmHandler] Throwing Process for " + self.selectedAlgorithm + " algorithm")
        dijkstraProcess = Dijkstra(self.comms.algorithmEnd, self.comms.algorithmInterrupt, gridQueue, grid, width, height)
        self.processes.append(dijkstraProcess)

        dijkstraProcess.start()

    def joinProcesses(self):
        # [BUG-FIX] currQueue would hang when interrrputing as the process 
        # might be trying to put information into a full queue
        while not self.currQueue.empty():
            self.currQueue.get()

        for process in self.processes:
            process.join()
        del self.processes[:]
