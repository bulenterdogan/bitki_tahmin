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

if __name__ == "__main__":
    app.run(debug=True)
