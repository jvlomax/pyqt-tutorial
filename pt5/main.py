import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from app_ui import Ui_MainWindow


class MyApplication(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApplication()
    sys.exit(app.exec_())