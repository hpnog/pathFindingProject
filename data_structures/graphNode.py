import sys

class GraphNode(object):
    def __init__(self, vertexVal: int, coords: (int, int)):
        self.vertexVal = vertexVal
        self.adjacenctVertexes = []
        self.coords = coords
        self.visited = False

        self.cost = sys.maxsize

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
        return self.adjacenctVertexes

    def addAjacent(self, adjacent: object) -> None:
        self.adjacenctVertexes.append(adjacent)

    def setVisited(self, val: bool) -> None:
        self.visited = val