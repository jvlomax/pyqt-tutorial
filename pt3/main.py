from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QMainWindow, QLabel, QLayout, QBoxLayout, QVBoxLayout
import sys


from PyQt5.QtWidgets import *



@pyqtSlot()
def on_click():
    box = QMessageBox("button pressed")
    box.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    label = QLabel("Hello world", main_window)
    button = QPushButton("test", main_window)
    button.move(0, 25)
    button.clicked.connect(on_click)
    main_window.show()
    sys.exit(app.exec_())
