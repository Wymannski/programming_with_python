import sys

from PyQt6.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Mouse tracking")
        self.setGeometry(100, 100, 400, 400)
        self.label = QLabel("Test",self)
        self.label.resize(400,40)
        self.setMouseTracking(True)
        self.show()

    def mouseMoveEvent(self,event):
        x = event.position().x()
        y = event.position().y()
        print(f'({x}, {y})')
        self.label.setText(f'Mouse Coordinates: ({x}, {y})')



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
