import os
import pandas as pd
from predict import predict
from advisor import get_advice

# Test klasörünü belirle
test_folder = "data/test/"

# Sonuçları tutmak için boş liste
sonuclar = []

# Klasördeki tüm dosyaları tara
for file_name in os.listdir(test_folder):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(test_folder, file_name)
        try:
            tahmin = predict(image_path)
            tavsiye = get_advice(tahmin)
            sonuclar.append({
                "Dosya Adı": file_name,
                "Tahmin": tahmin,
                "Tavsiye": tavsiye
            })
            print(f"[✓] {file_name} → {tahmin}")
        except Exception as e:
            print(f"[X] {file_name} için hata: {e}")

# DataFrame olarak kaydet
df = pd.DataFrame(sonuclar)
df.to_csv("sonuc_raporu.csv", index=False, encoding="utf-8-sig")

print("\n✅ Toplu analiz tamamlandı. Sonuçlar: sonuc_raporu.csv dosyasına kaydedildi.")
