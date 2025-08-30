from PyQt6.QtWidgets import *

def main():
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec()

if __name__ == '__main__':
    main()