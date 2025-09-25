import sys
import sympy as sp
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QLabel
)
from PyQt6.QtCore import Qt
from sympy import sympify
from PyQt6.QtGui import QPixmap
from io import BytesIO

from view.latex2img import latex2img
from view.str2latex import str2latex

from controller.controller import Controller

c = Controller()


class calcTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expressions")
        layout = QVBoxLayout(self)
        # make table
        self.table = QTableWidget(0, 3)  # 0 rows, 3 columns
        self.table.setHorizontalHeaderLabels(["Edit Field", "Symbolic", "Value"])
        layout.addWidget(self.table)
        colwidth = 150
        rowheight = 200
        self.table.setColumnWidth(0, colwidth)  
        self.table.setColumnWidth(1, colwidth)  
        self.table.setColumnWidth(2, colwidth)
        # i coulda just for looped...
        self.table.setRowHeight(0, rowheight)  
        self.table.setRowHeight(1, rowheight)  
        self.table.setRowHeight(2, rowheight)  


        # the button to add rows
        add_row_btn = QPushButton("Add Row")
        add_row_btn.clicked.connect(self.add_row)
        layout.addWidget(add_row_btn)

        self.table.itemChanged.connect(self.on_item_changed) # this guy checks if thing changed

    def add_row(self):
        self.table.blockSignals(True)

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

        # call to control, note line is empty when added
        c.add_line()
        self.table.blockSignals(False)

    def on_item_changed(self, item): # later gonna eval with model for third col
       
        if item is None:
            return

        row = item.row()
        col = item.column()
    # math text in  collumns 
        # basicallly check if first col
        if col != 0:
            return
        try:
            expr = str2latex(item.text())
        except:
            expr = None
        # the cool display part hehe
        pixmap = latex2img(expr) if expr else latex2img("error")
        pixmap = pixmap.scaled(
        self.table.columnWidth(col),
        self.table.rowHeight(row),
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation
        )


        # the label to import!!!
        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Prevent signal recursion if needed
        self.table.blockSignals(True)
        self.table.setCellWidget(row, 1, label)
        self.table.blockSignals(False)
        ''
    # evaluating with control
        #values = c.item_changed(row,expr) # expr is the latek expression
        expr_val_dict, lines = c.item_changed(row,item.text())
        values = list(expr_val_dict.values())
        exprs = list(expr_val_dict.keys())
        #print('values:')
        #print(values)
        self.table.blockSignals(True)
        for r in range(self.table.rowCount()):
            self.table.setItem(r, 2, QTableWidgetItem(str(values[r])))
            self.table.setItem(r, 0, QTableWidgetItem(str(lines[r].raw_line))) # this is not line i figure out later
        self.table.blockSignals(False)

        
        


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = calcTable()
    window.show()
    sys.exit(app.exec())
