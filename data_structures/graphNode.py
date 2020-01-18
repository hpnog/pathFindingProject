class GraphNode(object):
    def __init__(self, vertexVal: int, coords: (int, int)):
        self.vertexVal = vertexVal
        self.adjacenctVertexes = []
        self.coords = coords
        
    def getVal(self) -> int:
        return self.vertexVal
    
    def getCoords(self) -> int:
        return self.coords

    def getAdjacent(self) -> [object]:
        return self.adjacenctVertexes

    def addAjacent(self, adjacent: object) -> None:
        self.adjacenctVertexes.append(adjacent)