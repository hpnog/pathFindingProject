from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5 import QtCore
from multiprocessing import Array

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
        self.gridUpdates = []
        self.grid = None
        self.toClear = False
        self.selectingStart = False
        self.selectingEnd = False
        self.selectingObstacles = False
        self.comms = None

        self.startPosition = None
        self.endPosition = None

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
        del self.gridUpdates[:]
        for j in range(self.cellHeight):
            for i in range(self.cellWidth):
                self.gridUpdates.append((i, j))
                self.setGridElem(i, j, 0)
        self.repaint()
        self.comms.print.emit(
            "[DrawingBoard] Full Grid painting set Size: " + str(self.cellWidth) + " vs " + str(self.cellHeight))

    def clearGrid(self):
        del self.gridUpdates[:]
        self.startPosition = None
        self.endPosition = None
        self.toClear = True
        self.comms.print.emit("[DrawingBoard] Grid cleared")
        self.repaint()

    def paintEvent(self, event):
        if self.grid is None:
            return
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
            pen_end = QPen(CELL_COLLORS[2], CELL_SIZE)
            pen_obstacles = QPen(CELL_COLLORS[3], CELL_SIZE)

            while len(gridUpdates) > 0:
                newUpdate = gridUpdates.pop()
                currVal = currGrid[newUpdate[0] + self.cellWidth * newUpdate[1]]
                if currVal == 0:
                    painter.setPen(pen_1)
                elif currVal == 1:
                    painter.setPen(pen_start)
                elif currVal == 2:
                    painter.setPen(pen_end)
                elif currVal == 3:
                    painter.setPen(pen_obstacles)

                xCoord = newUpdate[0] * (CELL_SIZE + MIN_CELL_SPACING) + MIN_CELL_SPACING + CELL_SIZE // 2
                yCoord = newUpdate[1] * (CELL_SIZE + MIN_CELL_SPACING) + MIN_CELL_SPACING + CELL_SIZE // 2

                painter.drawLine(xCoord, yCoord, xCoord, yCoord)

        painter.end()

    def mousePressEvent(self, event):
        self.handleMouseEvent(event)

    def mouseMoveEvent(self, event):
        self.handleMouseEvent(event)

    def setGridElem(self, coordX, coordY, val):
        self.grid[coordX + self.cellWidth * coordY] = val

    def handleMouseEvent(self, event):
        if len(self.grid) == 0:
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
                self.gridUpdates.append((cellNumX, cellNumY))

                if self.startPosition is not None:
                    self.setGridElem(self.endPosition[0], self.endPosition[1], 0)
                    self.gridUpdates.append((self.startPosition[0], self.startPosition[1]))

                self.startPosition = (cellNumX, cellNumY)

                self.repaint()
                self.comms.startSelected.emit()
                self.comms.print.emit(
                    "[DrawingBoard] Selected Start position: X: " + str(cellNumX) + " Y:" + str(cellNumY))
            elif self.selectingEnd:
                if gridElem != 0:
                    self.comms.print.emit("[DrawingBoard] Cell not empty - Remove assignment firsrt")
                    return
                self.selectingEnd = False

                self.setGridElem(cellNumX, cellNumY, 2)
                self.gridUpdates.append((cellNumX, cellNumY))

                if self.endPosition is not None:
                    self.setGridElem(self.endPosition[0], self.endPosition[1], 0)
                    self.gridUpdates.append((self.endPosition[0], self.endPosition[1]))

                self.endPosition = (cellNumX, cellNumY)

                self.repaint()
                self.comms.endSelected.emit()
                self.comms.print.emit(
                    "[DrawingBoard] Selected End position: X: " + str(cellNumX) + " Y:" + str(cellNumY))

            elif self.selectingObstacles:
                if gridElem != 0:
                    # self.comms.print.emit("[DrawingBoard] Cell not empty - Remove assignment firsrt")
                    return

                self.setGridElem(cellNumX, cellNumY, 3)
                self.gridUpdates.append((cellNumX, cellNumY))

                self.repaint()
                self.comms.print.emit(
                    "[DrawingBoard] Selected Obstacle position: X: " + str(cellNumX) + " Y:" + str(cellNumY))

    def initComms(self, comms):
        self.comms = comms
