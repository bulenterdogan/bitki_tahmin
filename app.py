from flask import Flask, render_template, request
from predict import predict
from advisor import get_advice
from config import PLANTS
from PIL import Image
from io import BytesIO
import base64
import re
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", plants=PLANTS)

@app.route("/tahmin", methods=["POST"])
def predict_route():
    image = None
    plant_key = request.form.get("plant", "domates")

    if plant_key not in PLANTS:
        return render_template("index.html", plants=PLANTS, result="⚠️ Geçersiz bitki seçimi.")

    plant = PLANTS[plant_key]

    # Model dosyası var mı kontrol et
    if not os.path.exists(plant["model_path"]):
        return render_template(
            "index.html", plants=PLANTS,
            result=f"⚠️ {plant['name']} için model henüz eğitilmedi.\n"
                   f"Lütfen önce çalıştırın: python train.py --plant {plant_key}"
        )

    if "image" in request.files and request.files["image"].filename != "":
        try:
            image = Image.open(request.files["image"]).convert("RGB")
        except Exception as e:
            return render_template("index.html", plants=PLANTS, result=f"❌ Görsel işlenemedi: {e}")

    else:
        return render_template("index.html", plants=PLANTS, result="⚠️ Lütfen bir görsel yükleyin.")

    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image_path = tmp.name
    tmp.close()
    image.save(image_path)

    prediction, confidence = predict(image_path, plant_key)
    os.remove(image_path)
    advice = get_advice(prediction)

    result = (
        f"🌿 Bitki: {plant['icon']} {plant['name']}\n"
        f"🔬 Tahmin: {prediction}\n"
        f"📈 Güven: %{confidence:.2f}\n"
        f"📋 Tavsiye:\n{advice}"
    )

    return render_template("index.html", plants=PLANTS, result=result)

@app.route("/camera", methods=["POST"])
def camera():
    img_data = request.form.get("img_data")
    plant_key = request.form.get("plant", "domates")

    if not img_data:
        return render_template("index.html", plants=PLANTS, result="⚠️ Kamera verisi alınamadı.")

    if plant_key not in PLANTS:
        return render_template("index.html", plants=PLANTS, result="⚠️ Geçersiz bitki seçimi.")

    plant = PLANTS[plant_key]

    if not os.path.exists(plant["model_path"]):
        return render_template(
            "index.html", plants=PLANTS,
            result=f"⚠️ {plant['name']} için model henüz eğitilmedi.\n"
                   f"Lütfen önce çalıştırın: python train.py --plant {plant_key}"
        )

    try:
        img_str = re.search(r'base64,(.*)', img_data).group(1)
        image_data = base64.b64decode(img_str)
        image = Image.open(BytesIO(image_data)).convert("RGB")

        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        image_path = tmp.name
        tmp.close()
        image.save(image_path)

        prediction, confidence = predict(image_path, plant_key)
        os.remove(image_path)
        advice = get_advice(prediction)

        result = (
            f"🌿 Bitki: {plant['icon']} {plant['name']}\n"
            f"🔬 Tahmin: {prediction}\n"
            f"📈 Güven: %{confidence:.2f}\n"
            f"📋 Tavsiye:\n{advice}"
        )

        return render_template("index.html", plants=PLANTS, result=result)

    except Exception as e:
        return render_template("index.html", plants=PLANTS, result=f"❌ Kamera verisi işlenemedi: {e}")

# ---------------------------------------------------------
# MOBİL UYGULAMA (REACT NATIVE) İÇİN JSON API ENDPOINT
# ---------------------------------------------------------
from flask import jsonify

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    Mobil uygulamadan gelen fotoğrafı alır, analiz eder ve sonucu JSON olarak döner.
    Gelen veri 'multipart/form-data' formatında olmalıdır (image ve plant key).
    """
    if "image" not in request.files:
        return jsonify({"error": "Resim bulunamadı"}), 400
        
    plant_key = request.form.get("plant", "domates")
    
    if plant_key not in PLANTS:
        return jsonify({"error": "Geçersiz bitki seçimi"}), 400
        
    plant = PLANTS[plant_key]
    
    if not os.path.exists(plant["model_path"]):
        return jsonify({"error": f"{plant['name']} modeli bulunamadı"}), 404
        
    image_file = request.files["image"]
    
    if image_file.filename == "":
        return jsonify({"error": "Boş dosya gönderildi"}), 400
        
    try:
        image = Image.open(image_file).convert("RGB")
        
        # Geçici dosyaya kaydet
        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        image_path = tmp.name
        tmp.close()
        image.save(image_path)
        
        # Tahmin yap
        prediction, confidence = predict(image_path, plant_key)
        
        # Geçici dosyayı sil
        os.remove(image_path)
        
        # Tavsiyeyi al
        advice = get_advice(prediction)
        
        # Sonucu JSON olarak döndür
        return jsonify({
            "success": True,
            "bitki_adi": plant["name"],
            "tahmin": prediction,
            "guven_skoru": float(confidence),
            "tavsiye": advice
        })
        
    except Exception as e:
        return jsonify({"error": f"Görüntü işlenirken hata oluştu: {str(e)}"}), 500

if __name__ == "__main__":
    # Host '0.0.0.0' yapılarak telefondan yerel ağda erişime izin veriliyor
    app.run(host="0.0.0.0", port=5000, debug=True)
