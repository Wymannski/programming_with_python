import sys

from PyQt6.QtWidgets import *

class SecondWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        layout = QVBoxLayout()
        label = QLabel("Second window")
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        button = QPushButton("Open new window")
        button.clicked.connect(self.open_new_window)
        self.setCentralWidget(button)
        self.show()

    def open_new_window(self,checked):
        global second_window
        second_window = SecondWindow()
        second_window.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()