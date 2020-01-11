from PyQt5.QtWidgets import QWidget

CELL_W = 10
CELL_H = 10
CELL_SPACING = 1

class DrawingBoard(QWidget) :
    def __init__(self, obj):
        super().__init__(obj)

        self.out = None
        self.statusBar = None

    def resizeEvent(self, event):
        super().resizeEvent(event)

        newWidth = self.width()
        newHeight = self.height()

        newCellWidth = newWidth // (CELL_W + CELL_SPACING)
        newCellHeight = newHeight // (CELL_H + CELL_SPACING)

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