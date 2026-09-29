# 🌿 VizyPlant — Yapay Zeka ile Bitki Sağlığı Analizi

Bitki yapraklarındaki hastalıkları yapay zeka ile tespit eden ve detaylı tedavi önerileri sunan web uygulaması.

Kullanıcı analiz etmek istediği bitkiyi seçer, yaprak fotoğrafı yükler ve model hastalığı tahmin ederek Türkçe tedavi tavsiyesi verir.

---

## ✨ Özellikler

- 🧠 **3 bitki türü** desteği (Domates, Patates, Biber)
- 🔍 **14 farklı sınıf** tanıma (11 hastalık + 3 sağlıklı)
- 📁 **Dosya yükleme** ile tahmin
- 📷 **Kamera** ile canlı fotoğraf çekip tahmin
- 💊 Her hastalık için **detaylı Türkçe tedavi tavsiyeleri** (belirtiler, ilaçlama dozları, önleme)
- 🎯 Her bitki için **ayrı özelleştirilmiş model** (daha yüksek doğruluk)
- 📊 Eğitim sonrası **accuracy/loss grafikleri**
- 🔌 Yeni bitki eklemek için **modüler yapı**

---

## 🧠 Tanınan Hastalıklar

### 🍅 Domates (9 Sınıf)
| # | Sınıf | Açıklama |
|---|-------|----------|
| 1 | `healthy_tomato` | Sağlıklı domates yaprağı |
| 2 | `passalora_fulva_mantarli_domates` | Passalora fulva mantarı |
| 3 | `tomato_bacterial_disease` | Bakteriyel benek hastalığı |
| 4 | `tomato_early_blight` | Erken yanıklık (Alternaria solani) |
| 5 | `tomato_late_blight` | Geç yanıklık (Phytophthora infestans) |
| 6 | `tomato_leaf_mold_fungal` | Yaprak küf mantarı |
| 7 | `tomato_mosaic_virus` | Mozaik virüsü |
| 8 | `tomato_septoria_leaf_spot` | Septoria yaprak lekesi |
| 9 | `tomato_spider_mite_disease` | Kırmızı örümcek akarı |

### 🥔 Patates (3 Sınıf)
| # | Sınıf | Açıklama |
|---|-------|----------|
| 1 | `potato_healthy` | Sağlıklı patates yaprağı |
| 2 | `potato_early_blight` | Erken yanıklık (Alternaria solani) |
| 3 | `potato_late_blight` | Geç yanıklık (Phytophthora infestans) |

### 🫑 Biber (2 Sınıf)
| # | Sınıf | Açıklama |
|---|-------|----------|
| 1 | `pepper_healthy` | Sağlıklı biber yaprağı |
| 2 | `pepper_bacterial_spot` | Bakteriyel leke (Xanthomonas) |

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3.13+**
- **PyTorch** — Derin öğrenme (ResNet18 Transfer Learning)
- **Flask** — Web sunucusu
- **Pillow** — Görüntü işleme
- **Matplotlib** — Eğitim grafikleri
- **HTML / CSS / JavaScript** — Arayüz

---

## 📁 Proje Yapısı

```
bitki_tahmin/
├── config.py              # Bitki konfigürasyonları (isim, ikon, yollar)
├── train.py               # Model eğitim scripti (bitki bazlı)
├── predict.py             # Tahmin fonksiyonu (çoklu model desteği)
├── app.py                 # Flask web sunucusu
├── advisor.py             # Detaylı hastalık tavsiye sistemi
├── utils/
│   └── db.py              # SQLite veritabanı yardımcısı
├── templates/
│   └── index.html         # Web arayüzü (bitki seçim kartları)
├── static/
│   └── background.jpg     # Arka plan görseli
├── model/
│   ├── domates_model.pth  # Domates modeli
│   ├── patates_model.pth  # Patates modeli
│   └── biber_model.pth    # Biber modeli
└── data/
    ├── domates/           # Domates eğitim verileri (9 alt klasör)
    ├── patates/           # Patates eğitim verileri (3 alt klasör)
    └── biber/             # Biber eğitim verileri (2 alt klasör)
```

---

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimleri Kur

```bash
pip install torch torchvision flask pillow matplotlib
```

### 2. Veri Setini Hazırla

[PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) adresinden veri setini indirin ve her bitkinin klasörlerini uygun dizine yerleştirin:

```
data/domates/  → healthy_tomato, tomato_bacterial_disease, ...
data/patates/  → potato_healthy, potato_early_blight, potato_late_blight
data/biber/    → pepper_healthy, pepper_bacterial_spot
```

### 3. Modelleri Eğit

```bash
# Her bitki için ayrı model eğitilir:
python train.py --plant domates
python train.py --plant patates
python train.py --plant biber

# Epoch sayısını özelleştirmek için:
python train.py --plant domates --epochs 20
```

### 4. Uygulamayı Başlat

```bash
python app.py
```

Tarayıcıda [http://127.0.0.1:5000](http://127.0.0.1:5000) adresine gidin.

---

## 📸 Kullanım

1. **Bitki Seçin**: Ana sayfadaki kartlardan (🍅 Domates, 🥔 Patates, 🫑 Biber) birini tıklayın
2. **Fotoğraf Yükleyin**: Bir yaprak fotoğrafı seçin ve "Tahmin Et" butonuna basın
3. **Veya Kamera Kullanın**: "Kamerayı Aç" → "Fotoğraf Çek" → "Gönder ve Tahmin Et"
4. **Sonuçları Görün**: Hastalık tahmini, güven oranı ve detaylı tedavi tavsiyesi ekranda gösterilir

---

## 🏗️ Model Mimarisi

- **ResNet18** (ImageNet ile önceden eğitilmiş — Transfer Learning)
- **Görsel boyutu**: 224×224 piksel
- **Optimizer**: AdamW (LR: 0.001)
- **LR Scheduler**: ReduceLROnPlateau (patience=3)
- **Early Stopping**: 5 epoch sabır ile
- **Veri Artırma**: RandomFlip, Rotation, ColorJitter, Affine
- **Dropout**: 0.3 (son katmanda)

---

## ➕ Yeni Bitki Ekleme

Projeye yeni bir bitki eklemek sadece 3 adım:

1. **`config.py`** → `PLANTS` sözlüğüne yeni bitki tanımını ekleyin
2. **`advisor.py`** → Yeni hastalıklar için Türkçe tavsiye metinlerini yazın
3. **Veriyi** `data/<bitki_adi>/` altına koyun ve `python train.py --plant <bitki_adi>` ile eğitin

UI ve tahmin sistemi yeni bitkiyi otomatik algılar — başka kod değişikliğine gerek yoktur.

---

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.
