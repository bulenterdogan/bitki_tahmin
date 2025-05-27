import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import cv2
from predict import predict
from advisor import get_advice
from utils.db import init_db, veriyi_kaydet

# Veritabanını başlat
init_db()

def sec_ve_tahmin_et():
    dosya_yolu = filedialog.askopenfilename(
        filetypes=[("Görsel Dosyaları", "*.jpg *.jpeg *.png")]
    )
    if dosya_yolu:
        try:
            tahmin, oran = predict(dosya_yolu)
            tavsiye = get_advice(tahmin)

            # Veritabanına kaydet
            veriyi_kaydet(os.path.basename(dosya_yolu), tahmin, oran)

            # Sonuçları göster
            sonuc_label.config(text=f"Tahmin: {tahmin}\n📈 Güven Oranı: %{oran:.2f}")
            tavsiye_label.config(text=tavsiye)

            # Görseli yükle ve göster
            img = Image.open(dosya_yolu).resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            gorsel_label.config(image=img_tk)
            gorsel_label.image = img_tk

        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")

def kamera_ile_tahmin_et():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise Exception("Kamera açılamadı.")

        messagebox.showinfo("Kamera", "Kamerayı açtık. Yaprağı göster ve 'Space' tuşuna bas. Çıkmak için 'Esc' tuşuna bas.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Kamera - Space için hazır", frame)
            key = cv2.waitKey(1)

            if key == 27:  # ESC tuşu
                break
            elif key == 32:  # SPACE tuşu
                foto_yolu = "kamera_goruntu.jpg"
                cv2.imwrite(foto_yolu, frame)
                cap.release()
                cv2.destroyAllWindows()

                tahmin, oran = predict(foto_yolu)
                tavsiye = get_advice(tahmin)
                veriyi_kaydet(os.path.basename(foto_yolu), tahmin, oran)

                sonuc_label.config(text=f"Tahmin: {tahmin}\n📈 Güven Oranı: %{oran:.2f}")
                tavsiye_label.config(text=tavsiye)

                img = Image.open(foto_yolu).resize((200, 200))
                img_tk = ImageTk.PhotoImage(img)
                gorsel_label.config(image=img_tk)
                gorsel_label.image = img_tk

                return

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        messagebox.showerror("Kamera Hatası", str(e))


# Ana pencere
pencere = tk.Tk()
pencere.title("VizyPlant | Bitki Sağlık Tahmini")
pencere.geometry("900x800")

# Arka plan görseli
bg_image = Image.open("background_forest.png").resize((900, 800))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(pencere, width=900, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Başlık ve butonlar
baslik = tk.Label(pencere, text="🌿 Bitki Hastalığı Tanı Sistemi",
                  font=("Helvetica", 16, "bold"), bg="#ffffff")
canvas.create_window(450, 40, window=baslik)

sec_button = tk.Button(pencere, text="📁 Görsel Seç ve Tahmin Et",
                       font=("Arial", 12), command=sec_ve_tahmin_et, bg="#ffffff")
canvas.create_window(450, 100, window=sec_button)

kamera_button = tk.Button(pencere, text="📷 Kamerayla Tahmin Et",
                          font=("Arial", 12), command=kamera_ile_tahmin_et, bg="#ffffff")
canvas.create_window(450, 150, window=kamera_button)

# Sonuçlar
sonuc_label = tk.Label(pencere, text="", font=("Arial", 13, "bold"), bg="#ffffff")
canvas.create_window(450, 210, window=sonuc_label)

tavsiye_label = tk.Label(pencere, text="", font=("Arial", 11), wraplength=750,
                         justify="left", bd=2, relief="groove", padx=10, pady=10, bg="#ffffff")
canvas.create_window(450, 320, window=tavsiye_label)

gorsel_label = tk.Label(pencere, bg="#ffffff")
canvas.create_window(450, 530, window=gorsel_label)

# Çalıştır
pencere.mainloop()










