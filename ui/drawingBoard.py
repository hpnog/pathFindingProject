from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor

CELL_SIZE = 20
CELL_SPACING = 2

class DrawingBoard(QWidget) :
    def __init__(self, obj):
        super().__init__(obj)

        self.out, self.statusBar = None, None
        self.cellWidth, cellHeight = 0, 0
        self.gridUpdates = []
        self.grid = []

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

    def triggerFullGrid(self):
        self.grid = [[0 for i in range(self.cellWidth)] for j in range(self.cellHeight)]
            
        self.gridUpdates = []
        for j in range(self.cellHeight):
            for i in range(self.cellWidth):
                self.gridUpdates.append((i, j)) 
        self.repaint()
        self.print("[DrawingBoard] Full Grid painting triggered...")
        
    def paintEvent(self, event):

        painter = QPainter()
        gridUpdates = self.gridUpdates[:]

        defaultPen = QPen(QColor("#eeeeeeee"), CELL_SIZE)
        while len(gridUpdates) > 0:

            painter.begin(self)
            painter.setPen(defaultPen)
            newUpdate = gridUpdates.pop()

            painter.drawLine(
                                newUpdate[0] * (CELL_SIZE + CELL_SPACING) + CELL_SPACING, 
                                newUpdate[1] * (CELL_SIZE + CELL_SPACING) + CELL_SPACING + CELL_SIZE // 2,
                                newUpdate[0] * (CELL_SIZE + CELL_SPACING) + CELL_SPACING,
                                newUpdate[1] * (CELL_SIZE + CELL_SPACING) + CELL_SPACING + CELL_SIZE // 2,
                            )
            painter.end()

