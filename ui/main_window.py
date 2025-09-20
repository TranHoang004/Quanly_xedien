from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from .tab_nhap import TabNhap
from .tab_xuat import TabXuat
from .tab_ton import TabTon
from .tab_baohanh import TabBaoHanh
from .tab_doanhthu import TabDoanhThu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý Xe Điện")
        self.resize(1000, 650)

        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane { border: 1px solid #ccc; }
            QTabBar::tab { padding: 10px 20px; font-size: 14px; }
            QTabBar::tab:selected { background: #e0f7fa; font-weight: bold; }
        """)

        tabs.addTab(TabNhap(), "📥 Nhập kho")
        tabs.addTab(TabXuat(), "📤 Xuất kho")
        tabs.addTab(TabTon(), "📦 Tồn kho")
        tabs.addTab(TabBaoHanh(), "🛠️ Bảo hành")
        tabs.addTab(TabDoanhThu(), "💰 Doanh thu")

        self.setCentralWidget(tabs)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
