import sys

from PyQt6.QtWidgets import QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow


class AnotherWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Another window')



class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Main window')

        layout = QHBoxLayout()

        button = QPushButton('New window')
        button.clicked.connect(self.open_window)
        layout.addWidget(button)

        self.setLayout(layout)


        self.show()

    def open_window(self):
        global window
        window = AnotherWindow()
        window.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
