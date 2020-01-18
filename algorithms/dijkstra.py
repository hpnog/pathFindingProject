from multiprocessing import Process
import copy
import constants
from data_structures.graphNode import GraphNode

class Dijkstra(Process):
    def __init__(self, agorithmEnd, algorithmInterrupt, gridQueue, grid, width, height):
        super().__init__()
        self.algorithmInterrupt = algorithmInterrupt
        self.agorithmEnd = agorithmEnd
        self.gridQueue = gridQueue

        self.currGrid = copy.deepcopy(grid)
        self.gridW = width
        self.gridH = height

        self.graphNodes = []

    def buildGraphStructure(self) -> None:
        # Create all graph nodes with no dependencies
        for j in range(self.gridH):
            for i in range(self.gridW):
                self.graphNodes.append(GraphNode(self.currGrid[j][i], (i, j)))

        # need to add adjacents

    def run(self) -> None:
        print("[Dijkstra] - Building Graph structure")
        self.buildGraphStructure()
        print("[Dijkstra] - Graph structure built")

        if self.algorithmInterrupt.is_set():
            return

        # for j in range(self.gridH):
        #     for i in range(self.gridW):
        #         if self.algorithmInterrupt.is_set():
        #             return
        #         self.currGrid[j][i] = 4
        #     gridUpdate = copy.deepcopy(self.currGrid)
        #     self.gridQueue.put(gridUpdate)

        self.agorithmEnd.set()

