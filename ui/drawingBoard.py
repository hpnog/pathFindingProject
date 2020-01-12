from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor

CELL_SIZE = 20
CELL_SPACING = 2

CELL_COLLORS = [
        QColor("#eeeeeeee")
    ]

class DrawingBoard(QWidget) :
    def __init__(self, obj):
        super().__init__(obj)

        self.out, self.statusBar = None, None
        self.cellWidth, cellHeight = 0, 0
        self.gridUpdates = []
        self.grid = []
        self.toClear = False

    def resizeEvent(self, event):
        super().resizeEvent(event)

        newWidth = self.width()
        newHeight = self.height()
        newCellWidth = newWidth // (CELL_SIZE + CELL_SPACING)
        newCellHeight = newHeight // (CELL_SIZE + CELL_SPACING)

        if newCellWidth != self.cellWidth or newCellHeight != self.cellHeight:
            self.cellWidth = newCellWidth
            self.cellHeight = newCellHeight
            self.print("[DrawingBoard] New Width: " + str(newCellWidth) + " new height: " + str(newCellHeight))
            

    def setOutput(self, obj):
        self.out = obj

    def setStatusBar(self, obj):
        self.statusBar = obj

    def print(self, string):
        if self.out is not None:
            self.out.appendPlainText(string)

        if self.statusBar is not None:
            self.statusBar.showMessage(string, 1500)

        print(string)

    def setFullGrid(self):
        self.grid = []
        self.gridUpdates = []
        for j in range(self.cellWidth):
            currRow = []
            for i in range(self.cellHeight):
                self.gridUpdates.append((j, i))
                currRow.append(0)
            self.grid.append(currRow)
        self.repaint()
        self.print("[DrawingBoard] Full Grid painting set Size: " + str(len(self.grid)) + " vs " + str(len(self.grid[0])))
    
    def clearGrid(self):
        self.grid = []
        self.gridUpdates = []
        self.toClear = True
        self.print("[DrawingBoard] Grid cleared")
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        if self.toClear:
            self.toClear = False
            defaultPen = QPen(QColor("#ffffffff"), 2000, 2000)
            painter.drawLine(0, 1000, 2000, 1000)
        elif len(self.grid) > 0 and len(self.gridUpdates) > 0:
            gridUpdates = self.gridUpdates[:]
            currGrid = self.grid[:]

            pen_1 = QPen(CELL_COLLORS[0], CELL_SIZE)

            while len(gridUpdates) > 0:
                newUpdate = gridUpdates.pop()
                if currGrid[newUpdate[0]][newUpdate[1]] == 0:
                    painter.setPen(pen_1)

                xCoord = newUpdate[0] * (CELL_SIZE + CELL_SPACING) + CELL_SPACING + CELL_SIZE // 2
                yCoord = newUpdate[1] * (CELL_SIZE + CELL_SPACING) + CELL_SPACING + CELL_SIZE // 2

                painter.drawLine(xCoord, yCoord, xCoord, yCoord)
        
        painter.end()

