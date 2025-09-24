import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem
)
from PyQt6.QtCore import Qt


class calcTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expressions")

        # Layout
        layout = QVBoxLayout(self)

        # Table
        self.table = QTableWidget(0, 3)  # 0 rows, 3 columns
        self.table.setHorizontalHeaderLabels(["Edit Field", "Symbolic", "Value"])
        layout.addWidget(self.table)

        # Button to add a row
        add_row_btn = QPushButton("Add Row")
        add_row_btn.clicked.connect(self.add_row)
        layout.addWidget(add_row_btn)

    def add_row(self):
        row_pos = self.table.rowCount()
        self.table.insertRow(row_pos)

        # First column: editable item
        item1 = QTableWidgetItem("")
        item1.setFlags(item1.flags() | Qt.ItemFlag.ItemIsEditable)
        self.table.setItem(row_pos, 0, item1)

        # Second column: non-editable
        item2 = QTableWidgetItem("")
        item2.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.table.setItem(row_pos, 1, item2)

        # Third column: non-editable
        item3 = QTableWidgetItem("")
        item3.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.table.setItem(row_pos, 2, item3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = calcTable()
    window.show()
    sys.exit(app.exec())
