from PyQt5.QtGui import QColor
CELL_SIZE = 20
MIN_CELL_SPACING = 1

CELL_COLLORS = [
    QColor("#CCCCCC"),  # Empty
    QColor("#FF0000"),  # Starting Point
    QColor("#AA0000"),  # End Point
    QColor("#FFFF00"),  # Obstacles
    QColor("#00FF00"),  # Algorithm - visited
    QColor("#0000FF")  # Algorithm - path
]

DRAWING_UPDATE_TIMER = 0.01

MIN_WINDOW_WIDTH = 500
MIN_WINDOW_HEIGHT = 500
MAX_WINDOW_WIDTH = 4000
MAX_WINDOW_HEIGHT = 2000