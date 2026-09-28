from flask import Flask, render_template, request
from predict import predict
from advisor import get_advice
from PIL import Image
from io import BytesIO
import base64
import requests
import re
from urllib.parse import urlparse, parse_qs
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tahmin", methods=["POST"])
def predict_route():
    image = None

    if "image" in request.files and request.files["image"].filename != "":
        try:
            image = Image.open(request.files["image"]).convert("RGB")
        except Exception as e:
            return f"❌ Uploaded image could not be processed: {e}"

    elif "url" in request.form and request.form["url"]:
        try:
            url = request.form["url"]

            # Google Görseller linkinden asıl görsel URL'sini çıkar
            parsed = urlparse(url)
            if "google.com" in parsed.netloc and "imgurl" in parsed.query:
                img_url = parse_qs(parsed.query).get("imgurl", [None])[0]
                if img_url:
                    url = img_url

            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, timeout=10, headers=headers, verify=False)

            if response.status_code != 200:
                return f"❌ Image could not be downloaded. Status code: {response.status_code}"

            try:
                image = Image.open(BytesIO(response.content)).convert("RGB")
            except Exception:
                return "⚠️ The provided URL does not point to a valid image."

        except Exception as e:
            return f"❌ Failed to retrieve image from URL: {e}"

    else:
        return "⚠️ No image or URL provided."

    tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    image_path = tmp.name
    tmp.close()
    image.save(image_path)

    prediction, confidence = predict(image_path)
    os.remove(image_path)
    advice = get_advice(prediction)

    result = (
        f"🌿 Prediction: {prediction}\n"
        f"📈 Confidence: %{confidence:.2f}\n"
        f"📋 Recommendation:\n{advice}"
    )

    return render_template("index.html", result=result)

@app.route("/camera", methods=["POST"])
def camera():
    img_data = request.form.get("img_data")
    if not img_data:
        return "⚠️ Camera data not received."

    try:
        img_str = re.search(r'base64,(.*)', img_data).group(1)
        image_data = base64.b64decode(img_str)
        image = Image.open(BytesIO(image_data)).convert("RGB")

        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        image_path = tmp.name
        tmp.close()
        image.save(image_path)

        prediction, confidence = predict(image_path)
        os.remove(image_path)
        advice = get_advice(prediction)

        result = (
            f"🌿 Prediction: {prediction}\n"
            f"📈 Confidence: %{confidence:.2f}\n"
            f"📋 Recommendation:\n{advice}"
        )

        return render_template("index.html", result=result)

    except Exception as e:
        return f"❌ Camera data could not be processed: {e}"

if __name__ == "__main__":
    app.run(debug=True)


