from multiprocessing import Process
import copy

class Dijkstra(Process):
    def __init__(self, endSignal, gridQueue, grid, width, height):
        super().__init__()
        self.endSignal = endSignal
        self.gridQueue = gridQueue
        self.currGrid = grid
        self.gridW = width
        self.gridH = height

    def run(self) -> None:

        for j in range(self.gridH):
            for i in range(self.gridW):
                self.currGrid[j][i] = 4
            gridUpdate = copy.deepcopy(self.currGrid)
            self.gridQueue.put(gridUpdate)

        self.endSignal.set()
        print("Exiting Dijkstra Algorithm Process")

