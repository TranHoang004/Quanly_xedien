from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from database import db

def export_invoice_pdf(invoice_id, filename):
    try:
        invoice = db.get_invoice_by_id(invoice_id)
        if not invoice:
            return False

        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4

        # Tiêu đề
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(width / 2, height - 50, "HÓA ĐƠN BÁN HÀNG")

        # Nội dung hóa đơn
        c.setFont("Helvetica", 12)
        y = height - 100
        fields = ["Mã HD", "Tên KH", "Địa chỉ", "SĐT", "Tên xe", "Giá", "Ngày bán"]

        for i, field in enumerate(fields):
            c.drawString(100, y - (i * 25), f"{field}: {invoice[i]}")

        c.showPage()
        c.save()
        return True
    except Exception as e:
        print("Error export PDF:", e)
        return False
