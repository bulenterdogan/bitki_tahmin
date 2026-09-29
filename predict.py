import torch
from torchvision import transforms
from PIL import Image
from train import create_model
from config import PLANTS
import os

# Her bitki için model lazy-load edilir (ilk istendiğinde yüklenir ve cache'lenir)
_loaded_models = {}


def _load_model(plant_key):
    """Belirtilen bitki için modeli yükler ve cache'ler."""
    if plant_key in _loaded_models:
        return _loaded_models[plant_key]

    if plant_key not in PLANTS:
        raise ValueError(f"Bilinmeyen bitki: {plant_key}. Geçerli bitkiler: {list(PLANTS.keys())}")

    config = PLANTS[plant_key]
    model_path = config["model_path"]

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"{config['name']} için model dosyası bulunamadı: {model_path}\n"
            f"Lütfen önce eğitin: python train.py --plant {plant_key}"
        )

    checkpoint = torch.load(model_path, map_location="cpu", weights_only=False)
    class_names = checkpoint["class_names"]

    model = create_model(num_classes=len(class_names))
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    _loaded_models[plant_key] = (model, class_names)
    print(f"✅ {config['name']} modeli yüklendi ({len(class_names)} sınıf)")
    return model, class_names


def predict(image_path, plant_key="domates"):
    """
    Belirtilen bitki modeli ile görsel tahmini yapar.

    Args:
        image_path: Görsel dosya yolu
        plant_key: Bitki anahtarı (domates, patates, biber)

    Returns:
        (tahmin_adı, güven_yüzdesi) tuple
    """
    model, class_names = _load_model(plant_key)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        probabilities = torch.softmax(output, dim=1).squeeze()
        predicted_index = torch.argmax(probabilities).item()
        confidence = float(probabilities[predicted_index].item()) * 100

    return class_names[predicted_index], confidence
