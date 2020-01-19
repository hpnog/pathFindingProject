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
        print("[Dijkstra][PID-" + str(self.pid) + "] - " + string)

    def buildGraphStructure(self) -> None:
        # Create all graph nodes with no dependencies
        for j in range(self.gridH):
            for i in range(self.gridW):
                newNode = GraphNode(self.currGrid[j][i], (i, j))
                self.graphNodes.append(newNode)

                # self.print("Added node: " + str(newNode.coords))
                
                # Setting starting point
                if newNode.vertexVal == 1:
                    self.startingNode = self.graphNodes[i + j * self.gridW]

                # Setting end point
                if newNode.vertexVal == 2:
                    self.endNode = self.graphNodes[i + j * self.gridW]

        self.print("Blank Nodes created. Adding Node edges.")
        # Add adjacencies to all nodes

        for j in range(self.gridH):
            for i in range(self.gridW):
                if i > 0 and self.graphNodes[(i - 1) + (j * self.gridW)].vertexVal != 3:   # add left adjacency
                    self.graphNodes[i + j * self.gridW].adjacentVertexes.append(self.graphNodes[(i - 1) + (j * self.gridW)])
                if i < self.gridW - 1 and self.graphNodes[(i + 1) + (j * self.gridW)].vertexVal != 3:   # add right adjacency
                    self.graphNodes[i + j * self.gridW].adjacentVertexes.append(self.graphNodes[(i + 1) + (j * self.gridW)])
                if j > 0 and self.graphNodes[i + ((j - 1) * self.gridW)].vertexVal != 3:   # add up adjacency
                    self.graphNodes[i + j * self.gridW].adjacentVertexes.append(self.graphNodes[i + ((j - 1) * self.gridW)])
                if j < self.gridH - 1 and self.graphNodes[i + ((j + 1) * self.gridW)].vertexVal != 3:   # add down adjacency
                    self.graphNodes[i + j * self.gridW].adjacentVertexes.append(self.graphNodes[i + ((j + 1) * self.gridW)])
                
                # The following print prints all neighboors of node
                # self.print(self.graphNodes[i + j * self.gridW].printNeighboors())
        self.print("Node edges added.")

    def getShortestPath(self):
        currNode = self.endNode.predecessor
        while currNode is not self.startingNode:
            currCoords = currNode.coords
            self.print("Backtracking shortest path Vertice: " + str(currCoords))
            if self.currGrid[currCoords[1]][currCoords[0]] == 4: 
                self.currGrid[currCoords[1]][currCoords[0]] = 5
            currNode = currNode.predecessor

        self.markUpdate()

    def findPath(self) -> int:
        if self.startingNode is None:
            self.print("No Starting node was defined")
            return 1
        elif self.endNode is None:
            self.print("No End node was defined")
            return 2

        self.print("Starting Node selected was: " + str(self.startingNode.coords))
        self.print("End Node selected was: " + str(self.endNode.coords))

        # Dijkstra Algorithm Implementation ##############################
        foundEnd = False
        
        self.startingNode.cost = 0
        self.visitNode(self.startingNode)
        heapq.heappush(self.queue, self.startingNode)

        while len(self.queue) > 0 and not foundEnd:
            currNode = heapq.heappop(self.queue)
            newDistance = currNode.cost + 1
            for neighboor in currNode.adjacentVertexes:
                if newDistance < neighboor.cost:
                    neighboor.predecessor = currNode
                    neighboor.cost = newDistance
                    # NOTE: As we know that all vertices are all equally positioned
                    # then when we find the end, it is already the best result
                    # and there is no need to keep serching for a shorter path
                    if self.visitNode(neighboor):
                        foundEnd = True
                    heapq.heappush(self.queue, neighboor)

        ##################################################################

        self.print("Algorithm ended")
        return 0
    
    def visitNode(self, node: object) -> None:
        coords = node.coords
        node.visited = True

        # Empty Node -> setVisited Color
        if self.currGrid[coords[1]][coords[0]] == 0: 
            self.currGrid[coords[1]][coords[0]] = 4

        # self.print("Visiting Coordinates: " + str(coords) + " wich is: " + str(coords[0]) + ", " + str(coords[1]))

        self.markUpdate()

        if node is self.endNode:
            return True
        return False

    def run(self) -> None:
        self.print("Building Graph structure")
        self.buildGraphStructure()
        self.print("Graph structure built")

        if self.algorithmInterrupt.is_set():
            return

        if self.findPath() == 0:
            self.print("Algorithm ended successfuly")
            self.getShortestPath()
        else:
            self.print("Algorithm ended with errors")

        #for j in range(self.gridH):
        #    for i in range(self.gridW):
        #        if self.algorithmInterrupt.is_set():
        #            return
        #        self.currGrid[j][i] = 4
        
        self.agorithmEnd.set()

        self.print("Process returning")
        return