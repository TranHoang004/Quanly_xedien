from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from database import db

class TabTon(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Tồn kho xe điện")
        title.setStyleSheet("font-size:18px; font-weight:bold; margin-bottom:10px;")
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Mã xe", "Tên xe", "Số lượng tồn"])
        self.table.setStyleSheet("QHeaderView::section{font-weight:bold;}")
        layout.addWidget(self.table)

        self.load_data()

    def load_data(self):
        data = db.get_ton_kho()
        self.table.setRowCount(0)
        for row, item in enumerate(data):
            self.table.insertRow(row)
            for col, val in enumerate(item):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))