from multiprocessing import Process
import copy

class Dijkstra(Process):
    def __init__(self, agorithmEnd, algorithmInterrupt, gridQueue, grid, width, height):
        super().__init__()
        self.agorithmEnd = agorithmEnd
        self.gridQueue = gridQueue
        self.currGrid = grid
        self.gridW = width
        self.gridH = height
        self.algorithmInterrupt = algorithmInterrupt

    def run(self) -> None:

        for j in range(self.gridH):
            for i in range(self.gridW):
                if self.algorithmInterrupt.is_set():
                    return
                self.currGrid[j][i] = 4
            gridUpdate = copy.deepcopy(self.currGrid)
            self.gridQueue.put(gridUpdate)

        self.agorithmEnd.set()

