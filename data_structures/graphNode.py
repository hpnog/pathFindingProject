import sys

class GraphNode(object):
    def __init__(self, vertexVal: int, coords: (int, int)):
        self.vertexVal = vertexVal
        self.adjacentVertexes = []
        self.coords = coords
        self.visited = False
        self.cost = sys.maxsize
        self.predecessor = None

    def __cmp__(self, other):
        return self.cmp(self.cost, other.cost)

    def __lt__(self, other):
        return self.cost < other.cost

    def printNeighboors(self):
        string = str(self.coords) + " nodes neighboors are: "
        for adjacent in self.adjacentVertexes:
            string += " " + str(adjacent.coords)

        return string