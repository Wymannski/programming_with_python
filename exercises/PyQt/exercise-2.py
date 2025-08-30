import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Calculator')
        self.setGeometry(200, 200, 200, 200)

        self.calc_text = ''

        button_map = {'Cls': (1, 0), 'Bck': (1, 1), 'Close': (1, 3),
                      '7': (2, 0), '8': (2, 1), '9': (2, 2), '/': (2, 3),
                      '4': (3, 0), '5': (3, 1), '6': (3, 2), '*': (3, 3),
                      '1': (4, 0), '2': (4, 1), '3': (4, 2), '-': (4, 3),
                      '0': (5, 0), '.': (5, 1), '=': (5, 2), '+': (5, 3),
                      }

        layout = QGridLayout()

        self.text_field = QLineEdit()
        self.text_field.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout.addWidget(self.text_field,0,0,1,4)

        for key,value in button_map.items():
            button = QPushButton(key)
            button.clicked.connect(self.on_button_click)
            layout.addWidget(button,value[0],value[1])

        self.setLayout(layout)

        self.show()

    def on_button_click(self):
        self.calc_text += self.sender().text()
        self.text_field.setText(self.calc_text)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
