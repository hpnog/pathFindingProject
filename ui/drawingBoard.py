from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5 import QtCore
from multiprocessing import Queue
from threading import Timer, get_ident
from algorithmHandler import AlgorithmHandler
import time
import constants

class DrawingBoard(QWidget):
    def __init__(self, obj):
        super().__init__(obj)

        self.cellWidth, self.cellHeight = 0, 0
        self.grid = None
        self.selectingStart = False
        self.selectingEnd = False
        self.selectingObstacles = False
        self.comms = None
        self.gridNeedsCleaning = False

        self.startPosition = None
        self.endPosition = None

        self.updateThreads = []

        self.sharedQueue = Queue()
        self.algorithmHandler = AlgorithmHandler(self.sharedQueue)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        newWidth = self.width()
        newHeight = self.height()
        newCellWidth = newWidth // (constants.CELL_SIZE + constants.MIN_CELL_SPACING)
        newCellHeight = newHeight // (constants.CELL_SIZE + constants.MIN_CELL_SPACING)

        if newCellWidth != self.cellWidth or newCellHeight != self.cellHeight:
            self.cellWidth = newCellWidth
            self.cellHeight = newCellHeight
            # if self.comms:  # if already exists
            #     self.comms.print.emit(
            #         "[DrawingBoard] New Width: " + str(newCellWidth) + " new height: " + str(newCellHeight))

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
        self.grid = []
        for j in range(self.cellHeight):
            row = []
            for i in range(self.cellWidth):
                row.append(0)
            self.grid.append(row)
        self.update()
        self.comms.print.emit(
            "[DrawingBoard] Full Grid painting set Size: " + str(self.cellWidth) + " vs " + str(self.cellHeight))
    
    def cleanFullGrid(self):
        self.gridNeedsCleaning = False
        for j in range(self.cellHeight):
            for i in range(self.cellWidth):
                if self.grid[j][i] > 3:
                    self.grid[j][i] = 0
        self.update()
        self.comms.print.emit(
            "[DrawingBoard] Full Grid cleaned")

    def clearGrid(self):
        self.grid = None
        self.startPosition = None
        self.endPosition = None
        self.comms.print.emit("[DrawingBoard] Grid cleared")
        self.update()

    def paintEvent(self, event):
        if self.grid is None:  # When grid is null it returns painting blank
            return
        painter = QPainter()
        painter.begin(self)

        currGrid = self.grid[:]

        pen_1 = QPen(constants.CELL_COLLORS[0], constants.CELL_SIZE)
        pen_start = QPen(constants.CELL_COLLORS[1], constants.CELL_SIZE)
        pen_end = QPen(constants.CELL_COLLORS[2], constants.CELL_SIZE)
        pen_obstacles = QPen(constants.CELL_COLLORS[3], constants.CELL_SIZE)
        pen_seen = QPen(constants.CELL_COLLORS[4], constants.CELL_SIZE)
        pen_path = QPen(constants.CELL_COLLORS[5], constants.CELL_SIZE)

        for j in range(self.cellHeight):
            for i in range(self.cellWidth):
                currVal = currGrid[j][i]
                if currVal == 0:
                    painter.setPen(pen_1)
                elif currVal == 1:
                    painter.setPen(pen_start)
                elif currVal == 2:
                    painter.setPen(pen_end)
                elif currVal == 3:
                    painter.setPen(pen_obstacles)
                elif currVal == 4:
                    painter.setPen(pen_seen)
                elif currVal == 5:
                    painter.setPen(pen_path)

                xCoord = i * (constants.CELL_SIZE + constants.MIN_CELL_SPACING) + constants.MIN_CELL_SPACING + constants.CELL_SIZE // 2
                yCoord = j * (constants.CELL_SIZE + constants.MIN_CELL_SPACING) + constants.MIN_CELL_SPACING + constants.CELL_SIZE // 2

                painter.drawLine(xCoord, yCoord, xCoord, yCoord)

        painter.end()

    def mousePressEvent(self, event):
        self.handleMouseEvent(event)

    def mouseMoveEvent(self, event):
        self.handleMouseEvent(event)

    def setGridElem(self, coordX, coordY, val):
        self.grid[coordY][coordX] = val

    def handleMouseEvent(self, event):
        if self.grid is None:
            return

        if self.gridNeedsCleaning:
            self.cleanFullGrid()

        if event.buttons() and QtCore.Qt.LeftButton:
            cellNumX = event.pos().x() // (constants.CELL_SIZE + constants.MIN_CELL_SPACING)
            cellNumY = event.pos().y() // (constants.CELL_SIZE + constants.MIN_CELL_SPACING)

            if cellNumX >= self.cellWidth or cellNumY >= self.cellHeight:
                self.comms.print.emit("[DrawingBoard] Selected a Cell out of the drawn grid")
                return

            gridElem = self.grid[cellNumY][cellNumX]

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
        if self.gridNeedsCleaning:
            self.cleanFullGrid()
        self.gridNeedsCleaning = True

        self.algorithmHandler.runAlgorithm(self.sharedQueue, self.grid, self.cellWidth, self.cellHeight)
        s = Timer(constants.DRAWING_UPDATE_TIMER, passiveWaitForAlgorithm, (self, 0))
        self.updateThreads.append(s)
        s.start()

        # NOTE: If join is set here, no logs will be printed and no drawings made
        # for thread in self.updateThreads:
        #     thread.join()
        #
        # self.comms.print.emit("[DrawingBoard] All Drawing Algorithm Threads have ended")

    def joinProcessesAndThreads(self):
        self.comms.print.emit("[DrawingBoard] Waiting for threads to terminate")
        for thread in self.updateThreads:
            thread.join()
        self.comms.print.emit("[DrawingBoard] Threads terminated. Going For processes")
        self.algorithmHandler.joinProcesses()
        self.comms.algorithmEnd.clear()
        self.comms.algorithmInterrupt.clear()
        self.comms.print.emit("[DrawingBoard] Processes terminated.")

    def setAlgorithmPressed(self):
        self.algorithmHandler.setAlgorithm("Dijkstra")

    def initComms(self, comms):
        self.comms = comms
        self.algorithmHandler.initComms(comms)

    def update(self) -> None:
        super().update()


#######################################################
# Thread to be thrown to wait for drawings
#######################################################
def passiveWaitForAlgorithm(drawingBoard: DrawingBoard, counter: int):
    update = None
    try:
        update = drawingBoard.sharedQueue.get(0)
    except Exception:
        update = None

    if drawingBoard.comms.algorithmInterrupt.is_set():
        drawingBoard.comms.print.emit(
            "[THREAD][" + str(get_ident()) + "][DrawingBoard] Received AlgorithmInterrupt Signal - Iteration " + str(
            counter))
        drawingBoard.comms.endParallelAlgorithmsAndThreads.emit()
        return
    if update is None:
        if drawingBoard.comms.algorithmEnd.is_set():
            drawingBoard.comms.print.emit(
                "[THREAD][" + str(get_ident()) + "][DrawingBoard] Received AlgorithmEnd Signal - Iteration " + str(
                    counter))
            drawingBoard.comms.endParallelAlgorithmsAndThreads.emit()
            return
        drawingBoard.comms.print.emit(
            "[THREAD][" + str(get_ident()) + "][DrawingBoard] did NOT draw " + str(counter) + " iteration")
    else:
        drawingBoard.grid = update
        drawingBoard.update()
        # drawingBoard.comms.print.emit(
        #     "[THREAD][" + str(get_ident()) + "][DrawingBoard] drawing " + str(counter) + " iteration done")

    s = Timer(constants.DRAWING_UPDATE_TIMER, passiveWaitForAlgorithm, (drawingBoard, counter + 1))
    drawingBoard.updateThreads.append(s)
    s.start()
