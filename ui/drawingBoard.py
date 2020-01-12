from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5 import QtCore
from ui.comms import Comms

CELL_SIZE = 20
MIN_CELL_SPACING = 1

CELL_COLLORS = [
        QColor("#CCCCCC"),
        QColor("#FF0000")
    ]

class DrawingBoard(QWidget) :
    def __init__(self, obj):
        super().__init__(obj)

        self.out, self.statusBar = None, None
        self.cellWidth, cellHeight = 0, 0
        self.gridUpdates = []
        self.grid = []
        self.toClear = False
        self.selectingStart = False
        self.setSelectStartCallback = None
        self.comms = None

        self.startPosition = None

    def resizeEvent(self, event):
        super().resizeEvent(event)

        newWidth = self.width()
        newHeight = self.height()
        newCellWidth = newWidth // (CELL_SIZE + MIN_CELL_SPACING)
        newCellHeight = newHeight // (CELL_SIZE + MIN_CELL_SPACING)

        if newCellWidth != self.cellWidth or newCellHeight != self.cellHeight:
            self.cellWidth = newCellWidth
            self.cellHeight = newCellHeight
            self.print("[DrawingBoard] New Width: " + str(newCellWidth) + " new height: " + str(newCellHeight))
            

    def setOutput(self, obj):
        self.out = obj

    def setStatusBar(self, obj):
        self.statusBar = obj

    def toggleSelectStart(self) -> str:
        self.selectingStart = not self.selectingStart
        return self.selectingStart

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
        self.startPosition = None
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
            pen_start = QPen(CELL_COLLORS[1], CELL_SIZE)

            while len(gridUpdates) > 0:
                newUpdate = gridUpdates.pop()
                if currGrid[newUpdate[0]][newUpdate[1]] == 0:
                    painter.setPen(pen_1)
                elif currGrid[newUpdate[0]][newUpdate[1]] == 1:
                    painter.setPen(pen_start)

                xCoord = newUpdate[0] * (CELL_SIZE + MIN_CELL_SPACING) + MIN_CELL_SPACING + CELL_SIZE // 2
                yCoord = newUpdate[1] * (CELL_SIZE + MIN_CELL_SPACING) + MIN_CELL_SPACING + CELL_SIZE // 2

                painter.drawLine(xCoord, yCoord, xCoord, yCoord)
        
        painter.end()

    def mousePressEvent(self, event):
        if len(self.grid) == 0:
            return

        if event.buttons() & QtCore.Qt.LeftButton:
            if self.selectingStart:
                self.selectingStart = False

                cellNumX = event.pos().x() // (CELL_SIZE + MIN_CELL_SPACING)
                cellNumY = event.pos().y() // (CELL_SIZE + MIN_CELL_SPACING)

                self.grid[cellNumX][cellNumY] = 1
                self.gridUpdates.append((cellNumX, cellNumY))

                if self.startPosition is not None:
                    self.grid[self.startPosition[0]][self.startPosition[1]] = 0
                    self.gridUpdates.append((self.startPosition[0], self.startPosition[1]))

                self.startPosition = (cellNumX, cellNumY)

                self.repaint()
                self.comms.startSelected.emit()
                self.print("[DrawingBoard] Selected Start position: X: " + str(cellNumX) + " Y:" + str(cellNumX))

    def addComms(self, comms):
        self.comms = comms
