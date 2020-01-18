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
        
        self.startingNode = None
        self.endNode = None
        self.graphNodes = []

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
                
                # Setting starting point
                if newNode.getVal() == 1:
                    self.startingNode = newNode

                # Setting end point
                if newNode.getVal() == 2:
                    self.endNode = newNode

        self.print("Blank Nodes created. Adding Node edges.")
        # Add adjacencies to all nodes

        for j in range(self.gridH):
            for i in range(self.gridW):
                if i > 0:   # add left adjacency
                    self.graphNodes[i + j * self.gridH].addAjacent(self.graphNodes[i - 1 + j * self.gridH])
                if i < self.gridW - 1:   # add right adjacency
                    self.graphNodes[i + j * self.gridH].addAjacent(self.graphNodes[i + 1 + j * self.gridH])
                if j > 0:   # add up adjacency
                    self.graphNodes[i + j * self.gridH].addAjacent(self.graphNodes[i + (j - 1) * self.gridH])
                if j < self.gridH - 1:   # add down adjacency
                    self.graphNodes[i + j * self.gridH].addAjacent(self.graphNodes[i + (j + 1) * self.gridH])
        self.print("Node edges added.")

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
        
        self.visitNode(self.startingNode)
        self.markUpdate()
        ##################################################################

        self.print("Algorithm ended")
        return 0
    
    def visitNode(self, node: object, currCost: int = 0) -> None:
        coords = node.getCoords()
        node.setVisited(True)
        node.setCost(currCost)

        # Empty Node -> setVisited Color
        if self.currGrid[coords[1]][coords[0]] == 0: 
            self.currGrid[coords[1]][coords[0]] = 4

        for neighboor in node.getAdjacent():
            if currCost + 1 < neighboor.getCost():
                neighboor.setCost(currCost + 1)

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

        # for j in range(self.gridH):
        #     for i in range(self.gridW):
        #         if self.algorithmInterrupt.is_set():
        #             return
        #         self.currGrid[j][i] = 4
        

        self.agorithmEnd.set()
