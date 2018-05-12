from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = QMessageBox()
    dialog.setText("Hello world")
    dialog.show()
    sys.exit(app.exec_())
