import sys
import copy
from data_structures.graphNode import GraphNode

class Graph(object):
    def __init__(self, grid, width, height):
        self.currGrid = copy.deepcopy(grid)
        self.gridW = width
        self.gridH = height
        
        self.startingNode = None
        self.endNode = None
        self.graphNodes = []
        
        self.pid = None

    def buildGraphStructure(self) -> None:
        # Create all graph nodes with no dependencies
        for j in range(self.gridH):
            for i in range(self.gridW):
                newNode = GraphNode(self.currGrid[j][i], (i, j))
                self.graphNodes.append(newNode)
                
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

    def print(self, string: str) -> None:
        print("[Graph][PID-" + str(self.pid) + "] - " + string)
