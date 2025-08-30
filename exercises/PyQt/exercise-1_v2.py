import sys

from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication, QGridLayout, QLabel


class Incrementer:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value +=1

class MainWindow2(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Two Buttons')

        self.setGeometry(100,100,300,300)

        self.__incrementer1 = Incrementer()
        button1 = QPushButton('Button 1')
        button1.clicked.connect(self.on_button_1_clicked)

        self.__incrementer2 = Incrementer()
        button2 = QPushButton('Button 2')
        button2.clicked.connect(self.on_button_2_clicked)

        self.label1 = QLabel('A=0')
        self.label2 = QLabel('B=0')

        layout = QGridLayout()

        layout.addWidget(button1,0,0)
        layout.addWidget(button2,0,1)

        layout.addWidget(self.label1,1,0)
        layout.addWidget(self.label2,1,1)
        self.setLayout(layout)

        self.show()

    def on_button_1_clicked(self):
        self.__incrementer1.increment()
        self.label1.setText(f'A={self.__incrementer1.value}')

    def on_button_2_clicked(self):
        self.__incrementer2.increment()
        self.label2.setText(f'B={self.__incrementer2.value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow2()
    sys.exit(app.exec())
