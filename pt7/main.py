import sys
from collections import namedtuple
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from pt6.app_ui import Ui_MainWindow


class ShoppingListItem:
    def __init__(self, name, checked=False):
        self.name = name
        self.checked = checked


class MyApplication(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.shopping_list = []

        self.list_view_model = QStandardItemModel()
        self.ui.shoppingListView.setModel(self.list_view_model)

        uncheck_action = QAction("Remove checked items", self)
        uncheck_action.triggered.connect(self.remove_checked)

        clear_list_action = QAction("Clear list", self)
        clear_list_action.triggered.connect(self.clear_list)
        self.ui.menuFile.addAction(uncheck_action)
        self.ui.menuFile.addAction(clear_list_action)

        self.list_view_model.itemChanged.connect(self.item_checked)
        self.ui.addItemButton.clicked.connect(self.add_button_clicked)

    def update_ui(self):
        self.list_view_model.clear()
        for list_item in self.shopping_list:
            item = QStandardItem(list_item.name)
            item.setCheckable(True)
            item.setCheckState(list_item.checked)
            font = item.font()
            font.setStrikeOut(list_item.checked)
            item.setFont(font)
            self.list_view_model.appendRow(item)

    @pyqtSlot()
    def add_button_clicked(self):
        self.shopping_list.append(ShoppingListItem(name=self.ui.itemInputEdit.text(), checked=False))
        self.ui.itemInputEdit.clear()
        self.update_ui()

    @pyqtSlot()
    def item_checked(self, item):
        print(item.index().row())
        print(self.shopping_list[item.index().row()])
        self.shopping_list[item.index().row()].checked = item.checkState()
        self.update_ui()

    def remove_checked(self):
        self.shopping_list = [item for item in self.shopping_list if not item.checked]
        self.update_ui()

    @pyqtSlot()
    def clear_list(self):
        self.shopping_list = []
        self.list_view_model.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApplication()
    sys.exit(app.exec_())
