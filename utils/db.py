import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("bitki_tahminleri.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tahminler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dosya_adi TEXT,
            tahmin TEXT,
            oran REAL,
            tarih TEXT
        )
    ''')
    conn.commit()
    conn.close()

def veriyi_kaydet(dosya_adi, tahmin, oran):
    conn = sqlite3.connect("bitki_tahminleri.db")
    c = conn.cursor()
    c.execute("INSERT INTO tahminler (dosya_adi, tahmin, oran, tarih) VALUES (?, ?, ?, ?)",
              (dosya_adi, tahmin, oran, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
