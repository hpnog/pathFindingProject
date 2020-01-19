from multiprocessing import Process
import copy
import constants
from data_structures.graph import Graph
import heapq
import datetime

class Dijkstra(Process):
    def __init__(self, agorithmEnd, algorithmInterrupt, gridQueue, grid, width, height, byStep):
        super().__init__()
        self.algorithmInterrupt = algorithmInterrupt
        self.agorithmEnd = agorithmEnd
        self.gridQueue = gridQueue

        self.graph = Graph(grid, width, height)
        self.queue = []
        self.byStep = byStep

    def markUpdate(self, force = False) -> None:
        if force or self.byStep:
            gridUpdate = copy.deepcopy(self.graph.currGrid)
            self.gridQueue.put(gridUpdate)

    def print(self, string: str) -> None:
        print("[Dijkstra][PID-" + str(self.pid) + "] - " + string)

    def getShortestPath(self):
        currNode = self.graph.endNode.predecessor
        while currNode is not self.graph.startingNode:
            currCoords = currNode.coords
            # self.print("Backtracking shortest path Vertice: " + str(currCoords))
            if self.graph.currGrid[currCoords[1]][currCoords[0]] == 4: 
                self.graph.currGrid[currCoords[1]][currCoords[0]] = 5
            currNode = currNode.predecessor

        self.markUpdate()

    def findPath(self) -> int:
        if self.graph.startingNode is None:
            self.print("No Starting node was defined")
            return 1
        elif self.graph.endNode is None:
            self.print("No End node was defined")
            return 2

        self.print("Starting Node selected was: " + str(self.graph.startingNode.coords))
        self.print("End Node selected was: " + str(self.graph.endNode.coords))

        # Dijkstra Algorithm Implementation ##############################
        foundEnd = False
        
        self.graph.startingNode.cost = 0
        self.visitNode(self.graph.startingNode)
        heapq.heappush(self.queue, self.graph.startingNode)

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
        if not foundEnd:
            self.print("The end Node was not found.")
            return 1
        return 0
    
    def visitNode(self, node: object) -> None:
        coords = node.coords
        node.visited = True

        # Empty Node -> setVisited Color
        if self.graph.currGrid[coords[1]][coords[0]] == 0: 
            self.graph.currGrid[coords[1]][coords[0]] = 4

        self.markUpdate()

        if node is self.graph.endNode:
            return True
        return False

    def run(self) -> None:
        self.graph.pid = self.pid

        self.print("Building Graph structure")
        self.graph.buildGraphStructure()
        self.print("Graph structure built")

        if self.algorithmInterrupt.is_set():
            return

        algorithmStartTime = datetime.datetime.now()

        if self.findPath() == 0:
            self.print("Algorithm ended successfuly")
            self.getShortestPath()
        else:
            self.print("Algorithm ended with errors")

        algorithmEndTime = datetime.datetime.now()
        runTime = algorithmEndTime - algorithmStartTime
        self.print("Algorithm execution took: " + str(runTime))

        self.markUpdate(True)    
        self.agorithmEnd.set()

        self.print("Process returning")
        return