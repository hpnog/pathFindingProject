from PyQt5.QtGui import QColor

CELL_SIZE = 20
MIN_CELL_SPACING = 1

CELL_COLLORS = [
    QColor("#CCCCCC"),  # Empty
    QColor("#FF0000"),  # Starting Point
    QColor("#AA0000"),  # End Point
    QColor("#FFFF00"),  # Obstacles
    QColor("#00FF00")  # Algorithm - visited
]

DRAWING_UPDATE_TIMER = 0.1