from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QMainWindow, QLabel, QLayout, QBoxLayout, QVBoxLayout
import sys


from PyQt5.QtWidgets import *



class Application:
    def __init__(self):
        self.main_window = QMainWindow()
        self.label = QLabel("Hello world", self.main_window)
        self.button = QPushButton("test", self.main_window)
        self.button.move(0, 25)
        self.button.clicked.connect(self.on_click)
        #self.button.clicked.connect(self.change_label)
        self.main_window.show()

    @pyqtSlot()
    def on_click(self):
        box = QMessageBox(self.main_window)
        box.setText("Button clicked")
        box.show()

    @pyqtSlot()
    def change_label(self):
        self.label.setText("I have changed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = Application()

    sys.exit(app.exec_())
