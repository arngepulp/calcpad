import sys
import sympy as sp
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt


class calcTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expressions")
        layout = QVBoxLayout(self)
        # make table
        self.table = QTableWidget(0, 3)  # 0 rows, 3 columns
        self.table.setHorizontalHeaderLabels(["Edit Field", "Symbolic", "Value"])
        layout.addWidget(self.table)

        # the button to add rows
        add_row_btn = QPushButton("Add Row")
        add_row_btn.clicked.connect(self.add_row)
        layout.addWidget(add_row_btn)

        self.table.itemChanged.connect(self.on_item_changed) # this guy checks if thing changed

    def add_row(self):
        row_pos = self.table.rowCount()
        self.table.insertRow(row_pos)

        # first col
        item1 = QTableWidgetItem("")
        item1.setFlags(item1.flags() | Qt.ItemFlag.ItemIsEditable)
        self.table.setItem(row_pos, 0, item1)

        # 2nd
        item2 = QTableWidgetItem("")
        item2.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.table.setItem(row_pos, 1, item2)

        # 3rd
        item3 = QTableWidgetItem("")
        item3.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.table.setItem(row_pos, 2, item3)

    def on_item_changed(self, item): # later gonna eval with model for third col
        if item is None:
            return

        row = item.row()
        col = item.column()

        # basicallly check if first col
        if col != 0:
            return

        input_text = item.text()
        # makaes the cool math
        symbolic_item = self.table.item(row, 1)
        if symbolic_item is None:
            symbolic_item = QTableWidgetItem()
            symbolic_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.table.setItem(row, 1, symbolic_item)

        # im gonna be real i had an issue and chatgpt said to add this
        self.table.blockSignals(True)
        # have my actual text filtering in here, probably some library for this
        expr = input_text
        
        symbolic_item.setText(sp.latex(expr))
        self.table.blockSignals(False)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = calcTable()
    window.show()
    sys.exit(app.exec())
