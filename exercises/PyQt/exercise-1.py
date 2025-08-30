import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(150,150,80,80)

        self.counter_a = Counter()
        self.counter_b = Counter()

        self.setWindowTitle('Two Buttons')

        self.button_a = QPushButton('Button 1')
        self.button_b = QPushButton('Button2')

        self.button_a.setStyleSheet("background-color: red; color: black")
        self.button_b.setStyleSheet("background-color: green; color: black")

        self.label_a = QLabel('A=0')
        self.label_b = QLabel('B=0')

        self.label_a.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_b.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_a.clicked.connect(self.on_button_a_clicked)
        self.button_b.clicked.connect(self.on_button_b_clicked)



        layout = QGridLayout()
        layout.addWidget(self.button_a, 0, 0)
        layout.addWidget(self.button_b, 0, 1)

        layout.addWidget(self.label_a, 1, 0)
        layout.addWidget(self.label_b, 1, 1)

        self.setLayout(layout)

        self.show()

    def on_button_a_clicked(self):
        self.counter_a.increase()
        self.label_a.setText(f"A={self.counter_a.count}")


    def on_button_b_clicked(self):
        self.counter_b.increase()
        self.label_b.setText(f"B={self.counter_b.count}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
