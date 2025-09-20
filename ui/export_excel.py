from openpyxl import Workbook
from database import db

def export_revenue_excel(filename):
    try:
        data = db.get_all_hoadon()
        wb = Workbook()
        ws = wb.active
        ws.title = "DoanhThu"

        headers = ["Mã HD", "Tên KH", "Địa chỉ", "SĐT", "Tên xe", "Giá", "Ngày bán"]
        ws.append(headers)

        for row in data:
            ws.append(row)

        wb.save(filename)
        return True
    except Exception as e:
        print("Error export Excel:", e)
        return False
