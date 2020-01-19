import sys

class GraphNode(object):
    def __init__(self, vertexVal: int, coords: (int, int)):
        self.vertexVal = vertexVal
        self.adjacentVertexes = []
        self.coords = coords
        self.visited = False
        self.cost = sys.maxsize
        self.predecessor = None

    def getVal(self) -> int:
        return self.vertexVal
    
    def setVal(self, val: int) -> None:
        self.vertexVal = val

    def getCoords(self) -> int:
        return self.coords

    def setCost(self, cost) -> None:
        self.cost = cost

    def getCost(self) -> int:
        return self.cost

    def getAdjacent(self) -> [object]:
        return self.adjacentVertexes

    def addAjacent(self, adjacent: object) -> None:
        self.adjacentVertexes.append(adjacent)

    def setVisited(self, val: bool) -> None:
        self.visited = val

    def setPredecessor(self, node):
        self.predecessor = node

    def getPredecessor(self):
        return self.predecessor


    def __cmp__(self, other):
        return self.cmp(self.cost, other.cost)

    def __lt__(self, other):
        return self.cost < other.cost

    def printNeighboors(self):
        string = str(self.coords) + " nodes neighboors are: "
        for adjacent in self.adjacentVertexes:
            string += " " + str(adjacent.getCoords())

        return string