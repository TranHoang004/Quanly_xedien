from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QFormLayout, QMessageBox
from database import db

class TabNhap(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Nhập kho xe điện")
        title.setStyleSheet("font-size:18px; font-weight:bold; margin-bottom:10px;")
        layout.addWidget(title)

        form = QFormLayout()
        self.tenxe_input = QLineEdit()
        self.gia_input = QLineEdit()
        form.addRow("Tên xe:", self.tenxe_input)
        form.addRow("Giá nhập:", self.gia_input)
        layout.addLayout(form)

        btn_add = QPushButton("➕ Thêm xe vào kho")
        btn_add.setStyleSheet("padding:8px; font-weight:bold;")
        btn_add.clicked.connect(self.add_xe)
        layout.addWidget(btn_add)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Mã xe", "Tên xe", "Giá nhập"])
        self.table.setStyleSheet("QHeaderView::section{font-weight:bold;}")
        layout.addWidget(self.table)

        self.load_data()

    def add_xe(self):
        ten = self.tenxe_input.text().strip()
        gia = self.gia_input.text().strip()
        if not ten or not gia:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin!")
            return
        db.insert_xe(ten, gia)
        self.load_data()
        self.tenxe_input.clear()
        self.gia_input.clear()

    def load_data(self):
        data = db.get_all_xe()
        self.table.setRowCount(0)
        for row, item in enumerate(data):
            self.table.insertRow(row)
            for col, val in enumerate(item):
                self.table.setItem(row, col, QTableWidgetItem(str(val)))