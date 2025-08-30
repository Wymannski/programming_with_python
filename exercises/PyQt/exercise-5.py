import math
import sys

from PyQt6.QtGui import QPainter, QColor, QPainterPath
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Sierpinski triangle")
        self.setGeometry(100, 100, 400, 400)

        self.input_box = QLineEdit(self,placeholderText='Enter the level')
        self.input_box.returnPressed.connect(self.on_enter_textfield)

        layout = QVBoxLayout()
        layout.addWidget(self.input_box)
        self.setLayout(layout)
        self.level = 0


        self.show()

    def on_enter_textfield(self):
        self.level = int(self.input_box.text())
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        path = QPainterPath()
        qp.begin(self)
        start_x = 40
        start_y = 300
        width = 300
        height = math.sqrt(3) * 0.5 * width

        max_level = self.level

        self.draw_triangle(qp, path, 0, max_level, start_x, start_y, width, height)

        # if self.level > 0:
        #     self.draw_triangle(qp, path, 1, max_level, start_x, start_y, width, height)

        # self.draw_triangle(qp, path, 2, start_x, start_y, int(width / 2), int(height / 2), (1, 1), (1, 1), (1, 1))

        # left_corner = (start_x,start_y)
        # right_corner = (start_x+width,start_y)
        # top_corner = (int((width/2)+start_x),int(start_y-height))
        # self.draw_triangle(qp,path,0,left_corner,right_corner,top_corner)
        #
        # left_corner = (start_x+int(width/4),start_y-int(height/2))
        # right_corner = (start_x+int((width/4)*3),start_y-int(height/2))
        # top_corner = (start_x+int(width/2), start_y)
        #
        # self.draw_triangle(qp,path,1,left_corner,right_corner,top_corner)

        # self.draw_triangle(qp,left_corner, (170,200), (105,110))
        # self.draw_triangle(qp,left_corner, (170,200), (105,110))
        qp.end()

    def draw_triangle(self, qp, path, level: int, max_level: int, start_x: float, start_y: float, width: float,
                      height: float):
        if level == 0:
            # qp.setBrush(QColor(0, 0, 0))
            # qp.setBrush(QColor(255, 255, 255))
            left_corner = (start_x, start_y)
            right_corner = (start_x + width, start_y)
            top_corner = ((width / 2) + start_x, start_y - height)
        else:
            #if level == max_level:
            #qp.setBrush(QColor(0, 0, 0))
            # qp.setBrush(QColor(255, 255, 255))
            left_corner = (start_x + width / 4, start_y - height / 2)
            right_corner = (start_x + (width / 4) * 3, start_y - height / 2)
            top_corner = (start_x + width / 2, start_y)

        # if level == 2:
        # qp.setBrush(QColor(200))

        # qp.setBrush(QColor(0, 0, 0))
        qp.setPen(QColor(0, 0, 0))

        # qp.drawLine(left_corner[0],left_corner[1],right_corner[0],right_corner[1])
        #
        # qp.drawLine(left_corner[0],left_corner[1],top_corner[0],top_corner[1])
        #
        # qp.drawLine(top_corner[0],top_corner[1],right_corner[0],right_corner[1])

        #path.moveTo(left_corner[0], left_corner[1])
        path.moveTo(left_corner[0], left_corner[1])
        path.lineTo(right_corner[0], right_corner[1])

        path.lineTo(top_corner[0], top_corner[1])

        path.lineTo(left_corner[0], left_corner[1])

        qp.drawPath(path)
        # qp.setBrush(QColor(255, 255, 255))

        if level < max_level and level !=0:
            level += 1
            self.draw_triangle(qp, path, level, max_level,start_x, start_y, width / 2, height / 2)
            self.draw_triangle(qp, path, level, max_level,top_corner[0], top_corner[1], width / 2, height / 2)
            self.draw_triangle(qp, path, level, max_level,left_corner[0], left_corner[1], width / 2, height / 2)
        elif level < max_level and level == 0:
            level += 1
            self.draw_triangle(qp, path, level, max_level,start_x, start_y, width, height)

        # left_corner = (start_x+int(width/4),start_y-int(height/2))
        # right_corner = (start_x+int((width/4)*3),start_y-int(height/2))
        # top_corner = (start_x+int(width/2), start_y)
        #
        # self.draw_triangle(qp,path,1,left_corner,right_corner,top_corner)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
