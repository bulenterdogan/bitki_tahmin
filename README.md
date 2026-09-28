# 🌿 VizyPlant — Domates Yaprak Hastalığı Tahmin Uygulaması

Domates yapraklarındaki hastalıkları yapay zeka ile tespit eden ve tedavi önerileri sunan web uygulaması.

Kullanıcı bir domates yaprağı fotoğrafı yükler, model hastalığı tahmin eder ve Türkçe tedavi tavsiyesi verir.

---

## ✨ Özellikler

- 🔍 **9 farklı sınıf** tanıma (8 hastalık + 1 sağlıklı)
- 📁 **Dosya yükleme** ile tahmin
- 🌐 **URL yapıştırma** ile tahmin (Google Görseller desteği dahil)
- 📷 **Kamera** ile canlı fotoğraf çekip tahmin
- 💊 Her hastalık için **Türkçe tedavi tavsiyeleri**
- 📊 Eğitim sonrası **accuracy/loss grafikleri**

---

## 🧠 Tanınan Hastalıklar

| # | Sınıf | Açıklama |
|---|---|---|
| 1 | `healthy_tomato` | Sağlıklı domates yaprağı |
| 2 | `passalora_fulva_mantarli_domates` | Passalora fulva mantarı |
| 3 | `tomato_bacterial_disease` | Bakteriyel hastalık |
| 4 | `tomato_early_blight` | Erken yanıklık |
| 5 | `tomato_late_blight` | Geç yanıklık |
| 6 | `tomato_leaf_mold_fungal` | Yaprak küf mantarı |
| 7 | `tomato_mosaic_virus` | Mozaik virüsü |
| 8 | `tomato_septoria_leaf_spot` | Septoria yaprak lekesi |
| 9 | `tomato_spider_mite_disease` | Örümcek akarı hastalığı |

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **PyTorch** — Derin öğrenme (ResNet18 Transfer Learning)
- **Flask** — Web sunucusu
- **Pillow** — Görüntü işleme
- **Matplotlib** — Eğitim grafikleri
- **HTML / CSS / JavaScript** — Arayüz

---

## 📁 Proje Yapısı

```
plant_project/
├── train.py              # Model eğitim scripti (ResNet18)
├── predict.py             # Tahmin fonksiyonu
├── app.py                 # Flask web sunucusu
├── advisor.py             # Hastalık tavsiye sistemi
├── utils/
│   └── db.py              # SQLite veritabanı yardımcısı
├── templates/
│   └── index.html         # Web arayüzü
├── static/
│   └── background.jpg     # Arka plan görseli
├── model/
│   └── plant_model.pth    # Eğitilmiş model ağırlıkları
├── data/
│   └── train/             # Eğitim verileri (9 klasör)
└── accuracy_plot.png      # Eğitim grafikleri
```

---

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimleri Kur

```bash
pip install torch torchvision flask pillow matplotlib requests
```

### 2. Modeli Eğit

```bash
python train.py
```

Eğitim tamamlandığında `model/plant_model.pth` dosyası oluşur ve accuracy/loss grafikleri gösterilir.

### 3. Uygulamayı Başlat

```bash
python app.py
```

Tarayıcıda [http://127.0.0.1:5000](http://127.0.0.1:5000) adresine git.

---

## 📸 Kullanım

1. **Dosya Yükleme**: Bir domates yaprağı fotoğrafı seç ve "Tahmin Et" butonuna bas
2. **URL ile**: Görsel URL'sini yapıştır (Google Görseller linki de çalışır)
3. **Kamera ile**: "Kamerayı Aç" → "Fotoğraf Çek" → "Gönder ve Tahmin Et"

---

## 🏗️ Model Mimarisi

- **ResNet18** (ImageNet ile önceden eğitilmiş — Transfer Learning)
- **Görsel boyutu**: 224×224 piksel
- **Optimizer**: AdamW (LR: 0.001)
- **LR Scheduler**: ReduceLROnPlateau
- **Early Stopping**: 5 epoch sabır ile
- **Veri Artırma**: RandomFlip, Rotation, ColorJitter, Affine

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.
