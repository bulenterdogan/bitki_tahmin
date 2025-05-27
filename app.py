import base64
import requests
from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
from predict import predict
from advisor import get_advice

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tahmin", methods=["POST"])
def tahmin():
    image = None
    if "image" in request.files and request.files["image"].filename != "":
        image_file = request.files["image"]
        image = Image.open(image_file).convert("RGB")
    elif "url" in request.form and request.form["url"]:
        try:
            response = requests.get(request.form["url"])
            image = Image.open(BytesIO(response.content)).convert("RGB")
        except Exception as e:
            return f"❌ Görsel URL'si alınamadı: {e}"

    if image is None:
        return "❗ Lütfen bir görsel yükleyin ya da geçerli bir URL girin."

    image_path = "flask_temp.jpg"
    image.save(image_path)

    tahmin, oran = predict(image_path)
    tavsiye = get_advice(tahmin)
    sonuc = f"🌿 Tahmin: {tahmin}\n📈 Güven Oranı: %{oran:.2f}\n\n📋 Tavsiye:\n{tavsiye}"
    return render_template("index.html", result=sonuc)

@app.route("/kamera", methods=["POST"])
def kamera():
    data_url = request.form["img_data"]
    header, encoded = data_url.split(",", 1)
    image_data = base64.b64decode(encoded)
    image = Image.open(BytesIO(image_data)).convert("RGB")
    image_path = "kamera_temp.jpg"
    image.save(image_path)

    tahmin, oran = predict(image_path)
    tavsiye = get_advice(tahmin)
    sonuc = f"🌿 Tahmin: {tahmin}\n📈 Güven Oranı: %{oran:.2f}\n\n📋 Tavsiye:\n{tavsiye}"
    return render_template("index.html", result=sonuc)

if __name__ == "__main__":
    app.run(debug=True)
