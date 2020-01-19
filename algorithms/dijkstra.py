from multiprocessing import Process
import copy
import constants
from data_structures.graphNode import GraphNode
import heapq

class Dijkstra(Process):
    def __init__(self, agorithmEnd, algorithmInterrupt, gridQueue, grid, width, height):
        super().__init__()
        self.algorithmInterrupt = algorithmInterrupt
        self.agorithmEnd = agorithmEnd
        self.gridQueue = gridQueue

        self.currGrid = copy.deepcopy(grid)
        self.gridW = width
        self.gridH = height
        
        self.startingNode = None
        self.endNode = None
        self.graphNodes = []
        self.queue = []

    def markUpdate(self) -> None:
        gridUpdate = copy.deepcopy(self.currGrid)
        self.gridQueue.put(gridUpdate)

    def print(self, string: str) -> None:
        print("[Dijkstra][" + str(self.pid) + "] - " + string)

    def buildGraphStructure(self) -> None:
        # Create all graph nodes with no dependencies
        for j in range(self.gridH):
            for i in range(self.gridW):
                newNode = GraphNode(self.currGrid[j][i], (i, j))
                self.graphNodes.append(newNode)

                self.print("Added node: " + str(newNode.getCoords()))
                
                # Setting starting point
                if newNode.getVal() == 1:
                    self.startingNode = self.graphNodes[i + j * self.gridW]

                # Setting end point
                if newNode.getVal() == 2:
                    self.endNode = self.graphNodes[i + j * self.gridW]

        self.print("Blank Nodes created. Adding Node edges.")
        # Add adjacencies to all nodes

        for j in range(self.gridH):
            for i in range(self.gridW):
                if i > 0:   # add left adjacency
                    self.graphNodes[i + j * self.gridW].addAjacent(self.graphNodes[(i - 1) + (j * self.gridW)])
                if i < self.gridW - 1:   # add right adjacency
                    self.graphNodes[i + j * self.gridW].addAjacent(self.graphNodes[(i + 1) + (j * self.gridW)])
                if j > 0:   # add up adjacency
                    self.graphNodes[i + j * self.gridW].addAjacent(self.graphNodes[i + ((j - 1) * self.gridW)])
                if j < self.gridH - 1:   # add down adjacency
                    self.graphNodes[i + j * self.gridW].addAjacent(self.graphNodes[i + ((j + 1) * self.gridW)])
                self.print(self.graphNodes[i + j * self.gridW].printNeighboors())
        self.print("Node edges added.")

        self.print("Starting adjacencies: " + str(self.startingNode.getAdjacent()))

    def findPath(self) -> int:
        if self.startingNode is None:
            self.print("No Starting node was defined")
            return 1
        elif self.endNode is None:
            self.print("No End node was defined")
            return 2

        self.print("Starting Node selected was: " + str(self.startingNode.getCoords()))
        self.print("End Node selected was: " + str(self.endNode.getCoords()))

        # Dijkstra Algorithm Implementation ##############################
        unvisitedNodes = self.graphNodes[:]
        
        self.startingNode.setCost(0)
        self.visitNode(self.startingNode)
        heapq.heappush(self.queue, self.startingNode)

        # ??? INFITINE CYCLE ???
        while len(self.queue) > 0:
            currNode = heapq.heappop(self.queue)
            newDistance = currNode.getCost() + 1
            for neighboor in currNode.getAdjacent():
                if newDistance < neighboor.getCost():
                    neighboor.setPredecessor(currNode)
                    neighboor.setCost(newDistance)
                    self.visitNode(neighboor)
                    heapq.heappush(self.queue, neighboor)

        ##################################################################

        self.print("Algorithm ended")
        return 0
    
    def visitNode(self, node: object) -> None:
        coords = node.getCoords()
        node.setVisited(True)
        # node.setCost(currCost)
        # Empty Node -> setVisited Color
        if self.currGrid[coords[1]][coords[0]] == 0: 
            self.currGrid[coords[1]][coords[0]] = 4

        self.print("Visiting Coordinates: " + str(coords) + " wich is: " + str(coords[0]) + ", " + str(coords[1]))

        self.markUpdate()

    def run(self) -> None:
        self.print("Building Graph structure")
        self.buildGraphStructure()
        self.print("Graph structure built")

        if self.algorithmInterrupt.is_set():
            return

        if self.findPath() == 0:
            self.print("Algorithm ended successfuly")
        else:
            self.print("Algorithm ended with errors")

        for j in range(self.gridH):
            for i in range(self.gridW):
                if self.algorithmInterrupt.is_set():
                    return
                self.currGrid[j][i] = 4
        

        self.agorithmEnd.set()
