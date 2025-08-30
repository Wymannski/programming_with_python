import sys

from PyQt6.QtGui import QWindow, QAction, QIcon
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, \
    QFormLayout, QLineEdit, QPushButton, QToolBar, QMessageBox
from PyQt6.QtCore import Qt, QSize


class Scientist:
    def __init__(self,firstname:str,lastname:str,living_period:str):
        self.firstname = firstname
        self.lastname = lastname
        self.living_period = living_period

class MainWindow(QMainWindow):
    def __init__(self,scientists:list[Scientist],*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.setWindowTitle('Scientists')

        self.setGeometry(100,100,600,600)

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0,150)
        self.table.setColumnWidth(1,150)
        self.table.setColumnWidth(2,100)

        self.table.setHorizontalHeaderLabels(['Firstname','Lastname','Living period'])
        self.table.setRowCount(len(scientists))

        row = 0
        for scientist in scientists:
            self.table.setItem(row,0,QTableWidgetItem(scientist.firstname))
            self.table.setItem(row,1,QTableWidgetItem(scientist.lastname))
            self.table.setItem(row,2,QTableWidgetItem(scientist.living_period))
            row += 1

        dock = QDockWidget("New Scientiest")
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea,dock)

        form = QWidget()
        layout = QFormLayout()
        form.setLayout(layout)

        self.first_name = QLineEdit(form)
        self.last_name = QLineEdit(form)
        self.living_period = QLineEdit(form)

        layout.addRow('First Name:',self.first_name)
        layout.addRow('Last Name:',self.last_name)
        layout.addRow('Living Period:',self.living_period)

        btn_add = QPushButton('Add')
        btn_add.clicked.connect(self.add_scientist)
        layout.addRow(btn_add)

        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        delete_action = QAction(QIcon(''),'&Delete',self)
        delete_action.triggered.connect(self.delete_scientist)
        toolbar.addAction(delete_action)
        dock.setWidget(form)


        self.show()

    def valid(self):
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        living_period = self.living_period.text().strip()

        if not first_name:
            QMessageBox.critical(self,'Error','Please enter a firstname')
            self.first_name.setFocus()
            return False

        if not last_name:
            QMessageBox.critical(self,'Error','Please enter a lastname')
            self.first_name.setFocus()
            return False

        if not living_period:
            QMessageBox.critical(self,'Error','Please enter a living period')
            self.living_period.setFocus()
            return False

        return True

    def reset(self):
        self.first_name.clear()
        self.last_name.clear()
        self.living_period.clear()

    def add_scientist(self):
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row,0,QTableWidgetItem(self.first_name.text().strip()))
        self.table.setItem(row,1,QTableWidgetItem(self.last_name.text().strip()))
        self.table.setItem(row,2,QTableWidgetItem(self.living_period.text().strip()))

        self.reset()



    def delete_scientist(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self,'Warning','Please select a valid row')

        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)





if __name__ == '__main__':
    try:
        with open('data/famous-scientists','r',encoding='UTF-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found')

    if lines:
        scientists:list[Scientist] = []
        for line in lines:
            arr = line.split()
            scientists.append(Scientist(arr[0],arr[1],arr[2]))

        app = QApplication(sys.argv)

        window = MainWindow(scientists)

        sys.exit(app.exec())



