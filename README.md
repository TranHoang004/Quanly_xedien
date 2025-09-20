# Quản Lý Xe Điện

Phần mềm quản lý nhập kho, xuất bán, bảo hành và thống kê doanh thu xe điện.

## Tính năng

- Nhập kho xe điện
- Xuất bán xe điện (hóa đơn)
- Quản lý bảo hành
- Thống kê tồn kho
- Thống kê doanh thu theo tháng
- Xuất PDF, Excel

## Cài đặt

```bash
git clone https://github.com/TranHoang004/Quanly_xedien
cd quanly_xedien
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Khởi tạo database

Chạy lệnh sau để tạo các bảng cần thiết:

```bash
python -c "from database.db import init_db; init_db(); print('Đã khởi tạo database!')"
```

## Chạy chương trình

```bash
python -m ui.main_window
```

## Yêu cầu

- Python 3.8+
- Các thư viện: pyqt5, sqlite3, qrcode, python-barcode, reportlab, pandas, matplotlib, openpyxl

## Ghi chú

- Không commit file database thật nếu chứa dữ liệu nhạy cảm.
- Nếu cần, hãy xóa dữ liệu thật khỏi `xedien.db` trước khi chia sẻ.
