from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5 import QtCore
from multiprocessing import Array
from algorithmHandler import AlgorithmHandler

CELL_SIZE = 20
MIN_CELL_SPACING = 1

CELL_COLLORS = [
    QColor("#CCCCCC"),  # Empty
    QColor("#FF0000"),  # Starting Point
    QColor("#AA0000"),  # End Point
    QColor("#FFFF00")  # Obstacles
]


class DrawingBoard(QWidget):
    def __init__(self, obj):
        super().__init__(obj)

        self.cellWidth, self.cellHeight = 0, 0
        self.grid = None
        self.selectingStart = False
        self.selectingEnd = False
        self.selectingObstacles = False
        self.comms = None

        self.startPosition = None
        self.endPosition = None

        self.algorithmHandler = AlgorithmHandler()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        newWidth = self.width()
        newHeight = self.height()
        newCellWidth = newWidth // (CELL_SIZE + MIN_CELL_SPACING)
        newCellHeight = newHeight // (CELL_SIZE + MIN_CELL_SPACING)

        if newCellWidth != self.cellWidth or newCellHeight != self.cellHeight:
            self.cellWidth = newCellWidth
            self.cellHeight = newCellHeight
            if self.comms:  # if already exists
                self.comms.print.emit(
                    "[DrawingBoard] New Width: " + str(newCellWidth) + " new height: " + str(newCellHeight))

    def toggleSelectStart(self):
        self.selectingStart = not self.selectingStart
        return self.selectingStart

    def toggleSelectEnd(self):
        self.selectingEnd = not self.selectingEnd
        return self.selectingEnd

    def toggleSelectObstacles(self):
        self.selectingObstacles = not self.selectingObstacles
        return self.selectingObstacles

    def setFullGrid(self):
        self.grid = Array('i', self.cellWidth * self.cellHeight)
        for j in range(self.cellHeight):
            for i in range(self.cellWidth):
                self.setGridElem(i, j, 0)
        self.update()
        self.comms.print.emit(
            "[DrawingBoard] Full Grid painting set Size: " + str(self.cellWidth) + " vs " + str(self.cellHeight))

    def clearGrid(self):
        self.grid = None
        self.startPosition = None
        self.endPosition = None
        self.comms.print.emit("[DrawingBoard] Grid cleared")
        self.update()

    def paintEvent(self, event):
        if self.grid is None:   # When grid is null it returns painting blank
            return
        painter = QPainter()
        painter.begin(self)

        currGrid = self.grid[:]

        pen_1 = QPen(CELL_COLLORS[0], CELL_SIZE)
        pen_start = QPen(CELL_COLLORS[1], CELL_SIZE)
        pen_end = QPen(CELL_COLLORS[2], CELL_SIZE)
        pen_obstacles = QPen(CELL_COLLORS[3], CELL_SIZE)

        for j in range(self.cellHeight):
            for i in range(self.cellWidth):
                currVal = currGrid[i + self.cellWidth * j]
                if currVal == 0:
                    painter.setPen(pen_1)
                elif currVal == 1:
                    painter.setPen(pen_start)
                elif currVal == 2:
                    painter.setPen(pen_end)
                elif currVal == 3:
                    painter.setPen(pen_obstacles)

                xCoord = i * (CELL_SIZE + MIN_CELL_SPACING) + MIN_CELL_SPACING + CELL_SIZE // 2
                yCoord = j * (CELL_SIZE + MIN_CELL_SPACING) + MIN_CELL_SPACING + CELL_SIZE // 2

                painter.drawLine(xCoord, yCoord, xCoord, yCoord)

        painter.end()

    def mousePressEvent(self, event):
        self.handleMouseEvent(event)

    def mouseMoveEvent(self, event):
        self.handleMouseEvent(event)

    def setGridElem(self, coordX, coordY, val):
        self.grid[coordX + self.cellWidth * coordY] = val

    def handleMouseEvent(self, event):
        if self.grid is None:
            return

        if event.buttons() and QtCore.Qt.LeftButton:
            cellNumX = event.pos().x() // (CELL_SIZE + MIN_CELL_SPACING)
            cellNumY = event.pos().y() // (CELL_SIZE + MIN_CELL_SPACING)

            if cellNumX >= self.cellWidth or cellNumY >= self.cellHeight:
                self.comms.print.emit("[DrawingBoard] Selected a Cell out of the drawn grid")
                return

            gridElem = self.grid[cellNumX + self.cellWidth * cellNumY]

            if self.selectingStart:
                if gridElem != 0:
                    self.comms.print.emit("[DrawingBoard] Cell not empty - Remove assignment first")
                    return
                self.selectingStart = False

                self.setGridElem(cellNumX, cellNumY, 1)

                if self.startPosition is not None:
                    self.setGridElem(self.startPosition[0], self.startPosition[1], 0)

                self.startPosition = (cellNumX, cellNumY)

                self.update()
                self.comms.startSelected.emit()
                self.comms.print.emit(
                    "[DrawingBoard] Selected Start position: X: " + str(cellNumX) + " Y:" + str(cellNumY))
            elif self.selectingEnd:
                if gridElem != 0:
                    self.comms.print.emit("[DrawingBoard] Cell not empty - Remove assignment firsrt")
                    return
                self.selectingEnd = False

                self.setGridElem(cellNumX, cellNumY, 2)

                if self.endPosition is not None:
                    self.setGridElem(self.endPosition[0], self.endPosition[1], 0)

                self.endPosition = (cellNumX, cellNumY)

                self.update()
                self.comms.endSelected.emit()
                self.comms.print.emit(
                    "[DrawingBoard] Selected End position: X: " + str(cellNumX) + " Y:" + str(cellNumY))

            elif self.selectingObstacles:
                if gridElem != 0:
                    # self.comms.print.emit("[DrawingBoard] Cell not empty - Remove assignment firsrt")
                    return

                self.setGridElem(cellNumX, cellNumY, 3)

                self.update()
                self.comms.print.emit(
                    "[DrawingBoard] Selected Obstacle position: X: " + str(cellNumX) + " Y:" + str(cellNumY))

    def runAlgorithmPressed(self):
        self.algorithmHandler.runAlgorithm()

    def setAlgorithmPressed(self):
        self.algorithmHandler.setAlgorithm("Dijkstra")

    def initComms(self, comms):
        self.comms = comms
        self.algorithmHandler.initComms(comms)
