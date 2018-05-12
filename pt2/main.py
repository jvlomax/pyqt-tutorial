from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QMainWindow, QLabel, QLayout, QBoxLayout, QVBoxLayout
import sys


from PyQt5.QtWidgets import *

if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    label = QLabel("Hello world", main_window)
    main_window.show()
    sys.exit(app.exec_())
