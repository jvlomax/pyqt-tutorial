import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow

from app_ui import Ui_MainWindow


class MyApplication(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.shopping_list = []
        self.list_view_model = QStandardItemModel()
        self.ui.shoppingListView.setModel(self.list_view_model)

        self.ui.addItemButton.clicked.connect(self.add_button_clicked)

    @pyqtSlot()
    def add_button_clicked(self):
        text = self.ui.itemInputEdit.text()
        self.ui.itemInputEdit.clear()
        self.shopping_list.append(text)
        self.list_view_model.clear()

        for list_item in self.shopping_list:
            item = QStandardItem(list_item)
            self.list_view_model.appendRow(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApplication()
    sys.exit(app.exec_())
