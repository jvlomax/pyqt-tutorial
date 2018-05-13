import sys
from collections import OrderedDict
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from pt6.app_ui import Ui_MainWindow


class MyApplication(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.shopping_list = OrderedDict()
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

    @pyqtSlot()
    def add_button_clicked(self):
        text = self.ui.itemInputEdit.text()
        if not text:
            return
        self.ui.itemInputEdit.clear()
        self.shopping_list[text] = 0
        self.list_view_model.clear()

        for list_item in self.shopping_list.keys():
            item = QStandardItem(list_item)
            item.setCheckable(True)
            self.list_view_model.appendRow(item)

    def item_checked(self, item):
        if item.checkState():
            self.shopping_list[item.text()] = 1
        else:
            self.shopping_list[item.text()] = 0
        self.update_list_model()


    def remove_checked(self):
        self.shopping_list = OrderedDict({k: v for k, v in self.shopping_list.items() if not v})
        self.update_list_model()

    def update_list_model(self):
        self.list_view_model.clear()
        for list_item, checked in self.shopping_list.items():
            item = QStandardItem(list_item)
            item.setCheckable(True)
            item.setCheckState(checked)
            font = item.font()
            font.setStrikeOut(checked)
            item.setFont(font)
            self.list_view_model.appendRow(item)

    @pyqtSlot()
    def clear_list(self):
        self.shopping_list = []
        self.list_view_model.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApplication()
    sys.exit(app.exec_())
