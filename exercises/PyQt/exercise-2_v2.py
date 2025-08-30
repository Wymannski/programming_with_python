import sys

from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLineEdit


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Calculator')

        self.setGeometry(200, 200, 400, 400)

        self.calcText = ""

        self.text_field = QLineEdit()

        layout = QGridLayout()


        button_map = {'Cls': (0, 0), 'Bck': (0, 1), '': (0, 2), 'Close': (0, 3), '7': (1, 0), '8': (1, 1), '9': (1, 2),
                      '/': (1, 3)
            , '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3)
            , '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3)
            , '0': (4, 0), '.': (4, 1), '=': (4, 2), '+': (4, 3)
                      }

        for key,value in button_map.items():
            button = QPushButton(key)
            layout.addWidget(button,value[0],value[1])
            button.clicked.connect(self.on_button_clicked)

        layout.addWidget(self.text_field,5,0,1,4)

        self.setLayout(layout)

        self.show()

    def on_button_clicked(self):
        self.calcText += self.sender().text()
        self.text_field.setText(self.calcText)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
