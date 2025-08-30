import sys

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon, QAction


class Scientist:
    def __init__(self,first_name:str,last_name:str,living_period:str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__living_period = living_period

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def living_period(self):
        return self.__living_period

def read_from_file(file_name:str)->list[Scientist]:
    try:
        with open(f'./data/{file_name}') as file:
            file_data = file.readlines()
    except FileNotFoundError:
        print("File not found")

    scientists = []
    for line in file_data:
        attributes = line.split(' ')
        scientists.append(Scientist(attributes[0],attributes[1],attributes[2]))

    return scientists


class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Scientists')
        self.setGeometry(100,100,600,400)

        self.scientists = read_from_file('famous-scientists')

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0,150)
        self.table.setColumnWidth(1,150)
        self.table.setColumnWidth(2,150)

        self.table.setHorizontalHeaderLabels(['Firstname','Lastname','Living period'])
        self.table.setRowCount(len(self.scientists))

        row = 0
        for scientist in self.scientists:
            self.table.setItem(row,0,QTableWidgetItem(scientist.first_name))
            self.table.setItem(row,1,QTableWidgetItem(scientist.last_name))
            self.table.setItem(row,2,QTableWidgetItem(scientist.living_period))
            row += 1

        dock = QDockWidget('New scientist')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,dock)

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.first_name = QLineEdit(form)
        self.last_name = QLineEdit(form)
        self.living_period = QLineEdit(form)

        layout.addRow('First Name:',self.first_name)
        layout.addRow('Last Name:',self.last_name)
        layout.addRow('Living Period:',self.living_period)

        btn_add = QPushButton('Add')
        btn_add.clicked.connect(self.add_employee)
        layout.addRow(btn_add)

        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        delete_action = QAction(QIcon('./data/delete_icon.png'),'&Delete',self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)
        dock.setWidget(form)

    def delete(self):
        current_row = self.table.currentRow()

        if current_row < 0:
            return QMessageBox.warning(self,'Warning','Please select a record to delete')

        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)

    def valid(self):
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        living_period = self.living_period.text().strip()

        if not first_name:
            QMessageBox.critical(self,'Error','Please enter the first name')
            self.first_name.setFocus()
            return False

        if not last_name:
            QMessageBox.critical(self,'Error','Please enter the last name')
            self.last_name.setFocus()
            return False

        if not living_period:
            QMessageBox.critical(self,'Error','Please enter the living period')
            self.living_period.setFocus()
            return False

        return True

    def reset(self):
        self.first_name.clear()
        self.last_name.clear()
        self.living_period.clear()

    def add_employee(self):
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row,0,QTableWidgetItem(self.first_name.text().strip()))
        self.table.setItem(row,1,QTableWidgetItem(self.last_name.text().strip()))
        self.table.setItem(row,2,QTableWidgetItem(self.living_period.text().strip()))

        self.reset()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


