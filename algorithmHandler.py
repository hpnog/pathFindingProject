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
        
        
        for process in self.processes:
            processJoined = False
            attempt = 1
            while not processJoined:
                self.comms.print.emit("Attemt " + str(attempt) + " to stop current process")
                # [BUG-FIX] currQueue needs to be cleared for the net process
                while not self.currQueue.empty():
                    self.currQueue.get()
                self.comms.print.emit("[AlgorithmHandler] Removed All elements frmo Shared Queue")
                self.comms.print.emit("[AlgorithmHandler] Waiting for process to join")
                process.join(timeout=0.5)
                if not process.is_alive():
                    processJoined = True
                attempt += 1
            # if process.is_alive():
            #     self.comms.print.emit("[AlgorithmHander] Algorithm Background Process did not terminate gracefuly. Forcing quit...")
            #     process.terminate()
            #     process.join(timeout=2)
            # else:
            #     self.comms.print.emit("[AlgorithmHander] Algorithm Background Process terminated gracefuly.")

        del self.processes[:]
