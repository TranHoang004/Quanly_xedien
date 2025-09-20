import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "xedien.db")

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Bảng xe nhập kho
    cur.execute("""
        CREATE TABLE IF NOT EXISTS xe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_xe TEXT,
            hang TEXT,
            so_khung TEXT UNIQUE,
            so_may TEXT UNIQUE,
            ma_tim TEXT,
            trang_thai TEXT DEFAULT 'Trong kho'
        )
    """)

    # Bảng hóa đơn xuất bán
    cur.execute("""
        CREATE TABLE IF NOT EXISTS hoadon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_khach TEXT,
            dia_chi TEXT,
            sdt TEXT,
            ten_xe TEXT,
            gia REAL,
            ngay_ban TEXT
        )
    """)

    # Bảng bảo hành
    cur.execute("""
        CREATE TABLE IF NOT EXISTS baohanh (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_xe TEXT,
            so_khung TEXT,
            ngay_bd TEXT,
            ngay_kt TEXT,
            ghichu TEXT
        )
    """)

    conn.commit()
    conn.close()

# ---------------- CRUD cho Xe ----------------
def insert_xe(ten_xe, hang, so_khung, so_may, ma_tim):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO xe (ten_xe, hang, so_khung, so_may, ma_tim) VALUES (?, ?, ?, ?, ?)",
                (ten_xe, hang, so_khung, so_may, ma_tim))
    conn.commit()
    conn.close()

def get_all_xe():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM xe")
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------------- CRUD cho Hóa đơn ----------------
def insert_hoadon(ten_khach, dia_chi, sdt, ten_xe, gia, ngay_ban):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO hoadon (ten_khach, dia_chi, sdt, ten_xe, gia, ngay_ban) VALUES (?, ?, ?, ?, ?, ?)",
                (ten_khach, dia_chi, sdt, ten_xe, gia, ngay_ban))
    conn.commit()
    conn.close()

def get_all_hoadon():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM hoadon")
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------------- CRUD cho Bảo hành ----------------
def insert_baohanh(ten_xe, so_khung, ngay_bd, ngay_kt, ghichu):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO baohanh (ten_xe, so_khung, ngay_bd, ngay_kt, ghichu) VALUES (?, ?, ?, ?, ?)",
                (ten_xe, so_khung, ngay_bd, ngay_kt, ghichu))
    conn.commit()
    conn.close()

def get_all_baohanh():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM baohanh")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_ton_kho():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT ten_xe, COUNT(*) as so_luong
        FROM xe
        WHERE trang_thai = 'Trong kho'
        GROUP BY ten_xe
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_doanhthu_theothang():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            strftime('%Y-%m', ngay_ban) as thang,
            COUNT(*) as so_hoadon,
            SUM(gia) as tong_doanhthu
        FROM hoadon
        GROUP BY thang
        ORDER BY thang DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

# if __name__ == "__main__":
#     init_db()
#     print("Đã khởi tạo database và các bảng!")
